import numpy as np
import matplotlib.pyplot as plt

A = 2
f = 5
phi = np.pi / 3

t = np.linspace(0, 1, 1000)

x_sin = A * np.sin(2 * np.pi * f * t + phi)

x_cos = A * np.cos(2 * np.pi * f * t + phi - np.pi / 2)

fig, axs = plt.subplots(2)
axs[0].plot(t, x_sin)
axs[0].set_title('Semnal Sinus')

axs[1].plot(t, x_cos)
axs[1].set_title('Semnal Cosinus')
plt.tight_layout()

plt.savefig('grafic_ex1.pdf')
plt.show()