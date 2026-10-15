import numpy
import matplotlib.pyplot as plt

# a
t_a = numpy.linspace(0, 0.1, 1600)
sig_a = numpy.sin(2 * numpy.pi * 400 * t_a)

plt.figure()
plt.plot(t_a, sig_a)
plt.savefig('grafic_ex2a.pdf')

# b
t_b = numpy.linspace(0, 3, 24000)
sig_b = numpy.sin(2 * numpy.pi * 800 * t_b)

plt.figure()
plt.plot(t_b, sig_b)
plt.savefig('grafic_ex2b.pdf')

# c
t_c = numpy.linspace(0, 0.02, 1000)
sig_c = 2 * numpy.mod(240 * t_c, 1) - 1

plt.figure()
plt.plot(t_c, sig_c)
plt.savefig('grafic_ex2c.pdf')

# d
t_d = numpy.linspace(0, 0.02, 1000)
sig_d = numpy.sign(numpy.sin(2 * numpy.pi * 300 * t_d))

plt.figure()
plt.plot(t_d, sig_d)
plt.savefig('grafic_ex2d.pdf')

# e

plt.figure()
plt.imshow(numpy.random.rand(128, 128))
plt.savefig('grafic_ex2e.pdf')

# f

im = numpy.zeros((128, 128))
im[::16, :] = numpy.ones((8, 128))

plt.figure()
plt.imshow(im)
plt.savefig('grafic_ex2f.pdf')

plt.show()




