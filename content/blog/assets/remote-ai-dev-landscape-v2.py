import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

tools = [
    {"name": "Claude Web", "x": 1.0, "y": 1.0, "size": 260, "marker": "o", "alpha": 0.95},
    {"name": "Claude Remote", "x": 2.3, "y": 4.1, "size": 300, "marker": "s", "alpha": 0.95},
    {"name": "Happy", "x": 3.3, "y": 5.7, "size": 360, "marker": "^", "alpha": 0.95},
    {"name": "OpenClaw", "x": 4.2, "y": 6.2, "size": 320, "marker": "^", "alpha": 0.95},
    {"name": "ClaudeClaw", "x": 4.8, "y": 6.8, "size": 400, "marker": "^", "alpha": 0.95},
    {"name": "Maestro", "x": 7.3, "y": 5.2, "size": 520, "marker": "D", "alpha": 0.95},
    {"name": "OpenHands", "x": 7.8, "y": 4.8, "size": 430, "marker": "D", "alpha": 0.95},
    {"name": "SSH / mosh / tmux", "x": 9.4, "y": 9.4, "size": 280, "marker": "^", "alpha": 0.95},
    {"name": "Arbor", "x": 9.0, "y": 9.1, "size": 260, "marker": "^", "alpha": 0.55},
]

label_offsets = {
    "Claude Web": (0.12, 0.10),
    "Claude Remote": (0.12, 0.10),
    "Happy": (0.12, 0.10),
    "OpenClaw": (0.12, -0.28),
    "ClaudeClaw": (0.12, 0.10),
    "Maestro": (0.12, 0.10),
    "OpenHands": (0.12, -0.28),
    "SSH / mosh / tmux": (-1.45, 0.12),
    "Arbor": (-0.85, -0.40),
}

fig, ax = plt.subplots(figsize=(11.5, 7.5))

for t in tools:
    ax.scatter(
        t["x"],
        t["y"],
        s=t["size"],
        marker=t["marker"],
        alpha=t["alpha"],
    )
    dx, dy = label_offsets[t["name"]]
    ax.text(t["x"] + dx, t["y"] + dy, t["name"], fontsize=10)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

ax.set_xlabel("Infrastructure ownership  ← managed | bring your own →")
ax.set_ylabel("Constraints / access  ← constrained | unconstrained →")
ax.set_title("Remote AI dev tools: rough map of the space")

ax.grid(True, alpha=0.3)

ax.text(0.2, 9.7, "Marker size ≈ orchestration level / concurrent workflows", fontsize=9)
ax.text(0.2, 9.3, "Shape: o = tightly constrained product, s = product on local runtime, ^ = arbitrary/local execution, D = framework/platform", fontsize=9)
ax.text(0.2, 8.9, "Arbor is included as an in-progress reference point, not the focus of the survey", fontsize=9)

legend_elements = [
    Line2D([0], [0], marker='o', linestyle='None', label='Tightly constrained product'),
    Line2D([0], [0], marker='s', linestyle='None', label='Product on local runtime'),
    Line2D([0], [0], marker='^', linestyle='None', label='Arbitrary/local execution'),
    Line2D([0], [0], marker='D', linestyle='None', label='Framework / platform'),
]
ax.legend(handles=legend_elements, loc="lower right", frameon=True)

plt.tight_layout()
plt.savefig("remote-ai-dev-landscape-v2.png", dpi=220, bbox_inches="tight")
plt.savefig("remote-ai-dev-landscape-v2.svg", bbox_inches="tight")
plt.show()
