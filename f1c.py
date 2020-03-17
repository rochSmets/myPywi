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
run = heckle.Heckle('/home/smets/codeS/hecKle/heckle4Me/', 'Nb-00')
#run = heckle.Heckle('/run/media/smets/croq0Disk/blAckDog/00b/', 'Nb-00')
#
time = 20.0
component = 1
#
drift = ohm.drift(run, time, 'ions')[..., component]
hall  = ohm.hall(run, time)[..., component]
gradP = ohm.gradP(run, time, 'electrons')[..., component]
resis = ohm.resistive(run, time)[..., component]
hyper = ohm.hyper(run, time)[..., component]
#
# .. set the needed parameter to plot the 2d field
shifts    = None # for a section, the list of shifts is considered after slice : so lenght is 1
stride    = None
section   = [3.0, None]
shade     = None
diff      = None
drawstyle = ['steps-mid', 'steps-mid', 'steps-mid', 'steps-mid', 'steps-mid']
linlog    = None
linestyle = ['-', '--', '-', '-.', ':']
linecolor = ['r', 'g', 'k', 'b', 'c']
linewidth = [1, 1, 1, 1, 1]
ticks     = None
subticks  = None
strticks  = None
extent    = [None, [-1.3, 1.3]]
marker    = None
legend    = None
text      = None
xytext    = None
labels    = ['$y \, d_0^{-1}$', '$E_z$']
figsize   = [6, 9]
filetype  = 'pdf'
filename  = None
#
#
# .. load the data for line plot
dri = field.Field(limit = [[0, run.domsize[0]], [0, run.domsize[1]]],
                  data = drift,
                  domain = None,
                  stride = stride,
                  section = section,
                  shifts = shifts,
                  labels = None)
#
hal = field.Field(limit = [[0, run.domsize[0]], [0, run.domsize[1]]],
                  data = hall,
                  domain = None,
                  stride = stride,
                  section = section,
                  shifts = shifts,
                  labels = None)
#
gra = field.Field(limit = [[0, run.domsize[0]], [0, run.domsize[1]]],
                  data = gradP,
                  domain = None,
                  stride = stride,
                  section = section,
                  shifts = shifts,
                  labels = None)
#
res = field.Field(limit = [[0, run.domsize[0]], [0, run.domsize[1]]],
                  data = resis,
                  domain = None,
                  stride = stride,
                  section = section,
                  shifts = shifts,
                  labels = None)
#
hyp = field.Field(limit = [[0, run.domsize[0]], [0, run.domsize[1]]],
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
                figsize = [5, 4],
                filetype = filetype,
                filename = filename)
#
