import logging

import tkinter
from tkinter import filedialog as fd

import os
import numpy as np

import tecplot
from tecplot.exception import *
from tecplot.constant import *

import sys

logging.basicConfig(level=logging.DEBUG)

# Run this script with "-c" to connect to Tecplot 360 on port 7600
# To enable connections in Tecplot 360, click on:
#   "Scripting" -> "PyTecplot Connections..." -> "Accept connections"

if '-c' in sys.argv:
    tecplot.session.connect()

turbVariables = 1
wallRegions = 5
inletRegions = 2
rotationRate = 3500
radiusPropeller = 21 * 0.0254 / 2

views = [

    # ["Name", View width, X, Y, Z, Psi, Theta, Alpha]
    ["Bottom", 0.28, -0.13837, -0.0118782, 10, 0.00, 0.00, 0.00],
    ["Top", 0.28, -0.13837, -0.00469803, -27.2985, 180.00, -180.00, 0.00]
]

radii = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 98]


def convertData():
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="SetFieldVariables ConvectionVarsAreMomentum='F' UVarNum=6 VVarNum=7 WVarNum=8 ID1='Density' Variable1=4 ID2='NotUsed' Variable2=0")
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="Calculate Function='GRIDKUNITNORMAL' Normalization='None' ValueLocation='Nodal' CalculateOnDemand='T' UseMorePointsForFEGradientCalculations='F'")
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="Calculate Function='VELOCITYMAG' Normalization='None' ValueLocation='Nodal' CalculateOnDemand='T' UseMorePointsForFEGradientCalculations='F'")

    tecplot.data.operate.execute_equation(equation='{px} = -({Pressure (N/m^2)}-101325) * {X Grid K Unit Normal}')
    tecplot.data.operate.execute_equation(equation='{py} = -({Pressure (N/m^2)}-101325)  * {Y Grid K Unit Normal}')
    tecplot.data.operate.execute_equation(equation='{pz} = -({Pressure (N/m^2)}-101325)  * {Z Grid K Unit Normal}')
    tecplot.data.operate.execute_equation(equation='{mx} = Y * {pz} - Z * {py}')
    tecplot.data.operate.execute_equation(equation='{my} = Z * {px} - X * {pz}')
    tecplot.data.operate.execute_equation(equation='{mz} = X * {py} - Y * {px}')
    tecplot.data.operate.execute_equation(
        equation='{taux} = {SF1-shear stress (Pa); Shear} - {X Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
    tecplot.data.operate.execute_equation(
        equation='{tauy} = {SF2-shear stress (Pa)} - {Y Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
    tecplot.data.operate.execute_equation(
        equation='{tauz} = {SF3-shear stress (Pa)} - {Z Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
    tecplot.data.operate.execute_equation(equation='{mxt} = Y * {tauz} - Z * {tauy} ')
    tecplot.data.operate.execute_equation(equation='{myt} = Z * {taux} - X * {tauz}')
    tecplot.data.operate.execute_equation(equation='{mzt} = X * {tauy} - Y * {taux}')
    tecplot.data.operate.execute_equation(
        equation='{ShearStress} = sqrt({SF1-shear stress (Pa); Shear}**2+ {SF2-shear stress (Pa)}**2+ {SF3-shear stress (Pa)}**2)')
    tecplot.data.operate.execute_equation(equation='{rot} = -' + str(rotationRate) + '/60')
    tecplot.data.operate.execute_equation(equation='{vx} = {V1-velocity (m/s); Velocity} - 2 * 3.14159265 *  Y * {rot}')
    tecplot.data.operate.execute_equation(equation='{vy} = {V2-velocity (m/s)} + 2 * 3.14159265 *  X * {rot}')
    tecplot.data.operate.execute_equation(equation='{vmag} =  sqrt({vx}**2+ {vy}**2+ {V3-velocity (m/s)}**2)')


def prepareScene():

    tecplot.macro.execute_file('changePaperSize.mcr')

    tecplot.active_frame().plot().frame.width = 14
    tecplot.active_frame().plot().frame.height = 8
    tecplot.active_frame().plot().frame.position=(0,0)
    #tecplot.macro.execute_command('''$!PAGE
    #                PAPERATTRIBUTES
    #                    {
    #                        SHOWGRID = NO
    #                        PAPERSIZE = CUSTOM1
    #                        PAPERSIZEINFO
    #                        {
    #                            CUSTOM1
    #                                {
    #                                    WIDTH = 14
    #                                    HEIGHT = 8
    #                                }
    #                        }
    #                    }''')

    # hide inlets
    i = 1
    while (i <= inletRegions):
        plot.fieldmaps(i).show = False
        i = i + 1

    # Hide Outlet and periodics
    plot.fieldmaps(inletRegions + wallRegions + 1).show = False
    plot.fieldmaps(inletRegions + wallRegions + 2).show = False
    plot.fieldmaps(inletRegions + wallRegions + 3).show = False

    # Rotate Data
    tecplot.macro.execute_command('''$!AxialDuplicate 
      ZoneList =  [''' + str(inletRegions + 2) + '-' + str(inletRegions + wallRegions + 1) + ''']
      Angle = 180
      NumDuplicates = 1
      XVar = 1
      YVar = 2
      ZVar = 3''')

    tecplot.macro.execute_command('$!GlobalThreeD RotateOrigin{X = 0}')
    tecplot.macro.execute_command('$!GlobalThreeD RotateOrigin{Y = 0}')
    tecplot.macro.execute_command('$!GlobalThreeD RotateOrigin{Z = 0}')


def saveData():
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="Integrate [" + str(inletRegions + 2) + '-' + str(
                                               inletRegions + wallRegions + 1) + "] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=" + str(
                                               33 + turbVariables) + " Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="SaveIntegrationResults FileName='" + path.replace("\\",
                                                                                                      "\\\\") + '\\\\PostPro\\\\Plots\\\\TZ.txt' + "'")
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="Integrate [" + str(inletRegions + 2) + '-' + str(
                                               inletRegions + wallRegions + 1) + "] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=" + str(
                                               30 + turbVariables) + " Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="SaveIntegrationResults FileName='" + path.replace("\\",
                                                                                                      "\\\\") + '\\\\PostPro\\\\Plots\\\\PZ.txt' + "'")
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="Integrate [" + str(inletRegions + 2) + '-' + str(
                                               inletRegions + wallRegions + 1) + "] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=" + str(
                                               36 + turbVariables) + " Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="SaveIntegrationResults FileName='" + path.replace("\\",
                                                                                                      "\\\\") + '\\\\PostPro\\\\Plots\\\\MZ.txt' + "'")


def saveViews():
    density()
    pressure()
    velocity()
    shearstress()
    pressuretz()
    pressurez()
    momentz()


def density():
    plot.contour(0).variable_index = 3
    plot.contour(0).colormap_name = 'Large Rainbow'
    plot.contour(0).levels.reset_levels(np.linspace(1.2, 1.3, 21))
    plot.show_contour = True
    plot.show_shade = False
    plot.contour(0).legend.vertical = False
    plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
    plot.contour(0).legend.position = (50, 5)
    plot.contour(0).labels.step = 5
    savePicture("Density")


def pressure():
    plot.contour(0).variable_index = 4
    plot.contour(0).colormap_name = 'Large Rainbow'
    plot.contour(0).levels.reset_levels(np.linspace(97000, 106000, 21))
    plot.show_contour = True
    plot.show_shade = False
    plot.contour(0).legend.vertical = False
    plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
    plot.contour(0).legend.position = (50, 5)
    plot.contour(0).labels.step = 5
    savePicture("Pressure")


def velocity():
    plot.contour(0).variable_index = 40 + turbVariables
    plot.contour(0).colormap_name = 'Large Rainbow'
    plot.contour(0).levels.reset_levels(np.linspace(0, 150, 21))
    plot.show_contour = True
    plot.show_shade = False
    plot.contour(0).legend.vertical = False
    plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
    plot.contour(0).legend.position = (50, 5)
    plot.contour(0).labels.step = 5
    savePicture("Velocity")


def shearstress():
    plot.contour(0).variable_index = 36 + turbVariables
    plot.contour(0).colormap_name = 'Large Rainbow'
    plot.contour(0).levels.reset_levels(np.linspace(0, 150, 21))
    plot.show_contour = True
    plot.show_shade = False
    plot.contour(0).legend.vertical = False
    plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
    plot.contour(0).legend.position = (50, 5)
    plot.contour(0).labels.step = 5
    savePicture("ShearStress")


def pressuretz():
    plot.contour(0).variable_index = 32 + turbVariables
    plot.contour(0).colormap_name = 'Large Rainbow'
    plot.contour(0).levels.reset_levels(np.linspace(-4100, 4100, 21))
    plot.show_contour = True
    plot.show_shade = False
    plot.contour(0).legend.vertical = False
    plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
    plot.contour(0).legend.position = (50, 5)
    plot.contour(0).labels.step = 5
    savePicture("PressureTZ")


def pressurez():
    plot.contour(0).variable_index = 29 + turbVariables
    plot.contour(0).colormap_name = 'Large Rainbow'
    plot.contour(0).levels.reset_levels(np.linspace(-4100, 4100, 21))
    plot.show_contour = True
    plot.show_shade = False
    plot.contour(0).legend.vertical = False
    plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
    plot.contour(0).legend.position = (50, 5)
    plot.contour(0).labels.step = 5
    savePicture("PressureZ")


def momentz():
    plot.contour(0).variable_index = 35 + turbVariables
    plot.contour(0).colormap_name = 'Large Rainbow'
    plot.contour(0).levels.reset_levels(np.linspace(-1200, 1200, 21))
    plot.show_contour = True
    plot.show_shade = False
    plot.contour(0).legend.vertical = False
    plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
    plot.contour(0).legend.position = (50, 5)
    plot.contour(0).labels.step = 5
    savePicture("MomentZ")


def savePicture(name):
    for view in views:
        plot.view.width = view[1]
        plot.view.position = (view[2], view[3], view[4])
        plot.view.psi = view[5]
        plot.view.theta = view[6]
        plot.view.alpha = view[7]

        tecplot.export.save_png(path + '\\PostPro\\' + name + '\\' + name + '_' + view[0] + '.png',
                                width=1920,
                                region=ExportRegion.AllFrames,
                                supersample=1,
                                convert_to_256_colors=False)


def setupslices():
    frame.plot_type = tecplot.constant.PlotType.XYLine

    for radius in radii:
        tecplot.active_frame().plot_type = PlotType.Cartesian3D
        # extract an arbitrary slice from the surface data on the wing
        extracted_slice = tecplot.data.extract.extract_slice(
            origin=(radiusPropeller * radius / 100, 0, 0),
            normal=(1, 0, 0),
            source=tecplot.constant.SliceSource.SurfaceZones,
            dataset=dataset)

        tecplot.active_frame().plot_type = PlotType.XYLine
        plot = frame.plot()
        plot.delete_linemaps()
        extracted_slice.name = str(radius)

        # get x from slice
        extracted_x = extracted_slice.values('y')

        # copy of data as a numpy array
        x = extracted_x.as_numpy_array()

        # normalize x
        xc = (x - x.min()) / (x.max() - x.min())
        extracted_x[:] = xc

        # switch plot type in current frame
        # clear plot

        # create line plot from extracted zone data
        cp_linemap = plot.add_linemap(
            name=extracted_slice.name,
            zone=extracted_slice,
            x=dataset.variable('y'),
            y=dataset.variable('Pressure (N/m^2)'))

        # overlay result on plot in upper right corner
        text = frame.add_text(str(radius), (50, 95))

        # set style of linemap plot
        cp_linemap.line.color = tecplot.constant.Color.Blue
        cp_linemap.line.line_thickness = 0.2
        cp_linemap.y_axis.reverse = True

        # update axes limits to show data
        plot.view.fit()
        tecplot.active_frame().plot().axes.y_axis(0).title.font.size = 2.6
        tecplot.active_frame().plot().axes.y_axis(0).title.text = 'Pressure [Pa]]'
        tecplot.active_frame().plot().axes.y_axis(0).title.offset = 11
        # tecplot.active_frame().plot().axes.area.left = 15

        tecplot.active_frame().plot().axes.x_axis(0).title.text = 'Chord [-]'
        plot.view.fit()
        plot.axes.y_axis(0).min = 95000
        plot.axes.y_axis(0).max = 105000

        # export image of pressure coefficient as a function of x/c
        tecplot.export.save_png(path + '\\PostPro\\Slices\\' + str(radius) + '.png', 1920, supersample=3)
        text.text_string = ""


# Open File
tecplot.new_layout()

tkinter.Tk().withdraw()
filename = fd.askopenfilename()
path, file = os.path.split(filename)
dataset = tecplot.data.load_tecplot(filename)

# Get default variables
frame = tecplot.active_frame()
plot = frame.plot()

convertData()
saveData()
prepareScene()
saveViews()
setupslices()

# Save if not alreadt plt
if not filename.endswith('.plt'):
    tecplot.data.save_tecplot_plt(path + '\\soln.plt',
                                  include_text=False,
                                  include_geom=False,
                                  include_data_share_linkage=True)
