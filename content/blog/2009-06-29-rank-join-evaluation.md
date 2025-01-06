---
tags:
  # - post
  - tech
title: Robust and Efficient Algorithms for Rank Join Evaluation
---
This is about my graduate thesis on database query optimization.

In the 2000's, organizations were dealing with more and more data. Efficiently making sense of it all was a hot topic. Several universities were working on these problems and the [The Database Research Group at UCSC](https://engineering.ucsc.edu/departments/computer-science-and-engineering/research/#database) was no exception. We had quite a bit of active research on data mining and search efficiency. 

The particular issue I worked on was ranked search algorithms. The basic idea behind this is the larger a database gets, the slower it is to get the search results you want. The need for these type of systems can be shown by Google Search. Google has tremendous amounts of data. Users can search for a complex set of terms, but they only care about the top page of results - and they want it fast.

Traditionally, a relational database would have to do the expensive work of creating an exhaustive list of all possible results, and then picking off the top ones. If a user had to wait 45 seconds every time they entered some search terms, people would stop using it. This brought about rank join algorithms which were different ways to quickly pick off top results without having to compute everything up front.

We had published several papers on our particular take on "Top-K" solutions. My thesis involved implementing these (in PostgreSQL) and testing their efficiency in practice. [It was published in Sigmod 2009](https://tr.soe.ucsc.edu/sites/default/files/technical-reports/UCSC-SOE-09-01.pdf).

### Abstract

In the rank join problem we are given a relational join R1 x R2 and a function that assigns numeric scores to the join tuples, and the goal is to return the tuples with the highest score. This problem lies at the core of processing top-k SQL queries, and recent studies have introduced specialized operators that solve the rank join problem by accessing only a subset of the input tuples. A desirable property for such operators is instance-optimality, i.e., their I/O cost should remain within a factor of the optimal for different inputs. However, a recent theoretical study has shown that existing rank join operators are not instance-optimal even though they have been shown to perform well empirically. The same study proposed the PBRJ-RR/FR operator that was proved to be instance-optimal, but its performance was not tested empirically and in fact it was hinted that its complexity can be high. Thus, the following important question is raised: Is it possible to design a rank join operator that is both instance-optimal and computationally efficient?

In this paper we provide an answer to this challenging question. We perform an empirical study of PBRJ-RR/FR and show that its computational cost can offset the benefits of instance-optimality. Using the insights gained by the study, we develop the novel FRPA operator that addresses the efficiency bottlenecks of PBRJ-RR/FR. We prove that FRPA is instance-optimal in general and more specifically that it never performs more I/O than PBRJ-RR/FR. FRPA is the first operator that possesses these properties and is thus of interest in the theoretical study of rank join operators. We further identify cases where the overhead of FRPA becomes significant, and propose the FRPA operator that automatically adapts its overhead to the characteristics of the input. An extensive experimental study validates the effectiveness of the new operators and demonstrates that they offer significant performance improvements (up to an order of magnitude) over the state-of-the-art.

