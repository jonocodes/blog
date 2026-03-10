---
tags:
  - tech
  - tips
title: Making sudo Work with AI Agents
---

I have been doing a lot of system/network admin lately using Claude Code on my NixOS config files. It has been amazing since I do not like the Nix language, but I love the Nix experience. Now I can really cruse on trying new things and implementing production fixes. I really need to write that update to [Nix - Death by a thousand cuts](2025-01-10-nix-death-by-a-thousand-cuts). So much has changed in the past year.

One of the nice thinks about Nix is I can do a full system build as my user, without switching to it. This way the agent can try fixing syntax and the like until the build passes. Then I can manually to the rebuild switch, which requires sudo access.

However there are times when I want the agent to do the switch itself - and sometimes often. For example when I was troubleshooting a tailscale dns issue I had it try a bunch of different configs until I could get the communication working. In this case I don't want the agent to be constantly asking me to run the manual switch.

So how do I work around this issue of running sudo commands? Can I have the agent stop and ask for my password? Today, coding agents like Claude Code and OpenCode share a fundamental limitation: they can't handle interactive terminal prompts. When a command needs `sudo`, there's no TTY to type your password into. The agent's subprocess just fails:

```
sudo: a terminal is required to read the password
```

Here's what I tried, what exists in the community, and the solution I landed on.

## The Landscape: What Others Have Tried

This is an industry-wide problem. Gemini CLI has [open issues](https://github.com/google-gemini/gemini-cli/issues/10585). Claude Code has [a dozen+ related issues](https://github.com/anthropics/claude-code/issues/1135) on GitHub. Cursor has [forum threads](https://forum.cursor.com/t/regression-agent-terminals-no-longer-support-sudo-or-interactive-input/136719) about it. No tool has a built-in solution.

Here's what the community has come up with:

### NOPASSWD in sudoers

The most commonly recommended approach: make specific commands passwordless.

```
your_username ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart my-app.service
```

This works but requires pre-enumerating every command you'll need. In practice, you either end up with `NOPASSWD: ALL` (too permissive) or constantly editing sudoers when you need a new command.

### SUDO_ASKPASS with SSH Key Encryption

The most developed community solution is [GlassOnTin/secure-askpass](https://github.com/GlassOnTin/secure-askpass/) (and its [corrected fork by crypdick](https://www.ricardodecal.com/guides/running-sudo-commands-in-claude-code-and-cursor/)). It encrypts your sudo password with your SSH key using `age` (for Ed25519) or OpenSSL (for RSA), then provides a GUI confirmation dialog for each sudo invocation.

The agent's command gets rewritten from `sudo foo` to `SUDO_ASKPASS=/path/to/askpass sudo -A foo`, which triggers the helper instead of a terminal prompt.

I actually tried this approach early on — writing a Claude Code hook that rewrote `sudo` to `sudo -A` with an askpass helper. It works on GUI workstations, but it's complex: you need the encrypted password file, the decryption helper, a GUI dialog library, and the hook to tie it all together. For a personal dev machine, it felt like overkill. Also, I want this to work on terminal only intefaces without a GUI.

### polkit/pkexec with Auto-Expiry

[Issue #28930](https://github.com/anthropics/claude-code/issues/28930) on the Claude Code repo proposes using polkit for privilege escalation:

1. Claude calls `pkexec <grant-script>` which triggers a native OS password dialog
2. Upon approval, a timed sudoers entry is created
3. A `systemd` transient timer auto-revokes access after N minutes

This is the most security-conscious proposal — crash-safe, time-bounded, using OS-native auth. But it's Linux-only, requires polkit and systemd, and isn't built yet.

### pam_ssh_agent_auth

A system-level approach where sudo authenticates via your SSH agent instead of passwords. Well-established for Ansible automation, but there's a [known bug](https://github.com/sudo-project/sudo/issues/83) where `sudo -n` (non-interactive mode) still prompts for a password even when the SSH agent should handle it — which is exactly the mode AI agents need.

### File-Based sudo Watcher

[Issue #29275](https://github.com/anthropics/claude-code/issues/29275) proposes a shell watcher: run a loop as root in a spare terminal that watches for command files Claude writes, executes them, and writes output back. Simple but hacky — file-based IPC has race conditions and it's only suitable for single-user dev machines.

## What I Built

I wanted something that:
- Works without a GUI
- Doesn't require passwordless sudo
- Doesn't store or encrypt passwords
- Gives clear feedback when authentication is needed
- Doesn't require the user to manually tell Claude to retry
- Is not Nix specific

The solution has three pieces.

### 1. Global sudo Timestamp

The key insight: `sudo -v` caches your credentials, but by default the cache is per-TTY. Claude's subprocess runs in a different TTY, so it never sees the cache. In my sudo config setting `Defaults timestamp_type=global` makes the credential cache shared across all sessions.

Now when you run `sudo -v` in any terminal, Claude's subprocesses can use the cached credentials for 10 minutes.

### 2. The Hook: Deny-Then-Poll

Claude Code [hooks](https://code.claude.com/docs/en/hooks) let you run scripts before tool calls. A `PreToolUse` hook on `Bash` can inspect the command and allow or deny it.

The tricky part: how do you both show the user a message AND wait for them to act? Hook stderr isn't displayed in Claude's terminal. Only the `permissionDecisionReason` from a JSON deny response is visible. But if you deny, the command doesn't run and the user has to manually tell Claude to retry.

My solution: a **deny-then-poll** pattern using a state file.


$HOME/.claude/hooks/sudo-check.sh


```sh
#!/usr/bin/env sh

# Claude Code PreToolUse hook for Bash commands.
# Blocks sudo commands when credentials aren't cached.
# First attempt: denies immediately with a message.
# Subsequent attempts: polls for up to 30s for credentials.

STATEFILE="/tmp/claude-sudo-hook-notified"
INPUT=$(cat)
COMMAND=$(printf '%s' "$INPUT" | jq -r '.tool_input.command // empty')

# Only check commands that contain sudo
if ! printf '%s' "$COMMAND" | grep -qw 'sudo'; then
  exit 0
fi

# Test if sudo credentials are cached
if sudo -n true 2>/dev/null; then
  rm -f "$STATEFILE"
  exit 0
fi

# First time: deny with message so it's visible in the terminal
if [ ! -f "$STATEFILE" ]; then
  touch "$STATEFILE"
  echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Sudo credentials not cached. Please run sudo -v in another terminal. Retrying automatically..."}}'
  exit 0
fi

# Subsequent attempts: poll for up to 30s
ELAPSED=0
while ! sudo -n true 2>/dev/null; do
  sleep 1
  ELAPSED=$((ELAPSED + 1))
  if [ "$ELAPSED" -ge 30 ]; then
    rm -f "$STATEFILE"
    echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Sudo credentials not cached. Timed out after 30s. Please run sudo -v in another terminal and retry."}}'
    exit 0
  fi
done

rm -f "$STATEFILE"
exit 0
```

The flow:

1. **Sudo command attempted, creds not cached** — hook denies with a message visible in Claude's terminal: "Please run `sudo -v` in another terminal. Retrying automatically..."
2. **Claude sees the deny and automatically retries** — second attempt hits the poll loop
3. **User runs `sudo -v` in another terminal** — within 30 seconds, the hook detects the cached credentials and the command proceeds
4. **If 30 seconds pass** — hook denies again with a timeout message, waits for the user to explicitly retry

The `-qw` flag on grep ensures word-boundary matching — so a path like `/run/sudo/ts/` doesn't false-positive trigger the sudo check.

### 3. Porting to OpenCode


I do use Opus a lot these days, but I have no allegiance to it. I want to see how this would work with a more open agent. The same approach works in [OpenCode](https://github.com/opencode-ai/opencode), which uses a TypeScript plugin system instead of shell script hooks. OpenCode plugins implement `tool.execute.before` and throw an error to block a command — no JSON protocol needed.

```typescript
import type { Plugin } from "@opencode-ai/plugin"

export const SudoCheck: Plugin = async ({ $ }) => {
  return {
    "tool.execute.before": async (input, output) => {
      if (input.tool !== "bash") return
      if (!/\bsudo\b/.test(output.args.command)) return

      // Check if sudo credentials are cached
      try {
        await $`sudo -n true 2>/dev/null`
        return
      } catch {}

      // Poll for up to 30 seconds waiting for the user to run sudo -v
      console.error(
        "Sudo credentials not cached. Run 'sudo -v' in another terminal. Waiting up to 30s...",
      )
      for (let i = 0; i < 30; i++) {
        await new Promise((r) => setTimeout(r, 1000))
        try {
          await $`sudo -n true 2>/dev/null`
          return
        } catch {}
      }

      throw new Error(
        "Sudo credentials not cached. Timed out after 30s. Please run sudo -v in another terminal.",
      )
    },
  }
}
```

Drop this in `~/.config/opencode/plugins/sudo-check.ts` and OpenCode picks it up automatically.

The OpenCode version is simpler because async hooks can just `await` in a loop — no state file or deny-then-retry dance needed. But the core logic is identical: check for `sudo`, test `sudo -n true`, poll, timeout. The two implementations can't share a single file since the hook interfaces are fundamentally different (shell script with JSON stdin/stdout vs TypeScript async functions), but they're small enough that maintaining both is trivial.

## Things to Know

**Every Bash command goes through the hook.** The `matcher` config only filters by tool name, not command content. The script exits immediately for non-sudo commands (one `grep`, negligible overhead), but there's no way to avoid invoking it.

**`timestamp_type=global` has security implications.** Any process on the machine can use the cached credentials during the timeout window. This is fine for a personal dev machine. For shared systems, consider the polkit approach or NOPASSWD for specific commands instead.

**Claude Code has a history of dangerous sudo interactions.** The auto-updater once suggested `sudo chown -R $USER /usr` which [bricked multiple users' systems](https://github.com/anthropics/claude-code/issues/168) by breaking sudo's setuid bit. Sudo-elevated child processes can also [crash the terminal](https://github.com/anthropics/claude-code/issues/7877) or [cause unbounded disk growth](https://github.com/anthropics/claude-code/issues/29921). The hook adds a layer of protection here too — you're always aware when sudo is being used.

**This hook fires even with `--dangerously-skip-permissions`.** Hooks are the last line of defense. I use an alias `cl = "sudo -v && claude --dangerously-skip-permissions"` that pre-caches credentials and skips permission prompts, with the hook as the safety net.

**Built-in support from Claude Code**: [Issue #9881](https://github.com/anthropics/claude-code/issues/9881) requests PTY support via `node-pty`, which would solve sudo prompts at the root. Until then, hooks are the best we've got.

## The Code

All of this can be found in my public configs. Here are permalinks to the relevant files:

Claude Code hook - [claude-sudo-check.sh](https://github.com/jonocodes/configs/blob/c0cf447336c2979d52cf08ae314a306e0f49258e/home-manager/files/claude-sudo-check.sh)

OpenCode plugin - [opencode-sudo-check.ts](https://github.com/jonocodes/configs/blob/c0cf447336c2979d52cf08ae314a306e0f49258e/home-manager/files/opencode-sudo-check.ts)
