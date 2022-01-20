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
radiusPropeller = 21 * 0.0254 / 2  # Propeller radius in meter
picturewidth = 1920 * 2  # Amount of pixels for pictures

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

# In the next section default values for the slices are given. Those will be overwritten by the default files in the project folder or in the run folder

views = [
    # ["Name", View width, X, Y, Z, Psi, Theta, Alpha]
    ["Side", 0.0670616, -0.729903,0.201931, 7.76112, 6.53, 105.19, -104.77],
    ["Top", 0.0436031, -2.13318, -0.875292, 14.6705,9.35, 67.86, -53.77]
]

Cuts = [
    # ["Name", View width, X, Y, Z, Psi, Theta, Alpha]
    ["Default",0.015,0,0.1],
    ["LeadingEdge",0.0,0,0.01],
    ["TrailingEdge",0.035,0,0.025]
]

radii = [ 0.50]

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

droplet3DScenes = [
#   ["Variable", Colormap, reverse, Minimum Value, Maximum Value, Steps, Folder, CutviewFolder(optional)]
    ['Collection efficiency-Droplet', 'Magma', True, 0, 1, 21, "11_CollectionEfficiency", None],
    ['Droplet LWC (kg/m^3)', 'Magma', True, 0, 0.002, 21, "12_DropletLWC", "46_LWC"],

]

dropletSlices = []

dropletWrapSlices = [
#   [variable, variable2,foldername, min, max, reverse]
    ['Droplet LWC (kg/m^3)', None, '34_DropletLWC', 0, 0.005, False],
    ['Collection efficiency-Droplet', None, '33_CollectionEff', 0, 1, False],
    ['Collection efficiency-Droplet', 'Droplet LWC (kg/m^3)', '35_Collection', 0, 1, False]
]

ice3DScenes = [
#   ["Variable", Colormap, reverse, Minimum Value, Maximum Value, Steps, Folder, CutviewFolder(optional)]
    ['Mass Caught (kg/m^2s)', 'Magma', True, 0, None, 21, "22_MassCaught", None],
    ['21_Icethickness', 'Magma', True, None, None, 21, "21_Icethickness", None],
    ['Wall Temperature (C)', 'Diverging - Blue/Red', False, None, None, 21, "23_Temperature", None],
    ['Film Thickness (micron)', 'Diverging - Blue/Red', False, None, None, 21, "24_FilmThickness", None],
    ['RW Required HF (W/m^2)', 'Diverging - Blue/Red', False, 0, 50000, 21, "25_RWHeatFlow", None],
    ['RW Water Droplet HF (W/m^2)', 'Diverging - Blue/Red', True, -10000, 000000, 21,
                "27_RWWaterHeatFlow", None],
    ['FE Required HF (W/m^2)', 'Diverging - Blue/Red', False, 0, 100000, 21, "26_FEHeatFlow", None],
    ['RW Film height (micron)', 'Diverging - Blue/Red', False, 0, 10, 21, "29_RW_Film_Height", None],
    ['RW Evaporation HF (W/m^2)', 'Diverging - Blue/Red', False, 0000, 5000, 21,
                "28_RWEvaporationHeatFlow", None],
    ['RW Convection HF (W/m^2)', 'Diverging - Blue/Red', False, 0000, 5000, 21,
                "28_RWConvectionHeatFlow", None],

]

iceSlices = []

iceWrapSlices = [
#   [variable, variable2,foldername, min, max, reverse]
    ['Mass Caught (kg/m^2s)', None, '37_MassCaught', 0, None, False],
    ['RW Required HF (W/m^2)', 'RW Film height (micron)', '39_RWTotal', 0, None, False],
    ['RW Required HF (W/m^2)', 'RW Water Droplet HF (W/m^2)', '39_RWTotal-Droplet', None, None,
                    False],
    ['Mass Caught (kg/m^2s)', None, '37_MassCaught', 0, None, False],
    ['RW Required HF (W/m^2)', 'RW Convection HF (W/m^2)', '39_RWTotal-Convection', 0, None, False],
    ['RW Required HF (W/m^2)', 'RW Evaporation HF (W/m^2)', '39_RWTotal-Evaporation', 0, None, False],
    ['Wall Temperature (C)', None, '36_WallTemp', -15, 2, False],
    ['Mass Caught (kg/m^2s)', None, '37_MassCaught', 0, None, False],
    ['RW Film height (micron)', None, '39_RW_Film_Height', 0, 10, False],
    ['Ice thickness  (m)', None, '35_IceThickness', 0, None, False],
    ['RW Required HF (W/m^2)', None, '38_RWHeatFlow', 0, None, False],
    ['RW Required HF (W/m^2)', None, '38_RWHeatFlow', 0, None, False],
    ['Instant. Ice Growth (kg/m^2s))', None, '38_InsICe', 0, None, False],
    ['Freezing fraction', None, '38_FrezingFraction', 0, None, False],
]

def searchFile2D(Folder):
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
    global initGrid

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
    cht3D = False

    for root, dirs, files in os.walk(Folder):
        # print('Looking in:',root)
        for directory in dirs:

            if directory == "CHT_compute":
                cht3D = True

        for File in files:
            if File.startswith("soln.fensap.") and not File.endswith(".dat") \
                    and not File.endswith(".disp") and not File.endswith(".plt"):
                fensapSolutions.append(File)
                grids.append("grid.ice." + File.split(".")[2])
                if cht3D:  # Include Initial Grid if CHT3D Calc because there might be multi simulations without new mesh
                    grids.append(os.path.join(path, "Initialgrid.grid"))
            if File.startswith("droplet.drop.") and not File.endswith(".dat") \
                    and not File.endswith(".disp") and not File.endswith(".plt"):
                dropletSolutions.append(File)
            if File.startswith("swimsol.ice.") and not File.endswith(".dat") \
                    and not File.endswith(".plt"):
                iceSolutions.append(File)
            if File.startswith("ice.ice.") and File.endswith(".stl"):
                iceGrids.append(File)
            if File.endswith("soln.plt"):
                fensaptecplotFiles.append(File)
            if File.endswith("drop.plt"):
                droplettecplotFiles.append(File)
            if File.startswith("soln.fensap.") and File.endswith(".dat"):
                fensapdatFiles.append(File)
            if File.startswith("droplet.drop.") and File.endswith(".dat"):
                dropletdatFiles.append(File)
            if File.startswith("swimsol.ice.") and File.endswith(".dat"):
                icedatFiles.append(File)
            if File.startswith("swimsol.ice.") and File.endswith(".plt"):
                icetecplotFiles.append(File)
            if File.startswith("ice.grid.ice") and not File.endswith(".3dtmp"):
                icegridFiles.append(File)
            if File == "soln":
                fensapSolutions.append(File)
            if File == "droplet":
                dropletSolutions.append(File)
            if File == "droplet.dat":
                dropletdatFiles.append(File)
            if File == "swimsol":
                iceSolutions.append(File)
            if File == "map.grid":
                icegridFiles.append(File)
            if File == "swimsol.dat":
                icedatFiles.append(File)
            if File == "fensap.par":
                fensapparfiles.append(File)
            if File == "ice.par":
                iceparfiles.append(File)
            if File == "soln.dat":
                fensapdatFiles.append(File)
            if File.startswith("Initialgrid.grid"):
                hasinitGrid = True
                initGrid = "Initialgrid.grid"

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
    global initGrid

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
    cht3D = False

    for root, dirs, files in os.walk(Folder):
        # print('Looking in:',root)
        for directory in dirs:

            if directory == "CHT_compute":
                cht3D = True

        for Files in files:
            if Files.startswith("soln.fensap.") and not Files.endswith(".dat") \
                    and not Files.endswith(".disp") and not Files.endswith(".plt"):
                fensapSolutions.append(os.path.join(root, Files))
                if cht3D:  # Include Initial Grid if CHT3D Calc because there might be mult simulations without new mesh
                    grids.append(os.path.join(path, "Initialgrid.grid"))
            if Files.startswith("droplet.drop.") and not Files.endswith(".dat") \
                    and not Files.endswith(".disp") and not Files.endswith(".plt"):
                dropletSolutions.append(os.path.join(root, Files))
            if Files.startswith("swimsol.ice.") and not Files.endswith(".dat") \
                    and not Files.endswith(".plt"):
                iceSolutions.append(os.path.join(root, Files))
            if Files.startswith("ice.ice.") and Files.endswith(".stl"):
                iceGrids.append(os.path.join(root, Files))
            if Files.startswith("grid.ice."):
                grids.append(os.path.join(root, Files))
            if Files.endswith("soln.plt"):
                fensaptecplotFiles.append(os.path.join(root, Files))
            if Files.endswith("drop.plt"):
                droplettecplotFiles.append(os.path.join(root, Files))
            if Files.startswith("soln.fensap.") and Files.endswith(".dat") and not Files.endswith(".disp"):
                fensapdatFiles.append(os.path.join(root, Files))
            if Files.startswith("droplet.drop.") and Files.endswith(".dat") and not Files.endswith(".disp"):
                dropletdatFiles.append(os.path.join(root, Files))
            if Files.startswith("swimsol.ice.") and Files.endswith(".dat") and not Files.endswith(".plt"):
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
            if Files == "fensap.par":
                fensapparfiles.append(os.path.join(root, Files))
            if Files == "ice.par":
                iceparfiles.append(os.path.join(root, Files))
            if Files == "soln.dat":
                fensapdatFiles.append(os.path.join(root, Files))
            if Files.startswith("Initialgrid.grid"):
                hasinitGrid = True
                initGrid = "Initialgrid.grid"


def createdatfileOld():
    global initGrid

    for i in range(len(fensapSolutions)):
        if not fensapdatFiles.__contains__(fensapSolutions[i] + ".dat") \
                and not fensaptecplotFiles.__contains__(fensapSolutions[i] + ".soln.plt"):
            insertInitialGrid()
            print("Convert " + fensapSolutions[i])
            string = "CreateDatFiles.bat \"" + path + "\" \"" \
                     + grids[i].replace("\\", "/") + "\" \"" + fensapSolutions[i] + "\""
            os.system(string)
    for i in range(len(dropletSolutions)):
        if not dropletdatFiles.__contains__(dropletSolutions[i] + ".dat") \
                and not droplettecplotFiles.__contains__(dropletSolutions[i] + ".drop.plt"):
            insertInitialGrid()
            print("Convert " + dropletSolutions[i])
            string = "CreateDatFilesDrop.bat \"" + path + "\" \"" \
                     + grids[i] + "\" \"" + dropletSolutions[i] + "\""
            os.system(string)
    if len(iceSolutions) > 1:  # To deal with multishot simulation with an link to the original mesh --> Remove swinsol solution
        iceSolutions.pop(0)
    for i in range(len(iceSolutions)):
        if not icedatFiles.__contains__(iceSolutions[i] + ".dat") \
                and not icetecplotFiles.__contains__(iceSolutions[i] + ".ice.plt"):
            print("Convert " + iceSolutions[i])
            string = "CreateDatFilesIce.bat \"" + path + "\" \"" + icegridFiles[i] + "\" \"" + iceSolutions[i] + "\""
            os.system(string)

def createdatfile():
    global initGrid

    insertInitialGrid()
    if len(fensapSolutions) > 1:  # To deal with multishot simulation with an link to the original mesh --> Remove swinsol solution
        fensapSolutions.pop(0)
    for i in range(len(fensapSolutions)):
        if not fensapdatFiles.__contains__(fensapSolutions[i] + ".dat") \
                and not fensaptecplotFiles.__contains__(fensapSolutions[i] + ".soln.plt"):
            fensapsolution = fensapSolutions[i]
            print("Convert " + fensapSolutions[i])
            if len(fensapsolution.split(".")) > 1:  # To deal with multishot simulation with an link to the original mesh --> Remove swinsol solution

               string = "CreateDatFiles.bat \"" + path + "\" \"" \
                         + "grid.ice."+fensapsolution.split(".")[2] + "\" \"" + fensapSolutions[i] + "\""
               os.system(string)
            else:  # To deal with multishot simulation with an link to the original mesh --> Remove swinsol solution
                string = "CreateDatFiles.bat \"" + path + "\" \"" \
                         + grids[i].replace("\\", "/") + "\" \"" + fensapSolutions[i] + "\""
                os.system(string)
    if len(dropletSolutions) > 1:  # To deal with multishot simulation
        dropletSolutions.pop(0)
    for i in range(len(dropletSolutions)):
        if not dropletdatFiles.__contains__(dropletSolutions[i] + ".dat") \
                and not droplettecplotFiles.__contains__(dropletSolutions[i] + ".drop.plt"):
            dropletSolution = dropletSolutions[i]
            print("Convert " + dropletSolution)
            if len(dropletSolution.split(".")) > 1:
                string = "CreateDatFilesDrop.bat \"" + path + "\" \"" \
                         +"grid.ice."+dropletSolution.split(".")[2] + "\" \"" + dropletSolutions[i] + "\""
                os.system(string)
            else:
                string = "CreateDatFilesDrop.bat \"" + path + "\" \"" \
                         + grids[i] + "\" \"" + dropletSolutions[i] + "\""
                os.system(string)
    if len(iceSolutions) > 1:  # To deal with multishot simulation with an link to the original mesh --> Remove swinsol solution
        iceSolutions.pop(0)
    for i in range(len(iceSolutions)):
        if not icedatFiles.__contains__(iceSolutions[i] + ".dat") \
                and not icetecplotFiles.__contains__(iceSolutions[i] + ".ice.plt"):
            iceSolution = iceSolutions[i]
            print("Convert " + iceSolution)


            if len(iceSolution.split(".")) > 1:
                string = "CreateDatFilesIce.bat \"" + path + "\" \"" + "ice.grid.ice."+iceSolution.split(".")[2] + "\" \"" + iceSolutions[
                    i] + "\""
                os.system(string)
            else:
                string = "CreateDatFilesIce.bat \"" + path + "\" \"" + icegridFiles[i] + "\" \"" + iceSolutions[i] + "\""
                os.system(string)

def insertInitialGrid():  # Insert initial grid if necessary
    global initGrid
    global insertInitGrid
    # if len(grids) > 1: # To deal with multishot simulation with an link to the original mesh --> No need for the initial grid
    #    insertInitGrid = True
    if not insertInitGrid:  # Check if it is necessary to insert the initial grid
        if not hasinitGrid:
            firstGrid = fd.askopenfilename()
            initGrid = "Initialgrid.grid"
            os.link(firstGrid, path + "\\" + initGrid)
        # grids.insert(0, os.path.join(path, initGrid))  # absolute path
        grids.insert(0, initGrid)  # local path
        insertInitGrid = True


def createTecplotFile():
    for i in range(len(fensapdatFiles)):
        if not fensaptecplotFiles.__contains__(fensapdatFiles[i].replace(".dat", ".soln.plt")):
            print('Working on File ' + fensapdatFiles[i])
            tecplot.data.load_tecplot(os.path.join(path, fensapdatFiles[i]), read_data_option=ReadDataOption.Replace)
            tecplot.data.save_tecplot_plt(os.path.join(path, fensapdatFiles[i].replace(".dat", ".soln.plt")),
                                          include_text=False,
                                          include_geom=False,
                                          include_data_share_linkage=True)
            os.remove(os.path.join(path, fensapdatFiles[i]))  # delete dat file to free up space on the drive
    for i in range(len(dropletdatFiles)):
        if not droplettecplotFiles.__contains__(dropletdatFiles[i].replace(".dat", ".drop.plt")):
            print('Working on File ' + dropletdatFiles[i])
            tecplot.data.load_tecplot(os.path.join(path, dropletdatFiles[i]), read_data_option=ReadDataOption.Replace)
            tecplot.data.save_tecplot_plt(os.path.join(path, dropletdatFiles[i].replace(".dat", ".drop.plt")),
                                          include_text=False,
                                          include_geom=False,
                                          include_data_share_linkage=True)
            os.remove(os.path.join(path, dropletdatFiles[i]))  # delete dat file to free up space on the drive
    for i in range(len(icedatFiles)):
        if not icetecplotFiles.__contains__(icedatFiles[i].replace(".dat", ".ice.plt")):
            print('Working on File ' + icedatFiles[i])
            tecplot.data.load_tecplot(os.path.join(path, icedatFiles[i]), read_data_option=ReadDataOption.Replace)
            tecplot.data.save_tecplot_plt(os.path.join(path, icedatFiles[i].replace(".dat", ".ice.plt")),
                                          include_text=False,
                                          include_geom=False,
                                          include_data_share_linkage=True)
            os.remove(os.path.join(path, icedatFiles[i]))  # delete dat file to free up space on the drive


def mainRun():
    print('Main Run')
    global folder
    global dataset
    global plot
    global frame
    global rotationRate
    global temperature
    global parameterFile

    for File in fensaptecplotFiles:
        print('Working on File ' + File)
        dataset = tecplot.data.load_tecplot(os.path.join(path, File), read_data_option=ReadDataOption.Replace)
        setDatasetValues()
        folder = "PostPro"
        try:
            if str(File.split(".")[2]).isnumeric():
                folder = "PostPro" + str(File.split(".")[2])
        except:
            pass
        try:
            os.mkdir(path.replace("/", "\\") + "\\" + folder)
        except:
            pass
        try:
            os.mkdir(path.replace("/", "\\") + "\\" + folder + "\\Plots")
        except:
            pass

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

    for File in droplettecplotFiles:
        print('Working on File ' + File)
        folder = "PostPro"

        try:  # Create required folders. In except due to error if folder exists
            if str(File.split(".")[2]).isnumeric():
                folder = "PostPro" + str(File.split(".")[2])
        except:
            pass
        try:
            os.mkdir(path.replace("/", "\\") + "\\" + folder)
        except:
            pass
        try:
            os.mkdir(path.replace("/", "\\") + "\\" + folder + "\\Plots")
        except:
            pass

        dataset = tecplot.data.load_tecplot(os.path.join(path, File), read_data_option=ReadDataOption.Replace)
        plot = frame.plot()
        setDatasetValues()
        prepareScene()
        for scene in droplet3DScenes:
            threeDScene(scene[0], scene[1], scene[2], scene[3], scene[4],scene[5], scene[6], scene[7])
        for slice in dropletSlices:
            setupslices(slice[0], slice[1], slice[2], slice[3], slice[4])
        for slice in dropletWrapSlices:
            setupsliceswrap(slice[0], slice[1], slice[2], slice[3], slice[4], slice[5])

    for File in icetecplotFiles:
        print('Working on File ' + File)
        folder = "PostPro"
        try:
            if str(File.split(".")[2]).isnumeric():
                folder = "PostPro" + str(File.split(".")[2])
        except:
            pass
        try:
            os.mkdir(path.replace("/", "\\") + "\\" + folder)
        except:
            pass
        try:
            os.mkdir(path.replace("/", "\\") + "\\" + folder + "\\Plots")
        except:
            pass
        dataset = tecplot.data.load_tecplot(os.path.join(path, File), read_data_option=ReadDataOption.Replace)
        setDatasetValues()
        prepareSceneIce()
        for scene in ice3DScenes:
            threeDScene(scene[0], scene[1], scene[2], scene[3], scene[4],scene[5], scene[6], scene[7])
        for slice in iceSlices:
            setupslices(slice[0], slice[1], slice[2], slice[3], slice[4])
        for slice in iceWrapSlices:
            setupsliceswrap(slice[0], slice[1], slice[2], slice[3], slice[4], slice[5])

    for File in iceGrids:

        createPostProFolder(File)

        dataset = tecplot.data.load_tecplot(os.path.join(path, fensaptecplotFiles[0]), read_data_option=ReadDataOption.Replace)
        dataset = tecplot.data.load_stl(os.path.join(path, File))
        setDatasetValues()
        prepareSceneIceGrids()
        icescenes()


def createPostProFolder(File):
    print('Working on File ' + File)
    folder = "PostPro"
    try:
        if str(File.split(".")[2]).isnumeric():
            folder = "PostPro" + str(File.split(".")[2])
    except:
        pass
    try:
        os.mkdir(path.replace("/", "\\") + "\\" + folder)
    except:
        pass


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


def icescenes():
    plot.show_contour = False
    plot.show_shade = True
    plot.fieldmaps(wallRegions + inletRegions + 4).shade.color = Color.Red
    plot.fieldmaps(2 * wallRegions + inletRegions + 5).shade.color = Color.Red
    savePicture("25_Ice")
    plot.show_contour = False
    plot.show_shade = False

    slice_0 = plot.slice(0)
    slice_0.slice_source = SliceSource.SurfaceZones
    slice_0.edge.show = True
    slice_0.contour.show = False
    plot.show_shade = False
    slice_0.edge.line_thickness = 0.1
    # Turn on slice and get handle to slice object
    plot.show_slices = True

    slice_0.effects.use_translucency = False

    # Setup 4 evenly spaced slices
    slice_0.show_primary_slice = True
    slice_0.show_start_and_end_slices = False
    slice_0.show_intermediate_slices = False
    slice_0.orientation = SliceSurface.ZPlanes
    # Turn on contours of X Velocity on the slice

    for view in views:
        plot.view.width = view[1]
        plot.view.position = (view[2], view[3], view[4])
        plot.view.psi = view[5]
        plot.view.theta = view[6]
        plot.view.alpha = view[7]

        try:
            os.mkdir(path.replace("/", "\\") + '\\' + folder + '\\45_IceContour')
        except:
            pass
        for cut in Cuts:
            plot.view.width = cut[3]
            plot.view.position = (cut[1],cut[2], 1)
            for radius in radii:
                text = frame.add_text(str(radius), (50, 95))
                plot.slice(0).origin.z = radii
                tecplot.export.save_png(path.replace("/", "\\") + '\\' + folder + '\\45_IceContour\\' + cut[0] + ' ' + str(view[0]) + '.png',
                                        picturewidth, supersample=1)
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

    writeToFile("\nvelocity,all,ref,%s" % velocity)
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
            command='''Integrate [3-7] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar={scalar_var} Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0'''.format(scalar_var=dataset.variable('areaint').index + 1))

    total = float(frame.aux_data['CFDA.INTEGRATION_TOTAL'])/2
    print(total)
    writeToFile("\narea,all,int,%s" % total)
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="SaveIntegrationResults FileName='" + path.replace("/",
                                                                                                      "\\\\") + '\\\\' + folder + '\\\\Plots\\\\Area.txt' + "'")
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command='''Integrate [3-7] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar={scalar_var} Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0'''.format(
                                               scalar_var=dataset.variable('taux').index + 1))

    total = float(frame.aux_data['CFDA.INTEGRATION_TOTAL'])
    print(total)
    writeToFile("\ntaux,all,int,%s" % total)
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="SaveIntegrationResults FileName='" + path.replace("\\",
                                                                                                      "\\\\") + '\\\\' + folder + '\\\\Plots\\\\TX.txt' + "'")

    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command='''Integrate [3-7] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar={scalar_var} Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0'''.format(
                                               scalar_var=dataset.variable('tauy').index + 1))
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command="SaveIntegrationResults FileName='" + path.replace("\\",
                                                                                                      "\\\\") + '\\\\' + folder + '\\\\Plots\\\\TY.txt' + "'")

    total = float(frame.aux_data['CFDA.INTEGRATION_TOTAL'])
    print(total)
    writeToFile("\ntauy,all,int,%s" % total)
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command='''Integrate [3-7] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar={scalar_var} Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0'''.format(
                                               scalar_var=dataset.variable('py').index + 1))

    total = float(frame.aux_data['CFDA.INTEGRATION_TOTAL'])
    print(total)
    writeToFile("\npy,all,int,%s" % total)
    tecplot.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
                                           command='''Integrate [3-7] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar={scalar_var} Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0'''.format(
                                               scalar_var=dataset.variable('px').index + 1))

    total = float(frame.aux_data['CFDA.INTEGRATION_TOTAL'])
    print(total)
    writeToFile("\npx,all,int,%s" % total)


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


def prepareSceneIceGrids():
    print('prepare Scene')
    # Change Aspect Ratio
    tecplot.macro.execute_file('changePaperSize.mcr')

    tecplot.active_frame().plot().frame.width = 14
    tecplot.active_frame().plot().frame.height = 8
    tecplot.active_frame().plot().frame.position = (0, 0)

    # Hide Inlets
    i = 1
    while i <= inletRegions:
        plot.fieldmaps(i).show = False
        i = i + 1

    i = inletRegions + 1

    while i <= inletRegions + wallRegions:
        plot.fieldmaps(i).mesh.line_thickness = 0.05
        i = i + 1

    # Hide Outlet and periodics
    plot.fieldmaps(inletRegions + wallRegions + 1).show = False
    plot.fieldmaps(inletRegions + wallRegions + 2).show = False
    plot.fieldmaps(inletRegions + wallRegions + 3).show = False

    if dataset.variable('X').min() > -0.01 and rotationRate != 0:
        print('\tPeriodic boundary detected')
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
    tecplot.active_frame().plot().frame.position = (0, 0)
    tecplot.active_frame().plot_type = PlotType.Cartesian3D
    plot = tecplot.active_frame().plot()

    if dataset.variable('X').min() > -0.01 and rotationRate != 0:
        print('\tPeriodic boundary detected')
        # Rotate Data
        tecplot.macro.execute_command('''$!AxialDuplicate 
          ZoneList =  [''' + str(1) + '-' + str(wallRegions) + ''']
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
        os.mkdir(path.replace("/", "\\") + '\\' + folder + '\\' + name)
    except:
        pass
    for view in views:
        plot.view.width = view[1]
        plot.view.position = (view[2], view[3], view[4])
        plot.view.psi = view[5]
        plot.view.theta = view[6]
        plot.view.alpha = view[7]

        tecplot.export.save_png(path.replace("/", "\\") + '\\' + folder + '\\' + name + '\\' + str(view[0]) + '.png',
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
        os.mkdir(path.replace("/", "\\") + '\\' + folder + '\\' + name)
    except:
        pass

    for cut in Cuts:
        plot.view.width = cut[3]
        plot.view.position = (cut[1],cut[2], 1)
        for radius in radii:
            text = frame.add_text(str(radius), (50, 95))
            plot.slice(0).origin.z = radius
            tecplot.export.save_png(path.replace("/", "\\") + '\\' + folder + '\\' + name + '\\'+ cut[0] + ' ' + str(radius) + '.png',
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
        os.mkdir(path.replace("/", "\\") + '\\' + folder + '\\49_Mesh')
    except:
        pass

    for cut in Cuts:
        plot.view.width = cut[3]
        plot.view.position = (cut[1],cut[2], 1)
        for radius in radii:
            text = frame.add_text(str(radius), (50, 95))
            plot.slice(0).origin.x = radiusPropeller * radius / 100
            tecplot.export.save_png(path.replace("/", "\\") + '\\' + folder + '\\49_Mesh\\'+ cut[0] + ' ' + str(radius) + '.png',
                                    picturewidth * 2, supersample=1)
        text.text_string = ""


    plot.show_slices = False
    slice_0.contour.show = True
    slice_0.mesh.show = False


def setupslices(variable, foldername, min, max, reverse):
    print('Chordwise plots of ' + variable)
    frame.plot_type = tecplot.constant.PlotType.XYLine

    try:
        os.mkdir(path.replace("/", "\\") + '\\' + folder + '\\' + foldername)
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
            path.replace("/", "\\") + '\\' + folder + '\\' + foldername + '\\' + str(radius) + '.png', picturewidth,
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
            os.mkdir(path.replace("/", "\\") + '\\' + folder + '\\' + foldername)
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
            file_object = open(path + '/' + folder + '/Plots/out.csv', 'a+')
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
                path.replace("/", "\\") + '\\' + folder + '\\' + foldername + '\\' + str(radius) + '.png', picturewidth,
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
        os.mkdir(path.replace("/", "\\") + '\\' + folder + '\\' + foldername)
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
            path.replace("/", "\\") + '\\' + folder + '\\' + foldername + '\\' + str(radius) + '.png', picturewidth,
            supersample=1)
        text.text_string = ""
        textmax.text_string = ""
        tecplot.active_frame().dataset.delete_zones(zone)

        # tecplot.active_frame().plot_type = PlotType.Cartesian3D


def writeToFile(string):
    file_object = open(path + '/' + folder + '/Plots/out.csv', 'a+')
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



searchFile2D(path)

for File in fensapparfiles:
    parameterFile = True
    print(File)
    file1 = open(os.path.join(path, File), 'r')
    data = file1.readlines()
    for line in data:
        if "FSP_ROTATION_VECTOR_Z" in line:
            rotationRate = abs(float(line.split(' ')[2]))
            print(rotationRate)
        if "FSP_FREESTREAM_TEMPERATURE" in line:
            temperature = abs(float(line.split(' ')[2])) - 273.15
            print(temperature)
        if "FSP_FREESTREAM_VELOCITY" in line:
            velocity = abs(float(line.split(' ')[2])) - 273.15
            print(velocity)
        if "GLB_FILE_GRID" in line:
            testString = os.path.join(path, line.split(' ')[2].replace("\"", "").replace("\n", ""))
            print(testString)
            if os.path.isfile(testString):
                initGrid = line.split(' ')[2].replace("\n", "").replace("\"", "")
                print(initGrid)
                hasinitGrid = True

for File in iceparfiles:
    parameterFile = True
    file1 = open(os.path.join(path, File), 'r')
    data = file1.readlines()
    for line in data:
        if "ICE_ROTATION_VECTOR_Z" in line:
            rotationRate = abs(float(line.split(' ')[2]))
            print(rotationRate)
        if "ICE_TEMPERATURE" in line:
            temperature = float(line.split(' ')[2])
            print(temperature)

if not parameterFile:
    root = tkinter.Tk()
    root.withdraw()
    a = simpledialog.askstring(title="Input",
                               prompt="What is the Temperature:")
    temperature = float(a)
    root.withdraw()

createdatfile()
searchFile(path)

tecplot.new_layout()
frame = tecplot.active_frame()
plot = frame.plot()
dataset = []
createTecplotFile()
searchFile(path)

mainRun()
