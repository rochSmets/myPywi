#
#
import sys
import os
import numpy as np
#
# .. add the path
sys.path.append(os.path.join(os.environ['PYWI_DIR'], 'runs'))
sys.path.append(os.path.join(os.environ['PYWI_DIR'], 'shapes'))
sys.path.append(os.path.join(os.environ['PYWI_DIR'], 'draws'))
#
# .. import the modulus
from heckle import Heckle
from fourier import Fourier
from colp import Colp
#
#
# .. load the run
run = Heckle('/home/roch/sherpa/heckle/munster/', 'zobi')
#
# .. set the needed parameter to plot the 2d field
#plane     = "xy"
#domain    = None
field = 'mod'
domain = 'full'
#cut       = 0.0
time      = [0, 20]
#shifts    = [-4, -2]
bounds    = [0, 1000]
colormap  = ['jet', 64]
#flines    = None
ticks     = None
subticks  = None
figsize   = [9, 6]
filetype  = None
#
#
# get the list of times & timegroups
mytimes, mygroups = run.getTimeGroups(time)
#
ds = float(run.dl)
dt = float(mytimes[1]-mytimes[0])
#
numoftimes = mytimes.__len__()
numofcells = int(run.ncells)+1
#
data = np.empty([numoftimes, numofcells], dtype = complex, order = 'C')
#
# then fill the data for input fft
for it in range(mytimes.__len__()) :
    data[it, :].real = run.GetB(mytimes[it])[..., 2]
    data[it, :].imag = 0.0
#
f = Fourier(data, field = field, domain = domain)
#
#
# .. draw the plot
plo = Colp(colordata = [f.xdata/float(run.dl), f.ydata/float(mytimes[1]-mytimes[0]), f.zdata],
           bounds = bounds,
           colormap = colormap,
           contourdata = None,
           flines = None,
           arrowdata = None,
           labels = ['$k$', '$\omega$'],
           ticks = ticks,
           subticks = subticks,
           figsize = figsize,
           filetype = filetype)
#
