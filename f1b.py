#
#
#
import sys
import os
#
# .. add the path
sys.path.append(os.environ['PYWI_DIR'])
sys.path.append(os.path.join(os.environ['PYWI_DIR'], 'draws'))
#
# .. import the modulus
import numpy as np
from reconnect import reconnectedFlux
import linp
#
#
#
# .. set the needed parameter to plot the 2d field
path      = '/run/media/smets/croq0Disk/blAckDog/L17-Cu.a/'
time      = [0, 90]
box       = [[90.0, 110.0], [140.0, 160.0]]
axis      = 1
shade     = None
diff      = None
drawstyle = None
linlog    = None
linestyle = ['-']
linecolor = ['k']
linewidth = [1]
ticks     = [20, 2]
subticks  = None
strticks  = None
extent    = None #[[0, 80], [0, 8]]
marker    = None
legend    = None
text      = None
xytext    = None
labels    = ['$t \, \Omega_0^{-1}$', '$A_z$']
figsize   = [4.0, 2.2]
filetype  = 'pdf'
filename  = 'Linp'
#
#
tim, ijx, Az, Ez = reconnectedFlux(path=path, time=time, xPointBox=box, axis=axis)
#
xdata = np.array(tim)
ydata = np.array(Az)
#
# .. draw the plot
plo = linp.Linp(axis = [xdata],
                data = [ydata],
                shade = shade,
                diff = diff,
                drawstyle = drawstyle,
                linlog = linlog,
                linestyle = linestyle,
                linecolor = linecolor,
                linewidth = linewidth,
                ticks = ticks,
                subticks = subticks,
                strticks = strticks,
                extent = extent,
                marker = marker,
                legend = legend,
                text = text,
                xytext = xytext,
                labels = labels,
                figsize = figsize,
                filetype = filetype,
                filename = filename)
#
