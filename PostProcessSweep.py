# Author Nicolas Mueller
#
# This code is meant to postprocess the data from the propeller simulations, to extract the thust and the moment and
# as pictures and pressure slices
#
#
# Usage:
#
# Start the program and a File Dialog will open. Select the results file from the simulation (either sol.dat or sol.plt)
#

import logging
import math
import tkinter
from tkinter import filedialog as fd
from tkinter import simpledialog
import os
import numpy as np
import tecplot
from tecplot.exception import *
from tecplot.constant import *
import sys


# from postprofunctions import *


logging.basicConfig(level=logging.DEBUG)

# Run this script with "-c" to connect to Tecplot 360 on port 7600
# To enable connections in Tecplot 360, click on:
#   "Scripting" -> "PyTecplot Connections..." -> "Accept connections"

if '-c' in sys.argv:
    tecplot.session.connect()


# Global Variables
turbVariables = 1  # Amount of turbulent variables (1 for SA, 2 fo Komega, automatically detected
eidValues = 0  # Extended icing data variables, automatically detected
wallRegions = 3  # Wall regions, automatically detected
inletRegions = 2  # inlet regions, automatically detected
rotationRate = 3500  # Rotation Rate, automatically detected
velocity = 10 # Reference Velocity, automatically detected
temperature = -5  # Temperature, automatically detected
pressure = 0  # Pressure, automatically detected
radiusPropeller = 21 * 0.0254 / 2  # Propeller radius in meter
picturewidth = 1920 * 2  # Amount of pixels for pictures
aoa =0 # Angle of attack
runNumber =0 # RunNumber
parameterFile = False

# File Vaiables, Filled by searchFile Function
fensapSolutions = []
dropletSolutions = []
iceSolutions = []
iceGrids = []
grids = []
fensapparfiles = []
iceparfiles = []
fensaptecplotFiles = []
fensapdatFiles = []
dropletdatFiles = []
droplettecplotFiles = []
icedatFiles = []
icetecplotFiles = []
icegridFiles = []
hasinitGrid = False
insertInitGrid = False
initGrid = ""
folder = "PostPro"

sweepResultsArray=[] # Angle of attack,Lift,Drag, Area

# In the next section default values for the slices are given. Those will be overwritten by the default files in the project folder or in the run folder

views = [
    # ["Name", View width, X, Y, Z, Psi, Theta, Alpha]
    ["Side", 0.0670616, -0.729903,0.201931, 7.76112, 6.53, 105.19, -104.77],
    ["Top", 0.0436031, -2.13318, -0.875292, 14.6705,9.35, 67.86, -53.77]
]

Cuts = [
    # ["Name", X, Y,View width]
    ["Default",0.015,0,0.1],
    ["LeadingEdge",0.0,0,0.01],
    ["TrailingEdge",0.035,0,0.025]
]

radii = [0.50]

fensap3DScenes = [
#   ["Variable", Colormap, reverse, Minimum Value, Maximum Value, Steps, Folder, CutviewFolder(optional)]
    ['Density (kg/m^3)', 'Large Rainbow', False, 1.0, 1.4, 21, "02_Density", "42_Density"],
    ['Pressure (N/m^2)', 'Large Rainbow', False, 97000, 106000, 21, "01_Pressure", "41_Pressure"],
    ['Velocity Magnitude', 'Large Rainbow', False, 0, 150, 21, "07_Velocity", "43_Velocity"],
    ['ShearStress', 'Large Rainbow', False, 0, 150, 21, "03_ShearStress", None],
    ['Static Temperature (K)', 'Diverging - Blue/Red', False, None, None, 21, "09_Temperature", None],
    ['Chordangle', 'Wild', False, -60, 60, 121, "91_Curvature", None]
]

fensapSlices = [
#   [variable, foldername, min, max, reverse]
    ['Pressure (N/m^2)', '30_Slices', 95000, 105000, True],
    ['ShearStress', '31_ShearStress', 0, 50, False]
]

fensapWrapSlices = [
#   [variable, variable2,foldername, min, max, reverse]
    ['ShearStress', None, '31b_ShearStress', 0, 150, False],
    ['ShearStress', 'Classical heat flux (W/m^2)', '31c_ShearStress', 0, None, False],
    ['Static temperature (K)', None, '32_Temperature', None, None, False],
    ['y-plus', None, '30_YPlus', 0, 4, False],
    ['Classical heat flux (W/m^2)', None, '30_HeatFlux', None, None, True],
    ['Chordangle', None, '90_Curvature', None, None, False]
]


def searchFile(Folder):
    global fensapSolutions
    global grids
    global fensaptecplotFiles
    global fensapdatFiles
    global hasinitGrid
    global initGrid
    global defaultsFile
    global sweepFolders
    global sweepResultsArray

    fensapSolutions = []
    grids = []
    fensaptecplotFiles = []
    fensapdatFiles = []
    sweepFolders = []
    sweepResultsArray = []
    defaultsFile = ""
    hasinitGrid = False
    cht3D = False

    for root, dirs, files in os.walk(Folder):
        # print('Looking in:',root)
        for directory in dirs:
            if directory.startswith("sweep_soln."):
                if os.path.isfile(os.path.join(root, directory, "soln")):
                    #fensapSolutions.append(os.path.join(root, directory, "soln")) # Absolute File Paths
                    fensapSolutions.append(os.path.join(directory, "soln")) # Relative File Paths
                if os.path.isfile(os.path.join(root, directory, "soln.dat")):
                    fensapdatFiles.append(os.path.join( directory, "soln.dat"))
                if os.path.isfile(os.path.join(root, directory, "soln.plt")):
                    fensaptecplotFiles.append(os.path.join( directory, "soln.plt"))
                    sweepFolders.append(os.path.join(root, "Postpro_" + str(float(directory[len("sweep_soln."):]))))
                    sweepResultsArray.append(float(directory[len("sweep_soln."):]))


        for Files in files:
            if Files == "fensap.par":
                fensapparfiles.append(os.path.join(root, Files))
            if Files.startswith("Initialgrid.grid"):
                hasinitGrid = True
                initGrid = "Initialgrid.grid"


def createdatfile():
    global initGrid

    for i in range(len(fensapSolutions)):
        if not fensapdatFiles.__contains__(fensapSolutions[i] + ".dat") \
                and not fensaptecplotFiles.__contains__(fensapSolutions[i] + ".plt"):
            insertInitialGrid()
            print("Convert " + fensapSolutions[i])
            string = "CreateDatFiles.bat \"" + path + "\" \"" \
                     + grid.replace("\\", "/") + "\" \"" + fensapSolutions[i] + "\""
            os.system(string)


def insertInitialGrid():  # Insert initial grid if necessary
    global initGrid
    global insertInitGrid
    global grid
    #if len(grids) > 1: # To deal with multishot simulation with an link to the original mesh --> No need for the initial grid
    #    insertInitGrid = True
    if not insertInitGrid:  # Check if it is necessary to insert the initial grid
        if not hasinitGrid:
            firstGrid = fd.askopenfilename()
            initGrid = "Initialgrid.grid"
            os.link(firstGrid, path + "\\" + initGrid)
        #grid=os.path.join(path, initGrid) # Use  Absolute Path for grids
        grid=initGrid # Use Local Path for grids
        insertInitGrid = True


def createTecplotFile():
    for i in range(len(fensapdatFiles)):
        if not fensaptecplotFiles.__contains__(fensapdatFiles[i].replace(".dat", ".plt")):
            print('Working on File ' + fensapdatFiles[i])
            tecplot.data.load_tecplot(os.path.join(path,fensapdatFiles[i]), read_data_option=ReadDataOption.Replace)
            tecplot.data.save_tecplot_plt(os.path.join(path,fensapdatFiles[i].replace(".dat", ".plt")),
                                          include_text=False,
                                          include_geom=False,
                                          include_data_share_linkage=True)
            os.remove(os.path.join(path,fensapdatFiles[i]))  # delete dat file to free up space on the drive


def mainRunSweep():
    print('Main Run')
    global folder
    global dataset
    global plot
    global path
    global frame
    global rotationRate
    global temperature
    global parameterFile
    global aoa
    global runNumber

    createPostProFolderSweep()

    for idx, File in enumerate(fensaptecplotFiles):
        print('Working on File ' + File)
        dataset = tecplot.data.load_tecplot(os.path.join(mainpath, File), read_data_option=ReadDataOption.Replace)
        path = sweepFolders[idx]
        aoa = sweepResultsArray[idx]
        setDatasetValues()
        runNumber = idx


        frame = tecplot.active_frame()
        plot = frame.plot()

        convertData()
        saveData()
        prepareScene()
        # curvature('0_Curvature', None, None, False)
        # setupsliceswrap('Z Grid K Unit Normal', 'Y Grid K Unit Normal', '0_Curvature2', None, None, False)
        #setupsliceswrap('Pressure (N/m^2)', None, '30_Pressure', 95000, 106000, False)

        meshslices()

        #mesh()
        #IsoTurb()

        for scene in fensap3DScenes:
            threeDScene(scene[0], scene[1], scene[2], scene[3], scene[4],scene[5], scene[6], scene[7])
        for slice in fensapSlices:
            setupslices(slice[0], slice[1], slice[2], slice[3], slice[4])
        for slice in fensapWrapSlices:
            setupsliceswrap(slice[0], slice[1], slice[2], slice[3], slice[4], slice[5])

    polar(0, 0, 0, 0)
    polarLift(0, 0, 0, 0)


def createPostProFolderSweep():
    #print('Working on File ' + File)
    for directory in sweepFolders:
        if not os.path.isdir(directory):
            os.mkdir(directory)
        if not os.path.isdir(os.path.join(directory, "Plots")):
            os.mkdir(os.path.join(directory, "Plots"))


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
        if ": rotated " in zone:  # Delete rotated Zones
            tecplot.active_frame().dataset.delete_zones(tecplot.active_frame().dataset.zone(zone))
        elif "WALL" in zone:
            wallRegions = wallRegions + 1
        elif "INLET" in zone:
            inletRegions = inletRegions + 1
    for variable in variables:
        if "EIDHS" in variable:
            eidValues = 4
        if "nutilde" in variable:
            turbVariables = 1
        if "omega" in variable:
            turbVariables = 2


def convertData():
    print('Convert Data')
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="SetFieldVariables ConvectionVarsAreMomentum='F' UVarNum=6 VVarNum=7 WVarNum=8 ID1='Density' Variable1=4 ID2='NotUsed' Variable2=0")
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="Calculate Function='GRIDKUNITNORMAL' Normalization='None' ValueLocation='Nodal' CalculateOnDemand='T' UseMorePointsForFEGradientCalculations='F'")
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="Calculate Function='VELOCITYMAG' Normalization='None' ValueLocation='Nodal' CalculateOnDemand='T' UseMorePointsForFEGradientCalculations='F'")

    tecplot.data.operate.execute_equation(equation='{Chordangle} = atan({Y Grid K Unit Normal} / if(0.01<=abs({Z Grid K Unit Normal}),{Z Grid K Unit Normal},0.01))*57.29577951')

    tecplot.data.operate.execute_equation(equation='{px} = ({Pressure (N/m^2)}-101325) * {X Grid K Unit Normal}')
    tecplot.data.operate.execute_equation(equation='{py} = ({Pressure (N/m^2)}-101325)  * {Y Grid K Unit Normal}')
    tecplot.data.operate.execute_equation(
        equation='{taux} = {SF1-shear stress (Pa); Shear} + {X Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
    tecplot.data.operate.execute_equation(
        equation='{tauy} = {SF2-shear stress (Pa)} + {Y Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
    tecplot.data.operate.execute_equation(equation='{areaint} =abs({Y Grid K Unit Normal})')


def saveData():
    print('Save Data')
    global sweepResultsArray


    writeToFile("\nvelocity,all,ref,%s" % velocity)
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
            command='''Integrate [3-7] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar={scalar_var} Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0'''.format(scalar_var=dataset.variable('areaint').index + 1))

    area = float(frame.aux_data['CFDA.INTEGRATION_TOTAL'])/2
    print('Area: %s' % area)
    writeToFile("\narea,all,int,%s" % area)
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="SaveIntegrationResults FileName='" + path.replace("\\",
                                                                                                      "\\\\") + '\\\\Plots\\\\Area.txt' + "'")
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command='''Integrate [3-7] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar={scalar_var} Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0'''.format(
                                               scalar_var=dataset.variable('taux').index + 1))

    taux = float(frame.aux_data['CFDA.INTEGRATION_TOTAL'])
    print('taux: %s' % taux)
    writeToFile("\ntaux,all,int,%s" % taux)
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="SaveIntegrationResults FileName='" + path.replace("\\",
                                                                                                      "\\\\") +'\\\\Plots\\\\TX.txt' + "'")

    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command='''Integrate [3-7] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar={scalar_var} Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0'''.format(
                                               scalar_var=dataset.variable('tauy').index + 1))
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="SaveIntegrationResults FileName='" + path.replace("\\",
                                                                                                      "\\\\") +'\\\\Plots\\\\TY.txt' + "'")

    tauy = float(frame.aux_data['CFDA.INTEGRATION_TOTAL'])
    print('tauy: %s' % tauy)
    writeToFile("\ntauy,all,int,%s" % tauy)
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command='''Integrate [3-7] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar={scalar_var} Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0'''.format(
                                               scalar_var=dataset.variable('py').index + 1))

    total = float(frame.aux_data['CFDA.INTEGRATION_TOTAL'])
    print('pressureLift: %s' % total)
    writeToFile("\npy,all,int,%s" % total)
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command='''Integrate [3-7] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar={scalar_var} Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0'''.format(
                                               scalar_var=dataset.variable('px').index + 1))

    total = float(frame.aux_data['CFDA.INTEGRATION_TOTAL'])
    print('pressureDrag: %s' % total)
    writeToFile("\npx,all,int,%s" % total)

    drag = np.cos(np.radians(aoa))*taux+np.sin(np.radians(aoa))*tauy
    lift = -np.sin(np.radians(aoa))*taux+np.cos(np.radians(aoa))*tauy
    print('drag: %s' % drag)
    print('lift: %s' % lift)
    writeToFile("\nlift,all,int,%s" % lift)
    writeToFile("\ndrag,all,int,%s" % drag)

    density = pressure/(287.058*(temperature+273.15))
    print('density: %s' % density)
    writeToFile("\ndensity,all,int,%s" % density)

    Cl = lift/((density/2)*area*velocity**2)
    print('CL: %s' % Cl)
    writeToFile("\ncl,all,int,%s" % Cl)

    Cd = drag/((density/2)*area*velocity**2)
    print('Cd: %s' % Cd)
    writeToFile("\ncd,all,int,%s" % Cd)

    sweepResultsArray[runNumber] = [aoa, Cl, Cd, lift, drag, area]

def prepareScene():
    print('prepare Scene')
    # Change Aspect Ratio
    tecplot.macro.execute_file('changePaperSize.mcr')

    tecplot.active_frame().plot().frame.width = 14
    tecplot.active_frame().plot().frame.height = 8
    tecplot.active_frame().plot().frame.position = (0, 0)

    # Hide Inlets
    i = 1
    while (i <= inletRegions):
        tecplot.active_frame().plot().fieldmaps(i).show = False
        i = i + 1

    i = inletRegions + 1

    while (i <= inletRegions + wallRegions):
        tecplot.active_frame().plot().fieldmaps(i).mesh.line_thickness = 0.05
        i = i + 1

    # Hide Outlet and periodics
    tecplot.active_frame().plot().fieldmaps(inletRegions + wallRegions + 1).show = False
    tecplot.active_frame().plot().fieldmaps(inletRegions + wallRegions + 2).show = False
    tecplot.active_frame().plot().fieldmaps(inletRegions + wallRegions + 3).show = False

    # Rotate Data

    if dataset.variable('X').min() > -0.01 and rotationRate != 0:
        print('\tPeriodic boundary detected')
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


def threeDScene(variableName, colormap, reverse, minc, maxc, spacing, folder, sliceFolder=""):
    print(variableName)
    variable = dataset.variable(variableName)
    if variable is not None:
        tecplot.active_frame().plot_type = PlotType.Cartesian3D
        plot = tecplot.active_frame().plot()
        plot.contour(0).variable = variable
        plot.contour(0).colormap_name = colormap
        plot.contour(0).colormap_filter.reversed = reverse

        if maxc is not None:
            plot.contour(0).levels.reset_levels(np.linspace(minc, maxc, spacing))
        plot.show_contour = True
        plot.show_shade = False
        plot.contour(0).legend.vertical = False
        plot.contour(0).legend.anchor_alignment = AnchorAlignment.BottomCenter
        plot.contour(0).legend.position = (50, 5)
        plot.contour(0).labels.step = 5
        savePicture(folder)
        if sliceFolder is not None:
            slices(sliceFolder)


def mesh():
    global picturewidth
    print('Mesh')
    plot.show_contour = False
    plot.show_shade = True
    plot.show_mesh = True
    picturewidth = picturewidth * 2
    savePicture("50_Mesh")
    picturewidth = picturewidth / 2
    plot.show_contour = True
    plot.show_shade = False
    plot.show_mesh = False


def IsoTurb():
    print('turbulent viscosity (kg/m s)')
    plot.contour(0).variable = dataset.variable('turbulent viscosity (kg/m s)')
    plot.show_contour = False
    plot.show_shade = True
    plot.show_mesh = False
    plot.show_isosurfaces = False
    plot.show_isosurfaces = True
    plot.isosurface(0).isosurface_values[0] = 2e-05
    plot.isosurface(0).contour.show = True
    plot.isosurface(0).contour.show = False
    plot.isosurface(0).shade.show = False
    plot.isosurface(0).shade.show = True
    plot.isosurface(0).shade.color = Color.Red
    savePicture("08_IsoTurb")
    plot.show_contour = True
    plot.show_shade = False
    plot.show_mesh = False
    plot.show_isosurfaces = False


def savePicture(name):
    try:
        #os.mkdir(path.replace("/", "\\") + '\\' + folder + '\\' + name)
        os.mkdir(path.replace("/", "\\")  + '\\' + name)
    except:
        pass
    for view in views:
        plot.view.width = view[1]
        plot.view.position = (view[2], view[3], view[4])
        plot.view.psi = view[5]
        plot.view.theta = view[6]
        plot.view.alpha = view[7]

        #tecplot.export.save_png(path.replace("/", "\\") + '\\' + folder + '\\' + name + '\\' + str(view[0]) + '.png',
        tecplot.export.save_png(path.replace("/", "\\") + '\\'  + name + '\\' + str(view[0]) + '.png',
                                width=picturewidth,
                                region=ExportRegion.AllFrames,
                                supersample=1,
                                convert_to_256_colors=False)


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
    slice_0.orientation = SliceSurface.ZPlanes

    plot.view.width = 0.10
    plot.view.position = (0, 0, 1)
    plot.view.psi = 0.00
    plot.view.theta = 90.00
    plot.view.alpha = -90.00

    try:
        #os.mkdir(path.replace("/", "\\") + '\\' + folder + '\\' + name)
        os.mkdir(path.replace("/", "\\") + '\\' + name)
    except:
        pass

    for cut in Cuts:
        plot.view.width = cut[3]
        plot.view.position = (cut[1],cut[2], 1)
        for radius in radii:
            text = frame.add_text(str(radius), (50, 95))
            plot.slice(0).origin.z = radius
            tecplot.export.save_png(path.replace("/", "\\") + '\\' + name + '\\'+ cut[0] + ' ' + str(radius) + '.png',
                                    picturewidth, supersample=1)
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
    slice_0.contour.show = False
    slice_0.mesh.show = True
    slice_0.orientation = SliceSurface.ZPlanes

    plot.view.width = 0.10
    plot.view.position = (0, 0, 1)
    plot.view.psi = 0.00
    plot.view.theta = 90.00
    plot.view.alpha = -90.00

    try:
        #os.mkdir(path.replace("/", "\\") + '\\' + folder + '\\49_Mesh')
        os.mkdir(path.replace("/", "\\") + '\\49_Mesh')
    except:
        pass

    for cut in Cuts:
        plot.view.width = cut[3]
        plot.view.position = (cut[1],cut[2], 1)
        for radius in radii:
            text = frame.add_text(str(radius), (50, 95))
            plot.slice(0).origin.x = radiusPropeller * radius / 100
            #tecplot.export.save_png(path.replace("/", "\\") + '\\' + folder + '\\49_Mesh\\'+ cut[0] + ' ' + str(radius) + '.png',
            tecplot.export.save_png(path.replace("/", "\\") + '\\49_Mesh\\'+ cut[0] + ' ' + str(radius) + '.png',
                                    picturewidth * 2, supersample=1)
        text.text_string = ""


    plot.show_slices = False
    slice_0.contour.show = True
    slice_0.mesh.show = False


def setupslices(variable, foldername, min, max, reverse):
    print('Chordwise plots of ' + variable)
    frame.plot_type = tecplot.constant.PlotType.XYLine

    try:
        #os.mkdir(path.replace("/", "\\") + '\\' + folder + '\\' + foldername)
        os.mkdir(path.replace("/", "\\") + '\\' + foldername)
    except:
        pass
    for radius in radii:
        tecplot.active_frame().plot_type = PlotType.Cartesian3D
        # extract an arbitrary slice from the surface data on the wing
        extracted_slice = tecplot.data.extract.extract_slice(
            origin=(0, 0,radius),
            normal=(0, 0, 1),
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

        tecplot.active_frame().plot().axes.x_axis(0).title.title_mode = AxisTitleMode.UseText
        tecplot.active_frame().plot().axes.x_axis(0).title.text = 'Chord [-]'
        plot.view.fit()
        plot.axes.y_axis(0).min = min
        plot.axes.y_axis(0).max = max

        # export image of pressure coefficient as a function of x/c
        tecplot.export.save_png(
            path.replace("/", "\\") + '\\' + foldername + '\\' + str(radius) + '.png', picturewidth,
            supersample=1)
        text.text_string = ""
        # tecplot.active_frame().plot_type = PlotType.Cartesian3D


# Create wrapping distance plots
def setupsliceswrap(variable, variable2, foldername, miny, maxy, reverse):
    print('Wrapping distance plots of ' + variable)
    # Check if variable is in dataset
    variableTest = dataset.variable(variable)
    if variableTest is not None:
        if variable2 is not None:
            variableTest = dataset.variable(variable2)
            if variableTest is None:
                variable2 = None

        frame.plot_type = tecplot.constant.PlotType.XYLine

        # make Folder
        try:
            #os.mkdir(path.replace("/", "\\") + '\\' + folder + '\\' + foldername)
            os.mkdir(path.replace("/", "\\") + '\\' + foldername)
        except:
            pass

        # Loop over all radii for the plot creation
        for radius in radii:

            tecplot.active_frame().plot_type = PlotType.Cartesian3D

            # extract an arbitrary slice from the surface data on the propeller
            extracted_slice = tecplot.data.extract.extract_slice(
                origin=(0, 0, radius),
                normal=(0, 0, 1),
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
            extracted_variable = extracted_slice.values(variable)

            # copy of data as a numpy array
            x = extracted_x.as_numpy_array()
            y = extracted_y.as_numpy_array()
            z = extracted_z.as_numpy_array()
            var = extracted_variable.as_numpy_array()
            var2 = np.empty(x.size)
            if variable2 is not None:
                extracted_variable2 = extracted_slice.values(variable2)
                var2 = extracted_variable2.as_numpy_array()

            # create empty arrays for later population
            arr = np.empty(x.size)  # Array for the wrapping distance
            dist = np.empty(x.size)  # Array for the distance between points
            i = 0  # iteration variable

            # Sort the point along the line, starting from the first element
            while i < x.size - 1:

                for idx, value in np.ndenumerate(y):
                    if idx[0] > i:
                        dist[idx[0]] = math.sqrt((x[idx[0]] - x[i]) ** 2 + (y[idx[0]] - y[i]) ** 2)
                    else:
                        dist[idx[0]] = 100
                pos = np.argmin(dist)

                x[i + 1], x[pos] = x[pos], x[i + 1]
                y[i + 1], y[pos] = y[pos], y[i + 1]
                var[i + 1], var[pos] = var[pos], var[i + 1]
                if variable2 is not None:
                    var2[i + 1], var2[pos] = var2[pos], var2[i + 1]
                i = i + 1

            # Integrate the distance along the line
            for idx, value in np.ndenumerate(y):
                if idx[0] > 0:
                    arr[idx[0]] = math.sqrt((y[idx[0]] - y[idx[0] - 1]) ** 2 + (x[idx[0]] - x[idx[0] - 1]) ** 2) + arr[
                        idx[0] - 1]
                else:
                    arr[idx[0]] = 0

            # Find the starting point and fix the orientation of the line
            i = 0
            maxd = 0
            maxind1 = 0
            maxind2 = 0
            while i < y.size - 1:

                for idx, value in np.ndenumerate(y):
                    dist[idx[0]] = math.sqrt((x[idx[0]] - x[i]) ** 2 + (y[idx[0]] - y[i]) ** 2)

                if dist.max(initial=-100000000) > maxd:
                    maxind1 = i
                    maxind2 = np.argmax(dist)
                    maxd = dist.max(initial=-100000000)

                i = i + 1

            if y[maxind1] < y[maxind2]:
                arr = arr - arr[maxind1]

                try:
                    arr = np.append(arr[maxind2:arr.size] - (arr.max() - arr.min()), arr[0:maxind2])
                    y = np.append(y[maxind2:y.size], y[0:maxind2])
                    var = np.append(var[maxind2:y.size], var[0:maxind2])
                    if variable2 is not None:
                        var2 = np.append(var2[maxind2:y.size], var2[0:maxind2])
                except:
                    print("Error1")
                    print(maxind2)
                    print(x.size)
                try:
                    if y[maxind2] > y[maxind2 + 1]:
                        arr = -arr
                        print("Flip Plot")
                except:
                    print("Error")
            else:
                arr = arr - arr[maxind2]

                try:
                    arr = np.append(arr[maxind1:arr.size], arr[0:maxind1] + arr.max() - arr.min())
                    y = np.append(y[maxind1:x.size], y[0:maxind1])
                    var = np.append(var[maxind1:x.size], var[0:maxind1])
                    if variable2 is not None:
                        var2 = np.append(var2[maxind1:y.size], var2[0:maxind1])
                except:
                    print("Error2")
                try:
                    if y[maxind1] > y[maxind1 + 1]:
                        arr = -arr
                except:
                    print("Error")

            arr = arr / maxd
            # Create new zone with the line and the results
            zone = dataset.add_ordered_zone('variable', y.size)
            zone.values('z')[:] = arr
            zone.values('y')[:] = var

            extracted_x[:] = arr
            plot.delete_linemaps()

            # create line plot from extracted zone data
            linemap = plot.add_linemap(
                name=variable,
                zone=zone,
                x=dataset.variable('z'),
                y=dataset.variable('y'))

            # overlay result on plot in upper right corner
            text = frame.add_text("Position: " + str(radius), (50, 95))
            text.anchor = TextAnchor.Center
            # set style of linemap plot
            linemap.line.color = tecplot.constant.Color.Blue
            linemap.line.line_thickness = 0.2
            linemap.y_axis.reverse = reverse

            # update axes limits to show data
            plot.view.fit()
            tecplot.active_frame().plot().axes.y_axis(0).title.font.size = 2.6
            tecplot.active_frame().plot().axes.y_axis(0).title.title_mode = AxisTitleMode.UseText
            tecplot.active_frame().plot().axes.y_axis(0).title.text = variable
            tecplot.active_frame().plot().axes.y_axis(0).title.offset = 11
            # tecplot.active_frame().plot().axes.area.left = 15
            tecplot.active_frame().plot().axes.x_axis(0).title.title_mode = AxisTitleMode.UseText
            tecplot.active_frame().plot().axes.x_axis(0).title.text = 'Wrapping distance [s/c]'

            if not reverse:
                textmax = frame.add_text("Max: " + str(var.max(initial=-10000000000000)), (10, 95))
            else:
                textmax = frame.add_text("Min: " + str(var.min(initial=1000000000000)), (10, 95))
            file_object = open(path +  '/Plots/out.csv', 'a+')
            # file_object.write('\n' + variable+","+pos+'max'+var.max())
            # file_object.write('\n' + variable+","+pos+'min'+var.min())
            file_object.write("\n%s,%s,max,%s" % (variable, str(radius), var.max(initial=-10000000000000)))
            file_object.write("\n%s,%s,min,%s" % (variable, str(radius), var.min(initial=100000000000)))
            plot.legend.show = False

            if variable2 is not None:
                zone.values('z')[:] = var2
                linemap2 = plot.add_linemap(
                    name=variable2,
                    zone=zone,
                    x=dataset.variable('z'),
                    y=dataset.variable('y'))
                linemap2.line.color = tecplot.constant.Color.Red
                linemap2.line.line_thickness = 0.2
                linemap2.y_axis.reverse = reverse
                plot.linemaps(1).y_axis_index = 1
                tecplot.active_frame().plot().axes.y_axis(1).title.font.size = 2.6
                tecplot.active_frame().plot().axes.y_axis(1).title.title_mode = AxisTitleMode.UseText
                tecplot.active_frame().plot().axes.y_axis(1).title.text = variable2
                tecplot.active_frame().plot().axes.y_axis(1).title.offset = 11
                plot.legend.show = True
                plot.legend.position = (90, 88)
                plot.legend.anchor_alignment = AnchorAlignment.MiddleRight
                textmax.text_string = ("Max: " + str(var.max(initial=-10000000000)) + "\nMax: " + str(var2.max(initial=-10000000000)))
                file_object.write("\n%s,%s,max,%s" % (variable2, str(radius), var2.max(initial=-10000000000)))
                file_object.write("\n%s,%s,min,%s" % (variable2, str(radius), var2.min(initial=10000000000)))
                # file_object.write('\n'+ variable2+","+pos+'max'+var2.max())
                # file_object.write('\n'+ variable2+","+pos+'min'+var2.min())

            plot.view.fit()
            plot.axes.x_axis(0).min = -1
            plot.axes.x_axis(0).max = 1

            if miny is not None:
                plot.axes.y_axis(0).min = miny

            if maxy is not None:
                plot.axes.y_axis(0).max = maxy

            # export image of pressure coefficient as a function of x/c
            tecplot.export.save_png(
                path.replace("/", "\\") + '\\' + foldername + '\\' + str(radius) + '.png', picturewidth,
                supersample=1)
            text.text_string = ""
            textmax.text_string = ""
            file_object.close()
            tecplot.active_frame().dataset.delete_zones(zone)

            # tecplot.active_frame().plot_type = PlotType.Cartesian3D


def curvature(foldername, miny, maxy, reverse):
    print('Wrapping distance plots of curvature')

    frame.plot_type = tecplot.constant.PlotType.XYLine

    # make Folder
    try:
        #os.mkdir(path.replace("/", "\\") + '\\' + folder + '\\' + foldername)
        os.mkdir(path.replace("/", "\\") + '\\' + foldername)
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
        var = np.empty(z.size)  # Array for the wrapping distance= extracted_variable.as_numpy_array()

        var[0] = 0

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

            i = i+1

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

            if dist.max(initial=-10000000000) > maxd:
                maxind1 = i
                maxind2 = np.argmax(dist)
                maxd = dist.max(initial=-10000000000)

            i = i + 1

        if y[maxind1] < y[maxind2]:
            arr = arr - arr[maxind1]

            try:
                arr = np.append(arr[maxind2:arr.size] - (arr.max(initial=-10000000000) - arr.min(initial=10000000000)), arr[0:maxind2])
                z = np.append(z[maxind2:z.size], z[0:maxind2])
            except:
                print("Error1")
                print(maxind2)
                print(z.size)
            try:
                if z[maxind2] > z[maxind2 + 1]:
                    arr = -arr
                    print("Flip Plot")
            except:
                print("Error")
        else:
            arr = arr - arr[maxind2]

            try:
                arr = np.append(arr[maxind1:arr.size], arr[0:maxind1] + arr.max() - arr.min())
                z = np.append(z[maxind1:z.size], z[0:maxind1])
            except:
                print("Error2")
            try:
                if z[maxind1] > z[maxind1 + 1]:
                    arr = -arr
            except:
                print("Error")

        i = 1
        while i < z.size - 1:
            area = (y[i] - y[i - 1]) * (z[i + 1] - z[i - 1]) - (z[i] - z[i - 1]) * (y[i + 1] - y[i - 1])
            area = (y[i-1] * (z[i]-z[i + 1]) + y[i] * (z[i + 1]-z[i - 1]) + y[i + 1] * (z[i - 1]-z[i]))/2

            a = math.sqrt((y[i] - y[i + 1]) ** 2 + (z[i] - z[i + 1]) ** 2)
            b = math.sqrt((y[i] - y[i - 1]) ** 2 + (z[i] - z[i - 1]) ** 2)
            c = math.sqrt((y[i - 1] - y[i + 1]) ** 2 + (z[i - 1] - z[i + 1]) ** 2)

            var[i] = 4 * area / (a * b * c)

            i = i + 1

        arr = arr / maxd
        # Create new zone with the line and the results
        zone = dataset.add_ordered_zone('variable', z.size)
        zone.values('x')[:] = arr
        zone.values('y')[:] = var

        extracted_x[:] = arr
        plot.delete_linemaps()

        # create line plot from extracted zone data
        linemap = plot.add_linemap(
            name="Curvature",
            zone=zone,
            x=dataset.variable('x'),
            y=dataset.variable('y'))

        # overlay result on plot in upper right corner
        text = frame.add_text("Position: " + str(radius), (50, 95))
        text.anchor = TextAnchor.Center
        # set style of linemap plot
        linemap.line.color = tecplot.constant.Color.Blue
        linemap.line.line_thickness = 0.2
        linemap.y_axis.reverse = reverse

        # update axes limits to show data
        plot.view.fit()
        tecplot.active_frame().plot().axes.y_axis(0).title.font.size = 2.6
        tecplot.active_frame().plot().axes.y_axis(0).title.title_mode = AxisTitleMode.UseText
        tecplot.active_frame().plot().axes.y_axis(0).title.text = "Curvature"
        tecplot.active_frame().plot().axes.y_axis(0).title.offset = 11
        # tecplot.active_frame().plot().axes.area.left = 15
        tecplot.active_frame().plot().axes.x_axis(0).title.title_mode = AxisTitleMode.UseText
        tecplot.active_frame().plot().axes.x_axis(0).title.text = 'Wrapping distance [s/c]'

        if not reverse:
            textmax = frame.add_text("Max: " + str(var.max(initial=-10000000000)), (10, 95))
        else:
            textmax = frame.add_text("Min: " + str(var.min(initial=10000000000)), (10, 95))
        plot.legend.show = False

        plot.view.fit()
        plot.axes.x_axis(0).min = -max(arr.max(), -arr.min())
        plot.axes.x_axis(0).max = max(arr.max(), -arr.min())
        plot.axes.x_axis(0).min = -1
        plot.axes.x_axis(0).max = 1

        if miny is not None:
            plot.axes.y_axis(0).min = miny

        if maxy is not None:
            plot.axes.y_axis(0).max = maxy

        # export image of pressure coefficient as a function of x/c

        tecplot.export.save_png(
            path.replace("/", "\\") + '\\' + foldername + '\\' + str(radius) + '.png', picturewidth,
            supersample=1)
        text.text_string = ""
        textmax.text_string = ""
        tecplot.active_frame().dataset.delete_zones(zone)

        # tecplot.active_frame().plot_type = PlotType.Cartesian3D


def polar(clmin, clmax, cdmin,cdmax):
    print('Polar')

    frame.plot_type = tecplot.constant.PlotType.XYLine

    # Loop over all radii for the plot creation

    # tecplot.active_frame().plot_type = PlotType.Cartesian3D
    tecplot.active_frame().plot_type = PlotType.XYLine
    plot = frame.plot()
    zone = dataset.add_ordered_zone('variable', len(sweepResultsArray))
    sorted_multi_list = sorted(sweepResultsArray, key=lambda x: x[0])
    zone.values('x')[:] = [row[2] for row in sorted_multi_list]
    zone.values('y')[:] = [row[1] for row in sorted_multi_list]
    #zone.values('x')[:] = [row[2] for row in sweepResultsArray]
    #zone.values('y')[:] = [row[1] for row in sweepResultsArray]

    plot.delete_linemaps()

    # create line plot from extracted zone data
    linemap = plot.add_linemap(
        name="Curvature",
        zone=zone,
        x=dataset.variable('x'),
        y=dataset.variable('y'))

    # overlay result on plot in upper right corner
    text = frame.add_text("Position: ")
    text.anchor = TextAnchor.Center
    # set style of linemap plot
    linemap.line.color = tecplot.constant.Color.Blue
    linemap.line.line_thickness = 0.2

    # update axes limits to show data
    plot.view.fit()
    tecplot.active_frame().plot().axes.y_axis(0).title.font.size = 2.6
    tecplot.active_frame().plot().axes.y_axis(0).title.title_mode = AxisTitleMode.UseText
    tecplot.active_frame().plot().axes.y_axis(0).title.text = "Lift Coefficient [-]"
    tecplot.active_frame().plot().axes.y_axis(0).title.offset = 11
    # tecplot.active_frame().plot().axes.area.left = 15
    tecplot.active_frame().plot().axes.x_axis(0).title.title_mode = AxisTitleMode.UseText
    tecplot.active_frame().plot().axes.x_axis(0).title.text = 'Drag Coefficient [-]'

    plot.legend.show = False

    plot.view.fit()
    #plot.axes.x_axis(0).min = -max(arr.max(), -arr.min())
    #plot.axes.x_axis(0).max = max(arr.max(), -arr.min())


    # export image of pressure coefficient as a function of x/c

    for path in sweepFolders:
        tecplot.export.save_png(
            path.replace("/", "\\") + '\\' + "Plots" + '\\' + "Polar" + '.png', picturewidth,
            supersample=1)
    text.text_string = ""
    tecplot.active_frame().dataset.delete_zones(zone)

    textfile = open(mainpath + "\\" + "Polar.txt", "w")
    for element in sorted_multi_list:
        for subelement in element:
            textfile.write(str(subelement)+",")
        textfile.write("\n")
    textfile.close()
    tecplot.active_frame().plot_type = PlotType.Cartesian3D

    # tecplot.active_frame().plot_type = PlotType.Cartesian3D

def polarLift(clmin, clmax, cdmin,cdmax):
    print('PolarLift')

    frame.plot_type = tecplot.constant.PlotType.XYLine

    # Loop over all radii for the plot creation

    tecplot.active_frame().plot_type = PlotType.XYLine
    plot = frame.plot()

    zone = dataset.add_ordered_zone('variable', len(sweepResultsArray))
    sorted_multi_list = sorted(sweepResultsArray, key=lambda x: x[0])
    zone.values('x')[:] = [row[0] for row in sorted_multi_list]
    zone.values('y')[:] = [row[1] for row in sorted_multi_list]

    plot.delete_linemaps()

    # create line plot from extracted zone data
    linemap = plot.add_linemap(
        name="Curvature",
        zone=zone,
        x=dataset.variable('x'),
        y=dataset.variable('y'))

    # overlay result on plot in upper right corner
    text = frame.add_text("Position: ")
    text.anchor = TextAnchor.Center
    # set style of linemap plot
    linemap.line.color = tecplot.constant.Color.Blue
    linemap.line.line_thickness = 0.2

    # update axes limits to show data
    plot.view.fit()
    tecplot.active_frame().plot().axes.y_axis(0).title.font.size = 2.6
    tecplot.active_frame().plot().axes.y_axis(0).title.title_mode = AxisTitleMode.UseText
    tecplot.active_frame().plot().axes.y_axis(0).title.text = "Lift Coefficient [-]"
    tecplot.active_frame().plot().axes.y_axis(0).title.offset = 11
    # tecplot.active_frame().plot().axes.area.left = 15
    tecplot.active_frame().plot().axes.x_axis(0).title.title_mode = AxisTitleMode.UseText
    tecplot.active_frame().plot().axes.x_axis(0).title.text = 'Angle of Attack [deg]'

    plot.legend.show = False

    plot.view.fit()
    #plot.axes.x_axis(0).min = -max(arr.max(), -arr.min())
    #plot.axes.x_axis(0).max = max(arr.max(), -arr.min())


    # export image of pressure coefficient as a function of x/c

    for path in sweepFolders:
        tecplot.export.save_png(
            path.replace("/", "\\") + '\\' + "Plots" + '\\' + "PolarLift" + '.png', picturewidth,
            supersample=1)
    text.text_string = ""
    tecplot.active_frame().dataset.delete_zones(zone)
    tecplot.active_frame().plot_type = PlotType.Cartesian3D

    # tecplot.active_frame().plot_type = PlotType.Cartesian3D

def writeToFile(string):
    file_object = open(path + '/Plots/out.csv', 'a+')
    file_object.write(string)
    file_object.close()


def importDefautlFile(path):
    projectdefaultfile = path+'/../defaults.py'
    rundefaultfile = path+'/../defaults.py'
    if os.path.isfile(projectdefaultfile):
        print('Import Project Default')
        sys.path.append(path+'/../')
        #from projectdefault import *
    if os.path.isfile(rundefaultfile):
        print('Import Run Default')
        sys.path.append(path)
        #from rundefault import *


# Open File
tkinter.Tk().withdraw()
path = fd.askdirectory()
mainpath = path
#importDefautlFile(path)

projectdefaultfile = path + '/../projectdefaults.py'
rundefaultfile = path + '/../rundefault.py'
if os.path.isfile(projectdefaultfile):
    print('Import Project Default')
    sys.path.append(path + '/../')
    from projectdefaults import *
if os.path.isfile(rundefaultfile):
    print('Import Run Default')
    sys.path.append(path)
    from rundefault import *



searchFile(path)

for File in fensapparfiles:
    parameterFile = True
    print(File)
    file1 = open(File, 'r')
    data = file1.readlines()
    for line in data:
        if "FSP_ROTATION_VECTOR_Z" in line:
            rotationRate = abs(movementfile)
            print(rotationRate)
        if "FSP_FREESTREAM_TEMPERATURE" in line:
            temperature = abs(float(line.split(' ')[2])) - 273.15
            print(temperature)
        if "FSP_FREESTREAM_VELOCITY" in line:
            velocity = abs(float(line.split(' ')[2]))
            print(velocity)
        if "FSP_FREESTREAM_PRESSURE" in line:
            pressure = abs(float(line.split(' ')[2]))
            print(pressure)
        if "GLB_FILE_GRID" in line:
            testString = os.path.join(path, line.split(' ')[2].replace("\"", "").replace("\n", ""))
            print(testString)
            if os.path.isfile(testString):
                initGrid = line.split(' ')[2].replace("\n", "").replace("\"", "")
                print(initGrid)
                hasinitGrid = True


if not parameterFile:
    root = tkinter.Tk()
    root.withdraw()
    a = simpledialog.askstring(title="Input",
                               prompt="What is the Temperature:")
    temperature = float(a)
    root.withdraw()
    a = simpledialog.askstring(title="Input",
                               prompt="What is the Rotation Rate:")
    rotationRate = float(a)

createdatfile()
searchFile(path)

tecplot.new_layout()
frame = tecplot.active_frame()
plot = frame.plot()
dataset = []
createTecplotFile()
searchFile(path)

mainRunSweep()
