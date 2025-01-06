---
tags:
  # - post
  - tech
title: "On Coding Interviews: What Works, What Doesn’t, and Why It Matters"
---
The relationship between technical interviews and real-world performance remains one of the most debated topics in software engineering recruitment. While you may be reading this because of a recent interview experience we shared, this post aims to explore a broader and more important question: how can companies better identify talented developers? Although many organizations have established interview processes they consider sufficient, the challenge of false negatives – rejecting qualified candidates – continues to impact both companies and developers [^googlehomebrew]. As Joel Spolsky notes, "A lot of good programmers end up getting rejected — while, even worse, companies end up hiring people who are good at passing tests, but under-perform in the real world" [^joelrecruiting]. Drawing from industry anecdotes [^seniorinterviews], professional discussions [^hackernews], and academic research [^devstalk], this post examines real-world examples and alternatives to traditional coding interviews.

## A bit about me

I am a lifelong developer. When I discovered programming in adolescence I took to it and never stopped. After decades of being a full time individual contributor my love of coding only continues to deepen.

I always have my hands in open source and side projects. After the work day is done it is not uncommon for me to put in another days worth of work on [my personal and open source projects](https://github.com/jonocodes). Many of these projects also directly benefit my place of work [^branchr] [^envoy] [^mystique].

Managers say I am enthusiastic and known for going above and beyond to work out innovative solutions. I am eager to learn and like to mentor. I regularly give tech talks, non-tech talks, lead projects, and security workshops [^juiceshop].  See my [reviews from peers and managers](https://digitus.notion.site/Jono-Finger-Professional-Info-113025d8c35b80bea249e1de35ae55c4). They can be [verified on linkedin](https://www.linkedin.com/in/jfinger/details/recommendations).

## The problem with coding questions

I do well on all parts of the interview process, but not on live coding questions. Most professions do not have an equivalent hurdle in their process, but these are common place in tech. Many experienced engineers, particularly at senior levels, view these assessments with skepticism or actively avoid organizations that rely heavily on them [^discriminatory]. They consider it a red flag or they find them insulting.

Still, companies rely heavily on these pass/fail "tests". In my tenure as a programmer I have actually seen interviews improve over the years by relying less on these assessments. But some traditions die hard [^bestpractices]. As technologists, we should strive to keep up with best practices.

Having an hour long tech question tends to rely on landing the "trick" to the answer early on.
If you don't happen to know the answer from previously doing the same one or miraculously stumbling upon it in the first few minutes you will be wasting the next 40. Some engineers have a knack for these types of questions - but it is not a good measure of the quality of their work.

Consider a magic trick: initially, it captivates audiences precisely because the solution seems impossibly clever. Yet once revealed, the same trick often appears deceptively simple, leading viewers to wonder why they didn't see through it immediately. This psychological shift reflects perfectly the dynamics of technical interview questions. This phenomenon can be explained by what psychologists call "the curse of knowledge" [^knowledge] or the "illusion of transparency" [^transparency] When an interviewer is given the answer to a coding question it becomes obvious to them. They feel it is trivial by virtue of knowing the answer. This is not their fault. It's a natural bias, but one we can address.

The problem compounds when companies reuse interview questions over extended periods - sometimes years. Engineer interviewers naturally refine their understanding of the problem space, discovering edge cases and optimization opportunities. This deepening expertise can widen the gap between their perception of the problem's difficulty and a candidate's first-time experience with it.

Another common pitfall occurs when companies frame interview questions around their domain expertise, even when hiring for general software engineering roles. For instance, a biotech company might ask candidates to implement a gene-pair categorizing algorithm, despite not requiring prior biology knowledge. The employee lives and breaths these questions every day. So does everyone around them. That's likely been what they have been working on for years. Such questions can create an unintended expertise bias, as interviewers who work with these concepts daily may struggle to view the problem from a newcomer's perspective. 

In practice these types of questions rarely come up at work. But if they do, we enjoy it. We share the problem with the team and try to figure out the best solutions. Sleep on it. Come back the next day and talk some more. Engineers are problem solvers and love a good challenge, but that experience is different then a timed pass/fail "test".

Much of the same can be said for interview sessions focused on algorithm whiteboarding. Balance a red black tree? When would someone ever need to implement that? In fact, they should not. A good engineer stands on the shoulders of giants and knows to not roll their own cryptography [^rollcrypto].

## Alternative Approaches

Here are several alternatives to traditional live coding interviews I have seen or implemented myself at companies that can better assess a candidate's real-world engineering capabilities:

### 1. Take-Home Projects

Provide candidates with a substantial coding assignment they can complete in their natural development environment. This approach allows for more complex problems than live coding sessions, as developers can utilize their usual tools and resources – reflecting actual workplace conditions [^livecoding]. Consider:

- Setting clear time expectations rather than strict limits
- Requesting documentation and test coverage
- Create your own unit tests that can check the answers
- Using platforms like Coderpad or Codility for streamlined administration
- Ensuring the scope remains reasonable and respectful of candidates' time

### 2. Code Review Sessions

Present candidates with existing code and evaluate their analytical abilities through various exercises:

- Identifying potential issues and red flags
- Debugging specific problems
- Conducting mock pull request reviews
- Discussing optimization opportunities
- Implementing test coverage strategies
- Analyzing algorithmic complexity

### 3. Portfolio Discussion

Have candidates present their own project work, which provides insight into their:

- Development process and decision-making
- Technical communication skills
- Understanding of trade-offs and improvements
- Testing strategies and quality assurance approaches
- Project management and prioritization abilities

### 4. Guided Implementation

Share pre-designed algorithms or pseudocode for candidates to implement in code. This method:

- Better mirrors real-world development scenarios
- Focuses on implementation skills rather than problem-solving under pressure
- Creates a collaborative environment for discussion
- Allows evaluation of coding style and testing approaches

### 5. Technical Discussion Series

Present a variety of shorter, focused technical discussions that might cover:

- Database schema design and optimization
- Algorithmic complexity analysis
- Data structure selection and trade-offs
- Security best practices and PII handling

### 6. Flexible Assessment Options

Consider offering candidates a choice of several of the different assessment methods above. This approach:

- Accommodates diverse working styles and preferences
- Promotes inclusive hiring practices [^discriminatory]
- Allows candidates to demonstrate their strengths
- Respects different time constraints and commitments


These alternative approaches can be implemented within the same time investment as traditional coding interviews, while potentially yielding richer insights into candidates' capabilities. If you want to improve the effectiveness even more, regularly gather candidate feedback and refine your methods over time.


[^rollcrypto]: Morrow, Susan (2019). [The Dangers of “Rolling Your Own” Encryption](https://www.infosecinstitute.com/resources/cryptography/the-dangers-of-rolling-your-own-encryption/) Infosec Institute

[^googlehomebrew]: Howell, Max (2018). [What's the logic behind Google rejecting Max Howell, the author of Homebrew, for not being able to invert a binary tree?](https://www.quora.com/Whats-the-logic-behind-Google-rejecting-Max-Howell-the-author-of-Homebrew-for-not-being-able-to-invert-a-binary-tree) Quora

[^juiceshop]: [OWASP Juice Shop](https://juice-shop.github.io/juice-shop/) - Insecure web application for security trainings

[^branchr]: jonocodes (2016). [Branchr](https://github.com/jonocodes/branchr) - Feature branch monitoring for product development

[^envoy]: jonocodes (2017). [Envoy](https://github.com/jonocodes/envoy)- Test framework for microservices using Docker

[^mystique]: jonocodes (2023). [Mystique](https://pypi.org/project/mystique/)- Python test helpers for loose data matching

[^hackernews]: Ellis, Ike (2013). [I will no do a tech interview](https://news.ycombinator.com/item?id=6251087) Hacker News

[^seniorinterviews]: Storm, Adam (2020). [Why Senior Engineers Hate Coding Interviews](https://medium.com/swlh/why-senior-engineers-hate-coding-interviews-d583d2855757) Medium

[^devstalk]: Behroozi, Mahnaz; Parnin, Chris; Barik, Titus (2019). [Hiring is Broken: What Do Developers Say About Technical Interviews?](https://www.researchgate.net/publication/334448588_Hiring_is_Broken_What_Do_Developers_Say_About_Technical_Interviews) IEEE Symposium on Visual Languages / Human-Centric Computing Languages and Environments

[^joelrecruiting]: Cassel, David (2018). [Joel Spolsky on Stack Overflow, Inclusion, and How He Broke IT Recruiting](https://thenewstack.io/joel-spolsky-on-stack-overflow-inclusion-and-how-he-broke-it-recruiting/) The New Stack

[^discriminatory]: Henry, Bradston (2022). [Why I Stopped Interviewing with Companies That Require a Coding Test](https://dev.to/bradstondev/why-i-stopped-interviewing-with-companies-that-require-a-coding-test-2j6n) DEV

[^bestpractices]: Goodin, Dan (2019). [Microsoft says mandatory password changing is “ancient and obsolete”](https://arstechnica.com/information-technology/2019/06/microsoft-says-mandatory-password-changing-is-ancient-and-obsolete/)
[^knowledge]: [Curse of Knowledge](https://en.wikipedia.org/wiki/Curse_of_knowledge) Wikipedia

[^transparency]: [Illusion of Transparency](https://en.wikipedia.org/wiki/Illusion_of_transparency) Wikipedia

[^livecoding]: Gentleman, Daniel (2022). [Live coding interviews are terrible - and they might be discriminatory](https://www.linkedin.com/pulse/live-coding-interviews-terrible-might-daniel-gentleman/) LinkedIn