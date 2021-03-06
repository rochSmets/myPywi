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
#
# .. load the run
run = Heckle('/run/media/smets/croq0Disk/blAckDog/L17-Cu.a/', '')
#
# .. set the needed parameter to plot the 2d field
time      = [0, 98]
domain    = None # [[20, 80], [5, 45]]
shifts    = None #[-50, -25]
bounds    = [0, 5]
colormap  = myColor('viridis_r', 16)
flines    = 8
ticks     = None #[10, 10]
subticks  = None
xytext    = [[4, 280]]
figsize   = [4.61, 5.4]
basename  = 'f2c_'
filetype  = 'png'
#
limit = [[0, run.domsize[0]], [0, run.domsize[1]]]
#
# .. set index for begining & end of film
times, groups = run.getTimeGroups(time)
times.sort()
#
for index, time in enumerate(times) :

    text = ['$N_e \mathrm{~@~} t = \mathrm{~}$'+'${:6.1f}$'.format(time)]
    print('time : '+str(time)+' / '+str(times[-1]))
    data = run.getN(time, 'a')
    flux = run.getA(time, 'z', 'fftw')
    filename = basename+str(index)

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
               filename = filename,
               filetype = filetype)

# ffmpeg -i f2c_%d.png -pix_fmt yuv420p out.mp4
