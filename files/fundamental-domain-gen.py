import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.autolayout"] = True

X = np.linspace(-0.5, 0.5, 1000)
Xs = np.linspace(-1, 1, 1000)
fig, ax = plt.subplots()

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.set_aspect('equal')

# left right
ax.plot([0.5, 0.5], [-0.1, 2.2], '--', color='b')
ax.plot([-0.5, -0.5], [-0.1, 2.2], '--', color='b')
ax.plot([-1.5, -1.5], [-0.1, 2.2], '--', color='purple')
ax.plot([1.5, 1.5], [-0.1, 2.2], '--', color='purple')

# semicircle
ax.plot(Xs, (1 - Xs ** 2) ** 0.5, '--', color='b')
ax.plot(Xs + 0.5, (1 - (Xs - 0.5) ** 2) ** 0.5, '--', color='purple')
ax.plot(Xs - 0.5, (1 - (Xs + 0.5) ** 2) ** 0.5, '--', color='purple')

# region
ax.fill_between(X, (1 - X ** 2) ** 0.5, 2.2, color='b', alpha=0.2)

plt.savefig("static/images/modular-forms-fundamental-domain-1.png")
