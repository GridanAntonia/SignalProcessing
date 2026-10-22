import numpy as np
import matplotlib.pyplot as plt

alpha = np.linspace(-np.pi / 2, np.pi / 2, 1000)

val_sin = np.sin(alpha)
aprox_taylor = alpha
aprox_pade = (alpha - (7 * alpha**3) / 60) / (1 + (alpha**2) / 20)

eroare_taylor = np.abs(val_sin - aprox_taylor)
eroare_pade = np.abs(val_sin - aprox_pade)

plt.figure()
plt.plot(alpha, val_sin)
plt.plot(alpha, aprox_taylor)
plt.savefig('grafic_ex8_sinVStaylor.pdf')

plt.figure()
plt.plot(alpha, val_sin)
plt.plot(alpha, aprox_pade)
plt.savefig('grafic_ex8_sinVSpade.pdf')

plt.figure()
plt.plot(alpha, eroare_taylor)
plt.plot(alpha, eroare_pade)
plt.savefig('grafic_ex8_erori.pdf')

plt.figure()
plt.plot(alpha, eroare_taylor)
plt.plot(alpha, eroare_pade)
plt.yscale('log')
plt.savefig('grafic_ex8_log.pdf')

plt.show()