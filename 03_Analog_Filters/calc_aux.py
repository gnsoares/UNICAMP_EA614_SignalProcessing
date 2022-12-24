import numpy as np


def calcula_coeficientes(w, wc, n):
    Tn = np.zeros((w.size,))
    Tn[abs(w) < wc] = np.cos(n * np.arccos(w[abs(w) < wc] / wc))
    Tn[abs(w) >= wc] = np.cosh(n * np.arccosh(w[abs(w) >= wc] / wc))

    return Tn


def chebyshev(w, wc, n, e):
    Tn = calcula_coeficientes(w, wc, n)
    Habs = (1 + e**2 * Tn**2)**(-.5)

    return Habs


def butterworth(w, wc, n):
    Habs = (1 + (w / wc)**(2 * n))**(-.5)

    return Habs
