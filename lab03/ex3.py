import math
import numpy as np
import matplotlib.pyplot as plt

N = 1000
t = np.linspace(0, 1, N, endpoint=False)

f1, A1 = 10, 1.5
f2, A2 = 35, 2.0
f3, A3 = 80, 0.8

x = np.zeros(N)
for n in range(N):
    x[n] = (A1 * math.cos(2 * math.pi * f1 * t[n]) + A2 * math.cos(2 * math.pi * f2 * t[n]) + A3 * math.cos(2 * math.pi * f3 * t[n]))

frecvente_w = list(range(0, 101))
M = len(frecvente_w)

X = np.zeros(M, dtype=complex)

for idx, w in enumerate(frecvente_w):
    suma = 0 + 0j
    for n in range(N):
        suma += x[n] * (math.e ** (-2 * math.pi * 1j * n * w / N))
    X[idx] = suma

modul_X = np.abs(X)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

ax1.plot(t, x)
ax1.set_xlabel("Timp (s)")
ax1.set_ylabel("x(t)")

ax2.stem(frecvente_w, modul_X, markerfmt='.')
ax2.set_xlabel("Frecventa (Hz)")
ax2.set_ylabel("|X(w)|")

plt.tight_layout()
plt.savefig("grafic_ex3.pdf")
plt.show()