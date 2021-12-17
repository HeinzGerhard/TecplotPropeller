
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
    global defaultsFile

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
    defaultsFile = ""
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
            if Files == "Post.defaults":
                defaultsFile = os.path.join(root, Files)
            if Files.startswith("Initialgrid.grid"):
                hasinitGrid = True
                initGrid = "Initialgrid.grid"


def createdatfile():
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
    if len(iceSolutions) > 1: # To deal with multishot simulation with an link to the original mesh --> Remove swinsol solution
        iceSolutions.pop(0)
    for i in range(len(iceSolutions)):
        if not icedatFiles.__contains__(iceSolutions[i] + ".dat") \
                and not icetecplotFiles.__contains__(iceSolutions[i] + ".ice.plt"):
            print("Convert " + iceSolutions[i])
            string = "CreateDatFilesIce.bat \"" + path + "\" \"" + icegridFiles[i] + "\" \"" + iceSolutions[i] + "\""
            os.system(string)


def insertInitialGrid():  # Insert initial grid if necessary
    global initGrid
    global insertInitGrid
    #if len(grids) > 1: # To deal with multishot simulation with an link to the original mesh --> No need for the initial grid
    #    insertInitGrid = True
    if not insertInitGrid:  # Check if it is necessary to insert the initial grid
        if not hasinitGrid:
            firstGrid = fd.askopenfilename()
            initGrid = "Initialgrid.grid"
            os.link(firstGrid, path + "\\" + initGrid)
        grids.insert(0, os.path.join(path, initGrid))
        insertInitGrid = True


def createTecplotFile():
    for i in range(len(fensapdatFiles)):
        if not fensaptecplotFiles.__contains__(fensapdatFiles[i].replace(".dat", ".soln.plt")):
            print('Working on File ' + fensapdatFiles[i])
            tecplot.data.load_tecplot(fensapdatFiles[i], read_data_option=ReadDataOption.Replace)
            tecplot.data.save_tecplot_plt(fensapdatFiles[i].replace(".dat", ".soln.plt"),
                                          include_text=False,
                                          include_geom=False,
                                          include_data_share_linkage=True)
            os.remove(fensapdatFiles[i])  # delete dat file to free up space on the drive
    for i in range(len(dropletdatFiles)):
        if not droplettecplotFiles.__contains__(dropletdatFiles[i].replace(".dat", ".drop.plt")):
            print('Working on File ' + dropletdatFiles[i])
            tecplot.data.load_tecplot(dropletdatFiles[i], read_data_option=ReadDataOption.Replace)
            tecplot.data.save_tecplot_plt(dropletdatFiles[i].replace(".dat", ".drop.plt"),
                                          include_text=False,
                                          include_geom=False,
                                          include_data_share_linkage=True)
            os.remove(dropletdatFiles[i])  # delete dat file to free up space on the drive
    for i in range(len(icedatFiles)):
        if not icetecplotFiles.__contains__(icedatFiles[i].replace(".dat", ".ice.plt")):
            print('Working on File ' + icedatFiles[i])
            tecplot.data.load_tecplot(icedatFiles[i], read_data_option=ReadDataOption.Replace)
            tecplot.data.save_tecplot_plt(icedatFiles[i].replace(".dat", ".ice.plt"),
                                          include_text=False,
                                          include_geom=False,
                                          include_data_share_linkage=True)
            os.remove(icedatFiles[i])  # delete dat file to free up space on the drive
