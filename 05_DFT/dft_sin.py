from numpy import abs, linspace, pi, sin
from numpy.fft import fft
from scipy.signal import freqz
import matplotlib.pyplot as plt


def dft_sin(N, f0, Nfft):

    n = linspace(0, 1, N)
    x = sin(2*pi*f0*n)
    Xk = fft(x, n=Nfft)
    XejW = freqz(x, whole=True)[1]

    fig, ax = plt.subplots(figsize=(16, 4))

    plt.scatter(linspace(0, 2*pi, Nfft + 1), list(abs(Xk)) + [abs(Xk[0])], c='r', label=r'$|X(k)|$')
    plt.plot(linspace(0, 2*pi, XejW.size + 1), list(abs(XejW)) + [abs(XejW[0])], label=r'$|X(e^{j\Omega})|$')

    plt.xlabel('$\Omega$ [rad]', fontsize=10)
    plt.xticks(ticks=[0, pi/2, pi, 3*pi/2, 2*pi],
               labels=[0, r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
    plt.grid(True)
    plt.legend(fontsize=12)

    ax.margins(x=0)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.hlines(0, *ax.get_xlim(), linewidth=.75)
    fig.tight_layout()

    plt.show()
