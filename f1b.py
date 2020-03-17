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
path      = '/run/media/smets/croq0Disk/blAckDog/02b/'
time      = None # [20, 22]
box       = [[40.0, 60.0], [24.0, 26.0]]
axis      = 1
shade     = None
diff      = None
step      = ['steps-mid']
linlog    = None
linestyle = ['-']
linecolor = ['k']
linewidth = [1]
ticks     = [20, 2]
subticks  = None
strticks  = None
extent    = [[0, 80], [0, 8]]
marker    = None
legend    = None
text      = None
xytext    = None
labels    = ['$t \, \Omega_0^{-1}$', '$A_z$']
figsize   = [4, 3]
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
                step = step,
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
                figsize = [5, 4],
                filetype = filetype,
                filename = filename)
#
