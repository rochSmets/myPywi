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
import linp
#
import numpy as np
#
# .. load the run
run = heckle.Heckle('/run/media/smets/croq0Disk/blAckDog/L17-Cu.a/', '')
#
time      = 70.0
component = 'x'
specie    = 'a'
#
# .. get the desired data giving time
dat1 = run.getN(time, specie)
dat2 = run.getB(time, component)
#
# .. set the needed parameter to plot the 2d field
shifts    = None #[-3] # list of shifts is considered after slice : lenght is 1
stride    = None #[None, 6]
section   = [100, None]
shade     = None #[[-2,2], [8,12]]
diff      = None
drawstyle = None #['steps-mid', None]
linlog    = None
linestyle = ['-', '-']
linecolor = ['r', 'k']
linewidth = [1, 1]
ticks     = None #[1, 0.5]
subticks  = None #[2, 2]
strticks  = None
extent    = [None, [-0.1, +4]] #[[-3, 3],[0, 2]]
marker    = None #['o']
legend    = None #['$B_of$']
text      = None #['$\mathrm{Proton~temperature~@~} t = 0.0$']
xytext    = None #[[-2.8, 1.8]]
labels    = ['$y/d_0$', '']
figsize   = [4.2, 2.4]
filetype  = 'pdf'
filename  = None
#
limit = [[0, run.domsize[0]], [0, run.domsize[1]]]
#
# .. load the data for line plot
li1 = field.Field(limit = limit,
                  data = dat1,
                  domain = None,
                  stride = stride,
                  section = section,
                  shifts = shifts,
                  labels = None)
#
li2 = field.Field(limit = limit,
                  data = dat2,
                  domain = None,
                  stride = stride,
                  section = section,
                  shifts = shifts,
                  labels = None)
#
# .. draw the plot
plo = linp.Linp(axis = [li1.axis[0], li2.axis[0]],
                data = [22*li1.data, np.fabs(li2.data)],
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
