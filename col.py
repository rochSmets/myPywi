
from matplotlib import cm
import numpy as np
from matplotlib.colors import ListedColormap


def mycolor(name, num) :

    N2 = num//2
    N = 2*N2

    if name.lower() == 'coolspring' :
        bot = cm.get_cmap('cool', N2)
        top = cm.get_cmap('spring', N2)

        newcolors = np.vstack((bot(np.linspace(0, 1, N2)),
                               top(np.linspace(0, 1, N2))))

        colormap = [ListedColormap(newcolors, name='coolSpring'), N]

    elif name.lower() == 'greypurple' :
        bot = cm.get_cmap('Greys_r', N2)
        top = cm.get_cmap('Purples', N2)

        newcolors = np.vstack((bot(np.linspace(0, 1, N2)),
                               top(np.linspace(0, 1, N2))))

        colormap = [ListedColormap(newcolors, name='greyPurple'), N]

    else :
        colormap  = [name, num]

    return colormap
