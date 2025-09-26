#!/bin/sh
dir="${PWD##*/}"

rm $dir.py
rm *.py *.ascii *.log *.h5 *.xml

echo "import openmc" > $dir.py


# Main input file
# -------------------------------------------------------
# --- Include files
# -------------------------------------------------------
# 
# - Surfaces
cat ../../link_SyncWithSerpent/CEFR-01-surf-250C.omc         >> $dir.py # All surface specs
# - Materials
cat ../../link_SyncWithSerpent/CEFR-02-mat-1-all-250C.omc    >> $dir.py # Fuel and Nnon-fuel material specs
# - Pins
cat ../../link_SyncWithSerpent/CEFR-03-pin-1-FU.omc          >> $dir.py # Definition of fuel pins
cat ../../link_SyncWithSerpent/CEFR-03-pin-2-CR.omc          >> $dir.py # Definition of CR pins
cat ../../link_SyncWithSerpent/CEFR-03-pin-3-RR.omc          >> $dir.py # Definition of radial reflector and boron shield pins
cat ../../link_SyncWithSerpent/CEFR-03-pin-4-VO.omc          >> $dir.py # Definition of sodium void fuel pins
# # - Assembly level lattices
cat ../../link_SyncWithSerpent/CEFR-04-lat-1-FU.omc          >> $dir.py # Definition of fuel lattices
cat ../../link_SyncWithSerpent/CEFR-04-lat-2-CR.omc          >> $dir.py # Definition of CR lattices
cat ../../link_SyncWithSerpent/CEFR-04-lat-3-RR.omc          >> $dir.py # Definition of radial reflector lattices
cat ../../link_SyncWithSerpent/CEFR-04-lat-4-RB.omc          >> $dir.py # Definition of radial shield lattices
cat ../../link_SyncWithSerpent/CEFR-04-lat-5-NS.omc          >> $dir.py # Definition of neutron source lattices
cat ../../link_SyncWithSerpent/CEFR-04-lat-6-VO.omc          >> $dir.py # Definition of sodium void fuel lattices 
# # - Separate assemblies                        
cat ../../link_SyncWithSerpent/CEFR-05-asy-1-FU.omc          >> $dir.py # Definition of fuel assemblies
#cat ../../link_SyncWithSerpent/CEFR-05-asy-2-CR.omc          >> $dir.py # Definition of CR with enriched B4C
cat ../../link_SyncWithSerpent/CEFR-05-asy-3-RR.omc          >> $dir.py # Definition of radial reflector assemblies
cat ../../link_SyncWithSerpent/CEFR-05-asy-4-RB.omc          >> $dir.py # Definition of radial shield assemblies
cat ../../link_SyncWithSerpent/CEFR-05-asy-5-NS.omc          >> $dir.py # Definition of neutron source assembly
cat ../../link_SyncWithSerpent/CEFR-05-asy-6-MU.omc          >> $dir.py # Definition of mock-up assembly
cat ../../link_SyncWithSerpent/CEFR-05-asy-7-VO.omc          >> $dir.py # Definition of sodium void fuel assembly 
# # - Control Rods Position 
cat ../../link_SyncWithSerpent/CEFR-07-rod-position-0-ARO.omc                  >> $dir.py # Control rod positions

# # - Core
cat ../../link_SyncWithSerpent/CEFR-06-core-lat-79assy-250C.omc                 >> $dir.py # Core lattice specs

echo "# Instantiate a Geometry, register the root Universe, and export to XML" >> $dir.py 
echo "geometry = openmc.Geometry(root)                                       " >> $dir.py 
echo "geometry.export_to_xml()                                               " >> $dir.py 

# -------------------------------------------------------
# --- Run options
# -------------------------------------------------------
cat ../../link_SyncWithSerpent/SET-01-BASIC.omc >> $dir.py
cat ../../link_SyncWithSerpent/SET-02-PLOT.omc  >> $dir.py
cat ../../link_SyncWithSerpent/SET-03-TALLY.omc >> $dir.py

# -------------------------------------------------------
# --- Simulate OpenMC
# -------------------------------------------------------
python3.10 ./$dir.py
openmc -p 
#nohup openmc -s $1 > $dir.log && h5dump summary.h5 > summary.ascii &
openmc -s $1 > $dir.log && h5dump summary.h5 > summary.ascii 

