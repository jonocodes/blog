---
tags:
  - tech
title: The Programmer's Job in an AI World
---


I have a friend who was a programmer a generation before me who I always looked up to. He now teaches at a community college. He recently reached out to me about what to teach his students. I'm putting it here as historical record of this moment in time.

---

Jono,
Been a while. 🙂 I hope you and your folks & family are doing well.

I am still teaching College computer science and (as I'm sure you know) AI changes EVERYTHING. It's not even clear to me whether the instructors in my department should continue teaching programming in its present form. My opinion is we need to teach our students to read and correct code (probably in Python) but it may not help them that much in the work world to teach them how to write code. But I'm not sure.

I see it as a 3-step process to really help my students:

1. Understand what the job responsibilities are of a typical programmer in an AI workplace environment NOW.
2. Identify the set of skills necessary to successfully complete those responsibilities.
3. Work out the details of teaching those skills.  

Which brings me to the point of this email. You struck me as one of the more professional programmers I've run into since retirement. I'd be seriously obliged if you could shoot me a summary of the responsibilities / deliverables of successful programmers these days.  I'm preparing a new course on "Prompt Engineering & AI Agents" and really want to make this meaningful in the lives of my students.

Regards and all the best,
RonK

---


Hey RonK!

Thanks for reaching out. I have a lot of thoughts on this topic. I was an early adopter, and am always mucking with the new tools. I think AI will probably be the end of humanity. But that's a whole separate conversation... Now lets ramble about coding.

About 6 months ago there was an inflection point with the deployment of Claude 4.5 where AI started becoming very powerful in such a way that you could do unattended tasks and trust that it would do things correctly. Since then, my immediate engineering team at work has been entirely let go and I'm the last engineer in my office. I'm still a full time software dev but I write very little code by hand. I probably spend about a day a month actually producing syntax from my brain. It's not uncommon for me to create an entire project in a couple days that I would have taken me couple months.

I also don't review code much, from myself or others. Code review agents are very thorough and the good ones will point out which parts are worth putting real eyes on and which are not. So things are fast and messy right now. It's going to cause a lot of problems, but also a lot of solutions.

We're definitely in a weird place right now. I think for the most part engineers are loving the new tools that we have. Especially the more senior ones who have built that same CRUD endpoint a hundred times. Now we can skip all the boilerplate and just get to the interesting parts.

Just yesterday, at work... I'm building a project around database synchronization. I wasn't sure which of several ways I wanted to go about it. So in a couple hours, I had an LLM essentially spit out three full runnable versions of the app to see which one I liked. This, of course, would not have been possible even a year ago. There are a lot of new workflows and methodologies that have come about from all of this new tech.

There are camps that think programming languages don't even matter any more and you should write everything in rust or even assembly. Why use a user friendly language like python if you don't have to actually look at the code?

Here's an example of a guy who built an interesting development framework that has caught some serious traction. https://www.youtube.com/watch?v=EJyuu6zlQCg&t=1s

His stuff may get to some of your questions about prompt engineering. I'm not entirely sold on the future of Skills-maxing, but it seems quite powerful at this immediate point in time.

Right now, I think junior developers are in quite a pickle. Most companies are shedding their juniors and only hire the most senior ones they can find. And that's mostly because they need someone who's experienced enough to direct the AI and build systems that make sense architecturally. But even that won't last forever. I think what's gonna happen is we're going to have some very good product managers who will be able to spit out a good program and manage a bunch of AI agents and not really have to know much about what's going on underneath. I see this happening in the next few years. The day of devs being on top of the world is gone. The economics of supply and demand are turning on its head.

My product manager (also part of our most recent layoffs), had really gotten pretty proficient at actually building our products. He started using AI to make nice mock-ups, but by the end, he was writing full on apps and doing half my job. He was a smart guy, but definitely not an engineer. If these lay offs happened in a couple years from now with improved LLMs, I think I would have been let go before he was.

I personally spend most of my time with AI creating design docks. Deep research on best practices, prior art, testing workflows, cost analysis, etc. Then, when I'm satisfied, I have the LLM spit out these very elaborate workbooks that a lesser agent can follow to actually write the code.

Funny thing is I got interviewed by a friend's kid the other day. A seventh grader who wants to learn about software engineering. I mostly told them all the reasons why I love it - because I truly do. But I don't know what to generally advise kids these days. Do my own kids need to have any hard skills? Should they go to college? Did they need to even go to a math class now? I don't know what the future is for white collar work in general. Maybe we'll all move towards a leisure economy where we can just sit around and read books all day while the robots serve us martinis by the pool. :)

AI also has many implications for the open source world. At the Linux conferences I go to, most conversations have turned to the new culture around forking and how to deal with incoming waves of slop pull requests. Lots of thoughts there. 

Speaking of open source, my personal collection of side projects has completely exploded in the last year. We all have documents of ideas that we will never implement. Now I've actually started to crack out a bunch of them. The feeling of programming and producing something is just entirely different than it used to be. But that's its own story. I've written about it a bit. 
https://www.dgt.is/blog/2026-01-24-ai-programming-junkie/

What practical advice could I actually give? Not much. 

* If you really wanna be a programmer, you should do it because you love it. Some argue that was always the case though I disagree.

* Don't fight AI. That wont work in your favor. It's like fighting the light bulb or the printing press. You can't go without it at in work environment. But for the most part, juniors I've worked with don't need this advice. As far as they're concerned, autocomplete in their IDE has just gotten better and better every year. That's all they know, so they're already pretty native to it. And these kids can move fast. Often faster then me. Using LLMs outside of work is a different story. You don't need to use it there if you don't want to.

* Use LLMs to dive deep discover what you need to know when working on something new. When trying to get up to speed on a new topic or technology we used to scour outdated forums and documents to find any advice we could. But now an LLM can help you step back and think broadly about a problem before you decide which direction to take something. Tackling "unknown unknowns" is a hard problem, but now with the right style of curious querying you can learn a lot, fast. And after you have started actually working on a project, continue to have agents look at the big picture, since it is easy to dive deep into a rabbit hole if you are not careful.

* Once you have specced something out, ask if what you designed is a solved problem. LLMs today still are a bit bullish to writing everything themself. You don't want to reinvent the wheel. Side note: That calculus is changing more and more, but the advice stands.

* Testing is more important then ever. I have always been test-obsessed, but my testing style has changed with AI use. I should write a blog post to force my self to formalize my thoughts around this. Lately I have been playing with more TDD style coding.

* Instead of creating a bunch of custom workflows that are meant to be understood by agents, focus on writing documents that are thorough and close to your code. It is of most importance that the docs do not drift, but you can often solve that by having AI check to see if the docs are out of sync with the code. These docs should really be directed at humans, but LLMs will discover them and will give them a lot of context and direction of how to run, build and test things. I've experimented with a bunch of things here and think the art of managing these docs is starting to settle.


If you wanna read some fun philosophical stuff about AI there's some interesting stuff on the 80k hours podcast.
https://80000hours.org/podcast/episodes/kyle-fish-ai-welfare-anthropic/

Speaking of podcasts, this was an entertaining one about a guy who tries to run a whole company with personified AI agents. Buffoonery ensues.
https://pca.st/j22grjam

Also unrelated. I started reading the Bobiverse books. You may enjoy them.

I use dictation to write this message so the wording is quite casual, but at least I didn't use an LLM. Give me a call sometime if you want to dig in on any of this or get into concrete examples. My thoughts on this stuff are really evolving day to day.

And now I have to get back to (not) programming.

-Jono
