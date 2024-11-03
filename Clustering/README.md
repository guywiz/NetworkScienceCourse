# Clustering

Clustering is a short name for *unsupervized classification*. Classification amounts to determining the class $$C$$ of an element $$x \in D$$ in a dataset $$D$$. Classes usually form a partition of the set $$D$$, that is $$DD$$ is partitioned (divided) into a number of pairwise distinct subsets $$C_1, C_2, \ldots, C_k$$.

Classes may sometimes also be called *groups* or *clusters*. Supervized classification is when classes are known, that is we know how many classes there are and characteristics of classes (or of elements in the class) can be used to determine whether a given element $$x \in D$$ belong to a class $$C \subset D$$.

Machine learning algorithms have proven to be quite good at learning how to classify elements based on examples implicitly describing the known classes.

Conversely, *unsupervized classification* is when classes are unknown, neither their number of their characteristics. The problem then is to determine whether some group structure emerge from the set $$D$$ based on some distance or dissimilarity between its elements.

- [Clustering high-dimensional data](./High_dimensional_data/)
  - $$k$$[-means clustering algorithm for high-dimensional data](./Clustering/kmeans.md)