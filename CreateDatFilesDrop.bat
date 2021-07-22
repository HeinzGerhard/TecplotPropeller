
cd %1

SET c="%1/%2"
SET d="%1/%3"

#"C:\Program Files\ANSYS Inc\v211\fensapice\bin\nti2tecplot.exe" SOLN "03_2113_IA/01_FirstTest.grid" "04_Results/run_01_FirstTest/soln.fensap.000001"
#"C:\Program Files\ANSYS Inc\v211\fensapice\bin\nti2tecplot.exe" DROPLET  %c% %d%
"C:\Program Files\ANSYS Inc\v211\fensapice\bin\nti2tecplot.exe" DROPLET  %2 %3