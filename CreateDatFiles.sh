#!/bin/sh 

cd "C:\\Users\\nicolacm\\OneDrive - NTNU\\Simulations\\03_2113IA"
cd $1

ls

#"C:\Program Files\ANSYS Inc\v211\fensapice\bin\nti2tecplot.exe" SOLN "03_2113_IA/01_FirstTest.grid" "04_Results/run_01_FirstTest/soln.fensap.000001"
"C:\Program Files\ANSYS Inc\v211\fensapice\bin\nti2tecplot.exe" SOLN $2 $3