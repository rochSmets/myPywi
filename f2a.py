#
#
#
import sys
import os
#
# .. add the path
sys.path.append(os.path.join(os.environ['PYWI_DIR'], 'runs'))
sys.path.append(os.path.join(os.environ['PYWI_DIR'], 'shapes'))
sys.path.append(os.path.join(os.environ['PYWI_DIR'], 'draws'))
#
# .. import the modulus
from heckle import Heckle
from field import Field
from colp import Colp
from col import myColor
#
import numpy as np
#
# .. load the run
run       = Heckle('/run/media/smets/croq0Disk/blAckDog/L17-Cu.a/', 'Nb')
time      = 40.0
component = 'y'
specie    = 'a'
#
strt = '$t = {0:4.1f}$'.format(time)
#
# .. get the data at the given time
# data = run.getB(time, component)
# data = run.getJ(time, component)
data = run.getV(time, specie, component)
# data = run.getN(time, specie)
flux = run.getA(time, 'z', 'fftw') # fft, fftw, fdm, fem
#
# .. set the needed parameter to plot the 2d field
domain    = None #[[20, 80], [5, 45]]
shifts    = None #[-50, -25]
bounds    = None #[-0.26, +0.26] #[0.16, 0.32]
colormap  = myColor('greyPurple', 16)
flines    = 6
ticks     = None #[10, 10]
subticks  = None
text      = None #[strt]
xytext    = [[-28, +22]]
figsize   = [4.6, 5.4]
filetype  = 'pdf'
#
limit = [[0, run.domsize[0]], [0, run.domsize[1]]]
#
# .. load the data for image
im0 = Field(limit = limit,
            data = data,
            domain = domain,
            shifts = shifts)
#
# .. load the data for contours
im1 = Field(limit = limit,
            data = flux,
            domain = domain,
            stride = None,
            section = None,
            shifts = shifts,
            labels = None)
#
# .. draw the plot
plo = Colp(coloraxis = im0.axis,
           colordata = im0.data,
           bounds = bounds,
           colormap = colormap,
           contouraxis = im1.axis,
           contourdata = im1.data,
           flines = flines,
           arrowaxis = None,
           arrowdata = None,
           labels = im0.labels,
           ticks = ticks,
           subticks = subticks,
           colorbar = True,
           text = text,
           xytext = xytext,
           figsize = figsize,
           filetype = filetype)
#
