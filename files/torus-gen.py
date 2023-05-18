import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

v1 = np.array([3, 1])
v2 = np.array([1, 2])


# lattice
for i in range(-5, 6):
    for j in range(-5, 6):
        P = v1 * i + v2 * j
        P1 = P + v1
        P2 = P + v2
        ax.scatter(P[0], P[1], color='k')
        ax.plot([P[0], P1[0]], [P[1], P1[1]], color='k')
        ax.plot([P[0], P2[0]], [P[1], P2[1]], color='k')

ax.set_xlim(-7.5, 7.5)
ax.set_ylim(-7.5, 7.5)

plt.show()
