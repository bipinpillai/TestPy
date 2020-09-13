from scipy.signal import chirp, spectrogram
import matplotlib.pyplot as plt
import numpy as np

fs = 500 #Hz
T = 10 #secs
t = np.linspace(0, T, T*fs)

ts = [0]*fs*1

frq = [0.2, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0]
#frq = 3.3 #Hz
for f in frq:
    sig = np.sin(2*np.pi*f*t)
    ts.extend(sig)
    print('sig=', len(sig))
    print('ts=', len(ts))

t1 = np.linspace(0, len(ts))
plt.plot(t1, ts)
plt.title("tmp")
plt.xlabel('t (sec)')
plt.show()