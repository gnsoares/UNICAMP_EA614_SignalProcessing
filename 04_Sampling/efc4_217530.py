# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav

from espectro import espectro
from kaiser import kaiser


# %%
def subsample(a, M):
    return np.array([a[n] for n in range(a.size) if n % M == 0])


# %%
Fs, y_stereo = wav.read('queen_I_want_it_all.wav')
y_mono = y_stereo[:, 0] + y_stereo[:, 1]


# %%
espectro(y_mono)


# %%
M = 6
y_dec = subsample(y_mono, M)
espectro(y_dec)


# %%
t1 = np.linspace(0, y_mono.size - 1, y_mono.size)
t2 = np.linspace(0, y_mono.size - 1, y_dec.size)
plt.plot(t1, y_mono)
plt.plot(t2, y_dec)


# %%
case1 = .45, 2
case2 = .45, .5
case3 = 1.5, 2
espectro(kaiser(*case1))
espectro(kaiser(*case2))
espectro(kaiser(*case3))


# %%
espectro(np.convolve(y_mono, kaiser(*case2)))
