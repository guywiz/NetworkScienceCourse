
# Indice IK de risque/protection mécanique des matériels électriques.
import matplotlib.pyplot as plt
import math
from scipy import stats

# square grid
inertia = [(2, 66400), (3, 42162), (4, 26400), (5, 22577), (6, 19161), (7, 16261), (8, 13773), (9, 12037)]
# randomly divided grid


X = list(map(lambda x: x[0], inertia))
Y = list(map(lambda x: x[1], inertia))

plt.ylabel('k')
plt.xlabel('inertia intra')
plt.title('k / intra inertia')


plt.plot(X, Y)
plt.show()

