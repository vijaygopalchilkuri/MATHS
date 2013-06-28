import numpy as np
import matplotlib
#matplotlib.use('PS')
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d,interp2d,bisplev,bisplrep
import os
import Ngl

def wrapper(thelist):
    for item in thelist:
        yield(item[0],item[1])

array = []
array1 = []
array2 = []
x = []
y = []
x1 = []
y1 = []
x2 = []
y2 = []
with open('/home/vijay/Documents/MATHS/graph/plt1.dat') as f:
    for line in f:
        array.append([float(j) for j in line.split()])
f.close

for a,b in wrapper(array):
    x.append(a)
    y.append(b)

with open('/home/vijay/Documents/MATHS/graph/plt2.dat') as f:
    for line in f:
        array1.append([float(j) for j in line.split()])
f.close

for a,b in wrapper(array1):
    x1.append(a)
    y1.append(b)

with open('/home/vijay/Documents/MATHS/graph/plt3.dat') as f:
    for line in f:
        array2.append([float(j) for j in line.split()])
f.close

for a,b in wrapper(array2):
    x2.append(a)
    y2.append(b)

wks_type = "ps"
wks = Ngl.open_wks(wks_type,"plot5")
res1 = Ngl.Resources()
res2 = Ngl.Resources()
res3 = Ngl.Resources()
# Don't maximize the plot in the frame, because we are controlling the
# size and location of both plots with the vpXXX resources.
#

res1.nglMaximize = False
res1.vpHeightF   = 0.75
res1.vpWidthF    = 0.65
res1.vpXF        = 0.20
res1.vpYF        = 0.90

#
# Set the actual limits of the X and Y axes.
#
res1.trXMinF     =   -1.0
res1.trXMaxF     =   1.
res1.trYMinF     =   -1.
res1.trYMaxF     =   1.
res1.trYReverse  = False

#
res1.nglMaximize           = False
res1.tiMainString          = "PhasePlot"
res1.tiXAxisString         = "K"
res1.tiYAxisString         = "U"
res1.tiXAxisFontHeightF    = 0.04
res1.tiYAxisFontHeightF    = 0.04

res1.xyLineColor           = "red"
res1.xyLineThicknessF      = 3.0

plot1 = Ngl.xy(wks,x,y,res1)

# Second plot

res2.nglMaximize = False
res2.vpHeightF   = res1.vpHeightF
res2.vpWidthF    = res1.vpWidthF
res2.vpXF        = res1.vpXF
res2.vpYF        = res1.vpYF

#
# Since the two plots share the same X data, the two trX**** resources
# make sure the X axis limits are the same for the second plot.
#
res2.trXMinF = res1.trXMinF
res2.trXMaxF = res1.trXMaxF
res2.trYMinF = res1.trYMinF
res2.trYMaxF = res1.trYMaxF
#res2.trYMaxF = 60.
#res2.trYMinF = 10.
res2.xyLineColor           = "blue"

#
res2.tmXBOn       = False
res2.tmXBLabelsOn = False
res2.tmXBMinorOn  = False
res2.tmYLOn       = False
res2.tmYLLabelsOn = False
res2.tmYLMinorOn  = False

#
# Turn on the right Y labels and tickmarks and move the axis string to
# the right.
#
res2.tmYRLabelsOn = False
res2.tmYROn       = False
res2.tmYUseLeft   = False
res2.tmYRFormat   = "f"      # Gets rid of unnecessary trailing zeros

plot2 = Ngl.xy(wks,x1,y1,res2)

# Second plot

res3.nglMaximize = False
res3.vpHeightF   = res1.vpHeightF
res3.vpWidthF    = res1.vpWidthF
res3.vpXF        = res1.vpXF
res3.vpYF        = res1.vpYF

#
# Since the two plots share the same X data, the two trX**** resources
# make sure the X axis limits are the same for the second plot.
#
res3.trXMinF = res1.trXMinF
res3.trXMaxF = res1.trXMaxF
res3.trYMinF = res1.trYMinF
res3.trYMaxF = res1.trYMaxF
#re32.trYMaxF = 60.
#re32.trYMinF = 10.
res3.xyLineColor           = "green"

#
res3.tmXBOn       = False
res3.tmXBLabelsOn = False
res3.tmXBMinorOn  = False
res3.tmYLOn       = False
res3.tmYLLabelsOn = False
res3.tmYLMinorOn  = False

#
# Turn on the right Y labels and tickmarks and move the axis string to
# the right.
#
res3.tmYRLabelsOn = False
res3.tmYROn       = False
res3.tmYUseLeft   = False
res3.tmYRFormat   = "f"      # Gets rid of unnecessary trailing zeros

plot3 = Ngl.xy(wks,x2,y2,res3)

# Two plots

sres = Ngl.Resources()
Ngl.set_values(plot1,sres)

sres = Ngl.Resources()
Ngl.set_values(plot2,sres)

sres = Ngl.Resources()
Ngl.set_values(plot3,sres)

Ngl.draw(plot1)
Ngl.draw(plot2)
Ngl.draw(plot3)
Ngl.frame(wks)
