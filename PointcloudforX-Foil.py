
import os
import numpy as np
import tecplot
from tecplot.exception import *
from tecplot.constant import *
import sys
import math
import logging

logging.basicConfig(level=logging.DEBUG)

# Run this script with "-c" to connect to Tecplot 360 on port 7600
# To enable connections in Tecplot 360, click on:
#   "Scripting" -> "PyTecplot Connections..." -> "Accept connections"

if '-c' in sys.argv:
    tecplot.session.connect()

File = "C:\\Users\\nicol\\OneDrive\\Desktop\\21x13coarse.stl"
saveFolder = "C:\\Users\\nicol\\OneDrive\\Desktop\\21x13Coarse"
radiusPropeller = -21 * 0.0254 / 2 * 1000  # Propeller radius in meter

radii = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 94.5, 95, 95.5, 98, 99, 99.5, 99.55]

tecplot.new_layout()
frame = tecplot.active_frame()
plot = frame.plot()

dataset = tecplot.data.load_stl(File)



frame.plot_type = tecplot.constant.PlotType.XYLine

# make Folder
try:
    os.mkdir(saveFolder)
    os.mkdir(saveFolder + "\\Plots")
except:
    pass

# Loop over all radii for the plot creation
for radius in radii:

    tecplot.active_frame().plot_type = PlotType.Cartesian3D

    # extract an arbitrary slice from the surface data on the propeller
    extracted_slice = tecplot.data.extract.extract_slice(
        origin=(radiusPropeller * radius / 100, 0, 0),
        normal=(1, 0, 0),
        source=tecplot.constant.SliceSource.SurfaceZones,
        dataset=dataset)

    tecplot.active_frame().plot_type = PlotType.XYLine
    plot = frame.plot()
    plot.delete_linemaps()
    extracted_slice.name = str(radius)

    # get variables from slice
    extracted_y = extracted_slice.values('y')
    extracted_x = extracted_slice.values('X')
    extracted_z = extracted_slice.values('Z')

    # copy of data as a numpy array
    x = extracted_x.as_numpy_array()
    y = extracted_y.as_numpy_array()
    z = extracted_z.as_numpy_array()

    # create empty arrays for later population
    arr = np.empty(z.size)  # Array for the wrapping distance
    dist = np.empty(z.size)  # Array for the distance between points
    i = 0  # iteration variable

    # Sort the point along the line, starting from the first element
    while i < z.size - 1:
        for idx, value in np.ndenumerate(z):
            if idx[0] > i:
                dist[idx[0]] = math.sqrt((y[idx[0]] - y[i]) ** 2 + (z[idx[0]] - z[i]) ** 2)
            else:
                dist[idx[0]] = 100
        pos = np.argmin(dist)

        y[i + 1], y[pos] = y[pos], y[i + 1]
        z[i + 1], z[pos] = z[pos], z[i + 1]
        i = i + 1

    # Integrate the distance along the line
    for idx, value in np.ndenumerate(z):
        if idx[0] > 0:
            arr[idx[0]] = math.sqrt((y[idx[0]] - y[idx[0] - 1]) ** 2 + (z[idx[0]] - z[idx[0] - 1]) ** 2) + arr[
                idx[0] - 1]
        else:
            arr[idx[0]] = 0

    # Find the starting point and fix the orientation of the line
    i = 0
    maxd = 0
    maxind1 = 0
    maxind2 = 0
    while i < z.size - 1:

        for idx, value in np.ndenumerate(z):
            dist[idx[0]] = math.sqrt((y[idx[0]] - y[i]) ** 2 + (z[idx[0]] - z[i]) ** 2)

        if dist.max(initial=-100000000) > maxd:
            maxind1 = i
            maxind2 = np.argmax(dist)
            maxd = dist.max(initial=-100000000)

        i = i + 1


    # Set the start of the lines appropriately still to be done
    if y[maxind1] < y[maxind2]:
        arr = arr - arr[maxind1]

    else:
        arr = arr - arr[maxind2]

    # Create new zone with the line and the results
    zone = dataset.add_ordered_zone('variable', z.size)
    zone.values('x')[:] = y
    zone.values('y')[:] = z

    extracted_x[:] = arr
    plot.delete_linemaps()

    # create line plot from extracted zone data
    linemap = plot.add_linemap(
        name=radius,
        zone=zone,
        x=dataset.variable('x'),
        y=dataset.variable('y'))

    # overlay result on plot in upper right corner
    text = frame.add_text("Position: " + str(radius), (50, 95))
    text.anchor = TextAnchor.Center
    # set style of linemap plot
    linemap.line.color = tecplot.constant.Color.Blue
    linemap.line.line_thickness = 0.2
    linemap.y_axis.reverse = False

    # update axes limits to show data
    plot.view.fit()
    tecplot.active_frame().plot().axes.y_axis(0).title.font.size = 2.6
    tecplot.active_frame().plot().axes.y_axis(0).title.title_mode = AxisTitleMode.UseText
    tecplot.active_frame().plot().axes.y_axis(0).title.text = "X [m]"
    tecplot.active_frame().plot().axes.y_axis(0).title.offset = 11
    # tecplot.active_frame().plot().axes.area.left = 15
    tecplot.active_frame().plot().axes.x_axis(0).title.title_mode = AxisTitleMode.UseText
    tecplot.active_frame().plot().axes.x_axis(0).title.text = 'Y [m]'

    file_object = open(saveFolder + '\\out.csv', 'a+')

    for idx, val in enumerate(y):
        file_object.write("\n%s,%s,%s" % (radius, val, z[idx]))
    plot.legend.show = False


    plot.view.fit()

    # export image of pressure coefficient as a function of x/c
    tecplot.export.save_png(
        saveFolder + '\\' + str(radius) + '.png', 1920,
        supersample=1)
    text.text_string = ""
    file_object.close()
    tecplot.active_frame().dataset.delete_zones(zone)





