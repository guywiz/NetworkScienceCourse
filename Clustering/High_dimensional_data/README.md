# High dimensional data

We first a look at high dimensional data, that is data in tabular form where lines correponds to data items (observations, or individuals) and columns to data attributes (variables).

Intuitively, unsupervized classification corresponds to being able to determline whether data elements naturally separate into subgroups.
We first set out Huygens' principle stating that separating data elements into well formed subgroups is the same as identifying homogeneous (compact) subgroups.

Assume data element $$x \in D$$ all have weights $$w_x$$ such that $$\sum_x w_x = 1$$.

The *inertia* $$I_D$$ of the set $$D$$ is defined as:

$$I_D = \sum_{x, y \in D} w_x \cdot w_y \cdot d(x, y)^2$$

That is we form the sum of the weighted squared distances between all pairs of elements in $$D$$.

The barycenter $$g_D$$ of $$D$$ is define as the componentwise weighted sum:

$$g_D = \sum_{x \in D} w_x \cdot x$$

---

**Exercise**. Inertia can be computed relative to the barycenter, more precisely we have:

$$I_D = 2 \sum_{x \in D} w_x d(x, g_D)^2$$

---

Given a subgroup of elements (a cluster) $$C \subset D$$, we define

- the weight $$w_C = \sum_{x \in C} w_x$$, and
- the relative weight of $$x \in C$$ as $$w_{x|C} = \frac{w_x}{w_C}$$
- the cluster barycenter $$g_C = \sum_{x \in C} w_{x|C} x$$
- and consequently, we may compute the cluster inertia (using nay two fo the above formula) $$I_C = \sum_{x, y \in C} w_{x|C} \cdot w_{y|C} \cdot d(x, y)^2 = 2 \cdot \sum_{x \in C} w_{x|C} \cdot d(x, g_C)^2$$

---

**Exercise**. Show that $$D$$'s barycenter $$g_D$$ is also the barycenter of the set of all barycenters $$\{G_{C_1}, G_{C_2}, \ldots, G_{C_k}\}$$:

$$g_D = \sum_{i=1}^{k} w_C g_C$$

We also have $$I_{inter} = \sum_{i, j} w_{C_i} \cdot w_{C_j} \cdot d(g_{C_i}, g_{C_j})^2 = 2 \sum_{C} w_{C} \cdot d(g_C, g_D)^2$$

---


**Huygen's Principle**. We have:

$$I_D = \sum_C (w_C \cdot I_C) + I_{inter}$$

That is, the total inertia splits into cluster inertia (intra) and inter-cluster inertia (between berycenters).

Observe that this identity holds whatever clusters we may consider. As a consequence, since total inertia is invariant, Huygen's principle states that minimizing intra-cluster inertia is equivalent to maximizing inter-cluster distance.

*Proof*. The proof exploits the fact that we are dealing with Euclidean distances, for which we have

$$d(x, y)^2 = \langle x-y, x-y \rangle$$

where points $$x, y$$ may be considered as vectors and $$\langle \cdot, \cdot \rangle$$ denotes the usual scalar product. Hence,

$$\frac{1}{2} I_D = \sum_{x \in D} w_x d(x, g_D)^2 = \sum_{x \in D} w_x \langle x-g_D, x-g_D \rangle
= \sum_{x \in D} w_x \langle x, x \rangle - 2w_x \langle x, g_D \rangle + w_x \langle g_D, g_D \rangle$$

$$= \big( \sum_{x \in D} w_x \langle x, x \rangle - 2w_x \langle x, g_D \rangle \big) + \langle g_D, g_D \rangle$$

We also have:

$$\frac{1}{2} I_{intra} + \frac{1}{2} I_{inter} = \sum_C w_C \sum_{x \in C} w_{x|C} d(x, g_C)^2 + \sum_C w_C d(g_C, g_D)^2$$

$$= \sum_C w_C \sum_{x \in C} w_{x|C} \langle x-g_C, x-g_C \rangle + \sum_C w_C \langle g_C-g_D, , g-C-g_D \rangle$$

$$= \sum_C \sum_{x \in C} w_C w_{x|C} \langle x, x \rangle - 2 w_C w_{x|C} \langle x, g_C \rangle + w_C w_{x|C} \langle g_C, g_C \rangle$$

$$= \big( \sum_C \sum_{x \in C} w_C w_{x|C} \langle x, x \rangle - 2 w_C w_{x|C} \langle x, g_C \rangle \big) + \big( \sum_C \sum_{x \in C} w_C w_{x|C} \langle g_C, g_C \rangle \big)$$

Hence the equality $$\frac{1}{2} I_D = \frac{1}{2} I_{intra} + \frac{1}{2} I_{inter}$$ follows by properly grouping terms since $$w_{x|C} = w_x$$ and $$g_D = \sum_{i=1}^{k} w_C g_C$$.

