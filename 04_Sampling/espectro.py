from math import pi
import numpy as np
import matplotlib.pyplot as plt


def espectro(y):
    """ Rotina que exibe o espectro de magnitude (X(ejw)) de um sinal discreto """

    # modulo da transf. de Fourier
    Y = np.abs(np.fft.fft(y))
    # frequencias avaliadas
    w = np.linspace(-pi, pi, Y.size)

    # exibe o grafico do espectro
    plt.figure() 
    plt.plot(w, np.roll(Y/np.max(Y), Y.size//2))
    plt.xlabel('$\Omega$ [rad]', fontsize=10)
    plt.ylabel('|$Y(e^{j\Omega})$|', fontsize=10)
    plt.grid(True)
    plt.xticks(
        ticks=[-pi, -pi/2, 0, pi/2, pi],
        labels=[r'$-\pi$', r'$-\pi/2$', 0, r'$\pi/2$', r'$\pi$']
    )
    plt.show()

    return Y
