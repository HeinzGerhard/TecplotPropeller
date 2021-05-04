import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *

# Uncomment the following line to connect to a running instance of Tecplot 360:
# tp.session.connect()

tp.active_frame().plot_type=PlotType.Cartesian3D
tp.active_frame().plot_type=PlotType.Cartesian2D
tp.active_frame().plot_type=PlotType.Cartesian3D
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
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=34 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\TZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=31 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\PZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=37 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\MZ.txt'")
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
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
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
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=34 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\TZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=31 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\PZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=37 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\MZ.txt'")
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
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.08001
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(16).name = '30'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='30'
tp.active_frame().plot().linemaps(0).zone_index=16
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '30'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().axes.y_axis(0).reverse=True
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\30.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.10668
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(17).name = '40'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='40'
tp.active_frame().plot().linemaps(0).zone_index=17
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '40'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\40.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.13335
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(18).name = '50'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='50'
tp.active_frame().plot().linemaps(0).zone_index=18
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '50'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\50.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.16002
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(19).name = '60'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='60'
tp.active_frame().plot().linemaps(0).zone_index=19
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '60'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\60.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.18669
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(20).name = '70'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='70'
tp.active_frame().plot().linemaps(0).zone_index=20
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '70'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\70.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.21336
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(21).name = '80'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='80'
tp.active_frame().plot().linemaps(0).zone_index=21
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '80'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\80.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.24003
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(22).name = '90'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='90'
tp.active_frame().plot().linemaps(0).zone_index=22
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '90'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\90.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.253365
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(23).name = '95'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='95'
tp.active_frame().plot().linemaps(0).zone_index=23
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '95'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\95.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.261366
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(24).name = '98'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='98'
tp.active_frame().plot().linemaps(0).zone_index=24
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '98'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\98.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
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
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=34 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\TZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=31 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\PZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=37 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\MZ.txt'")
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
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.08001
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(16).name = '30'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='30'
tp.active_frame().plot().linemaps(0).zone_index=16
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '30'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().axes.y_axis(0).reverse=True
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\30.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.10668
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(17).name = '40'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='40'
tp.active_frame().plot().linemaps(0).zone_index=17
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '40'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\40.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.13335
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(18).name = '50'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='50'
tp.active_frame().plot().linemaps(0).zone_index=18
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '50'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\50.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.16002
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(19).name = '60'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='60'
tp.active_frame().plot().linemaps(0).zone_index=19
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '60'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\60.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.18669
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(20).name = '70'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='70'
tp.active_frame().plot().linemaps(0).zone_index=20
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '70'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\70.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.21336
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(21).name = '80'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='80'
tp.active_frame().plot().linemaps(0).zone_index=21
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '80'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\80.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.24003
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(22).name = '90'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='90'
tp.active_frame().plot().linemaps(0).zone_index=22
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '90'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\90.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.253365
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(23).name = '95'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='95'
tp.active_frame().plot().linemaps(0).zone_index=23
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '95'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\95.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.261366
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(24).name = '98'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='98'
tp.active_frame().plot().linemaps(0).zone_index=24
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '98'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\98.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
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
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=34 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\TZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=31 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\PZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=37 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\MZ.txt'")
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
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.08001
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(16).name = '30'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='30'
tp.active_frame().plot().linemaps(0).zone_index=16
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '30'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().axes.y_axis(0).reverse=True
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\30.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.10668
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(17).name = '40'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='40'
tp.active_frame().plot().linemaps(0).zone_index=17
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '40'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\40.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.13335
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(18).name = '50'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='50'
tp.active_frame().plot().linemaps(0).zone_index=18
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '50'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\50.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.16002
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(19).name = '60'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='60'
tp.active_frame().plot().linemaps(0).zone_index=19
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '60'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\60.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.18669
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(20).name = '70'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='70'
tp.active_frame().plot().linemaps(0).zone_index=20
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '70'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\70.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.21336
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(21).name = '80'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='80'
tp.active_frame().plot().linemaps(0).zone_index=21
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '80'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\80.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.24003
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(22).name = '90'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='90'
tp.active_frame().plot().linemaps(0).zone_index=22
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '90'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\90.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.253365
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(23).name = '95'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='95'
tp.active_frame().plot().linemaps(0).zone_index=23
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '95'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\95.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.261366
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(24).name = '98'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='98'
tp.active_frame().plot().linemaps(0).zone_index=24
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '98'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\98.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
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
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=34 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\TZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=31 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\PZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=37 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\MZ.txt'")
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
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.08001
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(16).name = '30'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='30'
tp.active_frame().plot().linemaps(0).zone_index=16
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '30'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().axes.y_axis(0).reverse=True
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\30.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.093345
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(17).name = '35'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='35'
tp.active_frame().plot().linemaps(0).zone_index=17
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '35'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\35.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.10668
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(18).name = '40'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='40'
tp.active_frame().plot().linemaps(0).zone_index=18
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '40'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\40.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.120015
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(19).name = '45'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='45'
tp.active_frame().plot().linemaps(0).zone_index=19
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '45'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\45.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.13335
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(20).name = '50'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='50'
tp.active_frame().plot().linemaps(0).zone_index=20
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '50'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\50.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.146685
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(21).name = '55'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='55'
tp.active_frame().plot().linemaps(0).zone_index=21
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '55'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\55.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.16002
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(22).name = '60'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='60'
tp.active_frame().plot().linemaps(0).zone_index=22
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '60'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\60.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.173355
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(23).name = '65'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='65'
tp.active_frame().plot().linemaps(0).zone_index=23
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '65'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\65.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.18669
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(24).name = '70'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='70'
tp.active_frame().plot().linemaps(0).zone_index=24
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '70'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\70.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.200025
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(25).name = '75'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='75'
tp.active_frame().plot().linemaps(0).zone_index=25
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '75'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\75.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.21336
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(26).name = '80'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='80'
tp.active_frame().plot().linemaps(0).zone_index=26
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '80'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\80.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.226695
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(27).name = '85'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='85'
tp.active_frame().plot().linemaps(0).zone_index=27
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '85'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\85.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.24003
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(28).name = '90'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='90'
tp.active_frame().plot().linemaps(0).zone_index=28
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '90'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\90.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.253365
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(29).name = '95'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='95'
tp.active_frame().plot().linemaps(0).zone_index=29
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '95'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\95.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.261366
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(30).name = '98'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='98'
tp.active_frame().plot().linemaps(0).zone_index=30
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '98'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\98.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
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
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=34 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\TZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=31 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\PZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=37 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\MZ.txt'")
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
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.08001
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(16).name = '30'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='30'
tp.active_frame().plot().linemaps(0).zone_index=16
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '30'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().axes.y_axis(0).reverse=True
tp.active_frame().plot().view.fit()
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
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=34 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\TZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=31 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\PZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=37 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\MZ.txt'")
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
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.066675
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(16).name = '25'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='25'
tp.active_frame().plot().linemaps(0).zone_index=16
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '25'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().axes.y_axis(0).reverse=True
tp.active_frame().plot().view.fit()
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
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=34 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\TZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=31 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\PZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=37 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\MZ.txt'")
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
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.066675
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(16).name = '25'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='25'
tp.active_frame().plot().linemaps(0).zone_index=16
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '25'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().axes.y_axis(0).reverse=True
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 1.33052792655
  Y = 4.10883703137
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 1.55776587605
  Y = 4.08817903596
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 1.41315990819
  Y = 3.46843917368
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 1.41315990819
  Y = 3.44778117827
  CollectingObjectsMode = HomogeneousAdd
  ConsiderStyle = Yes''')
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().axes.y_axis(0).title.font.size=2.6
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().axes.y_axis(0).title.font.size=3.6
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 5.56541698546
  Y = 0.596977811783
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 5.56541698546
  Y = 0.596977811783
  CollectingObjectsMode = HomogeneousAdd
  ConsiderStyle = Yes''')
tp.macro.execute_command('$!Pick Clear')
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  TextShape
    {
    Height = 30
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '25'""")
tp.macro.execute_command('''$!Pick SetMouseMode
  MouseMode = Select''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 1.92960979342
  Y = 3.5097551645
  CollectingObjectsMode = HomogeneousAdd
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!Pick SetMouseMode
  MouseMode = Select''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 2.09487375669
  Y = 3.86094108646
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 2.09487375669
  Y = 3.86094108646
  CollectingObjectsMode = HomogeneousAdd
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!Pick SetMouseMode
  MouseMode = Select''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 2.57000765111
  Y = 3.81962509564
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 2.28079571538
  Y = 2.06369548585
  ConsiderStyle = Yes''')
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().axes.y_axis(0).title.offset=12
tp.active_frame().plot().axes.y_axis(0).title.title_mode=AxisTitleMode.UseText
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 3.27237949503
  Y = 2.37356541699
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 3.08645753634
  Y = 2.51817138485
  CollectingObjectsMode = HomogeneousAdd
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!Pick SetMouseMode
  MouseMode = Select''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 3.2104055088
  Y = 3.17922723795
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 3.2104055088
  Y = 3.17922723795
  CollectingObjectsMode = HomogeneousAdd
  ConsiderStyle = Yes''')
tp.active_frame().plot().axes.viewport.left=15
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
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=34 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\TZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=31 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\PZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=37 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\MZ.txt'")
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
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.066675
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(16).name = '25'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='25'
tp.active_frame().plot().linemaps(0).zone_index=16
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '25'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().axes.y_axis(0).reverse=True
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().axes.y_axis(0).title.font.size=2.6
tp.active_frame().plot().axes.y_axis(0).title.text='Pressure [Pa]]'
tp.active_frame().plot().axes.y_axis(0).title.offset=11
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 2.09487375669
  Y = 4.81120887529
  ConsiderStyle = Yes''')
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
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=34 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\TZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=31 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\PZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=37 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\MZ.txt'")
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
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.066675
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(16).name = '25'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='25'
tp.active_frame().plot().linemaps(0).zone_index=16
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '25'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().axes.y_axis(0).reverse=True
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().axes.y_axis(0).title.font.size=2.6
tp.active_frame().plot().axes.y_axis(0).title.text='Pressure [Pa]]'
tp.active_frame().plot().axes.y_axis(0).title.offset=11
tp.active_frame().plot().axes.x_axis(0).title.text='Chord [-]'
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\25.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.08001
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(17).name = '30'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='30'
tp.active_frame().plot().linemaps(0).zone_index=17
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '30'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\30.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.093345
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(18).name = '35'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='35'
tp.active_frame().plot().linemaps(0).zone_index=18
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '35'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\35.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.10668
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(19).name = '40'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='40'
tp.active_frame().plot().linemaps(0).zone_index=19
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '40'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\40.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.120015
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(20).name = '45'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='45'
tp.active_frame().plot().linemaps(0).zone_index=20
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '45'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\45.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.13335
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(21).name = '50'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='50'
tp.active_frame().plot().linemaps(0).zone_index=21
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '50'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\50.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.146685
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(22).name = '55'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='55'
tp.active_frame().plot().linemaps(0).zone_index=22
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '55'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\55.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.16002
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(23).name = '60'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='60'
tp.active_frame().plot().linemaps(0).zone_index=23
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '60'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\60.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.173355
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(24).name = '65'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='65'
tp.active_frame().plot().linemaps(0).zone_index=24
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '65'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\65.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.18669
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(25).name = '70'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='70'
tp.active_frame().plot().linemaps(0).zone_index=25
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '70'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\70.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.200025
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(26).name = '75'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='75'
tp.active_frame().plot().linemaps(0).zone_index=26
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '75'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\75.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.21336
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(27).name = '80'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='80'
tp.active_frame().plot().linemaps(0).zone_index=27
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '80'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\80.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.226695
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(28).name = '85'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='85'
tp.active_frame().plot().linemaps(0).zone_index=28
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '85'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\85.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.24003
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(29).name = '90'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='90'
tp.active_frame().plot().linemaps(0).zone_index=29
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '90'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\90.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.253365
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(30).name = '95'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='95'
tp.active_frame().plot().linemaps(0).zone_index=30
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '95'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\95.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.261366
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(31).name = '98'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='98'
tp.active_frame().plot().linemaps(0).zone_index=31
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '98'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\98.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
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
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=34 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\TZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=31 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\PZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=37 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\MZ.txt'")
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
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.066675
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(16).name = '25'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='25'
tp.active_frame().plot().linemaps(0).zone_index=16
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '25'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().axes.y_axis(0).reverse=True
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().axes.y_axis(0).title.font.size=2.6
tp.active_frame().plot().axes.y_axis(0).title.text='Pressure [Pa]]'
tp.active_frame().plot().axes.y_axis(0).title.offset=11
tp.active_frame().plot().axes.x_axis(0).title.text='Chord [-]'
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\25.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.08001
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(17).name = '30'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='30'
tp.active_frame().plot().linemaps(0).zone_index=17
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '30'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\30.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.093345
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(18).name = '35'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='35'
tp.active_frame().plot().linemaps(0).zone_index=18
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '35'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\35.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.10668
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(19).name = '40'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='40'
tp.active_frame().plot().linemaps(0).zone_index=19
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '40'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\40.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.120015
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(20).name = '45'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='45'
tp.active_frame().plot().linemaps(0).zone_index=20
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '45'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\45.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.13335
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(21).name = '50'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='50'
tp.active_frame().plot().linemaps(0).zone_index=21
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '50'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\50.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.146685
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(22).name = '55'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='55'
tp.active_frame().plot().linemaps(0).zone_index=22
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '55'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\55.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.16002
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(23).name = '60'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='60'
tp.active_frame().plot().linemaps(0).zone_index=23
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '60'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\60.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.173355
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(24).name = '65'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='65'
tp.active_frame().plot().linemaps(0).zone_index=24
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '65'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\65.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.18669
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(25).name = '70'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='70'
tp.active_frame().plot().linemaps(0).zone_index=25
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '70'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\70.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.200025
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(26).name = '75'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='75'
tp.active_frame().plot().linemaps(0).zone_index=26
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '75'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\75.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.21336
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(27).name = '80'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='80'
tp.active_frame().plot().linemaps(0).zone_index=27
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '80'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\80.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.226695
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(28).name = '85'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='85'
tp.active_frame().plot().linemaps(0).zone_index=28
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '85'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\85.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.24003
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(29).name = '90'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='90'
tp.active_frame().plot().linemaps(0).zone_index=29
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '90'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\90.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.253365
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(30).name = '95'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='95'
tp.active_frame().plot().linemaps(0).zone_index=30
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '95'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\95.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.261366
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(31).name = '98'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='98'
tp.active_frame().plot().linemaps(0).zone_index=31
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '98'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\98.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
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
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=34 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\TZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=31 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\PZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=37 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\MZ.txt'")
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
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.066675
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(16).name = '25'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='25'
tp.active_frame().plot().linemaps(0).zone_index=16
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '25'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().axes.y_axis(0).reverse=True
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().axes.y_axis(0).title.font.size=2.6
tp.active_frame().plot().axes.y_axis(0).title.text='Pressure [Pa]]'
tp.active_frame().plot().axes.y_axis(0).title.offset=11
tp.active_frame().plot().axes.x_axis(0).title.text='Chord [-]'
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\25.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.08001
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(17).name = '30'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='30'
tp.active_frame().plot().linemaps(0).zone_index=17
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '30'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\30.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.093345
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(18).name = '35'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='35'
tp.active_frame().plot().linemaps(0).zone_index=18
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '35'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\35.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.10668
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(19).name = '40'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='40'
tp.active_frame().plot().linemaps(0).zone_index=19
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '40'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\40.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.120015
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(20).name = '45'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='45'
tp.active_frame().plot().linemaps(0).zone_index=20
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '45'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\45.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.13335
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(21).name = '50'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='50'
tp.active_frame().plot().linemaps(0).zone_index=21
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '50'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\50.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.146685
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(22).name = '55'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='55'
tp.active_frame().plot().linemaps(0).zone_index=22
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '55'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\55.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.16002
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(23).name = '60'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='60'
tp.active_frame().plot().linemaps(0).zone_index=23
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '60'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\60.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.173355
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(24).name = '65'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='65'
tp.active_frame().plot().linemaps(0).zone_index=24
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '65'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\65.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.18669
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(25).name = '70'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='70'
tp.active_frame().plot().linemaps(0).zone_index=25
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '70'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\70.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.200025
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(26).name = '75'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='75'
tp.active_frame().plot().linemaps(0).zone_index=26
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '75'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\75.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.21336
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(27).name = '80'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='80'
tp.active_frame().plot().linemaps(0).zone_index=27
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '80'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\80.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.226695
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(28).name = '85'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='85'
tp.active_frame().plot().linemaps(0).zone_index=28
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '85'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\85.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.24003
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(29).name = '90'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='90'
tp.active_frame().plot().linemaps(0).zone_index=29
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '90'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\90.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.253365
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(30).name = '95'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='95'
tp.active_frame().plot().linemaps(0).zone_index=30
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '95'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\95.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.261366
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(31).name = '98'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='98'
tp.active_frame().plot().linemaps(0).zone_index=31
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '98'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\98.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 9.90359602142
  Y = 1.2993496557
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!FrameControl ActivateByNumber
  Frame = 1''')
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
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=34 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\TZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=31 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\PZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=37 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\MZ.txt'")
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
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.066675
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(16).name = '25'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='25'
tp.active_frame().plot().linemaps(0).zone_index=16
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '25'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().axes.y_axis(0).reverse=True
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().axes.y_axis(0).title.font.size=2.6
tp.active_frame().plot().axes.y_axis(0).title.text='Pressure [Pa]]'
tp.active_frame().plot().axes.y_axis(0).title.offset=11
tp.active_frame().plot().axes.x_axis(0).title.text='Chord [-]'
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\25.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.08001
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(17).name = '30'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='30'
tp.active_frame().plot().linemaps(0).zone_index=17
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '30'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\30.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.093345
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(18).name = '35'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='35'
tp.active_frame().plot().linemaps(0).zone_index=18
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '35'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\35.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.10668
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(19).name = '40'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='40'
tp.active_frame().plot().linemaps(0).zone_index=19
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '40'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\40.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.120015
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(20).name = '45'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='45'
tp.active_frame().plot().linemaps(0).zone_index=20
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '45'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\45.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.13335
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(21).name = '50'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='50'
tp.active_frame().plot().linemaps(0).zone_index=21
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '50'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\50.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.146685
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(22).name = '55'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='55'
tp.active_frame().plot().linemaps(0).zone_index=22
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '55'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\55.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.16002
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(23).name = '60'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='60'
tp.active_frame().plot().linemaps(0).zone_index=23
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '60'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\60.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.173355
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(24).name = '65'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='65'
tp.active_frame().plot().linemaps(0).zone_index=24
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '65'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\65.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.18669
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(25).name = '70'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='70'
tp.active_frame().plot().linemaps(0).zone_index=25
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '70'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\70.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.200025
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(26).name = '75'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='75'
tp.active_frame().plot().linemaps(0).zone_index=26
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '75'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\75.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.21336
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(27).name = '80'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='80'
tp.active_frame().plot().linemaps(0).zone_index=27
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '80'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
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
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=34 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\TZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=31 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\PZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=37 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\MZ.txt'")
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
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.066675
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(16).name = '25'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='25'
tp.active_frame().plot().linemaps(0).zone_index=16
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '25'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().axes.y_axis(0).reverse=True
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().axes.y_axis(0).title.font.size=2.6
tp.active_frame().plot().axes.y_axis(0).title.text='Pressure [Pa]]'
tp.active_frame().plot().axes.y_axis(0).title.offset=11
tp.active_frame().plot().axes.x_axis(0).title.text='Chord [-]'
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\25.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.08001
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(17).name = '30'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='30'
tp.active_frame().plot().linemaps(0).zone_index=17
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '30'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\30.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.093345
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(18).name = '35'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='35'
tp.active_frame().plot().linemaps(0).zone_index=18
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '35'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\35.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.10668
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(19).name = '40'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='40'
tp.active_frame().plot().linemaps(0).zone_index=19
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '40'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\40.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.120015
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(20).name = '45'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='45'
tp.active_frame().plot().linemaps(0).zone_index=20
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '45'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\45.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.13335
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(21).name = '50'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='50'
tp.active_frame().plot().linemaps(0).zone_index=21
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '50'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\50.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.146685
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(22).name = '55'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='55'
tp.active_frame().plot().linemaps(0).zone_index=22
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '55'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\55.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.16002
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(23).name = '60'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='60'
tp.active_frame().plot().linemaps(0).zone_index=23
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '60'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\60.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.173355
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(24).name = '65'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='65'
tp.active_frame().plot().linemaps(0).zone_index=24
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '65'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\65.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.18669
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(25).name = '70'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='70'
tp.active_frame().plot().linemaps(0).zone_index=25
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '70'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\70.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.200025
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(26).name = '75'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='75'
tp.active_frame().plot().linemaps(0).zone_index=26
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '75'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\75.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.21336
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(27).name = '80'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='80'
tp.active_frame().plot().linemaps(0).zone_index=27
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '80'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\80.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.226695
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(28).name = '85'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='85'
tp.active_frame().plot().linemaps(0).zone_index=28
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '85'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\85.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.24003
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(29).name = '90'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='90'
tp.active_frame().plot().linemaps(0).zone_index=29
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '90'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\90.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.253365
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(30).name = '95'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='95'
tp.active_frame().plot().linemaps(0).zone_index=30
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '95'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\95.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.261366
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(31).name = '98'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='98'
tp.active_frame().plot().linemaps(0).zone_index=31
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '98'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\SLices\\98.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
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
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=34 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\TZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=31 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\PZ.txt'")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="Integrate [4-8] VariableOption='Scalar' XOrigin=0 YOrigin=0 ZOrigin=0 ScalarVar=37 Absolute='F' ExcludeBlanked='F' XVariable=1 YVariable=2 ZVariable=3 IntegrateOver='Cells' IntegrateBy='Zones' IRange={MIN =1 MAX = 0 SKIP = 1} JRange={MIN =1 MAX = 0 SKIP = 1} KRange={MIN =1 MAX = 0 SKIP = 1} PlotResults='F' PlotAs='Result' TimeMin=0 TimeMax=0")
tp.macro.execute_extended_command(command_processor_id='CFDAnalyzer4',
    command="SaveIntegrationResults FileName='C:/Users/nicolacm/OneDrive - NTNU/Simulations/Downloads/run_29_NoTransition\\\\PostPro\\\\Plots\\\\MZ.txt'")
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
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.066675
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(16).name = '25'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='25'
tp.active_frame().plot().linemaps(0).zone_index=16
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '25'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().axes.y_axis(0).reverse=True
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().axes.y_axis(0).title.font.size=2.6
tp.active_frame().plot().axes.y_axis(0).title.text='Pressure [Pa]]'
tp.active_frame().plot().axes.y_axis(0).title.offset=11
tp.active_frame().plot().axes.x_axis(0).title.text='Chord [-]'
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Slices\\25.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.08001
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(17).name = '30'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='30'
tp.active_frame().plot().linemaps(0).zone_index=17
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '30'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Slices\\30.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.093345
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(18).name = '35'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='35'
tp.active_frame().plot().linemaps(0).zone_index=18
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '35'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Slices\\35.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.10668
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(19).name = '40'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='40'
tp.active_frame().plot().linemaps(0).zone_index=19
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '40'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Slices\\40.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.120015
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(20).name = '45'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='45'
tp.active_frame().plot().linemaps(0).zone_index=20
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '45'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Slices\\45.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.13335
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(21).name = '50'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='50'
tp.active_frame().plot().linemaps(0).zone_index=21
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '50'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Slices\\50.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.146685
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(22).name = '55'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='55'
tp.active_frame().plot().linemaps(0).zone_index=22
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '55'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Slices\\55.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.16002
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(23).name = '60'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='60'
tp.active_frame().plot().linemaps(0).zone_index=23
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '60'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Slices\\60.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.173355
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(24).name = '65'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='65'
tp.active_frame().plot().linemaps(0).zone_index=24
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '65'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Slices\\65.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.18669
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(25).name = '70'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='70'
tp.active_frame().plot().linemaps(0).zone_index=25
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '70'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Slices\\70.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.200025
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(26).name = '75'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='75'
tp.active_frame().plot().linemaps(0).zone_index=26
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '75'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Slices\\75.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.21336
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(27).name = '80'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='80'
tp.active_frame().plot().linemaps(0).zone_index=27
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '80'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Slices\\80.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.226695
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(28).name = '85'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='85'
tp.active_frame().plot().linemaps(0).zone_index=28
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '85'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Slices\\85.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.24003
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(29).name = '90'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='90'
tp.active_frame().plot().linemaps(0).zone_index=29
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '90'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Slices\\90.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.253365
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(30).name = '95'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='95'
tp.active_frame().plot().linemaps(0).zone_index=30
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '95'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Slices\\95.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('''$!ExtractSliceToZones 
  SliceSource = SurfaceZones
  SurfaceGenerationMethod = AllowQuads
  CopyCellCenteredValues = No
  Resulting1DZoneType = FELineSegment
  TransientOperationMode = SingleSolutionTime
  Origin
    {
    X = 0.261366
    Y = 0
    Z = 0
    }
  Normal
    {
    X = 1
    Y = 0
    Z = 0
    }''')
tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().dataset.zone(31).name = '98'
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='98'
tp.active_frame().plot().linemaps(0).zone_index=31
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().linemaps(0).x_variable_index=1
tp.active_frame().plot().linemaps(0).y_variable_index=4
tp.macro.execute_command("""$!AttachText 
  AnchorPos
    {
    X = 50
    Y = 95
    }
  Box
    {
    Margin = 0.2
    LineThickness = 0.001
    }
  Text = '98'""")
tp.active_frame().plot().linemaps(0).line.color=Color.Blue
tp.active_frame().plot().linemaps(0).line.line_thickness=0.2
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=10500
tp.active_frame().plot().view.fit()
tp.active_frame().plot().axes.y_axis(0).min=95000
tp.active_frame().plot().axes.y_axis(0).max=105000
tp.export.save_png('C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\Downloads\\run_29_NoTransition\\PostPro\\Slices\\98.png',
    width=1920,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
