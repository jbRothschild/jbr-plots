import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import LogNorm
#from mpltools import style

#colours = cm.BuPu(np.linspace(0.2, 1, 10) #0.2-1: range, 10: number of colours
#plt.style.use('seaborn-deep')
font = {'family':'Freeserif','size':16, 'serif': ['computer modern roman']}
plt.rc('font',**font)
plt.rcParams['image.cmap'] = 'inferno'

#figsize = layout.figaspect(scale=1.2)
#fig, axes = plt.subplots(ncols=2, nrows=2, figsize=figsize)
#ax1, ax2, ax3, ax4 = axes.ravel()

def animation2D(z, title="Title", xlab="x-axis", ylab="y-axis", xlimit=(0,1000), ylimit=(0,1000)):
    "This function is not working really well. Need to redo."
    fig = plt.figure()
    ax = plt.axes()
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)

    ims = []
    for i in range(len(z[:,0,0])):
        im = plt.contourf(z[i], 25, cmap=plt.cm.inferno)
        ims.append([im])

    interval = 2
    ani = animation.FuncAnimation(fig, ims, 5, interval=interval*1e+3, blit=False)

def plotSlider3D(x, y, z, value, levels=25, title="Title", xlab="x-axis", ylab="y-axis"):
    """
    Function that plots a 2D heat map of z along the dimensions x and y.

    Args:
        x(array[unknown]): Values along x-axis.
        y(array[unknown]): Values along y-axis.
        z(array[unknown]): Values along z-axis, axis that we will slide along.
        value(array[unknown][unknown][unkown]): Function that is plotted.
        levels(int): Number of countour levels.
        title(string): Title of plot.
        xlab(string): x-axis label.
        ylab(string): y-axis label.
    Returns:
        None
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.subplots_adjust(left=0.25, bottom=0.25)

    C = ax.contourf(x, y, value[:,:,0], levels, cmap=plt.cm.inferno)
    ax.title(title)
    ax.xlabel(xlab)
    ax.ylabel(ylab)

    z_slider_ax = fig.add_axes([0.25, 0.1, 0.65, 0.03], axisbg=axis_color)
    z_slider = Slider(z_slider_ax, 'z-axis', 0, 30.0, valinit=freq_0)
    def sliders_on_changed(val):
        ax.contourf(x, y, value[:,:,val],levels)
        fig.canvas.draw_idle()
    z_slider.on_changed(sliders_on_changed)

def plotHeat2D(x, y, z, lvls=25, title="Title", xlab="x-axis", ylab="y-axis", zlab="z-axis"):
    """
    Function that plots a 2D heat map of z along the dimensions x and y.

    Args:
        x(array[unknown]): Values along x-axis.
        y(array[unknown]): Values along y-axis.
        z(array[unknown][unknown]): Function that is plotted.
        levels(int): Number of countour levels.
        title(string): Title of plot.
        xlab(string): x-axis label.
        ylab(string): y-axis label.
    Returns:
        None
    """
    plt.contourf(x, y, z, cmap=plt.cm.inferno, norm=LogNorm(), levels=lvls)
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)

def plotHeat2D_NotLog(x, y, z, lvls=25, title="Title", xlab="x-axis", ylab="y-axis", zlab="z-axis"):
    """
    Function that plots a 2D heat map of z along the dimensions x and y.

    Args:
        x(array[unknown]): Values along x-axis.
        y(array[unknown]): Values along y-axis.
        z(array[unknown][unknown]): Function that is plotted.
        levels(int): Number of countour levels.
        title(string): Title of plot.
        xlab(string): x-axis label.
        ylab(string): y-axis label.
    Returns:
        None
    """
    plt.contourf(x, y, z, cmap=plt.cm.inferno, levels=lvls)
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)

def plot1D(x, y, title="Title", xlab="x-axis", ylab="y-axis"):
    """
    Function that plots a y as a function of x.

    Args:
        x(array[unknown]): Values along x-axis.
        y(array[unknown]): Values along y-axis.
        title(string): Title of plot.
        xlab(string): x-axis label.
        ylab(string): y-axis label.
    Returns:
        None
    """
    plt.plot(x, y, linewidth=2)
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)

def multi_plot(x, y, y_legend=[] ,title="Title", xlab="x-axis", ylab="y-axis"):
    """
    Function that plots multiple functions y as a function of x. Plots with a legend that is determined by the user

    Args:
        x(array[unknown]): Values along x-axis.
        y(array[n][unknown]): Values along y-axis for the n functions.
        title(string): Title of plot.
        xlab(string): x-axis label.
        ylab(string): y-axis label.
        y_legend(array[n]): array of strings, legend for each plot
    Returns:
        None
    """

    if y_legend==[]:
        for i in range(0, np.size(y,0)):
            plt.plot(x, y[i][:], linewidth=2)
    else:
        for i in range(0, np.size(y,0)):
            plt.plot(x, y[i][:], label=y_legend[i], linewidth=2)
            plt.legend(prop={'size': 12}) #legend details

    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
