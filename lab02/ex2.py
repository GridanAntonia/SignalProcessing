import numpy as np
import matplotlib.pyplot as plt

A = 1
f = 4
fs = 1000
ts = 1 / fs
n = np.arange(0, 1000)

val = [0, np.pi/4, np.pi/2, np.pi]

plt.figure()
for phi in val:
    x = A * np.sin(2 * np.pi * f * n * ts + phi)
    plt.plot(n * ts, x)

#plt.savefig('grafic_ex2Faze.pdf')

x = A * np.sin(2 * np.pi * f * n * ts + np.pi/2)
z = np.random.normal(0, 1, len(x))

snr_list = [0.1, 1, 10, 100]
norm_x = np.linalg.norm(x) ** 2
norm_z = np.linalg.norm(z) ** 2

fig, axs = plt.subplots(4)
i = 0

for snr in snr_list:
    g = np.sqrt(norm_x / (snr * norm_z))
    axs[i].plot(n * ts, x + g * z)
    axs[i].set_title('SNR = ' + str(snr))
    i += 1

plt.tight_layout()
plt.savefig('grafic_ex2Zgomot.pdf')
plt.show()


