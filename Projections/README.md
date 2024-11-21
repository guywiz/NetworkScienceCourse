# Graph projections

Interaction between two entities $$x, x' \in X$$, be they persons or proteins, sometimes cannot be observed directly. Instead, some third party entity $$y \in Y$$ or fact will be used to induce interaction between $$x$$ and $$x'$$.

Examples are:

- *People* ($$x, x' \in X$$) who participate to different **events** ($$y \in Y$$)
- *Organizations* (companies, research laboratories) who participate to research or R&D **projects**
- Etc.

The graphs used to model these situations are bipartite: they comprise nodes or two different types $$X$$ or $$Y$$, and links necessarily connect nodes of different types.

These graphs can be studied *per se*. For instance, one can prove that a graph is bipartie exactly when (iif $$\Leftrightarrow$$) it does not contian any cycle of odd length.

***Exercise***. Come up with a proof of this fact. $$\square$$

Some authors have moreover claim that most social networks (or more precisely, Complex Networks)) take their origin in bipartite graphs.

Guillaume, J. L., & Latapy, M. (2006). *Bipartite graphs as models of complex networks*. Physica A: Statistical Mechanics and its Applications, 371(2), 795-813.

## One-mode projection

Although giving a more accurate account of the data, bipartite graphs do not allow to readily use node centralities in order analyse the data at hand. Indeed, in a social network, the degree of a node indicates how many persons a given actor knows, while in a bipartite graphs we'd need to look at distance 2 neighbors. The situation is even more complex when considering length of paths connecting actors.

***Exercise***. The [FP7 dataset](./FP7.tlp) contains nodes corresponding either to projects or to partners (organizations) participating to these projects that were funded by the EUropean Commission under the 7th framework programme over the period 2007-2013.

A network solely containing entities of the same type can be derived form the original bipartite graph. This derived network is called a *one-mode projection* since it amounts to build a new graph $$G = (V, E)$$ (where $$V = X$$ for instance) induce any length two path connecting $$x - y - x'$$ to a single edge $$\{x, x'\} \in E$$.

***Exercise***. A clique over a set of nodes $$C$$ is a graph where all pairs of nodes $$x, x' \in C$$ are connected. (Hence a clique contains $$\frac{|C| \cdot (|C|-1)}{2}$$ edges.)

Let $$H$$ be a bipartite graph over nodes $$X \oplus Y$$ and $$G = (X, E)$$ be the one-mode projection on $$X$$ obtained from $$H$$. Let $$C \subset X$$ be the nodes incident to a given node $$y \in Y$$ in $$H$$. Then the clique over $$C$$ is a subgraph of $$G$$. $$\square$$

Hence a one-mode projection of a graph being a collection of cliques will typically be dense: that is, its number of edges compared to its number of nodes $$\frac{|E}{|V|}$$can be quite large. 

More precisely,

- considering that a graph having a number of edges $$|E| = 4|V|$$ is hardly readable (using any layout algorithm), 
- considering one-mode projection graph consist of a collection of cliques, and consequently can locally have a quadratic number of edges (in terms of node size)

we see that one-mode projection can be hard to analyze, if not visualize.

### Filtering edges using weights

When projecting length 2 paths in $$H$$ onto edges in $$G = (V, E)$$, we may naturally assign edges $$e \in E$$ a weight corresponding to the number of different paths $$x - y - x'$$ leading to $$e = \{x, x'\}$$. That is, this number is equal to the *number of common neighbors* $$x$$ and $$x'$$ have in $$H$$ (number of events/projects people/organizations co-participate into, e.g.).

One may then consider this weight to filter out edges of a lesser weight, leading to a subgraph of lower edge density.


