# Clustering

Clustering is a short name for *unsupervized classification*. Classification amounts to determining the class $$C$$ of an element $$x \in D$$ in a dataset $$D$$. Classes usually form a partition of the set $$D$$, that is $$DD$$ is partitioned (divided) into a number of pairwise distinct subsets $$C_1, C_2, \ldots, C_k$$.

Classes may sometimes also be called *groups* or *clusters*. Supervized classification is when classes are known, that is we know how many classes there are and characteristics of classes (or of elements in the class) can be used to determine whether a given element $$x \in D$$ belong to a class $$C \subset D$$.

Machine learning algorithms have proven to be quite good at learning how to classify elements based on examples implicitly describing the known classes.

Conversely, *unsupervized classification* is when classes are unknown, neither their number of their characteristics. The problem then is to determine whether some group structure emerge from the set $$D$$ based on some distance or dissimilarity between its elements.

- [Clustering high-dimensional data](./High_dimensional_data/)
  - $$k$$[-means clustering algorithm for high-dimensional data](./High_dimensional_data/kmeans.md)
- [Graph communities](./Graphs/)

---

**Exercise**. Given clusters $$C_1, C_2, \ldots, C_k$$ of a graph $$G = (V, E)$$, we define the *silhouette score* of a node $$u \in V$$ as follows. Let $$C_u$$ denote the cluster to which $$u$$ belongs.

- Define $$a(u) = \frac{1}{|C_u|-1} \sum_{v \in C_u} d(u, v)$$, and $$b(u) = \min_{C \not = C_u} \frac{1}{|C|} \sum_{v \in C} d(u, v)$$.

That is, $$a(u)$$ measures how well suited is $$u$$ to its own cluster, while $$b(u)$$ measures how apart is $$u$$ from the nearest distinct cluster.

The silhouette score of $$u \in V$$ is defined as:

$$s(u) = \frac{b(u) - a(u)}{\max \{a(u), b(u)\}}$$

and $$s(u) = 0$$ when $$|C_u| = 1$$.

- Given a graph $$G$$, we may run the Louvain algorithm to infer clusters $$C_1, C_2, \ldots, C_p$$.
- Given a drawing of $$G$$, we may run the $$k$$-means algorithm to find clusters of the graph based on the $$2d$$- coordinates.

**Q**. How related (or how much do they differ) are the number of clusters found by Louvain and the one suggested by $$k$$-means when $$G$$ is drawn using the FM^3 algorithm (for instance)?

**Q**. The silhouette score of nodes, based on the Louvain community structure, may be defined using either the Euclidean distance between nodes, or the graph distance. Do they correlate, and if so how much?

**Q**. Are there any reason why the silhouette score of nodes may/may not correlate with a given network centrality? Explore this idea.