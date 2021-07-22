# Author Nicolas Mueller
#
# This code is meant to postprocess the data from the propeller simulations, to extract the thust and the moment, as well
# as pictures and pressure slices
#
#
# Usage:
#
# Start the program and a File Dialog will open. Select the results file from the simulation (either sol.dat or sol.plt)
#

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
eidValues = 0#4
wallRegions = 3#5
inletRegions = 2
rotationRate = 3500
radiusPropeller = 21 * 0.0254 / 2

picturewidth = 1920*2

views = [

    # ["Name", View width, X, Y, Z, Psi, Theta, Alpha]
    ["Bottom", 0.28, -0.13837, -0.0118782, 10, 0.00, 0.00, 0.00],
    ["Top", 0.28, -0.13837, -0.00469803, -27.2985, 180.00, -180.00, 0.00],
    ["ISO1", 0.209359, -23.5632, 12.2607, -6.29767, 103.31, 117.56, -176.19],
    ["ISO2", 0.168492, -19.4223, 8.33795, -11.4911, 118.63, 113.39, 153.57],
    ["Tip-1", 0.0508641, 1.91029, -0.230812, -0.395172, 102.43, -82.13, 178.55],
    ["Tip-2",0.0507068, 1.94302, -0.0404362, 0.0541199, 87.78, -88.66, -178.21],
    ["Tip-3",0.0494703,1.92428, 0.108381, -0.250, 97.69, -93.31, 162.90]
]

radii = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 98]

fensapSolutions = []
dropletSolutions = []
iceSolutions = []
iceGrids = []
grids = []
fensaptecplotFiles = []
fensapdatFiles = []
dropletdatFiles = []
droplettecplotFiles = []
icedatFiles = []
icetecplotFiles = []
icegridFiles = []
hasinitGrid = False
folder = "PostPro"

def searchFile(Folder):

    global fensapSolutions
    global dropletSolutions
    global iceSolutions
    global iceGrids
    global grids
    global fensaptecplotFiles
    global fensapdatFiles
    global dropletdatFiles
    global droplettecplotFiles
    global icedatFiles
    global icetecplotFiles
    global icegridFiles
    global hasinitGrid
    fensapSolutions = []
    dropletSolutions = []
    iceSolutions = []
    iceGrids = []
    grids = []
    fensaptecplotFiles = []
    fensapdatFiles = []
    dropletdatFiles = []
    droplettecplotFiles = []
    icedatFiles = []
    icetecplotFiles = []
    icegridFiles = []
    hasinitGrid = False
    for root, dirs, files in os.walk(Folder):
        # print('Looking in:',root)
        for Files in files:
            if Files.startswith("soln.fensap.") and not Files.endswith(".dat") and not Files.endswith(".disp")and not Files.endswith(".plt"):
                fensapSolutions.append(os.path.join(root, Files))
            if Files.startswith("droplet.drop.") and not Files.endswith(".dat") and not Files.endswith(".disp") and not Files.endswith(".plt"):
                dropletSolutions.append(os.path.join(root, Files))
            if Files.startswith("swimsol.ice.")and not Files.endswith(".dat") and not Files.endswith(".plt"):
                iceSolutions.append(os.path.join(root, Files))
            if Files.startswith("ice.ice.") and Files.endswith(".stl"):
                iceGrids.append(os.path.join(root, Files))
            if Files.startswith("grid.ice."):
                grids.append(os.path.join(root, Files))
            if Files.endswith("soln.plt"):
                fensaptecplotFiles.append(os.path.join(root, Files))
            if Files.endswith("drop.plt"):
                droplettecplotFiles.append(os.path.join(root, Files))
            if Files.startswith("soln.fensap.") and  Files.endswith(".dat") and not Files.endswith(".disp"):
                fensapdatFiles.append(os.path.join(root, Files))
            if Files.startswith("droplet.drop.") and  Files.endswith(".dat") and not Files.endswith(".disp"):
                dropletdatFiles.append(os.path.join(root, Files))
            if Files.startswith("swimsol.ice.") and  Files.endswith(".dat") and not Files.endswith(".plt"):
                icedatFiles.append(os.path.join(root, Files))
            if Files.startswith("swimsol.ice.") and Files.endswith(".plt") and not Files.endswith(".disp"):
                icetecplotFiles.append(os.path.join(root, Files))
            if Files.startswith("ice.grid.ice") and not Files.endswith(".3dtmp"):
                icegridFiles.append(os.path.join(root, Files))
            if Files == "soln":
                fensapSolutions.append(os.path.join(root, Files))
            if Files == "droplet":
                dropletSolutions.append(os.path.join(root, Files))
            if Files == "droplet.dat":
                dropletdatFiles.append(os.path.join(root, Files))
            if Files == "swimsol":
                iceSolutions.append(os.path.join(root, Files))
            if Files == "map.grid":
                icegridFiles.append(os.path.join(root, Files))
            if Files == "swimsol.dat":
                icedatFiles.append(os.path.join(root, Files))
            if Files == "soln.dat":
                fensapdatFiles.append(os.path.join(root, Files))
            if Files.startswith("Initialgrid.grid"):
                hasinitGrid = True


def createdatfile():
    if not hasinitGrid:
        firstGrid = fd.askopenfilename()
        os.link(firstGrid, path + "\\Initialgrid.grid")
    grids.insert(0, os.path.join(path,"Initialgrid.grid"))

    for i in range(len(fensapSolutions)):
        if not fensapdatFiles.__contains__(fensapSolutions[i] + ".dat") and not fensaptecplotFiles.__contains__(fensapSolutions[i]+".soln.plt"):
            print("Convert " + fensapSolutions[i])
            str = "CreateDatFiles.bat \"" + path + "\" \"" + grids[i] + "\" \"" + fensapSolutions[i] + "\""
            os.system(str)
            #print(str)
    for i in range(len(dropletSolutions)):
        if not dropletdatFiles.__contains__(dropletSolutions[i] + ".dat") and not droplettecplotFiles.__contains__(dropletSolutions[i] + ".drop.plt") :
            print("Convert " + dropletSolutions[i])
            str = "CreateDatFilesDrop.bat \"" + path + "\" \"" + grids[i] + "\" \"" + dropletSolutions[i] + "\""
            os.system(str)
    for i in range(len(iceSolutions)):
        if not icedatFiles.__contains__(iceSolutions[i] + ".dat") and not icetecplotFiles.__contains__(iceSolutions[i] + ".ice.plt"):
            print("Convert " + iceSolutions[i])
            str = "CreateDatFilesIce.bat \"" + path + "\" \"" + icegridFiles[i] + "\" \"" + iceSolutions[i] + "\""
            os.system(str)


def createcplotFile():
    for i in range(len(fensapdatFiles)):
        if not fensaptecplotFiles.__contains__(fensapdatFiles[i].replace(".dat",".soln.plt")):
            print('Working on File ' + fensapdatFiles[i])
            dataset = tecplot.data.load_tecplot(path + "\\" + fensapdatFiles[i], read_data_option=ReadDataOption.Replace)
            tecplot.data.save_tecplot_plt(path + "\\" + fensapdatFiles[i].replace(".dat",".soln.plt"),
                                          include_text=False,
                                          include_geom=False,
                                          include_data_share_linkage=True)
    for i in range(len(dropletdatFiles)):
        if not droplettecplotFiles.__contains__(dropletdatFiles[i].replace(".dat",".drop.plt")):
            print('Working on File ' + dropletdatFiles[i])
            dataset = tecplot.data.load_tecplot(path + "\\" + dropletdatFiles[i], read_data_option=ReadDataOption.Replace)
            tecplot.data.save_tecplot_plt(path + "\\" + dropletdatFiles[i].replace(".dat",".drop.plt"),
                                          include_text=False,
                                          include_geom=False,
                                          include_data_share_linkage=True)
    for i in range(len(icedatFiles)):
        if not icetecplotFiles.__contains__(icedatFiles[i].replace(".dat",".ice.plt")):
            print('Working on File ' + icedatFiles[i])
            dataset = tecplot.data.load_tecplot(path + "\\" + icedatFiles[i], read_data_option=ReadDataOption.Replace)
            tecplot.data.save_tecplot_plt(path + "\\" + icedatFiles[i].replace(".dat",".ice.plt"),
                                          include_text=False,
                                          include_geom=False,
                                          include_data_share_linkage=True)


def mainRun():
    print('Main Run')
    global folder
    global dataset
    global plot
    global frame
    for File in fensaptecplotFiles:
        print('Working on File ' + File)
        dataset = tecplot.data.load_tecplot(File, read_data_option=ReadDataOption.Replace)
        setDatasetValues()
        folder = "PostPro"
        try:
            if str(File.split(".")[2]).isnumeric():
                folder = "PostPro"+ str(File.split(".")[2])
        except:
            pass
        try:
            os.mkdir(path.replace("/","\\") + "\\" + folder)
        except:
            pass
        try:
            os.mkdir(path.replace("/","\\") + "\\" + folder + "\\Plots")
        except:
            pass

        frame = tecplot.active_frame()
        plot = frame.plot()

        convertData()
        saveData()
        prepareScene()
        saveViews()
        setupslices('Pressure (N/m^2)','30_Slices', 95000, 105000, True)
        setupslices('ShearStress','31_ShearStress', 0, 50, False)

    for File in droplettecplotFiles:
        print('Working on File ' + File)
        folder = "PostPro"
        try:
            if str(File.split(".")[2]).isnumeric():
                folder = "PostPro"+ str(File.split(".")[2])

        except:
            pass
        try:
            os.mkdir(path.replace("/","\\") + "\\" + folder)
        except:
            pass
        dataset = tecplot.data.load_tecplot(File, read_data_option=ReadDataOption.Replace)
        setDatasetValues()
        prepareScene()
        collection()
        dropletLWC()
        setupslices('Droplet LWC (kg/m^3)', '34_DropletLWC', 0, 0.005, False)
        setupslices('Collection efficiency-Droplet', '33_CollectionEff', 0, 1, False)

    for File in icetecplotFiles:
        print('Working on File ' + File)
        folder = "PostPro"
        try:
            if str(File.split(".")[2]).isnumeric():
                folder = "PostPro"+ str(File.split(".")[2])
        except:
            pass
        try:
            os.mkdir(path.replace("/","\\") + "\\" + folder)
        except:
            pass
        dataset = tecplot.data.load_tecplot(File, read_data_option=ReadDataOption.Replace)
        setDatasetValues()
        prepareSceneIce()
        masscaught()
        icethickness()
        walltemperature()
        filmthickness()
        rwHeatFlow()
        rwWaterHF()
        rwConvectionHF()
        rwEvaporationHF()
        feHeatFlow()
        setupslices('Ice thickness  (m)', '35_IceThickness', 0, 0.01, False)
        setupslices('Wall Temperature (C)', '36_WallTemp', -15, 2, False)

    for File in iceGrids:
        print('Working on File ' + File)
        folder = "PostPro"
        try:
            if str(File.split(".")[2]).isnumeric():
                folder = "PostPro"+ str(File.split(".")[2])
        except:
            pass
        try:
            os.mkdir(path.replace("/","\\") + "\\" + folder)
        except:
            pass

        dataset = tecplot.data.load_tecplot(path + "\\" + fensaptecplotFiles[0], read_data_option=ReadDataOption.Replace)
        dataset = tecplot.data.load_stl(path + "\\" + File)
        setDatasetValues()
        prepareSceneIceGrids()
        icescenes()


def setDatasetValues():
    global wallRegions
    global inletRegions
    global eidValues
    global turbVariables
    zones = dataset.zone_names
    variables = dataset.variable_names

    wallRegions = 0
    inletRegions = 0
    eidValues = 0
    for zone in zones:
        if "WALL" in zone:
            wallRegions = wallRegions+1
        if "INLET" in zone:
            inletRegions = inletRegions+1
    for variable in variables:
        if "EIDHS" in variable:
            eidValues = 4
        if "nutilde" in variable:
            turbVariables = 1
        if "omega" in variable:
            turbVariables = 2


def icescenes():
    plot.show_contour = False
    plot.show_shade = True
    plot.fieldmaps(wallRegions+inletRegions+4).shade.color = Color.Red
    plot.fieldmaps(2*wallRegions+inletRegions+5).shade.color = Color.Red
    savePicture("25_Ice")
    plot.show_contour = False
    plot.show_shade = False
    slice_0 = plot.slice(0)
    slice_0.slice_source=SliceSource.SurfaceZones
    slice_0.edge.show=True
    slice_0.contour.show=False
    plot.show_shade=False
    slice_0.edge.line_thickness=0.1
    # Turn on slice and get handle to slice object
    plot.show_slices = True

    slice_0.effects.use_translucency = False

    # Setup 4 evenly spaced slices
    slice_0.show_primary_slice = True
    slice_0.show_start_and_end_slices = False
    slice_0.show_intermediate_slices = False
    slice_0.orientation = SliceSurface.XPlanes
    # Turn on contours of X Velocity on the slice

    plot.view.width = 0.1
    plot.view.position = (8.66775, 0.00233312,-0.0198978)
    plot.view.psi = 90.00
    plot.view.theta = -90.00
    plot.view.alpha = 180.00

    try:
        os.mkdir(path.replace("/","\\") + '\\' + folder + '\\45_IceContour')
    except:
        pass
    for radius in radii:

        text = frame.add_text(str(radius), (50, 95))
        plot.slice(0).origin.x = radiusPropeller * radius / 100
        tecplot.export.save_png(path.replace("/","\\") + '\\' + folder + '\\45_IceContour\\' + str(radius) + '.png', picturewidth, supersample=1)
        text.text_string = ""

    plot.show_slices = False


def convertData():
    print('Convert Data')
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
    tecplot.data.operate.execute_equation(equation='{rot} = ' + str(rotationRate) + '/60')
    tecplot.data.operate.execute_equation(equation='{vx} = {V1-velocity (m/s); Velocity} - 2 * 3.14159265 *  Y * {rot}')
    tecplot.data.operate.execute_equation(equation='{vy} = {V2-velocity (m/s)} + 2 * 3.14159265 *  X * {rot}')
    tecplot.data.operate.execute_equation(equation='{vmag} =  sqrt({vx}**2+ {vy}**2+ {V3-velocity (m/s)}**2)')


def prepareScene():
    print('prepare Scene')
    # Change Aspect Ratio
    tecplot.macro.execute_file('changePaperSize.mcr')

    tecplot.active_frame().plot().frame.width = 14
    tecplot.active_frame().plot().frame.height = 8
    tecplot.active_frame().plot().frame.position=(0,0)

    # Hide Inlets
    i = 1
    while (i <= inletRegions):
        plot.fieldmaps(i).show = False
        i = i + 1

    i = inletRegions+1

    while (i <= inletRegions+wallRegions):
        plot.fieldmaps(i).mesh.line_thickness = 0.05
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

    tecplot.macro.execute_command('''$!AxialDuplicate 
      ZoneList =  [''' + str(1) + '-' + str(1) + ''']
      Angle = 180
      NumDuplicates = 1
      XVar = 1
      YVar = 2
      ZVar = 3''')
    tecplot.macro.execute_command('$!GlobalThreeD RotateOrigin{X = 0}')
    tecplot.macro.execute_command('$!GlobalThreeD RotateOrigin{Y = 0}')
    tecplot.macro.execute_command('$!GlobalThreeD RotateOrigin{Z = 0}')


def prepareSceneIceGrids():
    print('prepare Scene')
    # Change Aspect Ratio
    tecplot.macro.execute_file('changePaperSize.mcr')

    tecplot.active_frame().plot().frame.width = 14
    tecplot.active_frame().plot().frame.height = 8
    tecplot.active_frame().plot().frame.position=(0,0)

    # Hide Inlets
    i = 1
    while (i <= inletRegions):
        plot.fieldmaps(i).show = False
        i = i + 1

    i = inletRegions+1

    while (i <= inletRegions+wallRegions):
        plot.fieldmaps(i).mesh.line_thickness = 0.05
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

    tecplot.macro.execute_command('''$!AxialDuplicate 
      ZoneList =  [''' + str(inletRegions + wallRegions + 5) + '-' + str(inletRegions + wallRegions + 5) + ''']
      Angle = 180
      NumDuplicates = 1
      XVar = 1
      YVar = 2
      ZVar = 3''')
    tecplot.macro.execute_command('$!GlobalThreeD RotateOrigin{X = 0}')
    tecplot.macro.execute_command('$!GlobalThreeD RotateOrigin{Y = 0}')
    tecplot.macro.execute_command('$!GlobalThreeD RotateOrigin{Z = 0}')


def prepareSceneIce():
    global plot
    # Change Aspect Ratio
    tecplot.macro.execute_file('changePaperSize.mcr')

    tecplot.active_frame().plot().frame.width = 14
    tecplot.active_frame().plot().frame.height = 8
    tecplot.active_frame().plot().frame.position=(0,0)
    tecplot.active_frame().plot_type = PlotType.Cartesian3D
    plot = tecplot.active_frame().plot()

    # Rotate Data
    tecplot.macro.execute_command('''$!AxialDuplicate 
      ZoneList =  [''' + str( 1) + '-' + str(wallRegions) + ''']
      Angle = 180
      NumDuplicates = 1
      XVar = 1
      YVar = 2
      ZVar = 3''')

    tecplot.macro.execute_command('$!GlobalThreeD RotateOrigin{X = 0}')
    tecplot.macro.execute_command('$!GlobalThreeD RotateOrigin{Y = 0}')
    tecplot.macro.execute_command('$!GlobalThreeD RotateOrigin{Z = 0}')


def collection():
    print('Collection efficiency-Droplet')
    #plot.contour(0).variable_index = 29
    plot.contour(0).variable= dataset.variable('Collection efficiency-Droplet')
    plot.contour(0).colormap_name = 'Magma'
    plot.contour(0).colormap_filter.reversed=True
    plot.contour(0).levels.reset_levels(np.linspace(0, 1, 21))
    plot.show_contour = True
    plot.show_shade = False
    plot.contour(0).legend.vertical = False
    plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
    plot.contour(0).legend.position = (50, 5)
    plot.contour(0).labels.step = 5
    savePicture("11_CollectionEfficiency")


def dropletLWC():
    print('Droplet LWC (kg/m^3)')
    #plot.contour(0).variable_index = 29
    plot.contour(0).variable= dataset.variable('Droplet LWC (kg/m^3)')
    plot.contour(0).colormap_name = 'Magma'
    plot.contour(0).colormap_filter.reversed=True
    plot.contour(0).levels.reset_levels(np.linspace(0, 0.002, 21))
    plot.show_contour = True
    plot.show_shade = False
    plot.contour(0).legend.vertical = False
    plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
    plot.contour(0).legend.position = (50, 5)
    plot.contour(0).labels.step = 5
    savePicture("12_DropletLWC")
    slices("46_LWC")


def masscaught():
    print('Mass Caught (kg/m^2s)')
    variable = dataset.variable('Mass Caught (kg/m^2s)')
    if variable is not None:
        plot.contour(0).variable = variable
        plot.contour(0).colormap_name = 'Magma'
        plot.contour(0).colormap_filter.reversed=True
        #plot.contour(0).levels.reset_levels(np.linspace(0, 0.002, 21))
        plot.show_contour = True
        plot.show_shade = False
        plot.contour(0).legend.vertical = False
        plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
        plot.contour(0).legend.position = (50, 5)
        plot.contour(0).labels.step = 5
        savePicture("22_MassCaught")


def icethickness():
    print('Ice thickness  (m)')
    variable = dataset.variable('Ice thickness  (m)')
    if variable is not None:
        plot.contour(0).variable = variable
        plot.contour(0).colormap_name = 'Magma'
        plot.contour(0).colormap_filter.reversed=True
        #plot.contour(0).levels.reset_levels(np.linspace(0, 0.002, 21))
        plot.show_contour = True
        plot.show_shade = False
        plot.contour(0).legend.vertical = False
        plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
        plot.contour(0).legend.position = (50, 5)
        plot.contour(0).labels.step = 5
        savePicture("21_Icethickness")


def walltemperature():
    print('Wall Temperature (C)')
    variable = dataset.variable('Wall Temperature (C)')
    if variable is not None:
        plot.contour(0).variable = variable
        plot.contour(0).colormap_name='Diverging - Blue/Red'
        #plot.contour(0).levels.reset_levels(np.linspace(0, 0.002, 21))
        plot.show_contour = True
        plot.show_shade = False
        plot.contour(0).legend.vertical = False
        plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
        plot.contour(0).legend.position = (50, 5)
        plot.contour(0).labels.step = 5
        savePicture("23_Temperature")


def filmthickness():
    print('Film Thickness (micron)')
    variable = dataset.variable('Film Thickness (micron)')
    if variable is not None:
        plot.contour(0).variable = variable
        plot.contour(0).colormap_name='Diverging - Blue/Red'
        #plot.contour(0).levels.reset_levels(np.linspace(0, 0.002, 21))
        plot.show_contour = True
        plot.show_shade = False
        plot.contour(0).legend.vertical = False
        plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
        plot.contour(0).legend.position = (50, 5)
        plot.contour(0).labels.step = 5
        savePicture("24_FilmThickness")

def rwHeatFlow():
    print('RW Required HF (W/m^2)')
    variable = dataset.variable('RW Required HF (W/m^2)')
    if variable is not None:
        plot.contour(0).variable = variable
        plot.contour(0).colormap_name='Diverging - Blue/Red'
        plot.contour(0).colormap_filter.reversed=False
        plot.contour(0).levels.reset_levels(np.linspace(0, 5000, 21))
        plot.show_contour = True
        plot.show_shade = False
        plot.contour(0).legend.vertical = False
        plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
        plot.contour(0).legend.position = (50, 5)
        plot.contour(0).labels.step = 5
        savePicture("25_RWHeatFlow")


def feHeatFlow():
    print('FE Required HF (W/m^2)')
    variable = dataset.variable('FE Required HF (W/m^2)')
    if variable is not None:
        plot.contour(0).variable = variable
        plot.contour(0).colormap_name='Diverging - Blue/Red'
        plot.contour(0).colormap_filter.reversed=False
        plot.contour(0).levels.reset_levels(np.linspace(0, 100000, 21))
        plot.show_contour = True
        plot.show_shade = False
        plot.contour(0).legend.vertical = False
        plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
        plot.contour(0).legend.position = (50, 5)
        plot.contour(0).labels.step = 5
        savePicture("26_FEHeatFlow")


def rwWaterHF():
    print('RW Water Droplet HF (W/m^2)')
    variable = dataset.variable('RW Water Droplet HF (W/m^2)')
    if variable is not None:
        plot.contour(0).variable = variable
        plot.contour(0).colormap_name='Diverging - Blue/Red'
        plot.contour(0).colormap_filter.reversed=True
        plot.contour(0).levels.reset_levels(np.linspace(-10000, 0000, 21))
        plot.show_contour = True
        plot.show_shade = False
        plot.contour(0).legend.vertical = False
        plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
        plot.contour(0).legend.position = (50, 5)
        plot.contour(0).labels.step = 5
        savePicture("27_RWWaterHeatFlow")


def rwConvectionHF():
    print('RW Convection HF (W/m^2)')
    variable = dataset.variable('RW Convection HF (W/m^2)')
    if variable is not None:
        plot.contour(0).variable = variable
        plot.contour(0).colormap_name = 'Diverging - Blue/Red'
        plot.contour(0).colormap_filter.reversed = False
        plot.contour(0).levels.reset_levels(np.linspace(0, 5000, 21))
        plot.show_contour = True
        plot.show_shade = False
        plot.contour(0).legend.vertical = False
        plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
        plot.contour(0).legend.position = (50, 5)
        plot.contour(0).labels.step = 5
        savePicture("28_RWConvectionHeatFlow")


def rwEvaporationHF():
    print('RW Evaporation HF (W/m^2)')
    variable = dataset.variable('RW Evaporation HF (W/m^2)')
    if variable is not None:
        plot.contour(0).variable = variable
        plot.contour(0).colormap_name = 'Diverging - Blue/Red'
        plot.contour(0).colormap_filter.reversed = False
        plot.contour(0).levels.reset_levels(np.linspace(0, 5000, 21))
        plot.show_contour = True
        plot.show_shade = False
        plot.contour(0).legend.vertical = False
        plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
        plot.contour(0).legend.position = (50, 5)
        plot.contour(0).labels.step = 5
        savePicture("28_RWEvaporationHeatFlow")


def saveData():
    print('Save Data')
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="Integrate [" + str(inletRegions + 2) + '-' + str(
                                               inletRegions + wallRegions + 1) + "] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=" + str(
                                               33 + turbVariables+eidValues) + " Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="SaveIntegrationResults FileName='" + path.replace("/",
                                                                                                      "\\\\") + '\\\\' + folder + '\\\\Plots\\\\TZ.txt' + "'")
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="Integrate [" + str(inletRegions + 2) + '-' + str(
                                               inletRegions + wallRegions + 1) + "] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=" + str(
                                               30 + turbVariables+eidValues) + " Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="SaveIntegrationResults FileName='" + path.replace("\\",
                                                                                                      "\\\\") + '\\\\' + folder + '\\\\Plots\\\\PZ.txt' + "'")
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="Integrate [" + str(inletRegions + 2) + '-' + str(
                                               inletRegions + wallRegions + 1) + "] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=" + str(
                                               36 + turbVariables+eidValues) + " Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="SaveIntegrationResults FileName='" + path.replace("\\",
                                                                                                      "\\\\") + '\\\\' + folder + '\\\\Plots\\\\MZ.txt' + "'")


def saveViews():
    density()
    pressure()
    velocity()
    shearstress()
    pressuretz()
    pressurez()
    momentz()
    mesh()
    meshslices()
    IsoTurb()
    statictemperature()


def statictemperature():
    print('Static Temperature (K)')
    variable = dataset.variable('Static Temperature (K)')
    if variable is not None:
        plot.contour(0).variable = variable
        plot.contour(0).colormap_name='Diverging - Blue/Red'
        #plot.contour(0).levels.reset_levels(np.linspace(0, 0.002, 21))
        plot.show_contour = True
        plot.show_shade = False
        plot.contour(0).legend.vertical = False
        plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
        plot.contour(0).legend.position = (50, 5)
        plot.contour(0).labels.step = 5
        savePicture("09_Temperature")


def density():
    print('Density')
    plot.contour(0).variable_index = 3
    plot.contour(0).colormap_name = 'Large Rainbow'
    plot.contour(0).levels.reset_levels(np.linspace(1.2, 1.4, 21))
    plot.show_contour = True
    plot.show_shade = False
    plot.contour(0).legend.vertical = False
    plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
    plot.contour(0).legend.position = (50, 5)
    plot.contour(0).labels.step = 5
    plot.contour(0).colormap_name = 'Large Rainbow'
    savePicture("02_Density")
    slices("42_Density")


def mesh():
    print('Mesh')
    plot.show_contour = False
    plot.show_shade = True
    plot.show_mesh = True
    savePicture("50_Mesh")
    plot.show_contour = True
    plot.show_shade = False
    plot.show_mesh = False


def IsoTurb():
    print('turbulent viscosity (kg/m s)')
    plot.contour(0).variable= dataset.variable('turbulent viscosity (kg/m s)')
    plot.show_contour = False
    plot.show_shade = True
    plot.show_mesh = False
    plot.show_isosurfaces=False
    plot.show_isosurfaces=True
    plot.isosurface(0).isosurface_values[0]=2e-05
    plot.isosurface(0).contour.show=True
    plot.isosurface(0).contour.show=False
    plot.isosurface(0).shade.show=False
    plot.isosurface(0).shade.show=True
    plot.isosurface(0).shade.color=Color.Red
    savePicture("08_IsoTurb")
    plot.show_contour = True
    plot.show_shade = False
    plot.show_mesh = False
    plot.show_isosurfaces=False


def pressure():
    print('Pressure')
    plot.contour(0).variable_index = 4
    plot.contour(0).colormap_name = 'Large Rainbow'
    plot.contour(0).levels.reset_levels(np.linspace(97000, 106000, 21))
    plot.show_contour = True
    plot.show_shade = False
    plot.contour(0).legend.vertical = False
    plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
    plot.contour(0).legend.position = (50, 5)
    plot.contour(0).labels.step = 5
    savePicture("01_Pressure")
    slices("41_Pressure")


def velocity():
    print('Velocity')
    plot.contour(0).variable_index = 40 + turbVariables+eidValues
    plot.contour(0).colormap_name = 'Large Rainbow'
    plot.contour(0).levels.reset_levels(np.linspace(0, 150, 21))
    plot.show_contour = True
    plot.show_shade = False
    plot.contour(0).legend.vertical = False
    plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
    plot.contour(0).legend.position = (50, 5)
    plot.contour(0).labels.step = 5
    savePicture("07_Velocity")
    slices("43_Velocity")


def shearstress():
    print('ShearStress')
    plot.contour(0).variable_index = 36 + turbVariables+eidValues
    plot.contour(0).colormap_name = 'Large Rainbow'
    plot.contour(0).levels.reset_levels(np.linspace(0, 150, 21))
    plot.show_contour = True
    plot.show_shade = False
    plot.contour(0).legend.vertical = False
    plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
    plot.contour(0).legend.position = (50, 5)
    plot.contour(0).labels.step = 5
    savePicture("03_ShearStress")


def pressuretz():
    print('Pressure TZ')
    plot.contour(0).variable_index = 32 + turbVariables+eidValues
    plot.contour(0).colormap_name = 'Large Rainbow'
    plot.contour(0).levels.reset_levels(np.linspace(-4100, 4100, 21))
    plot.show_contour = True
    plot.show_shade = False
    plot.contour(0).legend.vertical = False
    plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
    plot.contour(0).legend.position = (50, 5)
    plot.contour(0).labels.step = 5
    savePicture("04_PressureTZ")


def pressurez():
    print('Pressure Z')
    plot.contour(0).variable_index = 29 + turbVariables+eidValues
    plot.contour(0).colormap_name = 'Large Rainbow'
    plot.contour(0).levels.reset_levels(np.linspace(-4100, 4100, 21))
    plot.show_contour = True
    plot.show_shade = False
    plot.contour(0).legend.vertical = False
    plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
    plot.contour(0).legend.position = (50, 5)
    plot.contour(0).labels.step = 5
    savePicture("05_PressureZ")


def momentz():
    print('moment TZ')
    plot.contour(0).variable_index = 35 + turbVariables+eidValues
    plot.contour(0).colormap_name = 'Large Rainbow'
    plot.contour(0).levels.reset_levels(np.linspace(-1200, 1200, 21))
    plot.show_contour = True
    plot.show_shade = False
    plot.contour(0).legend.vertical = False
    plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
    plot.contour(0).legend.position = (50, 5)
    plot.contour(0).labels.step = 5
    savePicture("06_MomentZ")


def slices(name):

    # Turn on slice and get handle to slice object
    plot.show_slices = True
    plot.show_contour = False
    slice_0 = plot.slice(0)

    slice_0.effects.use_translucency = False

    # Setup 4 evenly spaced slices
    slice_0.show_primary_slice = True
    slice_0.show_start_and_end_slices = False
    slice_0.show_intermediate_slices = False
    slice_0.orientation = SliceSurface.XPlanes
    # Turn on contours of X Velocity on the slice
    slice_0.contour.show = True

    plot.view.width = 0.144183
    plot.view.position = (8.66775, 0.00233312,-0.0198978)
    plot.view.psi = 90.00
    plot.view.theta = -90.00
    plot.view.alpha = 180.00

    try:
        os.mkdir(path.replace("/","\\") + '\\' + folder + '\\' + name )
    except:
        pass
    for radius in radii:

        text = frame.add_text(str(radius), (50, 95))
        plot.slice(0).origin.x = radiusPropeller * radius / 100
        tecplot.export.save_png(path.replace("/","\\") + '\\' + folder + '\\'+name+'\\' + str(radius) + '.png', picturewidth, supersample=1)
        text.text_string = ""

    plot.show_slices = False


def meshslices():

    # Turn on slice and get handle to slice object
    plot.show_slices = True
    plot.show_contour = False
    slice_0 = plot.slice(0)

    slice_0.effects.use_translucency = False

    # Setup 4 evenly spaced slices
    slice_0.show_primary_slice = True
    slice_0.show_start_and_end_slices = False
    slice_0.show_intermediate_slices = False
    slice_0.orientation = SliceSurface.XPlanes
    # Turn on contours of X Velocity on the slice
    slice_0.contour.show=False
    slice_0.mesh.show=True

    plot.view.width = 0.144183
    plot.view.position = (8.66775, 0.00233312,-0.0198978)
    plot.view.psi = 90.00
    plot.view.theta = -90.00
    plot.view.alpha = 180.00

    try:
        os.mkdir(path.replace("/","\\") + '\\' + folder + '\\49_Mesh' )
    except:
        pass
    for radius in radii:

        text = frame.add_text(str(radius), (50, 95))
        plot.slice(0).origin.x = radiusPropeller * radius / 100
        tecplot.export.save_png(path.replace("/","\\") + '\\' + folder + '\\49_Mesh\\' + str(radius) + '.png', picturewidth*2, supersample=1)
        text.text_string = ""

    plot.show_slices = False
    slice_0.contour.show=True
    slice_0.mesh.show=False


def savePicture(name):
    try:
        os.mkdir(path.replace("/","\\") + '\\' + folder + '\\' + name )
    except:
        pass
    for view in views:
        plot.view.width = view[1]
        plot.view.position = (view[2], view[3], view[4])
        plot.view.psi = view[5]
        plot.view.theta = view[6]
        plot.view.alpha = view[7]

        tecplot.export.save_png(path.replace("/","\\") + '\\' + folder + '\\' + name + '\\' + view[0] + ".png",
                                width=picturewidth,
                                region=ExportRegion.AllFrames,
                                supersample=1,
                                convert_to_256_colors=False)


def setupslices(variable, foldername, min, max,reverse):
    print('Slices')
    frame.plot_type = tecplot.constant.PlotType.XYLine

    try:
        os.mkdir(path.replace("/","\\") + '\\' + folder + '\\'+foldername)
    except:
        pass
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
            y=dataset.variable(variable))

        # overlay result on plot in upper right corner
        text = frame.add_text(str(radius), (50, 95))

        # set style of linemap plot
        cp_linemap.line.color = tecplot.constant.Color.Blue
        cp_linemap.line.line_thickness = 0.2
        cp_linemap.y_axis.reverse = reverse

        # update axes limits to show data
        plot.view.fit()
        tecplot.active_frame().plot().axes.y_axis(0).title.font.size = 2.6
        tecplot.active_frame().plot().axes.y_axis(0).title.text = variable
        tecplot.active_frame().plot().axes.y_axis(0).title.offset = 11
        # tecplot.active_frame().plot().axes.area.left = 15

        tecplot.active_frame().plot().axes.x_axis(0).title.text = 'Chord [-]'
        plot.view.fit()
        plot.axes.y_axis(0).min = min
        plot.axes.y_axis(0).max = max

        # export image of pressure coefficient as a function of x/c
        tecplot.export.save_png(path.replace("/","\\") + '\\' + folder + '\\'+foldername+'\\' + str(radius) + '.png', picturewidth, supersample=1)
        text.text_string = ""
        # tecplot.active_frame().plot_type = PlotType.Cartesian3D


# Open File
tkinter.Tk().withdraw()
path = fd.askdirectory()


searchFile(path)
createdatfile()
searchFile(path)

tecplot.new_layout()
frame = tecplot.active_frame()
plot = frame.plot()
dataset = []
createcplotFile()
searchFile(path)


mainRun()

