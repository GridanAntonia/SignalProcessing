import numpy
import scipy.io.wavfile
import sounddevice

# Am modificat duratele de la ex2 ca sa reusesc sa am sunet si pentru semnalele de la a, c si d
# a
t_a = numpy.linspace(0, 3, 44100 * 3)
sig_a = numpy.sin(2 * numpy.pi * 400 * t_a)

# b
t_b = numpy.linspace(0, 3, 44100 * 3)
sig_b = numpy.sin(2 * numpy.pi * 800 * t_b)

# c
t_c = numpy.linspace(0, 3, 44100 * 3)
sig_c = 2 * numpy.mod(240 * t_c, 1) - 1

# d
t_d = numpy.linspace(0, 3, 44100 * 3)
sig_d = numpy.sign(numpy.sin(2 * numpy.pi * 300 * t_d))

fs = 44100

sounddevice.play(sig_a, fs)
sounddevice.wait()

sounddevice.play(sig_b, fs)
sounddevice.wait()

sounddevice.play(sig_c, fs)
sounddevice.wait()

sounddevice.play(sig_d, fs)
sounddevice.wait()

rate = int(10e5)
scipy.io.wavfile.write('SunetSemnal2b.wav', rate, sig_b)

rate_citit, x = scipy.io.wavfile.read('SunetSemnal2b.wav')
print(x)


