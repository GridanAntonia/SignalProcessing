import numpy as np
import matplotlib.pyplot as plt

fs = 1000
ts = 1 / fs
n = np.arange(0, 1000)

s1 = np.sin(2 * np.pi * 5 * n * ts)

s2 = 2 * np.mod(10 * n * ts, 1) - 1

suma = s1 + s2

fig, axs = plt.subplots(3)
axs[0].plot(n * ts, s1)
axs[0].set_title('Semnal Sinusoidal')

axs[1].plot(n * ts, s2)
axs[1].set_title('Semnal Sawtooth')

axs[2].plot(n * ts, suma)
axs[2].set_title('Suma semnalelor')

plt.tight_layout()
plt.savefig('grafic_ex4.pdf')
plt.show()