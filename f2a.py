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
import heckle
import field
import colp
import col
#
import numpy as np
#
# .. load the run
# run = heckle.Heckle('/data/run/blAckDog/02e/', 'Nb')
run = heckle.Heckle('/home/smets/shErpA/blAckDog/run/Nlas/l17-a', 'Nl')
# run       = heckle.Heckle('/run/media/smets/croq0Disk/blAckDog/H1a/', 'Nb')
time      = 0.0
component = 'x'
specie    = 'electrons'
#
strt = '$t = {0:4.1f}$'.format(time)
#
# .. get the data at the given time
# data = run.getJ(time, component)
# data = run.getV(time, specie, component)
data = run.getN(time, specie)
# data = run.getP(time, specie, component)
flux = run.fourierFlux(time)
#
# .. set the needed parameter to plot the 2d field
domain    = None #[[20, 80], [5, 45]]
shifts    = None #[-50, -25]
bounds    = None #[-0.26, +0.26] #[0.16, 0.32]
colormap  = ['hot', 16]
flines    = 16
ticks     = [10, 10]
subticks  = None
text      = None #[strt]
xytext    = [[-28, +22]]
figsize   = [4.6, 4.4]
filetype  = 'pdf'
#
limit = [[0, run.domsize[0]], [0, run.domsize[1]]]
#
colormap = col.mycolor('Purples', 16)
#
# .. load the data for image
im0 = field.Field(limit = limit,
                  data = data,
                  domain = domain,
                  shifts = shifts)
#
# .. load the data for contours
im1 = field.Field(limit = limit,
                  data = flux,
                  domain = domain,
                  stride = None,
                  section = None,
                  shifts = shifts,
                  labels = None)
#
# .. draw the plot
plo = colp.Colp(coloraxis = im0.axis,
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
