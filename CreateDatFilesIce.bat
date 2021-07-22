
cd %1

SET c="%1/%2"
SET d="%1/%3"

#"C:\Program Files\ANSYS Inc\v211\fensapice\bin\nti2tecplot.exe" SWIMSOL %2 %3
"C:\Program Files\ANSYS Inc\v211\fensapice\bin\nti2tecplot.exe" SWIMSOL %c% %d%