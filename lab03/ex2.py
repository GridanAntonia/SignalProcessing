import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 1000
f = 4
t = np.linspace(0, 1, N, endpoint=False)
esantioane = np.arange(N)

x = np.sin(2 * math.pi * f * t)

y = x * (math.e ** (-2 * math.pi * 1j * t))
dist_y = np.abs(y)

idx = 620

# figura 1
fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))

ax1.plot(esantioane, x, color='gray')
ax1.scatter(esantioane, x, c=dist_y, s=5)
ax1.plot([idx, idx], [0, x[idx]], 'r')
ax1.plot(idx, x[idx], 'ro')
ax1.set_xlabel("Timp (esantioane)")
ax1.set_ylabel("Amplitudine")

ax2.scatter(y.real, y.imag, c=dist_y, s=5)
ax2.plot([0, y[idx].real], [0, y[idx].imag], 'r')
ax2.plot(y[idx].real, y[idx].imag, 'ro')
ax2.set_xlim([-1.1, 1.1])
ax2.set_ylim([-1.1, 1.1])
ax2.set_aspect('equal')
ax2.set_xlabel("Real")
ax2.set_ylabel("Imaginar")

plt.tight_layout()
plt.savefig("grafic_ex2_fig1.pdf")
plt.show()

# figura 2
frecvente_w = [1, 2, 4, 6]
fig2, axes2 = plt.subplots(2, 2, figsize=(8, 8))

for i in range(4):
    w = frecvente_w[i]
    ax = axes2.flat[i]

    z = x * (math.e ** (-2 * math.pi * 1j * w * t))
    dist_z = np.abs(z)

    ax.scatter(z.real, z.imag, c=dist_z, s=5)

    centru = np.mean(z)
    ax.plot([0, centru.real], [0, centru.imag], 'k')
    ax.plot(centru.real, centru.imag, 'ko')

    ax.set_title(f"w = {w}")
    ax.set_xlim([-1.1, 1.1])
    ax.set_ylim([-1.1, 1.1])
    ax.set_aspect('equal')
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginar")

plt.tight_layout()
plt.savefig("grafic_ex2_fig2.pdf")
plt.show()

# animatie
pas = 20
fig_anim, (ax_a1, ax_a2) = plt.subplots(1, 2, figsize=(10, 4.5))


def update(frame):
    k = (frame + 1) * pas

    ax_a1.clear()
    ax_a1.scatter(esantioane[:k], x[:k], c=dist_y[:k], vmin=0, vmax=1, s=5)
    ax_a1.plot(esantioane[k - 1], x[k - 1], 'ro')
    ax_a1.set_xlim([0, N])
    ax_a1.set_ylim([-1.1, 1.1])
    ax_a1.set_xlabel("Timp (esantioane)")
    ax_a1.set_ylabel("Amplitudine")

    ax_a2.clear()
    ax_a2.scatter(y[:k].real, y[:k].imag, c=dist_y[:k], vmin=0, vmax=1, s=5)
    ax_a2.plot(y[k - 1].real, y[k - 1].imag, 'ro')
    ax_a2.plot([0, y[k - 1].real], [0, y[k - 1].imag], 'r')
    ax_a2.set_xlim([-1.1, 1.1])
    ax_a2.set_ylim([-1.1, 1.1])
    ax_a2.set_aspect('equal')
    ax_a2.set_xlabel("Real")
    ax_a2.set_ylabel("Imaginar")


anim = FuncAnimation(fig_anim, update, frames=N // pas, interval=50, repeat=False)
anim.save("grafic_ex2_animat_fig1.gif", writer="pillow", fps=20)
plt.savefig("grafic_ex2_animat_fig1.pdf")
plt.show()

fig_anim2, axes_anim2 = plt.subplots(2, 2, figsize=(8, 8))
def update2(frame):
    k = (frame + 1) * pas

    for i in range(4):
        w = frecvente_w[i]
        ax = axes_anim2.flat[i]

        z = x * (math.e ** (-2 * math.pi * 1j * w * t))
        dist_z = np.abs(z)

        ax.clear()
        ax.scatter(z[:k].real, z[:k].imag, c=dist_z[:k], vmin=0, vmax=1, s=5)
        ax.plot(z[k - 1].real, z[k - 1].imag, 'ro')
        ax.plot([0, z[k - 1].real], [0, z[k - 1].imag], 'r')

        ax.set_title(f"w = {w}")
        ax.set_xlim([-1.1, 1.1])
        ax.set_ylim([-1.1, 1.1])
        ax.set_aspect('equal')
        ax.set_xlabel("Real")
        ax.set_ylabel("Imaginar")


anim2 = FuncAnimation(fig_anim2, update2, frames=N // pas, interval=50, repeat=False)
anim2.save("grafic_ex2_animat_fig2.gif", writer="pillow", fps=20)
plt.savefig("grafic_ex2_animat_fig2.pdf")
plt.show()