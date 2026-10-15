import numpy
import matplotlib.pyplot as plt

samples = int(numpy.round(0.03 / 0.0005)) + 1
t = numpy.linspace(0, 0.03, samples)

x = numpy.cos(520 * numpy.pi * t + numpy.pi / 3)
y = numpy.cos(280 * numpy.pi * t - numpy.pi / 3)
z = numpy.cos(120 * numpy.pi * t + numpy.pi / 3)

fig1, axs1 = plt.subplots(3)

axs1[0].plot(t, x)
axs1[1].plot(t, y)
axs1[2].plot(t, z)

for ax in axs1.flat:
    ax.set_xlim([0, 0.03])

plt.savefig('grafic_ex1b.pdf')

fs = 200
T = 1 / fs

samples_es = int(numpy.round(0.03 / T)) + 1
t_es = numpy.linspace(0, 0.03, samples_es)

x_es = numpy.cos(520 * numpy.pi * t_es + numpy.pi / 3)
y_es = numpy.cos(280 * numpy.pi * t_es - numpy.pi / 3)
z_es = numpy.cos(120 * numpy.pi * t_es + numpy.pi / 3)

fig2, axs2 = plt.subplots(3)

axs2[0].stem(t_es, x_es)
axs2[1].stem(t_es, y_es)
axs2[2].stem(t_es, z_es)

for ax in axs2.flat:
    ax.set_xlim([0, 0.03])

plt.savefig('grafic_ex1c.pdf')
plt.show()




