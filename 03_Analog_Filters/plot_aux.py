import numpy as np
import matplotlib.pyplot as plt


def clean_layout(fig, axs):
    for ax in axs:
        ax.margins(x=0)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.hlines(0, *ax.get_xlim(), linewidth=.75)
    fig.tight_layout()


def wc_vline(wc, ax, color):
    ax.vlines(wc, *ax.get_ylim(), color=color,
              linestyles='dashed', label=r'$\omega_c$')


def plot_custom_HY(w, wc, H, Y, label, figsize):
    fig, axs = plt.subplots(2, 1, sharex=True, figsize=figsize)

    ax = axs[0]
    ax.plot(w, H)
    ax.set_ylabel(r'$|H_{}(j\omega)|$'.format(label), fontsize=14)

    ax = axs[1]
    ax.plot(w, Y)
    ax.set_ylabel(r'$|Y_{}(j\omega)|$'.format(label), fontsize=14)
    ax.set_xticks(range(int(np.max(w) + 1)))
    ax.set_xlabel(r'$\omega$', fontsize=14)

    for ax in axs:
        wc_vline(wc, ax, 'k')
        ax.legend(fontsize=14)
    clean_layout(fig, axs)
