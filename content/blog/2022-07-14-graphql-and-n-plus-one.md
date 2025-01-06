---
tags:
  # - post
  - talks
  - work
  - tech
title: "Talk: GraphQL and the n+1 problem"
---
When I was working at [Udemy](https://www.udemy.com/), there was a new charter for all services to communicate internally via grpc, and all for public facing traffic to use GraphQL.

Some teams were using these technologies a bit, but for most of them these were both new technologies to learn. Since I had GraphQL experience from previous jobs, I was tasked with doing this work for my team, Adaptive Assessments.

This was one of the first projects to migrate in the company and best practices were not yet established. As someone with experience and opinions of how to implement GraphQL well, I experimented and proposed several ways to meet these requirements.

After my solution was rolled out, I taught my team how to work on our new system going forward. I then delivered a company wide presentation on my findings and best practices.

<div class="youtube-video">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/LE6tHglPPXk?si=PVUpuJDZWnFSb5ps" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>


Not really mentioned in this talk is my real take on GraphQL, which I should probably elaborate on in a separate post. Long story short: GraphQL is a nice-to-have for front end teams. In practice their GraphQL service probably does not really solve the problem they were designed for, and the backend team implementing them almost always does a poor job of it. I am not blaming them for it. Creating a robust backend for this is prohibitively difficult and I dont think I have ever seen an in-house implementation that is secure, efficient, and wont break if used wrong.

This is why I always suggest tools like [Hasura](https://hasura.io/), which essentially do all the backend GraphQL work for you. It comes loaded with best practices, efficiency, and extensibility. The takeaway here is: If you are implementing GraphQL yourself, you are probably doing it wrong.
