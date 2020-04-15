#
#
#
import sys
import os
#
# .. add the path
sys.path.append(os.environ['PYWI_DIR'])
sys.path.append(os.path.join(os.environ['PYWI_DIR'], 'runs'))
sys.path.append(os.path.join(os.environ['PYWI_DIR'], 'shapes'))
sys.path.append(os.path.join(os.environ['PYWI_DIR'], 'draws'))
#
# .. import the modulus
import heckle
import ohm
import field
import linp
#
#
# .. load the run
run = heckle.Heckle('/run/media/smets/croq0Disk/blAckDog/L17-Cu.a/', '')
#
time = 60.0
component = 'z'
#
drift = ohm.drift    (run, time, 'ions',      component, terms = 'all')
hall  = ohm.hall     (run, time,              component, terms = 'all')
gradP = ohm.gradP    (run, time, 'electrons', component, terms = 'all')
resis = ohm.resistive(run, time,              component               )
hyper = ohm.hyper    (run, time,              component, terms = 'all')
#
print(hyper.min(), hyper.max())
# .. set the needed parameter to plot the 2d field
shifts    = None # list of shifts is considered after slice : lenght is 1
stride    = None
section   = [100.0, None]
shade     = None
diff      = None
drawstyle = None #['steps-mid', 'steps-mid', 'steps-mid', 'steps-mid', 'steps-mid']
linlog    = None
linestyle = ['-', '--', '-', '-.', ':']
linecolor = ['r', 'g', 'k', 'b', 'c']
linewidth = [1, 1, 1, 1, 1]
ticks     = None
subticks  = None
strticks  = None
extent    = [[140, 160], None]
marker    = None
legend    = None
text      = None
xytext    = None
labels    = ['$y \, d_0^{-1}$', '$E_z$']
figsize   = [4, 2.4]
filetype  = 'pdf'
filename  = None
#
limit = [[0, run.domsize[0]], [0, run.domsize[1]]]
#
# .. load the data for line plot
dri = field.Field(limit = limit,
                  data = drift,
                  domain = None,
                  stride = stride,
                  section = section,
                  shifts = shifts,
                  labels = None)
#
hal = field.Field(limit = limit,
                  data = hall,
                  domain = None,
                  stride = stride,
                  section = section,
                  shifts = shifts,
                  labels = None)
#
gra = field.Field(limit = limit,
                  data = gradP,
                  domain = None,
                  stride = stride,
                  section = section,
                  shifts = shifts,
                  labels = None)
#
res = field.Field(limit = limit,
                  data = resis,
                  domain = None,
                  stride = stride,
                  section = section,
                  shifts = shifts,
                  labels = None)
#
hyp = field.Field(limit = limit,
                  data = hyper,
                  domain = None,
                  stride = stride,
                  section = section,
                  shifts = shifts,
                  labels = None)
#
# .. draw the plot
plo = linp.Linp(axis = [dri.axis[0], hal.axis[0], gra.axis[0], res.axis[0], hyp.axis[0]],
                data = [dri.data,    hal.data,    gra.data,    res.data,    hyp.data],
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
