#!/usr/bin/env python
# vim:set ts=4 sts=4 sw=4 et:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def diag(ax=None):
    """Plot a diagonal (identity) line, e.g. for use in correlation plots."""
    if ax is None:
        ax = plt.gca()
    lim_min = np.min((ax.get_xlim(), ax.get_ylim()))
    lim_max = np.max((ax.get_ylim(), ax.get_xlim()))
    diag_line, = ax.plot([lim_min, lim_max], [lim_min, lim_max], ls="--", c="0.0")
    return ax



def corr(x, y, ax=None, cmap='Greys', logscale=False, **kwargs):
    """Plot a 2D histogrammed correlation."""
    if ax is None:
        ax = plt.gca()
    plt.set_cmap(cmap)
    if logscale:
        c_norm = mpl.colors.LogNorm()
        c, xe, ye, img = ax.hist2d(x, y, norm=c_norm, **kwargs)
    else:
        c, xe, ye, img = ax.hist2d(x, y, **kwargs)
    plt.colorbar(img, ax=ax)
    return ax


def bar(dat, binlims, ax=None, fill=False, **kwargs):
    """Make a barplot of a precomputed histogram."""
    if ax is None:
        ax = plt.gca()
    # Assumes equally sized dat
    width = binlims[1] - binlims[0]
    center = (binlims[:-1] + binlims[1:]) / 2
    return ax.bar(center, dat, align='center', width=width, fill=fill, **kwargs)


def hist(dat, binlims, yerr=None, ax=None, log=False, **kwargs):
    """Plot a precomputed histogram.

    The method to plot the histograms steps is adapted from:
    http://stackoverflow.com/questions/5328556/histogram-matplotlib
    """
    if ax is None:
        ax = plt.gca()
    try:
        label = kwargs['label']
        del kwargs['label']
    except KeyError:
        label = None
    if log:
        ax.set_yscale('log')

    # Draw steps & errorbars separately
    # Using the option
    #   drawstyle='steps-mid'
    # in ax.errorbars screws up left half of first bin
    if yerr is not None:
        # Plot errorbars at bincenter
        bin_centers = 0.5*(binlims[1:] + binlims[:-1])
        ax.errorbar(bin_centers, dat,
                yerr=yerr,
                fmt=None,
                **kwargs
        )

    left, right = binlims[:-1], binlims[1:]
    x = np.array([left, right]).T.flatten()
    y = np.array([dat, dat]).T.flatten()
    if yerr is not None:
        # Get color from last line, so errors and line got the same color
        col = ax.lines[-1].get_color()
        return ax.plot(x, y, color=col, label=label, **kwargs)
    else:
        return ax.plot(x, y, label=label, **kwargs)


def pretty(ax=None, almost_black = '#262626', light_grey = '#F8F8F8'):
    """Apply prettyplotlit-like styling to axis."""
    if ax is None:
        ax = plt.gca()
    # Axes & ticks
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # coloring
    ax.spines['bottom'].set_color(almost_black)
    ax.spines['left'].set_color(almost_black)
    ax.title.set_color(almost_black)

    return ax


def legend(ax=None, on_top=False, ncol=None, almost_black = '#262626', light_grey = '#F8F8F8'):
    """Plot custom styled legend."""
    if ax is None:
        ax = plt.gca()
    if on_top:
        if ncol is None:
            ncol = len(ax.get_legend_handles_labels()[-1])
        leg = ax.legend(bbox_to_anchor= (0., 1.02, 1., 0.102),
                loc='upper center',
                mode='expand',
                ncol=ncol,
                frameon=True,
        )
    else:
        leg = ax.legend(loc=0, frameon=True)
    if leg is None:
        return None

    rect = leg.get_frame()
    rect.set_facecolor(light_grey)
    rect.set_linewidth(0.0)
    for text in leg.texts:
        text.set_color(almost_black)
    return leg
