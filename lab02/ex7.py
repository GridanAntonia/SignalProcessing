import numpy as np
import matplotlib.pyplot as plt

fs = 1000
ts = 1 / fs
n = np.arange(0, 100)
t = n * ts

f = 20
x = np.sin(2 * np.pi * f * n * ts)

t_dec = t[::4]
x_dec = x[::4]

t_dec2 = t[1::4]
x_dec2 = x[1::4]

fig, axs = plt.subplots(3)

axs[0].plot(t, x)
axs[0].set_title('Semnal initial')

axs[1].plot(t_dec, x_dec)
axs[1].set_title('Semnal decimat 1/4 (de la primul element)')

axs[2].plot(t_dec2, x_dec2)
axs[2].set_title('Semnal decimat 1/4 (de la al doilea element)')

plt.tight_layout()
plt.savefig('grafic_ex7.pdf')
plt.show()

# prin decimare, raman de 4 ori mai putine esantioane, iar graficul devine mai colturos, nu mai este la fel de curbat ca primul

# cand pornim de la al doilea element, esantioanele sunt decalate si se remarca o schimbare a punctelor din varful sinusoidei