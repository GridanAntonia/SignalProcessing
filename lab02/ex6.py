import numpy as np
import matplotlib.pyplot as plt

A = 1
phi = 0
fs = 100
ts = 1 / fs
n = np.arange(0, 20)

# a
f_a = fs / 2
sig_a = A * np.sin(2 * np.pi * f_a * n * ts + phi)

# b
f_b = fs / 4
sig_b = A * np.sin(2 * np.pi * f_b * n * ts + phi)

# c
f_c = 0
sig_c = A * np.sin(2 * np.pi * f_c * n * ts + phi)

fig, axs = plt.subplots(3)
axs[0].plot(n, sig_a)
axs[1].plot(n, sig_b)
axs[2].plot(n, sig_c)

plt.tight_layout()
plt.savefig('grafic_ex6.pdf')
plt.show()

# sig_a si sig_c ar trebui sa returneze acelasi grafic, dar din cauza erorilor de calcul, sig_a returneaza un grafic haotic
# sig_b ia doar valorile 0, 1, 0, -1 si de aici apar triunghirile
