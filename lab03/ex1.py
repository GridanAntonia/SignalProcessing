import math
import numpy as np
import matplotlib.pyplot as plt

N = 8

# varianta cu for explicit

F = np.zeros((N, N), dtype=complex)
for w in range(N):
    for n in range(N):
        F[w, n] = math.e**(-2 * math.pi * 1j * w * n / N)

# varianta cu numpy

n = np.arange(N)
w2 = n.reshape((N, 1))
F2 = np.exp(-2j * np.pi * w2 * n / N)

fig, axs = plt.subplots(N, 1, figsize=(7, 14), sharex=True)
for w in range(N):
    axs[w].plot(F[w].real, label="real")
    axs[w].plot(F[w].imag, label="imag")
axs[0].legend(loc="upper right")

plt.tight_layout()
plt.savefig("grafic_ex1.pdf")
plt.show()

# Verificare ca F e unitara

F_H = F.conj().T
prd = F_H @ F
target = N * np.eye(N)

isUnit = np.allclose(prd, target)
print(isUnit)

diff_norm = np.linalg.norm(prd - target)
print(diff_norm)



