
cd %1

dir
echo %1
echo %2
echo %3
SET c="%1/%2"
SET d="%1/%3"

#"C:\Program Files\ANSYS Inc\v211\fensapice\bin\nti2tecplot.exe" SOLN %1"/"%2 %1"/"%3
#"C:\Program Files\ANSYS Inc\v211\fensapice\bin\nti2tecplot.exe" SOLN %c% %d%
"C:\Program Files\ANSYS Inc\v211\fensapice\bin\nti2tecplot.exe" SOLN %2 %3