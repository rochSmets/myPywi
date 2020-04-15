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
# .. set the needed parameter to plot the 2d field
time      = [0, 98]
shifts    = None #[-3] # the list of shifts is considered after slice : lenght is 1
stride    = None #[None, 6]
section   = [100, None]
shade     = None #[[-2,2], [8,12]]
diff      = None
drawstyle = None #['steps-mid', None]
linlog    = None
linestyle = ['-', '-', '-']
linecolor = ['r', 'g', 'b']
linewidth = [1, 1, 1]
ticks     = None #[1, 0.5]
subticks  = None #[2, 2]
strticks  = None
extent    = [None, [-0.1, +4.0]]
marker    = None #['o']
legend    = ['$N_e$', '$|B_x|$', '$|V_y|$']
xytext    = [[10.0, 3.6]]
labels    = ['$y/d_0$', '']
figsize   = [4.21, 2.41]
basename  = 'f1d_'
filetype  = 'png'
#
limit = [[0, run.domsize[0]], [0, run.domsize[1]]]
#
# .. set index for begining & end of film
times, groups = run.getTimeGroups(time)
times.sort()
#
for index, time in enumerate(times) :
    text = ['$t = \mathrm{~}$'+'${:6.1f}$'.format(time)]
    print('time : '+str(time)+' / '+str(times[-1]))

    dat1 = run.getN(time, 'a')
    dat2 = run.getB(time, 'x')
    dat3 = run.getV(time, 'i', 'y')

    filename = basename+str(index)

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
    li3 = field.Field(limit = limit,
                      data = dat3,
                      domain = None,
                      stride = stride,
                      section = section,
                      shifts = shifts,
                      labels = None)
    #
    # .. draw the plot
    plo = linp.Linp(axis = [li1.axis[0], li2.axis[0], li3.axis[0]],
                    data = [22*li1.data, np.fabs(li2.data), np.fabs(li3.data)],
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

# ffmpeg -i f1d_%d.png -pix_fmt yuv420p out.mp4
