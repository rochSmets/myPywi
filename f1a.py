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
#
# .. load the run
run = heckle.Heckle('/home/smets/codeS/hecKle/heckle4Me/', 'Nb-00')
#
# .. get the desired data giving time
dat0 = run.GetPxx(0.0, "p")
dat1 = run.GetN(0.0, "p")
data = dat0/dat1
#
# .. set the needed parameter to plot the 2d field
shifts    = [-3] # for a section, the list of shifts is considered after slice : so lenght is 1
stride    = None #[None, 6]
section   = [3, None]
shade     = None #[[-2,2], [8,12]]
diff      = None
drawstyle = ['steps-mid']
linlog    = None
linestyle = ['-']
linecolor = ['k']
linewidth = [1]
ticks     = [1, 0.5]
subticks  = None #[2, 2]
strticks  = None
extent    = [[-3, 3],[0, 2]]
marker    = None #['o']
legend    = None #['$B_of$']
text      = ['$\mathrm{Proton~temperature~@~} t = 0.0$']
xytext    = [[-2.8, 1.8]]
labels    = ['$x/d_0$', '$T_i$']
figsize   = [4.2, 2.4]
filetype  = 'pdf'
filename  = None
#
#
# .. load the data for line plot
li0 = field.Field(run = run,
                  data = data,
                  domain = None,
                  stride = stride,
                  section=section,
                  shifts = shifts,
                  labels = None)
#
# .. draw the plot
plo = linp.Linp(axis = [li0.axis[0]],
                data = [li0.data],
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
