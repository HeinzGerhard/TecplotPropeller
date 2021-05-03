import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *

# Uncomment the following line to connect to a running instance of Tecplot 360:
# tp.session.connect()

tp.active_frame().plot().fieldmaps(1).show=False
tp.active_frame().plot().fieldmaps(2).show=False
tp.active_frame().plot().fieldmaps(8).show=False
tp.active_frame().plot().fieldmaps(9).show=False
tp.active_frame().plot().fieldmaps(10).show=False
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 6.10168233548
  Y = 4.96449777338
  ConsiderStyle = Yes''')
tp.active_frame().plot().view.position=(20.1271,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.3119,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.7287)
tp.active_frame().plot().view.width=3.54681
tp.active_frame().plot().view.position=(20.1271,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.3119,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.7287)
tp.active_frame().plot().view.width=2.40218
tp.active_frame().plot().view.position=(20.0597,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.8915,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.3279)
tp.active_frame().plot().view.width=2.40218
tp.active_frame().plot().view.position=(20.3679,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.3228,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.3581)
tp.active_frame().plot().view.width=2.40218
tp.active_frame().plot().view.position=(20.3679,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.3228,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.3581)
tp.active_frame().plot().view.width=1.24132
tp.active_frame().plot().view.position=(20.2016,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.5257,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.4318)
tp.active_frame().plot().view.width=1.24132
tp.active_frame().plot().view.position=(20.2016,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.5257,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.4318)
tp.active_frame().plot().view.width=0.808999
tp.macro.execute_command('''$!RotateData 
  ZoneList =  [4-8]
  Angle = 180
  XVar = 1
  YVar = 2
  ZVar = 3''')
tp.active_frame().plot().show_shade=False
tp.active_frame().plot().rgb_coloring.red_variable_index=38
tp.active_frame().plot().rgb_coloring.green_variable_index=20
tp.active_frame().plot().rgb_coloring.blue_variable_index=3
tp.active_frame().plot().contour(0).variable_index=3
tp.active_frame().plot().contour(1).variable_index=4
tp.active_frame().plot().contour(2).variable_index=5
tp.active_frame().plot().contour(3).variable_index=6
tp.active_frame().plot().contour(4).variable_index=7
tp.active_frame().plot().contour(5).variable_index=8
tp.active_frame().plot().contour(6).variable_index=9
tp.active_frame().plot().contour(7).variable_index=10
tp.active_frame().plot().show_contour=True
tp.active_frame().plot().contour(0).colormap_name='Large Rainbow'
tp.active_frame().dataset.delete_zones([11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28])
tp.macro.execute_command('$!RedrawAll')
tp.data.save_tecplot_plt('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\soln.plt',
    include_text=False,
    include_geom=False,
    include_data_share_linkage=True)
tp.active_page().name='Untitled'
tp.add_page()
tp.new_layout()
tp.macro.execute_command("""$!ReadDataSet  '\"C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\soln.plt\" '
  ReadDataOption = New
  ResetStyle = Yes
  VarLoadMode = ByName
  AssignStrandIDs = Yes
  VarNameList = '\"X\" \"Y\" \"Z\" \"Density (kg/m^3)\" \"Pressure (N/m^2)\" \"V1-velocity (m/s); Velocity\" \"V2-velocity (m/s)\" \"V3-velocity (m/s)\" \"Static temperature (K)\" \"nutilde (m^2/s)\" \"wall distance (m)\" \"turbulent viscosity (kg/m s)\" \"y-plus\" \"u-plus\" \"laminar viscosity (kg/m s)\" \"thermal conductivity (W/m/K)\" \"SF1-shear stress (Pa); Shear\" \"SF2-shear stress (Pa)\" \"SF3-shear stress (Pa)\" \"Classical heat flux (W/m^2)\" \"Gresho heat flux (W/m^2)\" \"Velocity Magnitude\" \"X Grid K Unit Normal\" \"Y Grid K Unit Normal\" \"Z Grid K Unit Normal\" \"px\" \"py\" \"pz\" \"mx\" \"my\" \"mz\" \"taux\" \"tauy\" \"tauz\" \"mxt\" \"myt\" \"mzt\" \"ShearStress\" \"rot\" \"vx\" \"vy\" \"vmag\"'""")
tp.active_frame().plot().fieldmaps(1).show=False
tp.active_frame().plot().fieldmaps(2).show=False
tp.active_frame().plot().fieldmaps(6).show=False
tp.active_frame().plot().fieldmaps(7).show=False
tp.active_frame().plot().fieldmaps(8).show=False
tp.macro.execute_command('''$!RotateData 
  ZoneList =  [4-6]
  Angle = 180
  XVar = 1
  YVar = 2
  ZVar = 3''')
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().view.position=(20.1295,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.3136,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.7305)
tp.active_frame().plot().view.width=3.40819
tp.active_frame().plot().fieldmaps(6).show=True
tp.active_frame().plot().fieldmaps(7).show=True
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().view.position=(20.1295,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.3136,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.7305)
tp.active_frame().plot().view.width=1.89177
tp.active_frame().plot().view.position=(20.1292,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.5238,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.549)
tp.active_frame().plot().view.width=1.89177
tp.active_frame().plot().view.position=(20.1292,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.5238,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.549)
tp.active_frame().plot().view.width=1.0006
tp.active_frame().plot().view.position=(20.0804,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.6176,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.5409)
tp.active_frame().plot().view.width=1.0006
tp.macro.execute_command('''$!AxialDuplicate 
  ZoneList =  [4-8]
  Angle = 180
  NumDuplicates = 1
  XVar = 1
  YVar = 2
  ZVar = 3''')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot(PlotType.Cartesian3D).use_lighting_effect=False
tp.active_frame().plot(PlotType.Cartesian3D).use_lighting_effect=True
tp.active_page().name='Untitled'
tp.add_page()
tp.new_layout()
tp.macro.execute_command("""$!ReadDataSet  '\"C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\soln.plt\" '
  ReadDataOption = New
  ResetStyle = Yes
  VarLoadMode = ByName
  AssignStrandIDs = Yes
  VarNameList = '\"X\" \"Y\" \"Z\" \"Density (kg/m^3)\" \"Pressure (N/m^2)\" \"V1-velocity (m/s); Velocity\" \"V2-velocity (m/s)\" \"V3-velocity (m/s)\" \"Static temperature (K)\" \"nutilde (m^2/s)\" \"wall distance (m)\" \"turbulent viscosity (kg/m s)\" \"y-plus\" \"u-plus\" \"laminar viscosity (kg/m s)\" \"thermal conductivity (W/m/K)\" \"SF1-shear stress (Pa); Shear\" \"SF2-shear stress (Pa)\" \"SF3-shear stress (Pa)\" \"Classical heat flux (W/m^2)\" \"Gresho heat flux (W/m^2)\" \"Velocity Magnitude\" \"X Grid K Unit Normal\" \"Y Grid K Unit Normal\" \"Z Grid K Unit Normal\" \"px\" \"py\" \"pz\" \"mx\" \"my\" \"mz\" \"taux\" \"tauy\" \"tauz\" \"mxt\" \"myt\" \"mzt\" \"ShearStress\" \"rot\" \"vx\" \"vy\" \"vmag\"'""")
tp.active_frame().plot().fieldmaps(1).show=False
tp.active_frame().plot().fieldmaps(2).show=False
tp.active_frame().plot().fieldmaps(6).show=False
tp.active_frame().plot().fieldmaps(7).show=False
tp.active_frame().plot().fieldmaps(8).show=False
tp.macro.execute_command('''$!AxialDuplicate 
  ZoneList =  [4-6]
  Angle = 180
  NumDuplicates = 1
  XVar = 1
  YVar = 2
  ZVar = 3''')
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().view.position=(20.1295,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.3136,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.7305)
tp.active_frame().plot().view.width=3.29752
tp.active_frame().plot().view.position=(20.2032,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.7429,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.2482)
tp.active_frame().plot().view.width=3.29752
tp.active_frame().plot().view.position=(20.2032,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.7429,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.2482)
tp.active_frame().plot().view.width=1.96124
tp.active_frame().plot().fieldmaps(9).show=False
tp.active_frame().plot().fieldmaps(10).show=False
tp.active_frame().plot().fieldmaps(7).show=True
tp.active_frame().plot().fieldmaps(6).show=True
tp.macro.execute_command('$!RedrawAll')
tp.active_page().name='Untitled'
tp.add_page()
tp.new_layout()
tp.macro.execute_command("""$!ReadDataSet  '\"C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\soln.plt\" '
  ReadDataOption = New
  ResetStyle = Yes
  VarLoadMode = ByName
  AssignStrandIDs = Yes
  VarNameList = '\"X\" \"Y\" \"Z\" \"Density (kg/m^3)\" \"Pressure (N/m^2)\" \"V1-velocity (m/s); Velocity\" \"V2-velocity (m/s)\" \"V3-velocity (m/s)\" \"Static temperature (K)\" \"nutilde (m^2/s)\" \"wall distance (m)\" \"turbulent viscosity (kg/m s)\" \"y-plus\" \"u-plus\" \"laminar viscosity (kg/m s)\" \"thermal conductivity (W/m/K)\" \"SF1-shear stress (Pa); Shear\" \"SF2-shear stress (Pa)\" \"SF3-shear stress (Pa)\" \"Classical heat flux (W/m^2)\" \"Gresho heat flux (W/m^2)\" \"Velocity Magnitude\" \"X Grid K Unit Normal\" \"Y Grid K Unit Normal\" \"Z Grid K Unit Normal\" \"px\" \"py\" \"pz\" \"mx\" \"my\" \"mz\" \"taux\" \"tauy\" \"tauz\" \"mxt\" \"myt\" \"mzt\" \"ShearStress\" \"rot\" \"vx\" \"vy\" \"vmag\"'""")
tp.active_frame().plot().fieldmaps(1).show=False
tp.active_frame().plot().fieldmaps(2).show=False
tp.active_frame().plot().fieldmaps(8).show=False
tp.active_frame().plot().fieldmaps(9).show=False
tp.active_frame().plot().fieldmaps(10).show=False
tp.macro.execute_command('''$!AxialDuplicate 
  ZoneList =  [4-8]
  Angle = 180
  NumDuplicates = 1
  XVar = 1
  YVar = 2
  ZVar = 3''')
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().view.position=(20.1295,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.3136,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.7305)
tp.active_frame().plot().view.width=2.83034
tp.active_frame().plot().view.position=(20.0832,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    12.1967,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.0352)
tp.active_frame().plot().view.width=2.83034
tp.active_frame().plot().view.position=(20.0832,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    12.1967,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.0352)
tp.active_frame().plot().view.width=1.38905
tp.active_frame().plot().view.position=(20.0728,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.96,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.2558)
tp.active_frame().plot().view.width=1.38905
tp.active_frame().plot().view.position=(20.0728,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.96,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.2558)
tp.active_frame().plot().view.width=0.91323
tp.active_frame().plot().view.position=(20.1072,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.8992,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.2569)
tp.active_frame().plot().view.width=0.91323
tp.active_frame().plot().rgb_coloring.red_variable_index=38
tp.active_frame().plot().rgb_coloring.green_variable_index=20
tp.active_frame().plot().rgb_coloring.blue_variable_index=3
tp.active_frame().plot().contour(0).variable_index=3
tp.active_frame().plot().contour(1).variable_index=4
tp.active_frame().plot().contour(2).variable_index=5
tp.active_frame().plot().contour(3).variable_index=6
tp.active_frame().plot().contour(4).variable_index=7
tp.active_frame().plot().contour(5).variable_index=8
tp.active_frame().plot().contour(6).variable_index=9
tp.active_frame().plot().contour(7).variable_index=10
tp.active_frame().plot().show_contour=True
tp.active_frame().plot().show_shade=False
tp.active_frame().plot().contour(0).colormap_name='Large Rainbow'
tp.active_frame().plot().contour(0).levels.reset_levels([1.16, 1.1875, 1.215, 1.2425, 1.27])
tp.active_frame().plot().contour(0).levels.reset_levels([1.16, 1.1875, 1.215, 1.2425, 1.27])
tp.active_frame().plot().contour(0).variable_index=4
tp.active_frame().plot().contour(0).levels.reset_levels([10000, 34000, 58000, 82000, 106000])
tp.active_frame().plot().contour(0).levels.reset_levels([10000, 33750, 57500, 81250, 105000])
tp.active_frame().plot().contour(0).levels.reset_levels([10000, 20555.6, 31111.1, 41666.7, 52222.2, 62777.8, 73333.3, 83888.9, 94444.4, 105000])
tp.active_frame().plot().contour(0).variable_index=3
tp.active_frame().plot().contour(0).legend.vertical=False
tp.active_frame().plot().contour(0).legend.anchor_alignment=AnchorAlignment.BottomCenter
tp.active_frame().plot().contour(0).legend.position=(50,
    tp.active_frame().plot().contour(0).legend.position[1])
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().contour(0).labels.step=3
tp.active_frame().plot().contour(0).labels.step=4
tp.active_frame().plot().contour(0).labels.step=5
tp.active_frame().plot().contour(0).levels.reset_levels([1.16, 1.1644, 1.1688, 1.1732, 1.1776, 1.182, 1.1864, 1.1908, 1.1952, 1.1996, 1.204, 1.2084, 1.2128, 1.2172, 1.2216, 1.226, 1.2304, 1.2348, 1.2392, 1.2436, 1.248, 1.2524, 1.2568, 1.2612, 1.2656, 1.27])
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().contour(0).levels.reset_levels([1.16, 1.1644, 1.1688, 1.1732, 1.1776, 1.182, 1.1864, 1.1908, 1.1952, 1.1996, 1.204, 1.2084, 1.2128, 1.2172, 1.2216, 1.226, 1.2304, 1.2348, 1.2392, 1.2436, 1.248, 1.2524, 1.2568, 1.2612, 1.2656, 1.27])
tp.active_frame().plot().contour(0).variable_index=4
tp.active_frame().plot().contour(0).levels.reset_levels([12, 12.04, 12.08, 12.12, 12.16, 12.2, 12.24, 12.28, 12.32, 12.36, 12.4, 12.44, 12.48, 12.52, 12.56, 12.6, 12.64, 12.68, 12.72, 12.76, 12.8, 12.84, 12.88, 12.92, 12.96, 13])
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().contour(0).labels.step=6
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().contour(0).labels.step=7
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().contour(0).labels.step=6
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 8.80925284513
  Y = 4.08572488867
  ConsiderStyle = Yes''')
tp.active_frame().plot().contour(0).levels.reset_levels([12, 12.05, 12.1, 12.15, 12.2, 12.25, 12.3, 12.35, 12.4, 12.45, 12.5, 12.55, 12.6, 12.65, 12.7, 12.75, 12.8, 12.85, 12.9, 12.95, 13])
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().contour(0).labels.step=5
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SetFieldVariables ConvectionVarsAreMomentum='F' UVarNum=6 VVarNum=7 WVarNum=8 ID1='Pressure' Variable1=5 ID2='NotUsed' Variable2=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SetFieldVariables ConvectionVarsAreMomentum='F' UVarNum=6 VVarNum=7 WVarNum=8 ID1='Density' Variable1=4 ID2='NotUsed' Variable2=0")
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Calculate Function='GRIDKUNITNORMAL' Normalization='None' ValueLocation='Nodal' CalculateOnDemand='T' UseMorePointsForFEGradientCalculations='F'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Calculate Function='VELOCITYMAG' Normalization='None' ValueLocation='Nodal' CalculateOnDemand='T' UseMorePointsForFEGradientCalculations='F'")
tp.data.operate.execute_equation(equation='{px} = -({Pressure (N/m^2)}-101325) * {X Grid K Unit Normal}')
tp.data.operate.execute_equation(equation='{py} = -({Pressure (N/m^2)}-101325)  * {Y Grid K Unit Normal}')
tp.data.operate.execute_equation(equation='{pz} = -({Pressure (N/m^2)}-101325)  * {Z Grid K Unit Normal}')
tp.data.operate.execute_equation(equation='{mx} = Y * {pz} - Z * {py}')
tp.data.operate.execute_equation(equation='{my} = Z * {px} - X * {pz}')
tp.data.operate.execute_equation(equation='{mz} = X * {py} - Y * {px}')
tp.data.operate.execute_equation(equation='{taux} = {SF1-shear stress (Pa); Shear} - {X Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
tp.data.operate.execute_equation(equation='{tauy} = {SF2-shear stress (Pa)} - {Y Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
tp.data.operate.execute_equation(equation='{tauz} = {SF3-shear stress (Pa)} - {Z Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
tp.data.operate.execute_equation(equation='{mxt} = Y * {tauz} - Z * {tauy} ')
tp.data.operate.execute_equation(equation='{myt} = Z * {taux} - X * {tauz}')
tp.data.operate.execute_equation(equation='{mzt} = X * {tauy} - Y * {taux}')
tp.data.operate.execute_equation(equation='{ShearStress} = sqrt({SF1-shear stress (Pa); Shear}**2+ {SF2-shear stress (Pa)}**2+ {SF3-shear stress (Pa)}**2)')
tp.data.operate.execute_equation(equation='{rot} = 5000/60')
tp.data.operate.execute_equation(equation='{vx} = {V1-velocity (m/s); Velocity} - 2 * 3.14159265 *  Y * {rot}')
tp.data.operate.execute_equation(equation='{vy} = {V2-velocity (m/s)} + 2 * 3.14159265 *  X * {rot}')
tp.data.operate.execute_equation(equation='{vmag} =  sqrt({vx}**2+ {vy}**2+ {V3-velocity (m/s)}**2)')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!GlobalThreeD RotateOrigin{X = 0}')
tp.macro.execute_command('$!GlobalThreeD RotateOrigin{Z = 0}')
tp.active_frame().plot().contour(0).variable_index=41
tp.active_frame().plot().contour(0).legend.show_cutoff_levels=True
tp.active_frame().plot().view.psi=59.525
tp.active_frame().plot().view.theta=-120
tp.active_frame().plot().view.alpha=-1.22379e-16
tp.active_frame().plot().view.position=(20.0113,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    11.8438,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    13.4501)
tp.active_frame().plot().view.width=0.91323
tp.active_frame().plot().contour(0).variable_index=37
tp.active_frame().plot().view.position=(0.0481052,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    0.318077,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    26.8613)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.position=(0.25141,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.200699,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.theta=0
tp.active_frame().plot().view.alpha=0
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    0,
    tp.active_frame().plot().view.position[2])
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().view.position=(0,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    0,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.width=0.568764
tp.macro.execute_command('''$!Pick SetMouseMode
  MouseMode = Select''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 1.57718951014
  Y = 0.570633349827
  CollectingObjectsMode = HomogeneousAdd
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!Pick SetMouseMode
  MouseMode = Select''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 1.45843641762
  Y = 0.867516081148
  CollectingObjectsMode = HomogeneousAdd
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!Pick SetMouseMode
  MouseMode = Select''')
tp.active_frame().plot().axes.x_axis.show=True
tp.active_frame().plot().axes.x_axis.show=False
tp.macro.execute_command('$!Paper PaperSize = A4')
tp.macro.execute_command('$!WorkspaceView FitPaper')
tp.macro.execute_command('$!Paper PaperSize = Custom1')
tp.macro.execute_command('$!WorkspaceView FitPaper')
tp.macro.execute_command('$!Paper PaperSize = Letter')
tp.macro.execute_command('$!WorkspaceView FitPaper')
tp.active_frame().plot().view.position=(0,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    0,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.width=0.579161
tp.active_frame().plot().view.position=(0,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    0,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.width=0.456721
tp.active_frame().plot().view.position=(-0.126975,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0200828,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.width=0.456721
tp.active_frame().plot().view.position=(-0.126975,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0200828,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.width=0.321346
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.width=0.321346
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.width=0.301161
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.width=0.204325
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.width=0.164863
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.width=0.180409
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.width=0.251842
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.width=0.284149
tp.active_frame().plot().view.rotate_axes(angle=180,normal=(0,1,0))
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().view.rotate_axes(angle=180,normal=(0,0,1))
tp.active_frame().plot().view.rotate_axes(angle=180,normal=(0,0,1))
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().view.position=(0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -1.69455e-17)
tp.active_frame().plot().view.width=0.268776
tp.active_frame().plot().view.position=(0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -1.69455e-17)
tp.active_frame().plot().view.width=0.437792
tp.active_frame().plot().view.position=(0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -1.69455e-17)
tp.active_frame().plot().view.width=0.559023
tp.active_frame().plot().view.position=(-0.137941,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0702983,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -2.40998e-17)
tp.active_frame().plot().view.width=0.559023
tp.active_frame().plot().view.position=(-0.137941,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0702983,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -2.40998e-17)
tp.active_frame().plot().view.width=0.248593
tp.active_frame().plot().view.position=(-0.137941,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0702983,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -2.40998e-17)
tp.active_frame().plot().view.width=0.335827
tp.active_frame().plot().view.position=(-0.0402435,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0465853,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -2.11958e-17)
tp.active_frame().plot().view.width=0.335827
tp.active_frame().plot().view.psi=168.815
tp.active_frame().plot().view.theta=-174.408
tp.active_frame().plot().view.alpha=-3.70424e-20
tp.active_frame().plot().view.position=(-0.0445055,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0415612,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -0.00903629)
tp.active_frame().plot().view.width=0.335827
tp.active_frame().plot().view.position=(-0.0445055,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0415612,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -0.00903629)
tp.active_frame().plot().view.width=0.395154
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -1)
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().view.position=(-0.0445055,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0415612,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    1)
tp.active_frame().plot().view.width=0.395154
tp.active_frame().plot().view.position=(-0.0445055,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0415612,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    1)
tp.active_frame().plot().view.width=0.209462
tp.active_frame().plot().view.position=(0.0694378,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0556339,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0.999426)
tp.active_frame().plot().view.width=0.209462
tp.active_frame().plot().view.position=(0.0694378,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0556339,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0.999426)
tp.active_frame().plot().view.width=0.335963
tp.active_frame().plot().view.position=(0.0694378,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0556339,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0.999426)
tp.active_frame().plot().view.width=0.485089
tp.active_frame().plot().view.position=(0.0694378,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0556339,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0.999426)
tp.active_frame().plot().view.width=1.06785
tp.active_frame().plot().view.position=(0.0694378,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0556339,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0.999426)
tp.active_frame().plot().view.width=2.37563
tp.active_frame().plot().view.position=(0.0694378,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0556339,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0.999426)
tp.active_frame().plot().view.width=4.3795
tp.active_frame().plot().view.position=(0.0694378,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0556339,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0.999426)
tp.active_frame().plot().view.width=7.70149
tp.active_frame().plot().view.position=(0.0694378,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0556339,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0.999426)
tp.active_frame().plot().view.width=11.5575
tp.active_frame().plot().view.position=(3.19195,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    0.346501,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    1.13873)
tp.active_frame().plot().view.width=11.5575
tp.active_frame().plot().view.psi=119.501
tp.active_frame().plot().view.theta=-131.194
tp.active_frame().plot().view.alpha=-3.68545e-20
tp.active_frame().plot().view.position=(1.74199,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -2.65215,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    1.23972)
tp.active_frame().plot().view.width=11.5575
tp.active_frame().plot().view.position=(1.74199,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -2.65215,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    1.23972)
tp.active_frame().plot().view.width=7.35233
tp.active_frame().plot().view.position=(1.04189,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -2.02305,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    1.04091)
tp.active_frame().plot().view.width=7.35233
tp.active_frame().plot().view.fit(consider_blanking=True)
tp.active_frame().plot().view.position=(18.3984,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    15.6359,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -12.7655)
tp.active_frame().plot().view.width=2.90158
tp.active_frame().plot().view.position=(18.3984,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    15.6359,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -12.7655)
tp.active_frame().plot().view.width=3.14925
tp.active_frame().plot().view.position=(17.718,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    15.4423,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -13.8958)
tp.active_frame().plot().view.width=3.14925
tp.active_frame().plot().view.position=(17.718,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    15.4423,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -13.8958)
tp.active_frame().plot().view.width=1.63627
tp.active_frame().plot().view.position=(18.0951,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    15.4468,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -13.389)
tp.active_frame().plot().view.width=1.63627
tp.active_frame().plot().view.position=(18.0951,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    15.4468,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -13.389)
tp.active_frame().plot().view.width=1.01029
tp.active_frame().plot().view.position=(17.7676,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    15.5735,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -13.6771)
tp.active_frame().plot().view.width=1.01029
tp.active_frame().plot().view.position=(17.7676,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    15.5735,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -13.6771)
tp.active_frame().plot().view.width=0.688635
tp.active_frame().plot().view.position=(17.9566,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    15.5554,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -13.4468)
tp.active_frame().plot().view.width=0.688635
tp.active_frame().plot().view.position=(0.0762682,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0942725,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().view.position=(0.12117,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.width=0.336154
tp.active_frame().plot().view.position=(0.12117,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.width=0.265334
tp.export.save_png('C:\\Users\\nicolacm\\Desktop\\untitled.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().show_shade=True
tp.active_frame().plot().show_shade=False
tp.active_page().name='Untitled'
tp.add_page()
tp.new_layout()
tp.macro.execute_command('''$!Pick SetMouseMode
  MouseMode = Select''')
tp.macro.execute_command("""$!ReadDataSet  '\"C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\soln.plt\" '
  ReadDataOption = New
  ResetStyle = Yes
  VarLoadMode = ByName
  AssignStrandIDs = Yes
  VarNameList = '\"X\" \"Y\" \"Z\" \"Density (kg/m^3)\" \"Pressure (N/m^2)\" \"V1-velocity (m/s); Velocity\" \"V2-velocity (m/s)\" \"V3-velocity (m/s)\" \"Static temperature (K)\" \"nutilde (m^2/s)\" \"wall distance (m)\" \"turbulent viscosity (kg/m s)\" \"y-plus\" \"u-plus\" \"laminar viscosity (kg/m s)\" \"thermal conductivity (W/m/K)\" \"SF1-shear stress (Pa); Shear\" \"SF2-shear stress (Pa)\" \"SF3-shear stress (Pa)\" \"Classical heat flux (W/m^2)\" \"Gresho heat flux (W/m^2)\" \"Velocity Magnitude\" \"X Grid K Unit Normal\" \"Y Grid K Unit Normal\" \"Z Grid K Unit Normal\" \"px\" \"py\" \"pz\" \"mx\" \"my\" \"mz\" \"taux\" \"tauy\" \"tauz\" \"mxt\" \"myt\" \"mzt\" \"ShearStress\" \"rot\" \"vx\" \"vy\" \"vmag\"'""")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SetFieldVariables ConvectionVarsAreMomentum='F' UVarNum=6 VVarNum=7 WVarNum=8 ID1='Density' Variable1=4 ID2='NotUsed' Variable2=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Calculate Function='GRIDKUNITNORMAL' Normalization='None' ValueLocation='Nodal' CalculateOnDemand='T' UseMorePointsForFEGradientCalculations='F'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Calculate Function='VELOCITYMAG' Normalization='None' ValueLocation='Nodal' CalculateOnDemand='T' UseMorePointsForFEGradientCalculations='F'")
tp.data.operate.execute_equation(equation='{px} = -({Pressure (N/m^2)}-101325) * {X Grid K Unit Normal}')
tp.data.operate.execute_equation(equation='{py} = -({Pressure (N/m^2)}-101325)  * {Y Grid K Unit Normal}')
tp.data.operate.execute_equation(equation='{pz} = -({Pressure (N/m^2)}-101325)  * {Z Grid K Unit Normal}')
tp.data.operate.execute_equation(equation='{mx} = Y * {pz} - Z * {py}')
tp.data.operate.execute_equation(equation='{my} = Z * {px} - X * {pz}')
tp.data.operate.execute_equation(equation='{mz} = X * {py} - Y * {px}')
tp.data.operate.execute_equation(equation='{taux} = {SF1-shear stress (Pa); Shear} - {X Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
tp.data.operate.execute_equation(equation='{tauy} = {SF2-shear stress (Pa)} - {Y Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
tp.data.operate.execute_equation(equation='{tauz} = {SF3-shear stress (Pa)} - {Z Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
tp.data.operate.execute_equation(equation='{mxt} = Y * {tauz} - Z * {tauy} ')
tp.data.operate.execute_equation(equation='{myt} = Z * {taux} - X * {tauz}')
tp.data.operate.execute_equation(equation='{mzt} = X * {tauy} - Y * {taux}')
tp.data.operate.execute_equation(equation='{ShearStress} = sqrt({SF1-shear stress (Pa); Shear}**2+ {SF2-shear stress (Pa)}**2+ {SF3-shear stress (Pa)}**2)')
tp.data.operate.execute_equation(equation='{rot} = 5000/60')
tp.data.operate.execute_equation(equation='{vx} = {V1-velocity (m/s); Velocity} - 2 * 3.14159265 *  Y * {rot}')
tp.data.operate.execute_equation(equation='{vy} = {V2-velocity (m/s)} + 2 * 3.14159265 *  X * {rot}')
tp.data.operate.execute_equation(equation='{vmag} =  sqrt({vx}**2+ {vy}**2+ {V3-velocity (m/s)}**2)')
tp.active_frame().plot().fieldmaps(1).show=False
tp.active_frame().plot().fieldmaps(2).show=False
tp.active_frame().plot().fieldmaps(8).show=False
tp.active_frame().plot().fieldmaps(9).show=False
tp.active_frame().plot().fieldmaps(10).show=False
tp.macro.execute_command('''$!AxialDuplicate 
  ZoneList =  [4-8]
  Angle = 180
  NumDuplicates = 1
  XVar = 1
  YVar = 2
  ZVar = 3''')
tp.macro.execute_command('$!GlobalThreeD RotateOrigin{X = 0}')
tp.macro.execute_command('$!GlobalThreeD RotateOrigin{Z = 0}')
tp.active_page().name='Untitled'
tp.add_page()
tp.new_layout()
tp.macro.execute_command("""$!ReadDataSet  '\"C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\soln.plt\" '
  ReadDataOption = New
  ResetStyle = Yes
  VarLoadMode = ByName
  AssignStrandIDs = Yes
  VarNameList = '\"X\" \"Y\" \"Z\" \"Density (kg/m^3)\" \"Pressure (N/m^2)\" \"V1-velocity (m/s); Velocity\" \"V2-velocity (m/s)\" \"V3-velocity (m/s)\" \"Static temperature (K)\" \"nutilde (m^2/s)\" \"wall distance (m)\" \"turbulent viscosity (kg/m s)\" \"y-plus\" \"u-plus\" \"laminar viscosity (kg/m s)\" \"thermal conductivity (W/m/K)\" \"SF1-shear stress (Pa); Shear\" \"SF2-shear stress (Pa)\" \"SF3-shear stress (Pa)\" \"Classical heat flux (W/m^2)\" \"Gresho heat flux (W/m^2)\" \"Velocity Magnitude\" \"X Grid K Unit Normal\" \"Y Grid K Unit Normal\" \"Z Grid K Unit Normal\" \"px\" \"py\" \"pz\" \"mx\" \"my\" \"mz\" \"taux\" \"tauy\" \"tauz\" \"mxt\" \"myt\" \"mzt\" \"ShearStress\" \"rot\" \"vx\" \"vy\" \"vmag\"'""")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SetFieldVariables ConvectionVarsAreMomentum='F' UVarNum=6 VVarNum=7 WVarNum=8 ID1='Density' Variable1=4 ID2='NotUsed' Variable2=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Calculate Function='GRIDKUNITNORMAL' Normalization='None' ValueLocation='Nodal' CalculateOnDemand='T' UseMorePointsForFEGradientCalculations='F'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Calculate Function='VELOCITYMAG' Normalization='None' ValueLocation='Nodal' CalculateOnDemand='T' UseMorePointsForFEGradientCalculations='F'")
tp.data.operate.execute_equation(equation='{px} = -({Pressure (N/m^2)}-101325) * {X Grid K Unit Normal}')
tp.data.operate.execute_equation(equation='{py} = -({Pressure (N/m^2)}-101325)  * {Y Grid K Unit Normal}')
tp.data.operate.execute_equation(equation='{pz} = -({Pressure (N/m^2)}-101325)  * {Z Grid K Unit Normal}')
tp.data.operate.execute_equation(equation='{mx} = Y * {pz} - Z * {py}')
tp.data.operate.execute_equation(equation='{my} = Z * {px} - X * {pz}')
tp.data.operate.execute_equation(equation='{mz} = X * {py} - Y * {px}')
tp.data.operate.execute_equation(equation='{taux} = {SF1-shear stress (Pa); Shear} - {X Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
tp.data.operate.execute_equation(equation='{tauy} = {SF2-shear stress (Pa)} - {Y Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
tp.data.operate.execute_equation(equation='{tauz} = {SF3-shear stress (Pa)} - {Z Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
tp.data.operate.execute_equation(equation='{mxt} = Y * {tauz} - Z * {tauy} ')
tp.data.operate.execute_equation(equation='{myt} = Z * {taux} - X * {tauz}')
tp.data.operate.execute_equation(equation='{mzt} = X * {tauy} - Y * {taux}')
tp.data.operate.execute_equation(equation='{ShearStress} = sqrt({SF1-shear stress (Pa); Shear}**2+ {SF2-shear stress (Pa)}**2+ {SF3-shear stress (Pa)}**2)')
tp.data.operate.execute_equation(equation='{rot} = 5000/60')
tp.data.operate.execute_equation(equation='{vx} = {V1-velocity (m/s); Velocity} - 2 * 3.14159265 *  Y * {rot}')
tp.data.operate.execute_equation(equation='{vy} = {V2-velocity (m/s)} + 2 * 3.14159265 *  X * {rot}')
tp.data.operate.execute_equation(equation='{vmag} =  sqrt({vx}**2+ {vy}**2+ {V3-velocity (m/s)}**2)')
tp.active_frame().plot().fieldmaps(1).show=False
tp.active_frame().plot().fieldmaps(2).show=False
tp.active_frame().plot().fieldmaps(8).show=False
tp.active_frame().plot().fieldmaps(9).show=False
tp.active_frame().plot().fieldmaps(10).show=False
tp.macro.execute_command('''$!AxialDuplicate 
  ZoneList =  [4-8]
  Angle = 180
  NumDuplicates = 1
  XVar = 1
  YVar = 2
  ZVar = 3''')
tp.macro.execute_command('$!GlobalThreeD RotateOrigin{X = 0}')
tp.macro.execute_command('$!GlobalThreeD RotateOrigin{Z = 0}')
tp.active_frame().plot().contour(0).variable_index=3
tp.active_frame().plot().contour(0).colormap_name='Large Rainbow'
tp.active_page().name='Untitled'
tp.add_page()
tp.new_layout()
tp.macro.execute_command("""$!ReadDataSet  '\"C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\soln.plt\" '
  ReadDataOption = New
  ResetStyle = Yes
  VarLoadMode = ByName
  AssignStrandIDs = Yes
  VarNameList = '\"X\" \"Y\" \"Z\" \"Density (kg/m^3)\" \"Pressure (N/m^2)\" \"V1-velocity (m/s); Velocity\" \"V2-velocity (m/s)\" \"V3-velocity (m/s)\" \"Static temperature (K)\" \"nutilde (m^2/s)\" \"wall distance (m)\" \"turbulent viscosity (kg/m s)\" \"y-plus\" \"u-plus\" \"laminar viscosity (kg/m s)\" \"thermal conductivity (W/m/K)\" \"SF1-shear stress (Pa); Shear\" \"SF2-shear stress (Pa)\" \"SF3-shear stress (Pa)\" \"Classical heat flux (W/m^2)\" \"Gresho heat flux (W/m^2)\" \"Velocity Magnitude\" \"X Grid K Unit Normal\" \"Y Grid K Unit Normal\" \"Z Grid K Unit Normal\" \"px\" \"py\" \"pz\" \"mx\" \"my\" \"mz\" \"taux\" \"tauy\" \"tauz\" \"mxt\" \"myt\" \"mzt\" \"ShearStress\" \"rot\" \"vx\" \"vy\" \"vmag\"'""")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SetFieldVariables ConvectionVarsAreMomentum='F' UVarNum=6 VVarNum=7 WVarNum=8 ID1='Density' Variable1=4 ID2='NotUsed' Variable2=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Calculate Function='GRIDKUNITNORMAL' Normalization='None' ValueLocation='Nodal' CalculateOnDemand='T' UseMorePointsForFEGradientCalculations='F'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Calculate Function='VELOCITYMAG' Normalization='None' ValueLocation='Nodal' CalculateOnDemand='T' UseMorePointsForFEGradientCalculations='F'")
tp.data.operate.execute_equation(equation='{px} = -({Pressure (N/m^2)}-101325) * {X Grid K Unit Normal}')
tp.data.operate.execute_equation(equation='{py} = -({Pressure (N/m^2)}-101325)  * {Y Grid K Unit Normal}')
tp.data.operate.execute_equation(equation='{pz} = -({Pressure (N/m^2)}-101325)  * {Z Grid K Unit Normal}')
tp.data.operate.execute_equation(equation='{mx} = Y * {pz} - Z * {py}')
tp.data.operate.execute_equation(equation='{my} = Z * {px} - X * {pz}')
tp.data.operate.execute_equation(equation='{mz} = X * {py} - Y * {px}')
tp.data.operate.execute_equation(equation='{taux} = {SF1-shear stress (Pa); Shear} - {X Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
tp.data.operate.execute_equation(equation='{tauy} = {SF2-shear stress (Pa)} - {Y Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
tp.data.operate.execute_equation(equation='{tauz} = {SF3-shear stress (Pa)} - {Z Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
tp.data.operate.execute_equation(equation='{mxt} = Y * {tauz} - Z * {tauy} ')
tp.data.operate.execute_equation(equation='{myt} = Z * {taux} - X * {tauz}')
tp.data.operate.execute_equation(equation='{mzt} = X * {tauy} - Y * {taux}')
tp.data.operate.execute_equation(equation='{ShearStress} = sqrt({SF1-shear stress (Pa); Shear}**2+ {SF2-shear stress (Pa)}**2+ {SF3-shear stress (Pa)}**2)')
tp.data.operate.execute_equation(equation='{rot} = 5000/60')
tp.data.operate.execute_equation(equation='{vx} = {V1-velocity (m/s); Velocity} - 2 * 3.14159265 *  Y * {rot}')
tp.data.operate.execute_equation(equation='{vy} = {V2-velocity (m/s)} + 2 * 3.14159265 *  X * {rot}')
tp.data.operate.execute_equation(equation='{vmag} =  sqrt({vx}**2+ {vy}**2+ {V3-velocity (m/s)}**2)')
tp.active_frame().plot().fieldmaps(1).show=False
tp.active_frame().plot().fieldmaps(2).show=False
tp.active_frame().plot().fieldmaps(8).show=False
tp.active_frame().plot().fieldmaps(9).show=False
tp.active_frame().plot().fieldmaps(10).show=False
tp.macro.execute_command('''$!AxialDuplicate 
  ZoneList =  [4-8]
  Angle = 180
  NumDuplicates = 1
  XVar = 1
  YVar = 2
  ZVar = 3''')
tp.macro.execute_command('$!GlobalThreeD RotateOrigin{X = 0}')
tp.macro.execute_command('$!GlobalThreeD RotateOrigin{Z = 0}')
tp.active_frame().plot().contour(0).variable_index=3
tp.active_frame().plot().contour(0).colormap_name='Large Rainbow'
tp.active_frame().plot().contour(0).levels.reset_levels([1.2, 1.205, 1.21, 1.215, 1.22, 1.225, 1.23, 1.235, 1.24, 1.245, 1.25, 1.255, 1.26, 1.265, 1.27, 1.275, 1.28, 1.285, 1.29, 1.295, 1.3])
tp.active_frame().plot().show_contour=True
tp.active_frame().plot().show_shade=False
tp.active_frame().plot().contour(0).legend.vertical=False
tp.active_frame().plot().contour(0).legend.anchor_alignment=AnchorAlignment.BottomCenter
tp.active_frame().plot().contour(0).legend.position=(50,
    tp.active_frame().plot().contour(0).legend.position[1])
tp.active_frame().plot().contour(0).legend.position=(tp.active_frame().plot().contour(0).legend.position[0],
    5)
tp.active_frame().plot().contour(0).labels.step=5
tp.active_frame().plot().view.width=0.28
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Density\\Density_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(0.12117,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Density\\Density_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().contour(0).variable_index=4
tp.active_frame().plot().contour(0).levels.reset_levels([97000, 97450, 97900, 98350, 98800, 99250, 99700, 100150, 100600, 101050, 101500, 101950, 102400, 102850, 103300, 103750, 104200, 104650, 105100, 105550, 106000])
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Pressure\\Pressure_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(0.12117,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Pressure\\Pressure_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().contour(0).variable_index=41
tp.active_frame().plot().contour(0).levels.reset_levels([0, 7.5, 15, 22.5, 30, 37.5, 45, 52.5, 60, 67.5, 75, 82.5, 90, 97.5, 105, 112.5, 120, 127.5, 135, 142.5, 150])
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Velocity\\Velocity_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(0.12117,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Velocity\\Velocity_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().contour(0).variable_index=37
tp.active_frame().plot().contour(0).levels.reset_levels([0, 7.5, 15, 22.5, 30, 37.5, 45, 52.5, 60, 67.5, 75, 82.5, 90, 97.5, 105, 112.5, 120, 127.5, 135, 142.5, 150])
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\ShearStress\\ShearStress_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(0.12117,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\ShearStress\\ShearStress_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().contour(0).variable_index=33
tp.active_frame().plot().contour(0).levels.reset_levels([-4100, -3690, -3280, -2870, -2460, -2050, -1640, -1230, -820, -410, 0, 410, 820, 1230, 1640, 2050, 2460, 2870, 3280, 3690, 4100])
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\PressureTZ\\PressureTZ_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(0.12117,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\PressureTZ\\PressureTZ_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().contour(0).variable_index=30
tp.active_frame().plot().contour(0).levels.reset_levels([-4100, -3690, -3280, -2870, -2460, -2050, -1640, -1230, -820, -410, 0, 410, 820, 1230, 1640, 2050, 2460, 2870, 3280, 3690, 4100])
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\PressureZ\\PressureZ_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(0.12117,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\PressureZ\\PressureZ_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().contour(0).variable_index=36
tp.active_frame().plot().contour(0).levels.reset_levels([-1200, -1080, -960, -840, -720, -600, -480, -360, -240, -120, 0, 120, 240, 360, 480, 600, 720, 840, 960, 1080, 1200])
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\MomentZ\\MomentZ_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(0.12117,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\MomentZ\\MomentZ_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_page().name='Untitled'
tp.add_page()
tp.new_layout()
tp.macro.execute_command("""$!ReadDataSet  '\"C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\soln.plt\" '
  ReadDataOption = New
  ResetStyle = Yes
  VarLoadMode = ByName
  AssignStrandIDs = Yes
  VarNameList = '\"X\" \"Y\" \"Z\" \"Density (kg/m^3)\" \"Pressure (N/m^2)\" \"V1-velocity (m/s); Velocity\" \"V2-velocity (m/s)\" \"V3-velocity (m/s)\" \"Static temperature (K)\" \"nutilde (m^2/s)\" \"wall distance (m)\" \"turbulent viscosity (kg/m s)\" \"y-plus\" \"u-plus\" \"laminar viscosity (kg/m s)\" \"thermal conductivity (W/m/K)\" \"SF1-shear stress (Pa); Shear\" \"SF2-shear stress (Pa)\" \"SF3-shear stress (Pa)\" \"Classical heat flux (W/m^2)\" \"Gresho heat flux (W/m^2)\" \"Velocity Magnitude\" \"X Grid K Unit Normal\" \"Y Grid K Unit Normal\" \"Z Grid K Unit Normal\" \"px\" \"py\" \"pz\" \"mx\" \"my\" \"mz\" \"taux\" \"tauy\" \"tauz\" \"mxt\" \"myt\" \"mzt\" \"ShearStress\" \"rot\" \"vx\" \"vy\" \"vmag\"'""")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SetFieldVariables ConvectionVarsAreMomentum='F' UVarNum=6 VVarNum=7 WVarNum=8 ID1='Density' Variable1=4 ID2='NotUsed' Variable2=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Calculate Function='GRIDKUNITNORMAL' Normalization='None' ValueLocation='Nodal' CalculateOnDemand='T' UseMorePointsForFEGradientCalculations='F'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Calculate Function='VELOCITYMAG' Normalization='None' ValueLocation='Nodal' CalculateOnDemand='T' UseMorePointsForFEGradientCalculations='F'")
tp.data.operate.execute_equation(equation='{px} = -({Pressure (N/m^2)}-101325) * {X Grid K Unit Normal}')
tp.data.operate.execute_equation(equation='{py} = -({Pressure (N/m^2)}-101325)  * {Y Grid K Unit Normal}')
tp.data.operate.execute_equation(equation='{pz} = -({Pressure (N/m^2)}-101325)  * {Z Grid K Unit Normal}')
tp.data.operate.execute_equation(equation='{mx} = Y * {pz} - Z * {py}')
tp.data.operate.execute_equation(equation='{my} = Z * {px} - X * {pz}')
tp.data.operate.execute_equation(equation='{mz} = X * {py} - Y * {px}')
tp.data.operate.execute_equation(equation='{taux} = {SF1-shear stress (Pa); Shear} - {X Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
tp.data.operate.execute_equation(equation='{tauy} = {SF2-shear stress (Pa)} - {Y Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
tp.data.operate.execute_equation(equation='{tauz} = {SF3-shear stress (Pa)} - {Z Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
tp.data.operate.execute_equation(equation='{mxt} = Y * {tauz} - Z * {tauy} ')
tp.data.operate.execute_equation(equation='{myt} = Z * {taux} - X * {tauz}')
tp.data.operate.execute_equation(equation='{mzt} = X * {tauy} - Y * {taux}')
tp.data.operate.execute_equation(equation='{ShearStress} = sqrt({SF1-shear stress (Pa); Shear}**2+ {SF2-shear stress (Pa)}**2+ {SF3-shear stress (Pa)}**2)')
tp.data.operate.execute_equation(equation='{rot} = -3500/60')
tp.data.operate.execute_equation(equation='{vx} = {V1-velocity (m/s); Velocity} - 2 * 3.14159265 *  Y * {rot}')
tp.data.operate.execute_equation(equation='{vy} = {V2-velocity (m/s)} + 2 * 3.14159265 *  X * {rot}')
tp.data.operate.execute_equation(equation='{vmag} =  sqrt({vx}**2+ {vy}**2+ {V3-velocity (m/s)}**2)')
tp.active_frame().plot().fieldmaps(1).show=False
tp.active_frame().plot().fieldmaps(2).show=False
tp.active_frame().plot().fieldmaps(8).show=False
tp.active_frame().plot().fieldmaps(9).show=False
tp.active_frame().plot().fieldmaps(10).show=False
tp.macro.execute_command('''$!AxialDuplicate 
  ZoneList =  [4-8]
  Angle = 180
  NumDuplicates = 1
  XVar = 1
  YVar = 2
  ZVar = 3''')
tp.macro.execute_command('$!GlobalThreeD RotateOrigin{X = 0}')
tp.macro.execute_command('$!GlobalThreeD RotateOrigin{Z = 0}')
tp.active_frame().plot().contour(0).variable_index=3
tp.active_frame().plot().contour(0).colormap_name='Large Rainbow'
tp.active_frame().plot().contour(0).levels.reset_levels([1.2, 1.205, 1.21, 1.215, 1.22, 1.225, 1.23, 1.235, 1.24, 1.245, 1.25, 1.255, 1.26, 1.265, 1.27, 1.275, 1.28, 1.285, 1.29, 1.295, 1.3])
tp.active_frame().plot().show_contour=True
tp.active_frame().plot().show_shade=False
tp.active_frame().plot().contour(0).legend.vertical=False
tp.active_frame().plot().contour(0).legend.anchor_alignment=AnchorAlignment.BottomCenter
tp.active_frame().plot().contour(0).legend.position=(50,
    tp.active_frame().plot().contour(0).legend.position[1])
tp.active_frame().plot().contour(0).legend.position=(tp.active_frame().plot().contour(0).legend.position[0],
    5)
tp.active_frame().plot().contour(0).labels.step=5
tp.active_frame().plot().view.width=0.28
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Density\\Density_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(0.12117,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Density\\Density_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().contour(0).variable_index=4
tp.active_frame().plot().contour(0).levels.reset_levels([97000, 97450, 97900, 98350, 98800, 99250, 99700, 100150, 100600, 101050, 101500, 101950, 102400, 102850, 103300, 103750, 104200, 104650, 105100, 105550, 106000])
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Pressure\\Pressure_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(0.12117,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Pressure\\Pressure_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().contour(0).variable_index=41
tp.active_frame().plot().contour(0).levels.reset_levels([0, 7.5, 15, 22.5, 30, 37.5, 45, 52.5, 60, 67.5, 75, 82.5, 90, 97.5, 105, 112.5, 120, 127.5, 135, 142.5, 150])
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Velocity\\Velocity_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(0.12117,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Velocity\\Velocity_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().contour(0).variable_index=37
tp.active_frame().plot().contour(0).levels.reset_levels([0, 7.5, 15, 22.5, 30, 37.5, 45, 52.5, 60, 67.5, 75, 82.5, 90, 97.5, 105, 112.5, 120, 127.5, 135, 142.5, 150])
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\ShearStress\\ShearStress_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(0.12117,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\ShearStress\\ShearStress_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().contour(0).variable_index=33
tp.active_frame().plot().contour(0).levels.reset_levels([-4100, -3690, -3280, -2870, -2460, -2050, -1640, -1230, -820, -410, 0, 410, 820, 1230, 1640, 2050, 2460, 2870, 3280, 3690, 4100])
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\PressureTZ\\PressureTZ_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(0.12117,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\PressureTZ\\PressureTZ_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().contour(0).variable_index=30
tp.active_frame().plot().contour(0).levels.reset_levels([-4100, -3690, -3280, -2870, -2460, -2050, -1640, -1230, -820, -410, 0, 410, 820, 1230, 1640, 2050, 2460, 2870, 3280, 3690, 4100])
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\PressureZ\\PressureZ_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(0.12117,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\PressureZ\\PressureZ_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().contour(0).variable_index=36
tp.active_frame().plot().contour(0).levels.reset_levels([-1200, -1080, -960, -840, -720, -600, -480, -360, -240, -120, 0, 120, 240, 360, 480, 600, 720, 840, 960, 1080, 1200])
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\MomentZ\\MomentZ_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(0.12117,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\MomentZ\\MomentZ_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_page().name='Untitled'
tp.add_page()
tp.new_layout()
tp.macro.execute_command("""$!ReadDataSet  '\"C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\soln.plt\" '
  ReadDataOption = New
  ResetStyle = Yes
  VarLoadMode = ByName
  AssignStrandIDs = Yes
  VarNameList = '\"X\" \"Y\" \"Z\" \"Density (kg/m^3)\" \"Pressure (N/m^2)\" \"V1-velocity (m/s); Velocity\" \"V2-velocity (m/s)\" \"V3-velocity (m/s)\" \"Static temperature (K)\" \"nutilde (m^2/s)\" \"wall distance (m)\" \"turbulent viscosity (kg/m s)\" \"y-plus\" \"u-plus\" \"laminar viscosity (kg/m s)\" \"thermal conductivity (W/m/K)\" \"SF1-shear stress (Pa); Shear\" \"SF2-shear stress (Pa)\" \"SF3-shear stress (Pa)\" \"Classical heat flux (W/m^2)\" \"Gresho heat flux (W/m^2)\" \"Velocity Magnitude\" \"X Grid K Unit Normal\" \"Y Grid K Unit Normal\" \"Z Grid K Unit Normal\" \"px\" \"py\" \"pz\" \"mx\" \"my\" \"mz\" \"taux\" \"tauy\" \"tauz\" \"mxt\" \"myt\" \"mzt\" \"ShearStress\" \"rot\" \"vx\" \"vy\" \"vmag\"'""")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SetFieldVariables ConvectionVarsAreMomentum='F' UVarNum=6 VVarNum=7 WVarNum=8 ID1='Density' Variable1=4 ID2='NotUsed' Variable2=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Calculate Function='GRIDKUNITNORMAL' Normalization='None' ValueLocation='Nodal' CalculateOnDemand='T' UseMorePointsForFEGradientCalculations='F'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Calculate Function='VELOCITYMAG' Normalization='None' ValueLocation='Nodal' CalculateOnDemand='T' UseMorePointsForFEGradientCalculations='F'")
tp.data.operate.execute_equation(equation='{px} = -({Pressure (N/m^2)}-101325) * {X Grid K Unit Normal}')
tp.data.operate.execute_equation(equation='{py} = -({Pressure (N/m^2)}-101325)  * {Y Grid K Unit Normal}')
tp.data.operate.execute_equation(equation='{pz} = -({Pressure (N/m^2)}-101325)  * {Z Grid K Unit Normal}')
tp.data.operate.execute_equation(equation='{mx} = Y * {pz} - Z * {py}')
tp.data.operate.execute_equation(equation='{my} = Z * {px} - X * {pz}')
tp.data.operate.execute_equation(equation='{mz} = X * {py} - Y * {px}')
tp.data.operate.execute_equation(equation='{taux} = {SF1-shear stress (Pa); Shear} - {X Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
tp.data.operate.execute_equation(equation='{tauy} = {SF2-shear stress (Pa)} - {Y Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
tp.data.operate.execute_equation(equation='{tauz} = {SF3-shear stress (Pa)} - {Z Grid K Unit Normal} * ({Pressure (N/m^2)}-101325)')
tp.data.operate.execute_equation(equation='{mxt} = Y * {tauz} - Z * {tauy} ')
tp.data.operate.execute_equation(equation='{myt} = Z * {taux} - X * {tauz}')
tp.data.operate.execute_equation(equation='{mzt} = X * {tauy} - Y * {taux}')
tp.data.operate.execute_equation(equation='{ShearStress} = sqrt({SF1-shear stress (Pa); Shear}**2+ {SF2-shear stress (Pa)}**2+ {SF3-shear stress (Pa)}**2)')
tp.data.operate.execute_equation(equation='{rot} = -3500/60')
tp.data.operate.execute_equation(equation='{vx} = {V1-velocity (m/s); Velocity} - 2 * 3.14159265 *  Y * {rot}')
tp.data.operate.execute_equation(equation='{vy} = {V2-velocity (m/s)} + 2 * 3.14159265 *  X * {rot}')
tp.data.operate.execute_equation(equation='{vmag} =  sqrt({vx}**2+ {vy}**2+ {V3-velocity (m/s)}**2)')
tp.active_frame().plot().fieldmaps(1).show=False
tp.active_frame().plot().fieldmaps(2).show=False
tp.active_frame().plot().fieldmaps(8).show=False
tp.active_frame().plot().fieldmaps(9).show=False
tp.active_frame().plot().fieldmaps(10).show=False
tp.macro.execute_command('''$!AxialDuplicate 
  ZoneList =  [4-8]
  Angle = 180
  NumDuplicates = 1
  XVar = 1
  YVar = 2
  ZVar = 3''')
tp.macro.execute_command('$!GlobalThreeD RotateOrigin{X = 0}')
tp.macro.execute_command('$!GlobalThreeD RotateOrigin{Z = 0}')
tp.active_frame().plot().contour(0).variable_index=3
tp.active_frame().plot().contour(0).colormap_name='Large Rainbow'
tp.active_frame().plot().contour(0).levels.reset_levels([1.2, 1.205, 1.21, 1.215, 1.22, 1.225, 1.23, 1.235, 1.24, 1.245, 1.25, 1.255, 1.26, 1.265, 1.27, 1.275, 1.28, 1.285, 1.29, 1.295, 1.3])
tp.active_frame().plot().show_contour=True
tp.active_frame().plot().show_shade=False
tp.active_frame().plot().contour(0).legend.vertical=False
tp.active_frame().plot().contour(0).legend.anchor_alignment=AnchorAlignment.BottomCenter
tp.active_frame().plot().contour(0).legend.position=(50,
    tp.active_frame().plot().contour(0).legend.position[1])
tp.active_frame().plot().contour(0).legend.position=(tp.active_frame().plot().contour(0).legend.position[0],
    5)
tp.active_frame().plot().contour(0).labels.step=5
tp.active_frame().plot().view.width=0.28
tp.active_frame().plot().view.position=(-0.13837,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    10)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Density\\Density_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Density\\Density_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().contour(0).variable_index=4
tp.active_frame().plot().contour(0).levels.reset_levels([97000, 97450, 97900, 98350, 98800, 99250, 99700, 100150, 100600, 101050, 101500, 101950, 102400, 102850, 103300, 103750, 104200, 104650, 105100, 105550, 106000])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    10)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Pressure\\Pressure_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Pressure\\Pressure_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().contour(0).variable_index=41
tp.active_frame().plot().contour(0).levels.reset_levels([0, 7.5, 15, 22.5, 30, 37.5, 45, 52.5, 60, 67.5, 75, 82.5, 90, 97.5, 105, 112.5, 120, 127.5, 135, 142.5, 150])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    10)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Velocity\\Velocity_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Velocity\\Velocity_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().contour(0).variable_index=37
tp.active_frame().plot().contour(0).levels.reset_levels([0, 7.5, 15, 22.5, 30, 37.5, 45, 52.5, 60, 67.5, 75, 82.5, 90, 97.5, 105, 112.5, 120, 127.5, 135, 142.5, 150])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    10)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\ShearStress\\ShearStress_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\ShearStress\\ShearStress_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().contour(0).variable_index=33
tp.active_frame().plot().contour(0).levels.reset_levels([-4100, -3690, -3280, -2870, -2460, -2050, -1640, -1230, -820, -410, 0, 410, 820, 1230, 1640, 2050, 2460, 2870, 3280, 3690, 4100])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    10)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\PressureTZ\\PressureTZ_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\PressureTZ\\PressureTZ_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().contour(0).variable_index=30
tp.active_frame().plot().contour(0).levels.reset_levels([-4100, -3690, -3280, -2870, -2460, -2050, -1640, -1230, -820, -410, 0, 410, 820, 1230, 1640, 2050, 2460, 2870, 3280, 3690, 4100])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    10)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\PressureZ\\PressureZ_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\PressureZ\\PressureZ_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().contour(0).variable_index=36
tp.active_frame().plot().contour(0).levels.reset_levels([-1200, -1080, -960, -840, -720, -600, -480, -360, -240, -120, 0, 120, 240, 360, 480, 600, 720, 840, 960, 1080, 1200])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.0118782,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    10)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\MomentZ\\MomentZ_Bottom.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.00469803,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -27.2985)
tp.active_frame().plot().view.psi=180
tp.active_frame().plot().view.theta=-180
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\MomentZ\\MomentZ_Top.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 7.80152671756
  Y = -1.1465648855
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 5.92595419847
  Y = 1.38854961832
  ConsiderStyle = Yes''')
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=37 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:\\\\Users\\\\nicolacm\\\\Desktop\\\\Out.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=34 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:\\\\Users\\\\nicolacm\\\\Desktop\\\\Out.txt'")
# End Macro.

