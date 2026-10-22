import numpy as np
import sounddevice
import scipy.io.wavfile


fs = 44100
ts = 1 / fs
n = np.arange(0, fs)

f1 = 675
f2 = 850
x1 = np.sin(2 * np.pi * f1 * n * ts)
x2 = np.sin(2 * np.pi * f2 * n * ts)

vec = np.concatenate((x1, x2))

sounddevice.play(vec, fs)
sounddevice.wait()

# al doilea semnal are mai multe oscilatii pe secunda si se aude mai subtire decat primul

scipy.io.wavfile.write('ConcatenareSunete.wav', fs, vec)