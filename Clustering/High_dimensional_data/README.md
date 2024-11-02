# High dimensional data

We first a look at high dimensional data, that is data in tabular form where lines correponds to data items (observations, or individuals) and columns to data attributes (variables).

Intuitively, unsupervized classification corresponds to being able to determline whether data elements naturally separate into subgroups.
We first set out Huygens' principle stating that separating data elements into well formed subgroups is the same as identifying homogeneous (compact) subgroups.

Assume data element $$x \in D$$ all have weights $$w_x$$ such that $$\sum_x w_x = 1$$.

The *inertia* $$I_D$$ of the set $$D$$ is defined as:

$$I_D = \sum_{x, y \in D} w_x w_y d(x, y)^2$$

That is we form the sum of the weighted squared distances between all pairs of elements in $$D$$.



Given a subgroup of elements (a cluster) $$C \subset D$$, we define

- the weight $$w_C = \sum_{x \in C} w_x$$, and
- the relative weight f $$x \in C$$ as $$w_{x|C} = \frac{w_x}{w_C}$$
