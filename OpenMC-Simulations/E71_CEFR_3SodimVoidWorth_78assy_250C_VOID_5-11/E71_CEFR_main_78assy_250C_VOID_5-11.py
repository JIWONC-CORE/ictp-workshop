import openmc
# Instantiate ZCylinder surfaces

#-----------------------------------------------------------------------------------
# --- Pin surfaces - fuel
#-----------------------------------------------------------------------------------       
# --- 61 pin lattices (same inner/outer clad)
#
# ---  Fuel fissile
cyl_FI_hole = openmc.ZCylinder( x0=0, y0=0, r=0.08020, name='cyl_FI_hole') # Fissile fuel pellet inner hole radius (cm)
cyl_FI_fuel = openmc.ZCylinder( x0=0, y0=0, r=0.25565, name='cyl_FI_fuel') # Fissile fuel pellet radius (cm)
# ---  Fuel fertile
cyl_FE_fuel = openmc.ZCylinder( x0=0, y0=0, r=0.25559, name='cyl_FE_fuel') # Fertile fuel pellet radius (cm)
# --- Cladding
cyl_Clad61_IN = openmc.ZCylinder( x0=0, y0=0, r=0.27112, name='cyl_Clad61_IN') # Inner clad radius (cm)
cyl_Clad61_OU = openmc.ZCylinder( x0=0, y0=0, r=0.30499, name='cyl_Clad61_OU') # Outer clad radius (cm)

#-----------------------------------------------------------------------------------
# --- Radial surfaces - Fuel assembly
#-----------------------------------------------------------------------------------
hex_HEA_IN   = openmc.hexagonal_prism(orientation='y', origin=(0.0, 0.0),edge_length= 2.909856904) # pitch = 2.52001, Head inner flat-to-flat/2 (cm)
cyl_USH_hole = openmc.ZCylinder( x0=0, y0=0, r=1.60662, name='cyl_USH_hole')                       #                  Upper shield inner hole radius (cm)                       
hex_UCN_IN   = openmc.hexagonal_prism(orientation='y', origin=(0.0, 0.0),edge_length= 3.234720353) # pitch = 2.80135, Upper connector inner flat-to-flat/2 (cm)             
hex_LCN_IN   = openmc.hexagonal_prism(orientation='y', origin=(0.0, 0.0),edge_length= 3.310260862) # pitch = 2.86677, Lower connector inner flat-to-flat/2 (cm) 

# --- SA wrapper hexagons
hex_WR_IN    = openmc.hexagonal_prism(orientation='y', origin=(0.0, 0.0),edge_length= 3.281335614) # pitch=2.84172, Wrapper tube inner flat-to-flat/2 (cm) 
hex_WR_OU    = openmc.hexagonal_prism(orientation='y', origin=(0.0, 0.0),edge_length= 3.420465482) # pitch=2.96221, Wrapper tube outer flat-to-flat/2 (cm) 
hex_SA_PITCH = openmc.hexagonal_prism(orientation='y', origin=(0.0, 0.0),edge_length= 3.536385869) # pitch=3.06260, S/A Pitch          flat-to-flat/2 (cm)

#-----------------------------------------------------------------------------------
# --- Radial surfaces - CR assembly 
#-----------------------------------------------------------------------------------
# -------------- Movable part ------------
# --- B4C cluster
cyl_CR_B4C      = openmc.ZCylinder( x0=0, y0=0, r=0.61000, name='cyl_CR_B4C')      # B4C radius (cm)
cyl_CR_Clad_IN  = openmc.ZCylinder( x0=0, y0=0, r=0.64767, name='cyl_CR_Clad_IN')  # Na radius (cm)
cyl_CR_Clad_OU2 = openmc.ZCylinder( x0=0, y0=0, r=0.74808, name='cyl_CR_Clad_OU2') # Clad radius (cm) 
cyl_CR_Clad_OU1 = openmc.ZCylinder( x0=0, y0=0, r=0.74940, name='cyl_CR_Clad_OU1') # Clad radius (cm) - central pin

cyl_CR_SHAFT_IN = openmc.ZCylinder( x0=0, y0=0, r=0.75311, name='cyl_CR_SHAFT_IN') # Shaft inner radius 
cyl_CR_CON_IN   = openmc.ZCylinder( x0=0, y0=0, r=2.00870, name='cyl_CR_CON_IN')   # Upper/lower connector inner radius 
cyl_CR_CON_OU   = openmc.ZCylinder( x0=0, y0=0, r=2.46014, name='cyl_CR_CON_OU')   # Upper/lower connector inner radius 
cyl_CR_WR_IN    = openmc.ZCylinder( x0=0, y0=0, r=2.35973, name='cyl_CR_WR_IN')    # Internal wrapper of CR inner radius 
cyl_CR_WR_OU    = openmc.ZCylinder( x0=0, y0=0, r=2.46014, name='cyl_CR_WR_OU')    # Internal wrapper of CR outer radius
cyl_CR_BAF_IN   = openmc.ZCylinder( x0=0, y0=0, r=2.05849, name='cyl_CR_BAF_IN')   # Baffle inner radius 
cyl_CR_BAF_OU   = openmc.ZCylinder( x0=0, y0=0, r=2.46014, name='cyl_CR_BAF_OU')   # Baffle outer radius

# --- Plenum = Empty internal wrapper of CR assembly 
# --- Lower connector = Upper connector upper

# -------------- NON-movable part ------------

cyl_CR_HEA_IN = openmc.ZCylinder( x0=0, y0=0, r=2.10869, name='cyl_CR_HEA_IN')  # Head handling + gripper inner radius 
cyl_CR_HEA_OU = openmc.ZCylinder( x0=0, y0=0, r=2.61076, name='cyl_CR_HEA_OU')  # Head handling + gripper outer radius
cyl_CR_HCO_IN = openmc.ZCylinder( x0=0, y0=0, r=2.10869, name='cyl_CR_HCO_IN')  # Head connector inner radius 
cyl_CR_HCO_OU = openmc.ZCylinder( x0=0, y0=0, r=2.61076, name='cyl_CR_HCO_OU')  # Head connector outer radius

cyl_CR_UPL_IN = openmc.ZCylinder( x0=0, y0=0, r=2.65093, name='cyl_CR_UPL_IN')  # Upper plenum inner radius
hex_CR_UPL_OU = openmc.hexagonal_prism(orientation='y', origin=(0.0, 0.0),edge_length= 3.420465482) # pitch=2.96221, Upper plenum outer radius
cyl_CR_LSH    = openmc.ZCylinder( x0=0, y0=0, r=2.61076, name='cyl_CR_LSH')     # Lower shielding inner radius

#cone_CR_PH_IN = openmc.ZCylinder( x0=0, y0=0, r=2.65093, name='cone_CR_PH_IN') # Approximate in OpenMC
cone_CR_PH_IN = openmc.ZCone(x0=0, y0=0, z0=197.11268, r2=2.65093, name='cone_CR_PH_IN')
#surf cone_CR_PH_IN cone  0.0 0.0 197.11268  # z1 = 196.300 Transition CR head plenum-connector
#                                   2.65093   
#                                   7.45925   
#cone_CR_PH_OU = openmc.ZCylinder( x0=0, y0=0, r=2.96221, name='cone_CR_PH_OU') # Approximate in OpenMC
cone_CR_PH_OU = openmc.ZCone(x0=0, y0=0, z0=197.11268, r2=2.96221, name='cone_CR_PH_OU')
#surf cone_CR_PH_OU cone  0.0 0.0 197.11268  # z2 = 197.300 Transition CR head plenum-connector
#                                   2.96221   
#                                   8.46339   

#-----------------------------------------------------------------------------------
# --- Radial surfaces - Radial Reflector + Neutron Source SA
#-----------------------------------------------------------------------------------
cyl_NS_IN       = openmc.ZCylinder( x0=0, y0=0, r=0.90373, name='cyl_NS_IN')    # Inner radius - Central rod of neutron source
cyl_RR_SS_T1    = openmc.ZCylinder( x0=0, y0=0, r=1.00414, name='cyl_RR_SS_T1') # RR rod radius (cm) - % Type   I & II
cyl_RR_SS_T3    = openmc.ZCylinder( x0=0, y0=0, r=2.71118, name='cyl_RR_SS_T3') # RR rod radius (cm) - % Type III & IV

# Upper shield in RR Type I,II,III,IV and Boron shield is EQUAL to rod in RR Type III & IV

# RB upper shield == rod in RR Type III & IV
# RB lower shield == CR lower shield --> cyl_CR_LSH

#-----------------------------------------------------------------------------------
# --- Radial surfaces - Radial Shield 
#-----------------------------------------------------------------------------------
cyl_RB_B4C      = openmc.ZCylinder( x0=0, y0=0, r=0.81078, name='cyl_RB_B4C')
cyl_RB_He       = openmc.ZCylinder( x0=0, y0=0, r=0.86356, name='cyl_RB_He')
cyl_RB_SS       = openmc.ZCylinder( x0=0, y0=0, r=0.96397, name='cyl_RB_SS')


# RB upper shield == rod in RR Type III & IV
# RB lower shield == CR lower shield --> cyl_CR_LSH

#-----------------------------------------------------------------------------------
# --- Axial surfaces - Fuel assembly 
#-----------------------------------------------------------------------------------
# --- fuel - axial s/a regions - upper boundary
pz_FUEL_HEA = openmc.ZPlane( z0= 220.473 ,name='pz_FUEL_HEA') # 01 - Head
pz_FUEL_USH = openmc.ZPlane( z0= 197.377 ,name='pz_FUEL_USH') # 02 - Upper shield
pz_FUEL_UCN = openmc.ZPlane( z0= 150.183 ,name='pz_FUEL_UCN') # 03 - Upper connector
pz_FUEL_TEP = openmc.ZPlane( z0= 144.158 ,name='pz_FUEL_TEP') # 04 - Top end plug
pz_FUEL_SPR = openmc.ZPlane( z0= 143.154 ,name='pz_FUEL_SPR') # 05 - Spring
pz_FUEL_UBL = openmc.ZPlane( z0= 137.631 ,name='pz_FUEL_UBL') # 06 - Upper blanket
pz_FUEL_FIS = openmc.ZPlane( z0= 127.608 ,name='pz_FUEL_FIS') # 07 - Fissile
pz_FUEL_LBL = openmc.ZPlane( z0= 82.494  ,name='pz_FUEL_LBL') # 08 - Lower blanket
pz_FUEL_LGP = openmc.ZPlane( z0= 57.437  ,name='pz_FUEL_LGP') # 09 - Lower gas plenum
pz_FUEL_BEP = openmc.ZPlane( z0= 12.251  ,name='pz_FUEL_BEP') # 10 - Bottom end plug
pz_FUEL_LCN = openmc.ZPlane( z0= 8.736   ,name='pz_FUEL_LCN') # 11 - Lower connector

#-----------------------------------------------------------------------------------
# --- Axial surfaces - CR assembly
#-----------------------------------------------------------------------------------
# --- CR assembly - Movable part - upper boundary
pz_CR_UCO = openmc.ZPlane( z0= 68.320, name='pz_CR_UCO') # Upper connector
pz_CR_PLE = openmc.ZPlane( z0= 61.794, name='pz_CR_PLE') # Plenum
pz_CR_ABS = openmc.ZPlane( z0= 58.681, name='pz_CR_ABS') # Absorber
pz_CR_LCO = openmc.ZPlane( z0=  7.631, name='pz_CR_LCO') # Lower connector
pz_CR_BAF = openmc.ZPlane( z0=  4.217, name='pz_CR_BAF') # Baffle
pz_CR_BOT = openmc.ZPlane( z0=  0.000, name='pz_CR_BOT') # Bottom

# --- CR assembly - NON-Movable part - upper boundary
pz_CR_HEA = openmc.ZPlane( z0= 219.405, name='pz_CR_HEA') # Head handling +gripper
pz_CR_HCO = openmc.ZPlane( z0= 206.451, name='pz_CR_HCO') # Head connector
pz_CR_TRS = openmc.ZPlane( z0= 198.518, name='pz_CR_TRS') # Transition
pz_CR_UPL = openmc.ZPlane( z0= 197.514, name='pz_CR_UPL') # Upper plenum
pz_CR_WRA = openmc.ZPlane( z0= 130.839, name='pz_CR_WRA') # Normal wrapper
pz_CR_SHL = openmc.ZPlane( z0=  65.872, name='pz_CR_SHL') # Lower shield

#-----------------------------------------------------------------------------------
# --- Axial surfaces - RR assembly Type I&II SS SA 
#-----------------------------------------------------------------------------------
pz_RR1_SHU = openmc.ZPlane( z0= 220.610 ,name='pz_RR1_SHU') # Upper shield
pz_RR1_USP = openmc.ZPlane( z0= 145.801 ,name='pz_RR1_USP') # Na plenum
pz_RR1_SSR = openmc.ZPlane( z0= 143.291 ,name='pz_RR1_SSR') # SS rods cluster
pz_RR1_LSP = openmc.ZPlane( z0=  56.131 ,name='pz_RR1_LSP') # Na plenum
pz_RR1_SHL = openmc.ZPlane( z0=  52.617 ,name='pz_RR1_SHL') # Lower shield

#-----------------------------------------------------------------------------------
# --- Axial surfaces - RR assembly Type III&IV SS SA 
#-----------------------------------------------------------------------------------
pz_RR2_SHU = openmc.ZPlane( z0= 220.610  ,name='pz_RR2_SHU') # Upper shield
pz_RR2_LSP = openmc.ZPlane( z0=  56.131  ,name='pz_RR2_LSP') # Na plenum
pz_RR2_SHL = openmc.ZPlane( z0=  52.617  ,name='pz_RR2_SHL') # Lower shield

#-----------------------------------------------------------------------------------
# --- Axial surfaces - Boron shielding SA
#-----------------------------------------------------------------------------------
pz_RB_SHU2 = openmc.ZPlane( z0=220.610  ,name='pz_RB_SHU2') # Upper shield
pz_RB_USP  = openmc.ZPlane( z0=145.801  ,name='pz_RB_USP')  # Na plenum	
pz_RB_SHU1 = openmc.ZPlane( z0=142.789  ,name='pz_RB_SHU1') # Upper shield
pz_RB_RB   = openmc.ZPlane( z0=137.768  ,name='pz_RB_RB')   # Rod cluster	
pz_RB_SHL2 = openmc.ZPlane( z0= 57.437  ,name='pz_RB_SHL2') # Lower shield
pz_RB_LSP  = openmc.ZPlane( z0= 54.625  ,name='pz_RB_LSP')  # Na plenum	
pz_RB_SHL1 = openmc.ZPlane( z0= 52.617  ,name='pz_RB_SHL1') # Lower shield

#-----------------------------------------------------------------------------------
# --- Axial surfaces - Neutron source SA
#-----------------------------------------------------------------------------------
pz_NS_SHU = openmc.ZPlane( z0= 220.610 ,name='pz_NS_SHU') # Upper shield
pz_NS_USP = openmc.ZPlane( z0= 145.801 ,name='pz_NS_USP') # Na plenum
pz_NS_SSR = openmc.ZPlane( z0= 143.291 ,name='pz_NS_SSR') # SS rods cluster
pz_NS_NSR = openmc.ZPlane( z0= 105.133 ,name='pz_NS_NSR') # NS rods cluster
pz_NS_LSP = openmc.ZPlane( z0=  56.131 ,name='pz_NS_LSP') # Na plenum
pz_NS_SHL = openmc.ZPlane( z0=  52.617 ,name='pz_NS_SHL') # Lower shield

#-----------------------------------------------------------------------------------
# --- Axial surfaces - Mock-up SA
#-----------------------------------------------------------------------------------
pz_MU_SHU = openmc.ZPlane( z0= 220.610, name='pz_MU_SHU') # Upper shield
pz_MU_USP = openmc.ZPlane( z0= 150.320, name='pz_MU_USP') # Na plenum
pz_MU_SSR = openmc.ZPlane( z0= 142.186, name='pz_MU_SSR') # Filter
pz_MU_SHL = openmc.ZPlane( z0= 114.271, name='pz_MU_SHL') # Lower shield

##-----------------------------------------------------------------------------------
## --- Axial surfaces - Na sealed SA
##-----------------------------------------------------------------------------------
#pz_VO_9 = openmc.ZPlane( z0= 149.316, name='pz_VO_9')
#pz_VO_8 = openmc.ZPlane( z0= 143.291, name='pz_VO_8')
#pz_VO_7 = openmc.ZPlane( z0= 142.287, name='pz_VO_7')
#pz_VO_6 = openmc.ZPlane( z0= 137.631, name='pz_VO_6')
#pz_VO_5 = openmc.ZPlane( z0= 127.608, name='pz_VO_5')
#pz_VO_4 = openmc.ZPlane( z0= 82.494 , name='pz_VO_4')
#pz_VO_3 = openmc.ZPlane( z0= 57.437 , name='pz_VO_3')
#pz_VO_2 = openmc.ZPlane( z0= 12.251 , name='pz_VO_2')
#pz_VO_1 = openmc.ZPlane( z0= 8.736  , name='pz_VO_1')

#-----------------------------------------------------------------------------------
# --- Core surfaces
#-----------------------------------------------------------------------------------
pz_BOT   = openmc.ZPlane( z0= 0.00    ,name='pz_BOT', boundary_type='vacuum') 
pz_TOP   = openmc.ZPlane( z0= 221.778 ,name='pz_TOP', boundary_type='vacuum') # 221.778 

# Surface define for CORE 
hexcore = openmc.hexagonal_prism(orientation='y', origin=(0.0, 0.0),edge_length= 102.7683479, boundary_type='vacuum')                                  

###############################################################################
#                 Exporting to OpenMC materials.xml file
###############################################################################

# Instantiate some Materials and register the appropriate Nuclides

# UO2 for Fuel 
# --- UOF at T=250.0 deg-C
UOF = openmc.Material( name='UOF')
UOF.temperature=523.15
UOF.set_density('atom/b-cm',density=7.02131E-02)
UOF.add_nuclide('U235',1.49981E-02) # 92235
UOF.add_nuclide('U238',8.26381E-03) # 92238
UOF.add_nuclide('O16', 4.69512E-02) # 8016

# UO2 for Blanket
# --- UOB at T=250.0 deg-C
UOB = openmc.Material( name='UOB')
UOB.temperature=523.15
UOB.set_density('atom/b-cm',density=7.01095E-02)
UOB.add_nuclide('U235',1.04432E-04) # 92235
UOB.add_nuclide('U238',2.30457E-02) # 92238
UOB.add_nuclide('O16', 4.69594E-02) # 8016

# 15-15Ti Stainless Steel
# --- SS at T=250.0 deg-C
SS = openmc.Material( name='SS')
SS.temperature=523.15
SS.set_density('atom/b-cm',density=8.49843E-02)
SS.add_nuclide('Fe54' ,3.18736E-03 ) # 26054
SS.add_nuclide('Fe56' ,5.00347E-02 ) # 26056
SS.add_nuclide('Fe57' ,1.15552E-03 ) # 26057
SS.add_nuclide('Fe58' ,1.53779E-04 ) # 26058
SS.add_nuclide('Cr50' ,6.43727E-04 ) # 24050
SS.add_nuclide('Cr52' ,1.24136E-02 ) # 24052
SS.add_nuclide('Cr53' ,1.40761E-03 ) # 24053
SS.add_nuclide('Cr54' ,3.50383E-04 ) # 24054
SS.add_nuclide('Ni58' ,8.11014E-03 ) # 28058
SS.add_nuclide('Ni60' ,3.12399E-03 ) # 28060
SS.add_nuclide('Ni61' ,1.35798E-04 ) # 28061
SS.add_nuclide('Ni62' ,4.32997E-04 ) # 28062
SS.add_nuclide('Ni64' ,1.10257E-04 ) # 28064
SS.add_nuclide('Mo92' ,1.57916E-04 ) # 42092
SS.add_nuclide('Mo94' ,9.94445E-05 ) # 42094
SS.add_nuclide('Mo95' ,1.72153E-04 ) # 42095
SS.add_nuclide('Mo96' ,1.81174E-04 ) # 42096
SS.add_nuclide('Mo97' ,1.04335E-04 ) # 42097
SS.add_nuclide('Mo98' ,2.65077E-04 ) # 42098
SS.add_nuclide('Mo100',1.06726E-04 ) # 42100
SS.add_nuclide('Mn55' ,1.29433E-03 ) # 25055
SS.add_nuclide('C0'   ,2.37026E-04 ) # 6000
SS.add_nuclide('Ti46' ,2.85966E-05 ) # 22046
SS.add_nuclide('Ti47' ,2.57889E-05 ) # 22047
SS.add_nuclide('Ti48' ,2.55532E-04 ) # 22048
SS.add_nuclide('Ti49' ,1.87524E-05 ) # 22049
SS.add_nuclide('Ti50' ,1.79552E-05 ) # 22050
SS.add_nuclide('Si28' ,7.00451E-04 ) # 14028
SS.add_nuclide('Si29' ,3.55834E-05 ) # 14029
SS.add_nuclide('Si30' ,2.34843E-05 ) # 14030

# Ti316 Stainless Steel
# --- 316Ti at T=250.0 deg-C
Ti316 = openmc.Material( name='Ti316')
Ti316.temperature=523.15
Ti316.set_density('atom/b-cm',density=8.54309E-02)
Ti316.add_nuclide('Fe54' ,3.23855E-03 ) # 26054.03c
Ti316.add_nuclide('Fe56' ,5.08384E-02 ) # 26056.03c
Ti316.add_nuclide('Fe57' ,1.17408E-03 ) # 26057.03c
Ti316.add_nuclide('Fe58' ,1.56248E-04 ) # 26058.03c
Ti316.add_nuclide('Cr50' ,6.74283E-04 ) # 24050.03c
Ti316.add_nuclide('Cr52' ,1.30029E-02 ) # 24052.03c
Ti316.add_nuclide('Cr53' ,1.47442E-03 ) # 24053.03c
Ti316.add_nuclide('Cr54' ,3.67015E-04 ) # 24054.03c
Ti316.add_nuclide('Ni58' ,6.88162E-03 ) # 28058.03c
Ti316.add_nuclide('Ni60' ,2.65077E-03 ) # 28060.03c
Ti316.add_nuclide('Ni61' ,1.15228E-04 ) # 28061.03c
Ti316.add_nuclide('Ni62' ,3.67407E-04 ) # 28062.03c
Ti316.add_nuclide('Ni64' ,9.35550E-05 ) # 28064.03c
Ti316.add_nuclide('Mo92' ,1.79675E-04 ) # 42092.03c
Ti316.add_nuclide('Mo94' ,1.13147E-04 ) # 42094.03c
Ti316.add_nuclide('Mo95' ,1.95874E-04 ) # 42095.03c
Ti316.add_nuclide('Mo96' ,2.06138E-04 ) # 42096.03c
Ti316.add_nuclide('Mo97' ,1.18712E-04 ) # 42097.03c
Ti316.add_nuclide('Mo98' ,3.01602E-04 ) # 42098.03c
Ti316.add_nuclide('Mo100',1.21432E-04 ) # 42100.03c
Ti316.add_nuclide('Mn55' ,1.51194E-03 ) # 25055.03c
Ti316.add_nuclide('C0'   ,2.37324E-04 ) #  6000.03c
Ti316.add_nuclide('Ti46' ,3.27229E-05 ) # 22046.03c
Ti316.add_nuclide('Ti47' ,2.95101E-05 ) # 22047.03c
Ti316.add_nuclide('Ti48' ,2.92403E-04 ) # 22048.03c
Ti316.add_nuclide('Ti49' ,2.14583E-05 ) # 22049.03c
Ti316.add_nuclide('Ti50' ,2.05460E-05 ) # 22050.03c
Ti316.add_nuclide('Si28' ,9.35106E-04 ) # 14028.03c
Ti316.add_nuclide('Si29' ,4.75041E-05 ) # 14029.03c
Ti316.add_nuclide('Si30' ,3.13517E-05 ) # 14030.03c

# -------------------------------------------------------
# --- B4C in different locations
# -------------------------------------------------------
# B4C 92.0 % for Control rod 
# Enriched B for control rods (92.0%)
# --- B4Cenr at T=250.0 deg-C
B4Cenr = openmc.Material( name='B4Cenr')
B4Cenr.temperature=523.15
B4Cenr.set_density('atom/b-cm',density=1.14461E-01)
B4Cenr.add_nuclide('B10',8.42435E-02) # 5010
B4Cenr.add_nuclide('B11',7.32552E-03) # 5011
B4Cenr.add_nuclide('C0', 2.28923E-02) # 6000

# B4C 19.6 % (Nat.) for Control rod 
# Natural B for control rods (19.6%)
# --- B4Cnat at T=250.0 deg-C
B4Cnat1 = openmc.Material( name='B4Cnat1')
B4Cnat1.temperature=523.15
B4Cnat1.set_density('atom/b-cm',density=1.07527E-01)
B4Cnat1.add_nuclide('B10',1.68602E-02) # 5010
B4Cnat1.add_nuclide('B11',6.91612E-02) # 5011
B4Cnat1.add_nuclide('C0', 2.15054E-02) # 6000

# B4C 19.8 % for Boron Shielding
# Natural B for boron shielding (19.8%)
# --- B4Cnat at T=250.0 deg-C
B4Cnat2 = openmc.Material( name='B4Cnat2')
B4Cnat2.temperature=523.15
B4Cnat2.set_density('atom/b-cm',density=1.14405E-01)
B4Cnat2.add_nuclide('B10',1.81217E-02) # 5010
B4Cnat2.add_nuclide('B11',7.34021E-02) # 5011
B4Cnat2.add_nuclide('C0', 2.28809E-02) # 6000

# -------------------------------------------------------
# --- AIR in different locations
# -------------------------------------------------------
He = openmc.Material( name='He')
He.temperature=523.15
He.set_density('sum')
He.add_nuclide('O16',1.00000E-11)

vacuum = openmc.Material( name='vacuum')
vacuum.temperature=523.15
vacuum.set_density('sum')
vacuum.add_nuclide('O16',1.00000E-23)


# -------------------------------------------------------
# --- Sodium in different locations
# -------------------------------------------------------
#T       20°C        470°C     545°C
#ND   2.48851E-02 2.19235E-02 2.14078E-02

# --- Na in inner fuel
# Outlet 
Na_FU_Out = openmc.Material( name='Na_FU_Out')
Na_FU_Out.temperature=523.15
Na_FU_Out.set_density('sum')
Na_FU_Out.add_nuclide('Na23',2.33599E-02)

# Fissile
Na_FU_FI = openmc.Material( name='Na_FU_FI')
Na_FU_FI.temperature=523.15
Na_FU_FI.set_density('sum')
Na_FU_FI.add_nuclide('Na23',2.33599E-02)

# Fertile
Na_FU_FE = openmc.Material( name='Na_FU_FE')
Na_FU_FE.temperature=523.15
Na_FU_FE.set_density('sum')
Na_FU_FE.add_nuclide('Na23',2.33599E-02)

# Inlet
Na_FU_In = openmc.Material( name='Na_FU_In')
Na_FU_In.temperature=523.15
Na_FU_In.set_density('sum')
Na_FU_In.add_nuclide('Na23',2.33599E-02)

# - Bypass Na outside S/A wrapper
# Outlet 
Na_FU_OUT_bypass = openmc.Material( name='Na_FU_OUT_bypass')
Na_FU_OUT_bypass.temperature=523.15
Na_FU_OUT_bypass.set_density('sum')
Na_FU_OUT_bypass.add_nuclide('Na23',2.33599E-02)

# Fissile
Na_FU_FI_bypass = openmc.Material( name='Na_FU_FI_bypass')
Na_FU_FI_bypass.temperature=523.15
Na_FU_FI_bypass.set_density('sum')
Na_FU_FI_bypass.add_nuclide('Na23',2.33599E-02)

# Fertile
Na_FU_FE_bypass = openmc.Material( name='Na_FU_FE_bypass')
Na_FU_FE_bypass.temperature=523.15
Na_FU_FE_bypass.set_density('sum')
Na_FU_FE_bypass.add_nuclide('Na23',2.33599E-02)

# Inlet
Na_FU_In_bypass = openmc.Material( name='Na_FU_In_bypass')
Na_FU_In_bypass.temperature=523.15
Na_FU_In_bypass.set_density('sum')
Na_FU_In_bypass.add_nuclide('Na23',2.33599E-02)


# --- Na in CR
# CSD Na outlet  
Na_CR_Out = openmc.Material( name='Na_CR_Out')
Na_CR_Out.temperature=523.15
Na_CR_Out.set_density('sum')
Na_CR_Out.add_nuclide('Na23',2.33599E-02)

# CSD Na inlet
Na_CR_In = openmc.Material( name='Na_CR_In')
Na_CR_In.temperature=523.15
Na_CR_In.set_density('sum')
Na_CR_In.add_nuclide('Na23',2.33599E-02)

# --- Na in R1(=R2) and R3
# DSD Na outlet  
Na_RR_In = openmc.Material( name='Na_RR_In')
Na_RR_In.temperature=523.15
Na_RR_In.set_density('sum')
Na_RR_In.add_nuclide('Na23',2.33599E-02)

# DSD Na inlet
Na_RR_Out = openmc.Material( name='Na_RR_Out')
Na_RR_Out.temperature=523.15
Na_RR_Out.set_density('sum')
Na_RR_Out.add_nuclide('Na23',2.33599E-02)

# -------------------------------------------------------
# --- Homogeneous mixtures
# -------------------------------------------------------
# ---    OpenMC format
# ---    <matname> = openmc.Material.mix_materials ([<mat1>,<mat2>, ...], [<frac1>,<frac2>, ...], 'xx')
# ---    'xx': Mass fractions are entered with 'wo', and volume fractions with 'vo'.
#
# SS Mixture 
SS_R1 = openmc.Material.mix_materials([Ti316], [1.00], 'vo', name='SS_R1')
SS_R1.temperature=523.15
SS_R2 = openmc.Material.mix_materials([Ti316], [1.00], 'vo', name='SS_R2')
SS_R2.temperature=523.15
SS_R3 = openmc.Material.mix_materials([Ti316], [1.00], 'vo', name='SS_R3')
SS_R3.temperature=523.15
SS_R4 = openmc.Material.mix_materials([Ti316], [1.00], 'vo', name='SS_R3')
SS_R4.temperature=523.15

# --- Homogeneous spring-NA
HOMOG_SPR_FU = openmc.Material.mix_materials([Ti316,He], [0.173,0.827], 'vo', name='HOMOG_SPR_FU')
HOMOG_SPR_FU.temperature=523.15

# --- Homogeneous SS-NA-connector
HOMOG_CR_CON = openmc.Material.mix_materials([Ti316,Na_CR_In], [0.333333,0.666664], 'vo', name='HOMOG_CR_CON')  
HOMOG_CR_CON.temperature=523.15

materials_file = openmc.Materials([
UOF,
UOB,
SS,
Ti316,
B4Cnat1,
B4Cenr,
B4Cnat2,
He,
vacuum,
Na_FU_Out,
Na_FU_FI,
Na_FU_FE,
Na_FU_In,
Na_FU_OUT_bypass,
Na_FU_FI_bypass,
Na_FU_FE_bypass,
Na_FU_In_bypass,
Na_CR_Out,
Na_CR_In,
Na_RR_In,
Na_RR_Out,
SS_R1, 
SS_R2, 
SS_R3, 
SS_R4, 
HOMOG_SPR_FU,
HOMOG_CR_CON
])

#materials_file.cross_sections = '/Users/jiwonchoe/Desktop/CEFR_TCS_Priviate/OpenMCforTCS_r1/OpenMCLib/cross_sections.xml'
materials_file.cross_sections = '/mnt/d/OpenMC_TCS/OpenMCLib/cross_sections.xml'
materials_file.export_to_xml()

# -------------------------------------------------------
# --- Pins - Fuel assemblies
# -------------------------------------------------------

# 11. Head                26.108 cm
# 10. Upper shield        44.182 cm
#  9. Upper connector      6.025 cm

# ------ Fuel pin top ------------
#  8. Top end plug        2.008 cm
#  7. Spring              4.519 cm
#  6. Upper blanket      10.023 cm
#  5. Fissile            45.114 cm
#  4. Lower blanket      25.058 cm
#  3. Lower gas plenum   45.186 cm
#  2. Bottom end plug     3.514 cm
# ------ Fuel pin bottom ---------

#  1. Lower connector     10.041 cm

# --- Void
# a_OU
c_VOID = openmc.Cell( name='c_VOID')
c_VOID.fill = None 
a_OU = openmc.Universe() 
a_OU.add_cells([c_VOID])

# --- Top end plug (TEP)
#pin02
c_FU_TEP1 = openmc.Cell( name='c_FU_TEP1') 
c_FU_TEP2 = openmc.Cell( name='c_FU_TEP2')

c_FU_TEP1.region = -cyl_Clad61_OU
c_FU_TEP2.region = +cyl_Clad61_OU

c_FU_TEP1.fill = SS 
c_FU_TEP2.fill = Na_FU_Out

p_FU_TEP = openmc.Universe()
p_FU_TEP.add_cells([
c_FU_TEP1,
c_FU_TEP2
])

# --- Spring (SPR)
#pin06
c_FU_SPR1 = openmc.Cell( name='c_FU_SPR1')
c_FU_SPR2 = openmc.Cell( name='c_FU_SPR2')
c_FU_SPR3 = openmc.Cell( name='c_FU_SPR3')

c_FU_SPR1.region = -cyl_Clad61_IN
c_FU_SPR2.region = +cyl_Clad61_IN & -cyl_Clad61_OU 
c_FU_SPR3.region = +cyl_Clad61_OU

c_FU_SPR1.fill = HOMOG_SPR_FU
c_FU_SPR2.fill = SS    
c_FU_SPR3.fill = Na_FU_Out

p_FU_SPR = openmc.Universe()
p_FU_SPR.add_cells([
c_FU_SPR1,
c_FU_SPR2,
c_FU_SPR3
])

# --- Upper fuel fertile/blanket (UBL)
#pin04
c_FU_UBL_1 = openmc.Cell( name='c_FU_UBL_1')
c_FU_UBL_2 = openmc.Cell( name='c_FU_UBL_2')
c_FU_UBL_3 = openmc.Cell( name='c_FU_UBL_3')
c_FU_UBL_4 = openmc.Cell( name='c_FU_UBL_4')

c_FU_UBL_1.region = -cyl_FE_fuel
c_FU_UBL_2.region = +cyl_FE_fuel   & -cyl_Clad61_IN 
c_FU_UBL_3.region = +cyl_Clad61_IN & -cyl_Clad61_OU 
c_FU_UBL_4.region = +cyl_Clad61_OU 

c_FU_UBL_1.fill = UOB
c_FU_UBL_2.fill = He 
c_FU_UBL_3.fill = SS 
c_FU_UBL_4.fill = Na_FU_FE

p_FU_UBL = openmc.Universe()
p_FU_UBL.add_cells([c_FU_UBL_1, c_FU_UBL_2, c_FU_UBL_3, c_FU_UBL_4])

# --- Fuel fissile (FIS)
#pin05
c_FU_FIS_0 = openmc.Cell( name='c_FU_FIS_0')
c_FU_FIS_1 = openmc.Cell( name='c_FU_FIS_1')
c_FU_FIS_2 = openmc.Cell( name='c_FU_FIS_2')
c_FU_FIS_3 = openmc.Cell( name='c_FU_FIS_3')
c_FU_FIS_4 = openmc.Cell( name='c_FU_FIS_4')

c_FU_FIS_0.region = -cyl_FI_hole
c_FU_FIS_1.region = +cyl_FI_hole   & -cyl_FI_fuel  
c_FU_FIS_2.region = +cyl_FI_fuel   & -cyl_Clad61_IN
c_FU_FIS_3.region = +cyl_Clad61_IN & -cyl_Clad61_OU
c_FU_FIS_4.region = +cyl_Clad61_OU 

c_FU_FIS_0.fill = He 
c_FU_FIS_1.fill = UOF
c_FU_FIS_2.fill = He 
c_FU_FIS_3.fill = SS 
c_FU_FIS_4.fill = Na_FU_FI

p_FU_FIS = openmc.Universe()
p_FU_FIS.add_cells([
c_FU_FIS_0,
c_FU_FIS_1,
c_FU_FIS_2,
c_FU_FIS_3,
c_FU_FIS_4
])

# --- Lower fuel fertile/blanket (LBL)
#pin04
c_FU_LBL_1 = openmc.Cell( name='c_FU_LBL_1')
c_FU_LBL_2 = openmc.Cell( name='c_FU_LBL_2')
c_FU_LBL_3 = openmc.Cell( name='c_FU_LBL_3')
c_FU_LBL_4 = openmc.Cell( name='c_FU_LBL_4')

c_FU_LBL_1.region = -cyl_FE_fuel
c_FU_LBL_2.region = +cyl_FE_fuel   & -cyl_Clad61_IN 
c_FU_LBL_3.region = +cyl_Clad61_IN & -cyl_Clad61_OU 
c_FU_LBL_4.region = +cyl_Clad61_OU 

c_FU_LBL_1.fill = UOB
c_FU_LBL_2.fill = He 
c_FU_LBL_3.fill = SS 
c_FU_LBL_4.fill = Na_FU_FE

p_FU_LBL = openmc.Universe()
p_FU_LBL.add_cells([
c_FU_LBL_1,
c_FU_LBL_2,
c_FU_LBL_3,
c_FU_LBL_4
])

# --- Lower gas plenum (LGP)
#pin06
c_FU_LGP1 = openmc.Cell( name='c_FU_LGP1')
c_FU_LGP2 = openmc.Cell( name='c_FU_LGP2')
c_FU_LGP3 = openmc.Cell( name='c_FU_LGP3')

c_FU_LGP1.region = -cyl_Clad61_IN
c_FU_LGP2.region = +cyl_Clad61_IN & -cyl_Clad61_OU
c_FU_LGP3.region = +cyl_Clad61_OU

c_FU_LGP1.fill = He
c_FU_LGP2.fill = SS
c_FU_LGP3.fill = Na_FU_In

p_FU_LGP = openmc.Universe()
p_FU_LGP.add_cells([
c_FU_LGP1,
c_FU_LGP2,
c_FU_LGP3
])

# --- Bottop end plug (BEP)                     
#pin02
c_FU_BEP1 = openmc.Cell( name='c_FU_BEP1') 
c_FU_BEP2 = openmc.Cell( name='c_FU_BEP2')

c_FU_BEP1.region = -cyl_Clad61_OU
c_FU_BEP2.region = +cyl_Clad61_OU

c_FU_BEP1.fill = SS 
c_FU_BEP2.fill = Na_FU_In

p_FU_BEP = openmc.Universe()
p_FU_BEP.add_cells([
c_FU_BEP1,
c_FU_BEP2
])

# --- Na pins
# Outlet Na
c_FU_NOU = openmc.Cell( name='c_FU_NOU')
c_FU_NOU.fill = Na_FU_Out
p_FU_NOU = openmc.Universe() 
p_FU_NOU.add_cells([c_FU_NOU])

# Na in  fissile
c_FU_NFI = openmc.Cell( name='c_FU_NFI')
c_FU_NFI.fill = Na_FU_FI
p_FU_NFI = openmc.Universe() 
p_FU_NFI.add_cells([c_FU_NFI])

# Na in  fertile
c_FU_NFE = openmc.Cell( name='c_FU_NFE')
c_FU_NFE.fill = Na_FU_FE
p_FU_NFE = openmc.Universe() 
p_FU_NFE.add_cells([c_FU_NFE])

# Inlet Na
c_FU_NIN = openmc.Cell( name='c_FU_NIN')
c_FU_NIN.fill = Na_FU_In
p_FU_NIN = openmc.Universe() 
p_FU_NIN.add_cells([c_FU_NIN])
# -------------------------------------------------------
# --- Pins - CR (regulating, safety,shim )
# CR1 = B4Cnat (regulating) 
# CR2 = B4Cenr (safety + shim)
# -------------------------------------------------------

# --- CR1 B4C enriched
#pin10c
c_CR11_ABS1 = openmc.Cell( name='c_CR11_ABS1')
c_CR11_ABS2 = openmc.Cell( name='c_CR11_ABS2')
c_CR11_ABS3 = openmc.Cell( name='c_CR11_ABS3')
c_CR11_ABS4 = openmc.Cell( name='c_CR11_ABS4')

c_CR11_ABS1.region = -cyl_CR_B4C 
c_CR11_ABS2.region = +cyl_CR_B4C     & -cyl_CR_Clad_IN 
c_CR11_ABS3.region = +cyl_CR_Clad_IN & -cyl_CR_Clad_OU1
c_CR11_ABS4.region = +cyl_CR_Clad_OU1

c_CR11_ABS1.fill = B4Cenr 
c_CR11_ABS2.fill = Na_CR_Out
c_CR11_ABS3.fill = SS 
c_CR11_ABS4.fill = Na_CR_Out

p_CR1_BENR= openmc.Universe() 
p_CR1_BENR.add_cells([
c_CR11_ABS1,
c_CR11_ABS2, 
c_CR11_ABS3, 
c_CR11_ABS4
])

#pin10
c_CR12_ABS1 = openmc.Cell( name='c_CR12_ABS1') 
c_CR12_ABS2 = openmc.Cell( name='c_CR12_ABS2')
c_CR12_ABS3 = openmc.Cell( name='c_CR12_ABS3')
c_CR12_ABS4 = openmc.Cell( name='c_CR12_ABS4')

c_CR12_ABS1.region = -cyl_CR_B4C
c_CR12_ABS2.region = +cyl_CR_B4C     & -cyl_CR_Clad_IN 
c_CR12_ABS3.region = +cyl_CR_Clad_IN & -cyl_CR_Clad_OU2
c_CR12_ABS4.region = +cyl_CR_Clad_OU2

c_CR12_ABS1.fill = B4Cenr   
c_CR12_ABS2.fill = Na_CR_Out 
c_CR12_ABS3.fill = SS     
c_CR12_ABS4.fill = Na_CR_Out

p_CR2_BENR = openmc.Universe()
p_CR2_BENR.add_cells([
c_CR12_ABS1, 
c_CR12_ABS2, 
c_CR12_ABS3, 
c_CR12_ABS4
])

# --- CR2 B4C natural
#pin9c
c_CR13_ABS1 = openmc.Cell( name='c_CR13_ABS1')
c_CR13_ABS2 = openmc.Cell( name='c_CR13_ABS2')
c_CR13_ABS3 = openmc.Cell( name='c_CR13_ABS3')
c_CR13_ABS4 = openmc.Cell( name='c_CR13_ABS4')

c_CR13_ABS1.region = -cyl_CR_B4C
c_CR13_ABS2.region = +cyl_CR_B4C     & -cyl_CR_Clad_IN 
c_CR13_ABS3.region = +cyl_CR_Clad_IN & -cyl_CR_Clad_OU1
c_CR13_ABS4.region = +cyl_CR_Clad_OU1

c_CR13_ABS1.fill = B4Cnat1
c_CR13_ABS2.fill = Na_CR_Out
c_CR13_ABS3.fill = SS
c_CR13_ABS4.fill = Na_CR_Out

p_CR1_BNAT= openmc.Universe() 
p_CR1_BNAT.add_cells([
c_CR13_ABS1, 
c_CR13_ABS2, 
c_CR13_ABS3, 
c_CR13_ABS4
])

# --- CR2 B4C natural
c_CR14_ABS1 = openmc.Cell( name='c_CR14_ABS1')
c_CR14_ABS2 = openmc.Cell( name='c_CR14_ABS2')
c_CR14_ABS3 = openmc.Cell( name='c_CR14_ABS3')
c_CR14_ABS4 = openmc.Cell( name='c_CR14_ABS4')

c_CR14_ABS1.region = -cyl_CR_B4C
c_CR14_ABS2.region = +cyl_CR_B4C     & -cyl_CR_Clad_IN  
c_CR14_ABS3.region = +cyl_CR_Clad_IN & -cyl_CR_Clad_OU2 
c_CR14_ABS4.region = +cyl_CR_Clad_OU2

c_CR14_ABS1.fill = B4Cnat1   
c_CR14_ABS2.fill = Na_CR_Out 
c_CR14_ABS3.fill = SS
c_CR14_ABS4.fill = Na_CR_Out

p_CR2_BNAT = openmc.Universe()
p_CR2_BNAT.add_cells([
c_CR14_ABS1, 
c_CR14_ABS2, 
c_CR14_ABS3, 
c_CR14_ABS4
])

# ___ Na pins
# CR1 Na outlet 
c_CR1_NaOU = openmc.Cell( name='c_CR1_NaOU')
c_CR1_NaOU.fill = Na_CR_Out
p_CR1_NaOU = openmc.Universe() 
p_CR1_NaOU.add_cells([c_CR1_NaOU])

# CR1 Na inlet
c_CR1_NaIN = openmc.Cell( name='c_CR1_NaIN')
c_CR1_NaIN.fill = Na_CR_In
p_CR1_NaIN = openmc.Universe() 
p_CR1_NaIN.add_cells([c_CR1_NaIN])

# CR2 Na outlet 
c_CR2_NaOU = openmc.Cell( name='c_CR2_NaOU')
c_CR2_NaOU.fill = Na_CR_Out
p_CR2_NaOU = openmc.Universe() 
p_CR2_NaOU.add_cells([c_CR2_NaOU])

# CR2 Na inlet
c_CR2_NaIN = openmc.Cell( name='c_CR2_NaIN')
c_CR2_NaIN.fill = Na_CR_In
p_CR2_NaIN = openmc.Universe() 
p_CR2_NaIN.add_cells([c_CR2_NaIN])

# -------------------------------------------------------
# --- Pins - RR (regulating, safety,shim )
# Type   I and II
# -------------------------------------------------------

# --- Type   I
c_RR11 = openmc.Cell( name='c_RR11')
c_RR12 = openmc.Cell( name='c_RR12')

c_RR11.region = -cyl_RR_SS_T1
c_RR12.region = +cyl_RR_SS_T1

c_RR11.fill = SS_R1
c_RR12.fill = Na_RR_In

p_RR_T1 = openmc.Universe()
p_RR_T1.add_cells([
c_RR11, 
c_RR12
])

# --- Type II
c_RR21 = openmc.Cell( name='c_RR21')
c_RR22 = openmc.Cell( name='c_RR22')

c_RR21.region = -cyl_RR_SS_T1
c_RR22.region = +cyl_RR_SS_T1

c_RR21.fill = SS_R2
c_RR22.fill = Na_RR_In

p_RR_T2 = openmc.Universe()
p_RR_T2.add_cells([
c_RR21,
c_RR22
])

# ___ Na pins
# RR1 Na outlet 
c_RR_NaOU = openmc.Cell( name='c_RR_NaOU')
c_RR_NaOU.fill = Na_RR_Out
p_RR_NaOU = openmc.Universe() 
p_RR_NaOU.add_cells([c_RR_NaOU])

# RR1 Na inlet
c_RR_NaIN = openmc.Cell( name='c_RR_NaIN')
c_RR_NaIN.fill = Na_RR_In
p_RR_NaIN = openmc.Universe() 
p_RR_NaIN.add_cells([c_RR_NaIN])

# -------------------------------------------------------
# --- Pins - RB (radial shield)
# Type   I and II
# -------------------------------------------------------
#pin18
c_RB11 = openmc.Cell( name='c_RB11')
c_RB12 = openmc.Cell( name='c_RB12')
c_RB13 = openmc.Cell( name='c_RB13')
c_RB14 = openmc.Cell( name='c_RB14')

c_RB11.region = -cyl_RB_B4C
c_RB12.region = +cyl_RB_B4C & -cyl_RB_He
c_RB13.region = +cyl_RB_He  & -cyl_RB_SS
c_RB14.region = +cyl_RB_SS

c_RB11.fill = B4Cnat2
c_RB12.fill = He
c_RB13.fill = SS
c_RB14.fill = Na_RR_In

p_RB = openmc.Universe()
p_RB.add_cells([
c_RB11, 
c_RB12, 
c_RB13, 
c_RB14
])

# ___ Na pins
# RB1 Na outlet 
c_RB_NaOU = openmc.Cell( name='c_RB_NaOU')
c_RB_NaOU.fill = Na_RR_Out
p_RB_NaOU = openmc.Universe() 
p_RB_NaOU.add_cells([c_RB_NaOU])

# RB1 Na inlet
c_RB_NaIN = openmc.Cell( name='c_RB_NaIN')
c_RB_NaIN.fill = Na_RR_In
p_RB_NaIN = openmc.Universe() 
p_RB_NaIN.add_cells([c_RB_NaIN])

# -------------------------------------------------------
# --- Pins - Neutron source
# -------------------------------------------------------
#pin23
c_NS1 = openmc.Cell( name='c_NS1')
c_NS2 = openmc.Cell( name='c_NS2')
c_NS3 = openmc.Cell( name='c_NS3')

c_NS1.region = -cyl_NS_IN
c_NS2.region = +cyl_NS_IN & -cyl_RR_SS_T1
c_NS3.region = +cyl_RR_SS_T1 

c_NS1.fill = Na_RR_In
c_NS2.fill = SS_R1
c_NS3.fill = Na_RR_In

p_NS = openmc.Universe()
p_NS.add_cells([
c_NS1, 
c_NS2, 
c_NS3
])

# ___ Na pins
# NS1 Na outlet 
c_NS_NaOU = openmc.Cell( name='c_NS_NaOU')
c_NS_NaOU.fill = Na_RR_Out
p_NS_NaOU = openmc.Universe() 
p_NS_NaOU.add_cells([c_NS_NaOU])

# NS1 Na inlet
c_NS_NaIN = openmc.Cell( name='c_NS_NaIN')
c_NS_NaIN.fill = Na_RR_In
p_NS_NaIN = openmc.Universe() 
p_NS_NaIN.add_cells([c_NS_NaIN])
# -------------------------------------------------------
# --- Pins - Fuel assemblies for sodium void 
# -------------------------------------------------------

# 11. Head                26.108 cm
# 10. Upper shield        44.182 cm
#  9. Upper connector      6.025 cm

# ------ Fuel pin top ------------
#  8. Top end plug        2.008 cm
#  7. Spring              4.519 cm
#  6. Upper blanket      10.023 cm
#  5. Fissile            45.114 cm
#  4. Lower blanket      25.058 cm
#  3. Lower gas plenum   45.186 cm
#  2. Bottom end plug     3.514 cm
# ------ Fuel pin bottom ---------

#  1. Lower connector     10.041 cm

# --- Void
# a_OU
c_VOID = openmc.Cell( name='c_VOID')
c_VOID.fill = None 
a_OU = openmc.Universe() 
a_OU.add_cells([c_VOID])

# --- Top end plug (TEP)
#pin02
c_VO_TEP1 = openmc.Cell( name='c_VO_TEP1') 
c_VO_TEP2 = openmc.Cell( name='c_VO_TEP2')

c_VO_TEP1.region = -cyl_Clad61_OU
c_VO_TEP2.region = +cyl_Clad61_OU

c_VO_TEP1.fill = SS 
c_VO_TEP2.fill = vacuum

p_VO_TEP = openmc.Universe()
p_VO_TEP.add_cells([
c_VO_TEP1,
c_VO_TEP2
])

# --- Spring (SPR)
#pin06
c_VO_SPR1 = openmc.Cell( name='c_VO_SPR1')
c_VO_SPR2 = openmc.Cell( name='c_VO_SPR2')
c_VO_SPR3 = openmc.Cell( name='c_VO_SPR3')

c_VO_SPR1.region = -cyl_Clad61_IN
c_VO_SPR2.region = +cyl_Clad61_IN & -cyl_Clad61_OU 
c_VO_SPR3.region = +cyl_Clad61_OU

c_VO_SPR1.fill = HOMOG_SPR_FU
c_VO_SPR2.fill = SS    
c_VO_SPR3.fill = vacuum

p_VO_SPR = openmc.Universe()
p_VO_SPR.add_cells([
c_VO_SPR1,
c_VO_SPR2,
c_VO_SPR3
])

# --- Upper fuel fertile/blanket (UBL)
#pin04
c_VO_UBL_1 = openmc.Cell( name='c_VO_UBL_1')
c_VO_UBL_2 = openmc.Cell( name='c_VO_UBL_2')
c_VO_UBL_3 = openmc.Cell( name='c_VO_UBL_3')
c_VO_UBL_4 = openmc.Cell( name='c_VO_UBL_4')

c_VO_UBL_1.region = -cyl_FE_fuel
c_VO_UBL_2.region = +cyl_FE_fuel   & -cyl_Clad61_IN 
c_VO_UBL_3.region = +cyl_Clad61_IN & -cyl_Clad61_OU 
c_VO_UBL_4.region = +cyl_Clad61_OU 

c_VO_UBL_1.fill = UOB
c_VO_UBL_2.fill = He 
c_VO_UBL_3.fill = SS 
c_VO_UBL_4.fill = vacuum  

p_VO_UBL = openmc.Universe()
p_VO_UBL.add_cells([c_VO_UBL_1, c_VO_UBL_2, c_VO_UBL_3, c_VO_UBL_4])

# --- Fuel fissile (FIS)
#pin05
c_VO_FIS_0 = openmc.Cell( name='c_VO_FIS_0')
c_VO_FIS_1 = openmc.Cell( name='c_VO_FIS_1')
c_VO_FIS_2 = openmc.Cell( name='c_VO_FIS_2')
c_VO_FIS_3 = openmc.Cell( name='c_VO_FIS_3')
c_VO_FIS_4 = openmc.Cell( name='c_VO_FIS_4')

c_VO_FIS_0.region = -cyl_FI_hole
c_VO_FIS_1.region = +cyl_FI_hole   & -cyl_FI_fuel  
c_VO_FIS_2.region = +cyl_FI_fuel   & -cyl_Clad61_IN
c_VO_FIS_3.region = +cyl_Clad61_IN & -cyl_Clad61_OU
c_VO_FIS_4.region = +cyl_Clad61_OU 

c_VO_FIS_0.fill = He 
c_VO_FIS_1.fill = UOF
c_VO_FIS_2.fill = He 
c_VO_FIS_3.fill = SS 
c_VO_FIS_4.fill = vacuum  

p_VO_FIS = openmc.Universe()
p_VO_FIS.add_cells([
c_VO_FIS_0,
c_VO_FIS_1,
c_VO_FIS_2,
c_VO_FIS_3,
c_VO_FIS_4
])

# --- Lower fuel fertile/blanket (LBL)
#pin04
c_VO_LBL_1 = openmc.Cell( name='c_VO_LBL_1')
c_VO_LBL_2 = openmc.Cell( name='c_VO_LBL_2')
c_VO_LBL_3 = openmc.Cell( name='c_VO_LBL_3')
c_VO_LBL_4 = openmc.Cell( name='c_VO_LBL_4')

c_VO_LBL_1.region = -cyl_FE_fuel
c_VO_LBL_2.region = +cyl_FE_fuel   & -cyl_Clad61_IN 
c_VO_LBL_3.region = +cyl_Clad61_IN & -cyl_Clad61_OU 
c_VO_LBL_4.region = +cyl_Clad61_OU 

c_VO_LBL_1.fill = UOB
c_VO_LBL_2.fill = He 
c_VO_LBL_3.fill = SS 
c_VO_LBL_4.fill = vacuum  

p_VO_LBL = openmc.Universe()
p_VO_LBL.add_cells([
c_VO_LBL_1,
c_VO_LBL_2,
c_VO_LBL_3,
c_VO_LBL_4
])

# --- Lower gas plenum (LGP)
#pin06
c_VO_LGP1 = openmc.Cell( name='c_VO_LGP1')
c_VO_LGP2 = openmc.Cell( name='c_VO_LGP2')
c_VO_LGP3 = openmc.Cell( name='c_VO_LGP3')

c_VO_LGP1.region = -cyl_Clad61_IN
c_VO_LGP2.region = +cyl_Clad61_IN & -cyl_Clad61_OU
c_VO_LGP3.region = +cyl_Clad61_OU

c_VO_LGP1.fill = He
c_VO_LGP2.fill = SS
c_VO_LGP3.fill = vacuum  

p_VO_LGP = openmc.Universe()
p_VO_LGP.add_cells([
c_VO_LGP1,
c_VO_LGP2,
c_VO_LGP3
])

# --- Bottop end plug (BEP)                     
#pin02
c_VO_BEP1 = openmc.Cell( name='c_VO_BEP1') 
c_VO_BEP2 = openmc.Cell( name='c_VO_BEP2')

c_VO_BEP1.region = -cyl_Clad61_OU
c_VO_BEP2.region = +cyl_Clad61_OU

c_VO_BEP1.fill = SS 
c_VO_BEP2.fill = vacuum  

p_VO_BEP = openmc.Universe()
p_VO_BEP.add_cells([
c_VO_BEP1,
c_VO_BEP2
])

# --- Na pins
# Outlet Na
c_VO_VOU = openmc.Cell( name='c_VO_VOU')
c_VO_VOU.fill = vacuum 
p_VO_VOU = openmc.Universe() 
p_VO_VOU.add_cells([c_VO_VOU])

# Na in  fissile
c_VO_VFI = openmc.Cell( name='c_VO_VFI')
c_VO_VFI.fill = vacuum
p_VO_VFI = openmc.Universe() 
p_VO_VFI.add_cells([c_VO_VFI])

# Na in  fertile
c_VO_VFE = openmc.Cell( name='c_VO_VFE')
c_VO_VFE.fill = vacuum  
p_VO_VFE = openmc.Universe() 
p_VO_VFE.add_cells([c_VO_VFE])

# Inlet Na
c_VO_VIN = openmc.Cell( name='c_VO_VIN')
c_VO_VIN.fill = vacuum  
p_VO_VIN = openmc.Universe() 
p_VO_VIN.add_cells([c_VO_VIN])
# --- FUEL ASSEMBLY LATTICES 
#
# 11. Head                26.00 cm
# 10. Upper shield        44.00 cm
#  9. Upper connector      6.00 cm
# ------ Fuel pin top ------------
#  8. Top end plug         2.00 cm
#  7. Spring               4.50 cm
#  6. Upper blanket       10.00 cm
#  5. Fissile             45.00 cm
#  4. Lower blanket       25.00 cm
#  3. Lower gas plenum    45.00 cm
#  2. Bottom end plug      3.50 cm
# ------ Fuel pin bottom ---------
#  1. Lower connector     10.00 cm


# -------------------------------------------------------
# --- HEAD
# -------------------------------------------------------
c_l_FU_HEA_01 = openmc.Cell( name='c_l_FU_HEA_01')
c_l_FU_HEA_02 = openmc.Cell( name='c_l_FU_HEA_02')
c_l_FU_HEA_03 = openmc.Cell( name='c_l_FU_HEA_03')

c_l_FU_HEA_01.region =  hex_HEA_IN 
c_l_FU_HEA_02.region = ~hex_HEA_IN & hex_WR_OU
c_l_FU_HEA_03.region = ~hex_WR_OU  

c_l_FU_HEA_01.fill = Na_FU_Out
c_l_FU_HEA_02.fill = Ti316
c_l_FU_HEA_03.fill = Na_FU_OUT_bypass

u_FU_HEA = openmc.Universe()
u_FU_HEA.add_cells([c_l_FU_HEA_01, c_l_FU_HEA_02, c_l_FU_HEA_03])

# -------------------------------------------------------
# --- Upper shield (USH)
# -------------------------------------------------------
c_l_FU_USH_01 = openmc.Cell( name='c_l_FU_USH_01')
c_l_FU_USH_02 = openmc.Cell( name='c_l_FU_USH_02')
c_l_FU_USH_03 = openmc.Cell( name='c_l_FU_USH_03')

c_l_FU_USH_01.region = -cyl_USH_hole
c_l_FU_USH_02.region =  hex_WR_OU & +cyl_USH_hole
c_l_FU_USH_03.region = ~hex_WR_OU

c_l_FU_USH_01.fill = Na_FU_Out
c_l_FU_USH_02.fill = Ti316
c_l_FU_USH_03.fill = Na_FU_OUT_bypass

u_FU_USH = openmc.Universe()
u_FU_USH.add_cells([c_l_FU_USH_01, c_l_FU_USH_02, c_l_FU_USH_03])

# -------------------------------------------------------
# --- Upper connector (UCN)
# -------------------------------------------------------
c_l_FU_UCN_01 = openmc.Cell( name='c_l_FU_UCN_01')
c_l_FU_UCN_02 = openmc.Cell( name='c_l_FU_UCN_02')
c_l_FU_UCN_03 = openmc.Cell( name='c_l_FU_UCN_03')

c_l_FU_UCN_01.region =  hex_UCN_IN
c_l_FU_UCN_02.region =  hex_WR_OU & ~hex_UCN_IN
c_l_FU_UCN_03.region = ~hex_WR_OU

c_l_FU_UCN_01.fill = Na_FU_Out
c_l_FU_UCN_02.fill = Ti316
c_l_FU_UCN_03.fill = Na_FU_OUT_bypass

u_FU_UCN = openmc.Universe()
u_FU_UCN.add_cells([c_l_FU_UCN_01, c_l_FU_UCN_02, c_l_FU_UCN_03])

# -------------------------------------------------------
# --- Top end plug (TEP) 
# -------------------------------------------------------
l_FU_TEP = openmc.HexLattice()
l_FU_TEP.center = [0., 0.]
l_FU_TEP.pitch  = [ 0.695]
l_FU_TEP.universes = \
       [ [p_FU_TEP]*24, [p_FU_TEP]*18, [p_FU_TEP]*12, [p_FU_TEP]*6, [p_FU_TEP] ]
l_FU_TEP.outer  = p_FU_NOU

c_l_FU_TEP_01 = openmc.Cell( name='c_l_FU_TEP_01')
c_l_FU_TEP_02 = openmc.Cell( name='c_l_FU_TEP_02')
c_l_FU_TEP_03 = openmc.Cell( name='c_l_FU_TEP_03')

c_l_FU_TEP_01.region =  hex_WR_IN
c_l_FU_TEP_02.region =  hex_WR_OU & ~hex_WR_IN
c_l_FU_TEP_03.region = ~hex_WR_OU

c_l_FU_TEP_01.fill = l_FU_TEP
c_l_FU_TEP_02.fill = Ti316
c_l_FU_TEP_03.fill = Na_FU_OUT_bypass

u_FU_TEP = openmc.Universe()
u_FU_TEP.add_cells([c_l_FU_TEP_01, c_l_FU_TEP_02, c_l_FU_TEP_03])

# -------------------------------------------------------
# --- Spring (SPR)
# -------------------------------------------------------
l_FU_SPR = openmc.HexLattice()
l_FU_SPR.center = [0., 0.]
l_FU_SPR.pitch  = [ 0.695]
l_FU_SPR.universes = \
       [ [p_FU_SPR]*24, [p_FU_SPR]*18, [p_FU_SPR]*12, [p_FU_SPR]*6, [p_FU_SPR] ]
l_FU_SPR.outer  = p_FU_NOU

c_l_FU_SPR_01 = openmc.Cell( name='c_l_FU_SPR_01')
c_l_FU_SPR_02 = openmc.Cell( name='c_l_FU_SPR_02')
c_l_FU_SPR_03 = openmc.Cell( name='c_l_FU_SPR_03')

c_l_FU_SPR_01.region =  hex_WR_IN
c_l_FU_SPR_02.region =  hex_WR_OU & ~hex_WR_IN
c_l_FU_SPR_03.region = ~hex_WR_OU

c_l_FU_SPR_01.fill = l_FU_SPR
c_l_FU_SPR_02.fill = Ti316
c_l_FU_SPR_03.fill = Na_FU_OUT_bypass

u_FU_SPR = openmc.Universe()
u_FU_SPR.add_cells([c_l_FU_SPR_01, c_l_FU_SPR_02, c_l_FU_SPR_03])

# -------------------------------------------------------
# --- Upper fuel fertile/blanket (UBL)
# -------------------------------------------------------
l_FU_UBL = openmc.HexLattice()
l_FU_UBL.center = [0., 0.]
l_FU_UBL.pitch  = [ 0.695]
l_FU_UBL.universes = \
       [ [p_FU_UBL]*24, [p_FU_UBL]*18, [p_FU_UBL]*12, [p_FU_UBL]*6, [p_FU_UBL] ]
l_FU_UBL.outer  = p_FU_NFE

c_l_FU_UBL_01 = openmc.Cell( name='c_l_FU_UBL_01')
c_l_FU_UBL_02 = openmc.Cell( name='c_l_FU_UBL_02')
c_l_FU_UBL_03 = openmc.Cell( name='c_l_FU_UBL_03')

c_l_FU_UBL_01.region =  hex_WR_IN
c_l_FU_UBL_02.region =  hex_WR_OU & ~hex_WR_IN
c_l_FU_UBL_03.region = ~hex_WR_OU

c_l_FU_UBL_01.fill = l_FU_UBL
c_l_FU_UBL_02.fill = Ti316
c_l_FU_UBL_03.fill = Na_FU_OUT_bypass

u_FU_UBL = openmc.Universe()
u_FU_UBL.add_cells([c_l_FU_UBL_01, c_l_FU_UBL_02, c_l_FU_UBL_03])

# -------------------------------------------------------
# --- Fuel fissile (FIS)
# -------------------------------------------------------
l_FU_FIS = openmc.HexLattice()
l_FU_FIS.center = [0., 0.]
l_FU_FIS.pitch  = [ 0.695]
l_FU_FIS.universes = \
       [ [p_FU_FIS]*24, [p_FU_FIS]*18, [p_FU_FIS]*12, [p_FU_FIS]*6, [p_FU_FIS] ]
l_FU_FIS.outer  = p_FU_NFI

c_l_FU_FIS_01 = openmc.Cell( name='c_l_FU_FIS_01')
c_l_FU_FIS_02 = openmc.Cell( name='c_l_FU_FIS_02')
c_l_FU_FIS_03 = openmc.Cell( name='c_l_FU_FIS_03')

c_l_FU_FIS_01.region =  hex_WR_IN
c_l_FU_FIS_02.region =  hex_WR_OU & ~hex_WR_IN
c_l_FU_FIS_03.region = ~hex_WR_OU

c_l_FU_FIS_01.fill = l_FU_FIS
c_l_FU_FIS_02.fill = Ti316
c_l_FU_FIS_03.fill = Na_FU_FI_bypass

u_FU_FIS = openmc.Universe()
u_FU_FIS.add_cells([c_l_FU_FIS_01, c_l_FU_FIS_02, c_l_FU_FIS_03])

# -------------------------------------------------------
# --- Lower fuel fertile/blanket (LBL)
# -------------------------------------------------------
l_FU_LBL = openmc.HexLattice()
l_FU_LBL.center = [0., 0.]
l_FU_LBL.pitch  = [ 0.695]
l_FU_LBL.universes = \
       [ [p_FU_LBL]*24, [p_FU_LBL]*18, [p_FU_LBL]*12, [p_FU_LBL]*6, [p_FU_LBL] ]
l_FU_LBL.outer  = p_FU_NFE

c_l_FU_LBL_01 = openmc.Cell( name='c_l_FU_LBL_01')
c_l_FU_LBL_02 = openmc.Cell( name='c_l_FU_LBL_02')
c_l_FU_LBL_03 = openmc.Cell( name='c_l_FU_LBL_03')

c_l_FU_LBL_01.region =  hex_WR_IN
c_l_FU_LBL_02.region =  hex_WR_OU & ~hex_WR_IN
c_l_FU_LBL_03.region = ~hex_WR_OU

c_l_FU_LBL_01.fill = l_FU_LBL
c_l_FU_LBL_02.fill = Ti316
c_l_FU_LBL_03.fill = Na_FU_FE_bypass

u_FU_LBL = openmc.Universe()
u_FU_LBL.add_cells([c_l_FU_LBL_01, c_l_FU_LBL_02, c_l_FU_LBL_03])

# -------------------------------------------------------
# --- Lower gas plenum (LGP)
# -------------------------------------------------------
l_FU_LGP = openmc.HexLattice()
l_FU_LGP.center = [0., 0.]
l_FU_LGP.pitch  = [ 0.695]
l_FU_LGP.universes = \
       [ [p_FU_LGP]*24, [p_FU_LGP]*18, [p_FU_LGP]*12, [p_FU_LGP]*6, [p_FU_LGP] ]
l_FU_LGP.outer  = p_FU_NIN

c_l_FU_LGP_01 = openmc.Cell( name='c_l_FU_LGP_01')
c_l_FU_LGP_02 = openmc.Cell( name='c_l_FU_LGP_02')
c_l_FU_LGP_03 = openmc.Cell( name='c_l_FU_LGP_03')

c_l_FU_LGP_01.region =  hex_WR_IN
c_l_FU_LGP_02.region =  hex_WR_OU & ~hex_WR_IN
c_l_FU_LGP_03.region = ~hex_WR_OU

c_l_FU_LGP_01.fill = l_FU_LGP
c_l_FU_LGP_02.fill = Ti316
c_l_FU_LGP_03.fill = Na_FU_In_bypass

u_FU_LGP = openmc.Universe()
u_FU_LGP.add_cells([c_l_FU_LGP_01, c_l_FU_LGP_02, c_l_FU_LGP_03])

# -------------------------------------------------------
# --- Bottop end plug (BEP) 
# -------------------------------------------------------
l_FU_BEP = openmc.HexLattice()
l_FU_BEP.center = [0., 0.]
l_FU_BEP.pitch  = [ 0.695]
l_FU_BEP.universes = \
       [ [p_FU_BEP]*24, [p_FU_BEP]*18, [p_FU_BEP]*12, [p_FU_BEP]*6, [p_FU_BEP] ]
l_FU_BEP.outer  = p_FU_NIN

c_l_FU_BEP_01 = openmc.Cell( name='c_l_FU_BEP_01')
c_l_FU_BEP_02 = openmc.Cell( name='c_l_FU_BEP_02')
c_l_FU_BEP_03 = openmc.Cell( name='c_l_FU_BEP_03')

c_l_FU_BEP_01.region =  hex_WR_IN
c_l_FU_BEP_02.region =  hex_WR_OU & ~hex_WR_IN
c_l_FU_BEP_03.region = ~hex_WR_OU

c_l_FU_BEP_01.fill = l_FU_BEP
c_l_FU_BEP_02.fill = Ti316
c_l_FU_BEP_03.fill = Na_FU_In_bypass

u_FU_BEP = openmc.Universe()
u_FU_BEP.add_cells([c_l_FU_BEP_01, c_l_FU_BEP_02, c_l_FU_BEP_03])

# -------------------------------------------------------
# --- Lower connector (LCN)
# -------------------------------------------------------
c_l_FU_LCN_01 = openmc.Cell( name='c_l_FU_LCN_01')
c_l_FU_LCN_02 = openmc.Cell( name='c_l_FU_LCN_02')
c_l_FU_LCN_03 = openmc.Cell( name='c_l_FU_LCN_03')

c_l_FU_LCN_01.region =  hex_LCN_IN 
c_l_FU_LCN_02.region =  hex_WR_OU & ~hex_LCN_IN
c_l_FU_LCN_03.region = ~hex_WR_OU  

c_l_FU_LCN_01.fill = Na_FU_Out
c_l_FU_LCN_02.fill = Ti316
c_l_FU_LCN_03.fill = Na_FU_OUT_bypass

u_FU_LCN = openmc.Universe()
u_FU_LCN.add_cells([c_l_FU_LCN_01, c_l_FU_LCN_02, c_l_FU_LCN_03])
# --- CR LATTICES and UNIVERSES

## Safety Rods 
# --- Shaft+HEA
c_l_CR_SHA_HEA_SAFT01 = openmc.Cell( name='c_l_CR_SHA_HEA_SAFT01')
c_l_CR_SHA_HEA_SAFT02 = openmc.Cell( name='c_l_CR_SHA_HEA_SAFT02')
c_l_CR_SHA_HEA_SAFT03 = openmc.Cell( name='c_l_CR_SHA_HEA_SAFT03')
c_l_CR_SHA_HEA_SAFT04 = openmc.Cell( name='c_l_CR_SHA_HEA_SAFT04')

c_l_CR_SHA_HEA_SAFT01.region = -cyl_CR_SHAFT_IN                  # Shaft in 
c_l_CR_SHA_HEA_SAFT02.region = -cyl_CR_HEA_IN & +cyl_CR_SHAFT_IN # Shaft out
c_l_CR_SHA_HEA_SAFT03.region = -cyl_CR_HEA_OU & +cyl_CR_HEA_IN      # Head connector +gripper
c_l_CR_SHA_HEA_SAFT04.region = +cyl_CR_HEA_OU                       # Head connector +gripper

c_l_CR_SHA_HEA_SAFT01.fill = Ti316
c_l_CR_SHA_HEA_SAFT02.fill = Na_CR_Out
c_l_CR_SHA_HEA_SAFT03.fill = SS
c_l_CR_SHA_HEA_SAFT04.fill = Na_CR_In

u_CR_SHA_HEA_SAFT = openmc.Universe()
u_CR_SHA_HEA_SAFT.add_cells([
c_l_CR_SHA_HEA_SAFT01, 
c_l_CR_SHA_HEA_SAFT02,
c_l_CR_SHA_HEA_SAFT03,
c_l_CR_SHA_HEA_SAFT04
])

# --- Shaft+HCO
c_l_CR_SHA_HCO_SAFT01 = openmc.Cell( name='c_l_CR_SHA_HCO_SAFT01')
c_l_CR_SHA_HCO_SAFT02 = openmc.Cell( name='c_l_CR_SHA_HCO_SAFT02')
c_l_CR_SHA_HCO_SAFT03 = openmc.Cell( name='c_l_CR_SHA_HCO_SAFT03')
c_l_CR_SHA_HCO_SAFT04 = openmc.Cell( name='c_l_CR_SHA_HCO_SAFT04')

c_l_CR_SHA_HCO_SAFT01.region = -cyl_CR_SHAFT_IN                   # Shaft in 
c_l_CR_SHA_HCO_SAFT02.region = -cyl_CR_HCO_IN & +cyl_CR_SHAFT_IN  # Shaft out
c_l_CR_SHA_HCO_SAFT03.region = -cyl_CR_HCO_OU & +cyl_CR_HCO_IN    # Head connector
c_l_CR_SHA_HCO_SAFT04.region = +cyl_CR_HCO_OU                     # Head connector

c_l_CR_SHA_HCO_SAFT01.fill = Ti316
c_l_CR_SHA_HCO_SAFT02.fill = Na_CR_Out
c_l_CR_SHA_HCO_SAFT03.fill = SS
c_l_CR_SHA_HCO_SAFT04.fill = Na_CR_In

u_CR_SHA_HCO_SAFT = openmc.Universe()
u_CR_SHA_HCO_SAFT.add_cells([
c_l_CR_SHA_HCO_SAFT01, 
c_l_CR_SHA_HCO_SAFT02,
c_l_CR_SHA_HCO_SAFT03,
c_l_CR_SHA_HCO_SAFT04
])

# --- Shaft+TRS
c_l_CR_SHA_TRS_SAFT01 = openmc.Cell( name='c_l_CR_SHA_TRS_SAFT01')
c_l_CR_SHA_TRS_SAFT02 = openmc.Cell( name='c_l_CR_SHA_TRS_SAFT02')
c_l_CR_SHA_TRS_SAFT03 = openmc.Cell( name='c_l_CR_SHA_TRS_SAFT03')
c_l_CR_SHA_TRS_SAFT04 = openmc.Cell( name='c_l_CR_SHA_TRS_SAFT04')

c_l_CR_SHA_TRS_SAFT01.region = -cyl_CR_SHAFT_IN                   # Shaft in 
c_l_CR_SHA_TRS_SAFT02.region = -cone_CR_PH_IN & +cyl_CR_SHAFT_IN  # Shaft out
c_l_CR_SHA_TRS_SAFT03.region = -cone_CR_PH_OU & +cone_CR_PH_IN    # Transition
c_l_CR_SHA_TRS_SAFT04.region = +cone_CR_PH_OU                     # Transition

c_l_CR_SHA_TRS_SAFT01.fill = Ti316
c_l_CR_SHA_TRS_SAFT02.fill = Na_CR_Out
c_l_CR_SHA_TRS_SAFT03.fill = SS
c_l_CR_SHA_TRS_SAFT04.fill = Na_CR_In

u_CR_SHA_TRS_SAFT = openmc.Universe()
u_CR_SHA_TRS_SAFT.add_cells([
c_l_CR_SHA_TRS_SAFT01, 
c_l_CR_SHA_TRS_SAFT02,
c_l_CR_SHA_TRS_SAFT03,
c_l_CR_SHA_TRS_SAFT04
])

# --- Shaft+UPL
c_l_CR_SHA_UPL_SAFT01 = openmc.Cell( name='c_l_CR_SHA_UPL_SAFT01')
c_l_CR_SHA_UPL_SAFT02 = openmc.Cell( name='c_l_CR_SHA_UPL_SAFT02')
c_l_CR_SHA_UPL_SAFT03 = openmc.Cell( name='c_l_CR_SHA_UPL_SAFT03')
c_l_CR_SHA_UPL_SAFT04 = openmc.Cell( name='c_l_CR_SHA_UPL_SAFT04')

c_l_CR_SHA_UPL_SAFT01.region = -cyl_CR_SHAFT_IN                   # Shaft in 
c_l_CR_SHA_UPL_SAFT02.region = -cyl_CR_UPL_IN & +cyl_CR_SHAFT_IN  # Shaft out
c_l_CR_SHA_UPL_SAFT03.region =  hex_CR_UPL_OU & +cyl_CR_UPL_IN    # Upper plenum
c_l_CR_SHA_UPL_SAFT04.region = ~hex_CR_UPL_OU                     # Upper plenum

c_l_CR_SHA_UPL_SAFT01.fill = Ti316
c_l_CR_SHA_UPL_SAFT02.fill = Na_CR_Out
c_l_CR_SHA_UPL_SAFT03.fill = SS
c_l_CR_SHA_UPL_SAFT04.fill = Na_CR_In

u_CR_SHA_UPL_SAFT = openmc.Universe()
u_CR_SHA_UPL_SAFT.add_cells([
c_l_CR_SHA_UPL_SAFT01, 
c_l_CR_SHA_UPL_SAFT02,
c_l_CR_SHA_UPL_SAFT03,
c_l_CR_SHA_UPL_SAFT04
])


# --- UCO+UPL
c_l_CR_UCO_UPL_SAFT01 = openmc.Cell( name='c_l_CR_UCO_UPL_SAFT01')
c_l_CR_UCO_UPL_SAFT02 = openmc.Cell( name='c_l_CR_UCO_UPL_SAFT02')
c_l_CR_UCO_UPL_SAFT03 = openmc.Cell( name='c_l_CR_UCO_UPL_SAFT03')
c_l_CR_UCO_UPL_SAFT04 = openmc.Cell( name='c_l_CR_UCO_UPL_SAFT04')

c_l_CR_UCO_UPL_SAFT01.region = -cyl_CR_CON_OU                      # Upper connector
c_l_CR_UCO_UPL_SAFT02.region = +cyl_CR_CON_OU & -cyl_CR_UPL_IN     # Upper connector
c_l_CR_UCO_UPL_SAFT03.region =  hex_CR_UPL_OU & +cyl_CR_UPL_IN     # Upper plenum   
c_l_CR_UCO_UPL_SAFT04.region = ~hex_CR_UPL_OU                      # Upper plenum

c_l_CR_UCO_UPL_SAFT01.fill = HOMOG_CR_CON
c_l_CR_UCO_UPL_SAFT02.fill = Na_CR_Out
c_l_CR_UCO_UPL_SAFT03.fill = SS
c_l_CR_UCO_UPL_SAFT04.fill = Na_CR_In

u_CR_UCO_UPL_SAFT = openmc.Universe()
u_CR_UCO_UPL_SAFT.add_cells([
c_l_CR_UCO_UPL_SAFT01,
c_l_CR_UCO_UPL_SAFT02,
c_l_CR_UCO_UPL_SAFT03,
c_l_CR_UCO_UPL_SAFT04 
])


# --- PLE+UPL
c_l_CR_PLE_UPL_SAFT01 = openmc.Cell( name='c_l_CR_PLE_UPL_SAFT01')
c_l_CR_PLE_UPL_SAFT02 = openmc.Cell( name='c_l_CR_PLE_UPL_SAFT02')
c_l_CR_PLE_UPL_SAFT03 = openmc.Cell( name='c_l_CR_PLE_UPL_SAFT03')
c_l_CR_PLE_UPL_SAFT04 = openmc.Cell( name='c_l_CR_PLE_UPL_SAFT04')
c_l_CR_PLE_UPL_SAFT05 = openmc.Cell( name='c_l_CR_PLE_UPL_SAFT05')

c_l_CR_PLE_UPL_SAFT01.region = -cyl_CR_WR_IN                    # Plenum
c_l_CR_PLE_UPL_SAFT02.region = -cyl_CR_WR_OU  & +cyl_CR_WR_IN   # Plenum
c_l_CR_PLE_UPL_SAFT03.region = -cyl_CR_UPL_IN & +cyl_CR_WR_OU   # Plenum
c_l_CR_PLE_UPL_SAFT04.region =  hex_CR_UPL_OU & +cyl_CR_UPL_IN  # Upper plenum  
c_l_CR_PLE_UPL_SAFT05.region = ~hex_CR_UPL_OU                   # Upper plenum  

c_l_CR_PLE_UPL_SAFT01.fill = Na_CR_Out
c_l_CR_PLE_UPL_SAFT02.fill = Ti316
c_l_CR_PLE_UPL_SAFT03.fill = Na_CR_Out
c_l_CR_PLE_UPL_SAFT04.fill = SS
c_l_CR_PLE_UPL_SAFT05.fill = Na_CR_In

u_CR_PLE_UPL_SAFT = openmc.Universe()
u_CR_PLE_UPL_SAFT.add_cells([
c_l_CR_PLE_UPL_SAFT01,
c_l_CR_PLE_UPL_SAFT02,
c_l_CR_PLE_UPL_SAFT03,
c_l_CR_PLE_UPL_SAFT04,
c_l_CR_PLE_UPL_SAFT05 
])

# --- ABS+UPL,  Enriched B4C - safety rod (u_CR_move_SAFT)
l_CR_SAFT = openmc.HexLattice()
l_CR_SAFT.center = [0., 0.]
l_CR_SAFT.pitch  = [1.5500]
l_CR_SAFT.universes = \
       [ [p_CR2_BENR]*6, [p_CR1_BENR] ]
l_CR_SAFT.outer  = p_CR2_NaOU
l_CR_SAFT.rotation = [0, 0,-30]

c_l_CR_ABS_UPL_SAFT01 = openmc.Cell( name='c_l_CR_ABS_UPL_SAFT01')
c_l_CR_ABS_UPL_SAFT02 = openmc.Cell( name='c_l_CR_ABS_UPL_SAFT02')
c_l_CR_ABS_UPL_SAFT03 = openmc.Cell( name='c_l_CR_ABS_UPL_SAFT03')
c_l_CR_ABS_UPL_SAFT04 = openmc.Cell( name='c_l_CR_ABS_UPL_SAFT04')
c_l_CR_ABS_UPL_SAFT05 = openmc.Cell( name='c_l_CR_ABS_UPL_SAFT05')

c_l_CR_ABS_UPL_SAFT01.region = -cyl_CR_WR_IN                       # Absorber
c_l_CR_ABS_UPL_SAFT02.region = -cyl_CR_WR_OU  & +cyl_CR_WR_IN      # Absorber
c_l_CR_ABS_UPL_SAFT03.region = -cyl_CR_UPL_IN & +cyl_CR_WR_OU      # Absorber
c_l_CR_ABS_UPL_SAFT04.region =  hex_CR_UPL_OU & +cyl_CR_UPL_IN    # Upper plenum  
c_l_CR_ABS_UPL_SAFT05.region = ~hex_CR_UPL_OU                     # Upper plenum  

c_l_CR_ABS_UPL_SAFT01.fill = l_CR_SAFT
c_l_CR_ABS_UPL_SAFT02.fill = Ti316
c_l_CR_ABS_UPL_SAFT03.fill = Na_CR_Out
c_l_CR_ABS_UPL_SAFT04.fill = SS
c_l_CR_ABS_UPL_SAFT05.fill = Na_CR_In

u_CR_ABS_UPL_SAFT = openmc.Universe()
u_CR_ABS_UPL_SAFT.add_cells([
c_l_CR_ABS_UPL_SAFT01,
c_l_CR_ABS_UPL_SAFT02,
c_l_CR_ABS_UPL_SAFT03,
c_l_CR_ABS_UPL_SAFT04,
c_l_CR_ABS_UPL_SAFT05
])

# --- LCO+UPL
c_l_CR_LCO_UPL_SAFT01 = openmc.Cell( name='c_l_CR_LCO_UPL_SAFT01')
c_l_CR_LCO_UPL_SAFT02 = openmc.Cell( name='c_l_CR_LCO_UPL_SAFT02')
c_l_CR_LCO_UPL_SAFT03 = openmc.Cell( name='c_l_CR_LCO_UPL_SAFT03')
c_l_CR_LCO_UPL_SAFT04 = openmc.Cell( name='c_l_CR_LCO_UPL_SAFT04')

c_l_CR_LCO_UPL_SAFT01.region = -cyl_CR_CON_OU                      # Lower connector
c_l_CR_LCO_UPL_SAFT02.region = -cyl_CR_UPL_IN & +cyl_CR_CON_OU     # Lower connector
c_l_CR_LCO_UPL_SAFT03.region =  hex_CR_UPL_OU & +cyl_CR_UPL_IN  # Upper plenum  
c_l_CR_LCO_UPL_SAFT04.region = ~hex_CR_UPL_OU                   # Upper plenum  

c_l_CR_LCO_UPL_SAFT01.fill = HOMOG_CR_CON
c_l_CR_LCO_UPL_SAFT02.fill = Na_CR_In
c_l_CR_LCO_UPL_SAFT03.fill = SS
c_l_CR_LCO_UPL_SAFT04.fill = Na_CR_In

u_CR_LCO_UPL_SAFT = openmc.Universe()
u_CR_LCO_UPL_SAFT.add_cells([
c_l_CR_LCO_UPL_SAFT01,
c_l_CR_LCO_UPL_SAFT02,
c_l_CR_LCO_UPL_SAFT03,
c_l_CR_LCO_UPL_SAFT04 
])

# --- LCO+WRA
c_l_CR_LCO_WRA_SAFT01 = openmc.Cell( name='c_l_CR_LCO_WRA_SAFT01')
c_l_CR_LCO_WRA_SAFT02 = openmc.Cell( name='c_l_CR_LCO_WRA_SAFT02')
c_l_CR_LCO_WRA_SAFT03 = openmc.Cell( name='c_l_CR_LCO_WRA_SAFT03')
c_l_CR_LCO_WRA_SAFT04 = openmc.Cell( name='c_l_CR_LCO_WRA_SAFT04')

c_l_CR_LCO_WRA_SAFT01.region = -cyl_CR_CON_OU                      # Lower connector
c_l_CR_LCO_WRA_SAFT02.region =  hex_WR_IN     & +cyl_CR_CON_OU     # Lower connector
c_l_CR_LCO_WRA_SAFT03.region =  hex_WR_OU     & ~hex_WR_IN  # Normal wrapper
c_l_CR_LCO_WRA_SAFT04.region = ~hex_WR_OU                   # Normal wrapper

c_l_CR_LCO_WRA_SAFT01.fill = HOMOG_CR_CON
c_l_CR_LCO_WRA_SAFT02.fill = Na_CR_In
c_l_CR_LCO_WRA_SAFT03.fill = SS
c_l_CR_LCO_WRA_SAFT04.fill = Na_CR_In

u_CR_LCO_WRA_SAFT = openmc.Universe()
u_CR_LCO_WRA_SAFT.add_cells([
c_l_CR_LCO_WRA_SAFT01,
c_l_CR_LCO_WRA_SAFT02,
c_l_CR_LCO_WRA_SAFT03,
c_l_CR_LCO_WRA_SAFT04 
])

# --- BAF+WRA
c_l_CR_BAF_WRA_SAFT01 = openmc.Cell( name='c_l_CR_BAF_WRA_SAFT01')
c_l_CR_BAF_WRA_SAFT02 = openmc.Cell( name='c_l_CR_BAF_WRA_SAFT02')
c_l_CR_BAF_WRA_SAFT03 = openmc.Cell( name='c_l_CR_BAF_WRA_SAFT03')
c_l_CR_BAF_WRA_SAFT04 = openmc.Cell( name='c_l_CR_BAF_WRA_SAFT04')
c_l_CR_BAF_WRA_SAFT05 = openmc.Cell( name='c_l_CR_BAF_WRA_SAFT05')

c_l_CR_BAF_WRA_SAFT01.region =                  -cyl_CR_BAF_IN    # Baffle
c_l_CR_BAF_WRA_SAFT02.region = +cyl_CR_BAF_IN & -cyl_CR_BAF_OU    # Baffle
c_l_CR_BAF_WRA_SAFT03.region =  hex_WR_IN     & +cyl_CR_BAF_OU    # Baffle
c_l_CR_BAF_WRA_SAFT04.region =  hex_WR_OU     & ~hex_WR_IN  # Normal wrapper 
c_l_CR_BAF_WRA_SAFT05.region = ~hex_WR_OU                   # Normal wrapper 

c_l_CR_BAF_WRA_SAFT01.fill = Na_CR_In
c_l_CR_BAF_WRA_SAFT02.fill = Ti316   
c_l_CR_BAF_WRA_SAFT03.fill = Na_CR_In
c_l_CR_BAF_WRA_SAFT04.fill = SS
c_l_CR_BAF_WRA_SAFT05.fill = Na_CR_In

u_CR_BAF_WRA_SAFT = openmc.Universe()
u_CR_BAF_WRA_SAFT.add_cells([
c_l_CR_BAF_WRA_SAFT01,
c_l_CR_BAF_WRA_SAFT02,
c_l_CR_BAF_WRA_SAFT03,
c_l_CR_BAF_WRA_SAFT04,
c_l_CR_BAF_WRA_SAFT05
])

# --- BOT+WRA

c_l_CR_BOT_WRA_SAFT01 = openmc.Cell( name='c_l_CR_BOT_WRA_SAFT01')
c_l_CR_BOT_WRA_SAFT02 = openmc.Cell( name='c_l_CR_BOT_WRA_SAFT02')
c_l_CR_BOT_WRA_SAFT03 = openmc.Cell( name='c_l_CR_BOT_WRA_SAFT03')

c_l_CR_BOT_WRA_SAFT01.region =  hex_WR_IN                   # Normal wrapper 
c_l_CR_BOT_WRA_SAFT02.region =  hex_WR_OU     & ~hex_WR_IN  # Normal wrapper
c_l_CR_BOT_WRA_SAFT03.region = ~hex_WR_OU                   # Normal wrapper

c_l_CR_BOT_WRA_SAFT01.fill = Na_CR_In
c_l_CR_BOT_WRA_SAFT02.fill = SS
c_l_CR_BOT_WRA_SAFT03.fill = Na_CR_In


u_CR_BOT_WRA_SAFT = openmc.Universe()
u_CR_BOT_WRA_SAFT.add_cells([
c_l_CR_BOT_WRA_SAFT01,
c_l_CR_BOT_WRA_SAFT02,
c_l_CR_BOT_WRA_SAFT03
])


## Regulating Rod 1
# --- Shaft+HEA
c_l_CR1_SHA_HEA_BNAT01 = openmc.Cell( name='c_l_CR1_SHA_HEA_BNAT01')
c_l_CR1_SHA_HEA_BNAT02 = openmc.Cell( name='c_l_CR1_SHA_HEA_BNAT02')
c_l_CR1_SHA_HEA_BNAT03 = openmc.Cell( name='c_l_CR1_SHA_HEA_BNAT03')
c_l_CR1_SHA_HEA_BNAT04 = openmc.Cell( name='c_l_CR1_SHA_HEA_BNAT04')

c_l_CR1_SHA_HEA_BNAT01.region = -cyl_CR_SHAFT_IN                  # Shaft in 
c_l_CR1_SHA_HEA_BNAT02.region = -cyl_CR_HEA_IN & +cyl_CR_SHAFT_IN # Shaft out
c_l_CR1_SHA_HEA_BNAT03.region = -cyl_CR_HEA_OU & +cyl_CR_HEA_IN      # Head connector +gripper
c_l_CR1_SHA_HEA_BNAT04.region = +cyl_CR_HEA_OU                       # Head connector +gripper

c_l_CR1_SHA_HEA_BNAT01.fill = Ti316
c_l_CR1_SHA_HEA_BNAT02.fill = Na_CR_Out
c_l_CR1_SHA_HEA_BNAT03.fill = SS
c_l_CR1_SHA_HEA_BNAT04.fill = Na_CR_In

u_CR_SHA_HEA_REGL1 = openmc.Universe()
u_CR_SHA_HEA_REGL1.add_cells([
c_l_CR1_SHA_HEA_BNAT01, 
c_l_CR1_SHA_HEA_BNAT02,
c_l_CR1_SHA_HEA_BNAT03,
c_l_CR1_SHA_HEA_BNAT04
])

# --- Shaft+HCO
c_l_CR1_SHA_HCO_BNAT01 = openmc.Cell( name='c_l_CR1_SHA_HCO_BNAT01')
c_l_CR1_SHA_HCO_BNAT02 = openmc.Cell( name='c_l_CR1_SHA_HCO_BNAT02')
c_l_CR1_SHA_HCO_BNAT03 = openmc.Cell( name='c_l_CR1_SHA_HCO_BNAT03')
c_l_CR1_SHA_HCO_BNAT04 = openmc.Cell( name='c_l_CR1_SHA_HCO_BNAT04')

c_l_CR1_SHA_HCO_BNAT01.region = -cyl_CR_SHAFT_IN                   # Shaft in 
c_l_CR1_SHA_HCO_BNAT02.region = -cyl_CR_HCO_IN & +cyl_CR_SHAFT_IN  # Shaft out
c_l_CR1_SHA_HCO_BNAT03.region = -cyl_CR_HCO_OU & +cyl_CR_HCO_IN    # Head connector
c_l_CR1_SHA_HCO_BNAT04.region = +cyl_CR_HCO_OU                     # Head connector

c_l_CR1_SHA_HCO_BNAT01.fill = Ti316
c_l_CR1_SHA_HCO_BNAT02.fill = Na_CR_Out
c_l_CR1_SHA_HCO_BNAT03.fill = SS
c_l_CR1_SHA_HCO_BNAT04.fill = Na_CR_In

u_CR_SHA_HCO_REGL1 = openmc.Universe()
u_CR_SHA_HCO_REGL1.add_cells([
c_l_CR1_SHA_HCO_BNAT01, 
c_l_CR1_SHA_HCO_BNAT02,
c_l_CR1_SHA_HCO_BNAT03,
c_l_CR1_SHA_HCO_BNAT04
])

# --- Shaft+TRS
c_l_CR1_SHA_TRS_BNAT01 = openmc.Cell( name='c_l_CR1_SHA_TRS_BNAT01')
c_l_CR1_SHA_TRS_BNAT02 = openmc.Cell( name='c_l_CR1_SHA_TRS_BNAT02')
c_l_CR1_SHA_TRS_BNAT03 = openmc.Cell( name='c_l_CR1_SHA_TRS_BNAT03')
c_l_CR1_SHA_TRS_BNAT04 = openmc.Cell( name='c_l_CR1_SHA_TRS_BNAT04')

c_l_CR1_SHA_TRS_BNAT01.region = -cyl_CR_SHAFT_IN                   # Shaft in 
c_l_CR1_SHA_TRS_BNAT02.region = -cone_CR_PH_IN & +cyl_CR_SHAFT_IN  # Shaft out
c_l_CR1_SHA_TRS_BNAT03.region = -cone_CR_PH_OU & +cone_CR_PH_IN    # Transition
c_l_CR1_SHA_TRS_BNAT04.region = +cone_CR_PH_OU                     # Transition

c_l_CR1_SHA_TRS_BNAT01.fill = Ti316
c_l_CR1_SHA_TRS_BNAT02.fill = Na_CR_Out
c_l_CR1_SHA_TRS_BNAT03.fill = SS
c_l_CR1_SHA_TRS_BNAT04.fill = Na_CR_In

u_CR_SHA_TRS_REGL1 = openmc.Universe()
u_CR_SHA_TRS_REGL1.add_cells([
c_l_CR1_SHA_TRS_BNAT01, 
c_l_CR1_SHA_TRS_BNAT02,
c_l_CR1_SHA_TRS_BNAT03,
c_l_CR1_SHA_TRS_BNAT04
])

# --- Shaft+UPL
c_l_CR1_SHA_UPL_BNAT01 = openmc.Cell( name='c_l_CR1_SHA_UPL_BNAT01')
c_l_CR1_SHA_UPL_BNAT02 = openmc.Cell( name='c_l_CR1_SHA_UPL_BNAT02')
c_l_CR1_SHA_UPL_BNAT03 = openmc.Cell( name='c_l_CR1_SHA_UPL_BNAT03')
c_l_CR1_SHA_UPL_BNAT04 = openmc.Cell( name='c_l_CR1_SHA_UPL_BNAT04')

c_l_CR1_SHA_UPL_BNAT01.region = -cyl_CR_SHAFT_IN                   # Shaft in 
c_l_CR1_SHA_UPL_BNAT02.region = -cyl_CR_UPL_IN & +cyl_CR_SHAFT_IN  # Shaft out
c_l_CR1_SHA_UPL_BNAT03.region =  hex_CR_UPL_OU & +cyl_CR_UPL_IN    # Upper plenum
c_l_CR1_SHA_UPL_BNAT04.region = ~hex_CR_UPL_OU                     # Upper plenum

c_l_CR1_SHA_UPL_BNAT01.fill = Ti316
c_l_CR1_SHA_UPL_BNAT02.fill = Na_CR_Out
c_l_CR1_SHA_UPL_BNAT03.fill = SS
c_l_CR1_SHA_UPL_BNAT04.fill = Na_CR_In

u_CR_SHA_UPL_REGL1 = openmc.Universe()
u_CR_SHA_UPL_REGL1.add_cells([
c_l_CR1_SHA_UPL_BNAT01, 
c_l_CR1_SHA_UPL_BNAT02,
c_l_CR1_SHA_UPL_BNAT03,
c_l_CR1_SHA_UPL_BNAT04
])


# --- UCO+UPL
c_l_CR1_UCO_UPL_BNAT01 = openmc.Cell( name='c_l_CR1_UCO_UPL_BNAT01')
c_l_CR1_UCO_UPL_BNAT02 = openmc.Cell( name='c_l_CR1_UCO_UPL_BNAT02')
c_l_CR1_UCO_UPL_BNAT03 = openmc.Cell( name='c_l_CR1_UCO_UPL_BNAT03')
c_l_CR1_UCO_UPL_BNAT04 = openmc.Cell( name='c_l_CR1_UCO_UPL_BNAT04')

c_l_CR1_UCO_UPL_BNAT01.region = -cyl_CR_CON_OU                      # Upper connector
c_l_CR1_UCO_UPL_BNAT02.region = +cyl_CR_CON_OU & -cyl_CR_UPL_IN     # Upper connector
c_l_CR1_UCO_UPL_BNAT03.region =  hex_CR_UPL_OU & +cyl_CR_UPL_IN     # Upper plenum   
c_l_CR1_UCO_UPL_BNAT04.region = ~hex_CR_UPL_OU                      # Upper plenum

c_l_CR1_UCO_UPL_BNAT01.fill = HOMOG_CR_CON
c_l_CR1_UCO_UPL_BNAT02.fill = Na_CR_Out
c_l_CR1_UCO_UPL_BNAT03.fill = SS
c_l_CR1_UCO_UPL_BNAT04.fill = Na_CR_In

u_CR_UCO_UPL_REGL1 = openmc.Universe()
u_CR_UCO_UPL_REGL1.add_cells([
c_l_CR1_UCO_UPL_BNAT01,
c_l_CR1_UCO_UPL_BNAT02,
c_l_CR1_UCO_UPL_BNAT03,
c_l_CR1_UCO_UPL_BNAT04 
])


# --- PLE+UPL
c_l_CR1_PLE_UPL_BNAT01 = openmc.Cell( name='c_l_CR1_PLE_UPL_BNAT01')
c_l_CR1_PLE_UPL_BNAT02 = openmc.Cell( name='c_l_CR1_PLE_UPL_BNAT02')
c_l_CR1_PLE_UPL_BNAT03 = openmc.Cell( name='c_l_CR1_PLE_UPL_BNAT03')
c_l_CR1_PLE_UPL_BNAT04 = openmc.Cell( name='c_l_CR1_PLE_UPL_BNAT04')
c_l_CR1_PLE_UPL_BNAT05 = openmc.Cell( name='c_l_CR1_PLE_UPL_BNAT05')

c_l_CR1_PLE_UPL_BNAT01.region = -cyl_CR_WR_IN                    # Plenum
c_l_CR1_PLE_UPL_BNAT02.region = -cyl_CR_WR_OU  & +cyl_CR_WR_IN   # Plenum
c_l_CR1_PLE_UPL_BNAT03.region = -cyl_CR_UPL_IN & +cyl_CR_WR_OU   # Plenum
c_l_CR1_PLE_UPL_BNAT04.region =  hex_CR_UPL_OU & +cyl_CR_UPL_IN  # Upper plenum  
c_l_CR1_PLE_UPL_BNAT05.region = ~hex_CR_UPL_OU                   # Upper plenum  

c_l_CR1_PLE_UPL_BNAT01.fill = Na_CR_Out
c_l_CR1_PLE_UPL_BNAT02.fill = Ti316
c_l_CR1_PLE_UPL_BNAT03.fill = Na_CR_Out
c_l_CR1_PLE_UPL_BNAT04.fill = SS
c_l_CR1_PLE_UPL_BNAT05.fill = Na_CR_In

u_CR_PLE_UPL_REGL1 = openmc.Universe()
u_CR_PLE_UPL_REGL1.add_cells([
c_l_CR1_PLE_UPL_BNAT01,
c_l_CR1_PLE_UPL_BNAT02,
c_l_CR1_PLE_UPL_BNAT03,
c_l_CR1_PLE_UPL_BNAT04,
c_l_CR1_PLE_UPL_BNAT05 
])

# --- ABS+UPL,  Natural B4C - regulating rod 1 (u_CR_move_REGL1)
l_CR_BNAT1 = openmc.HexLattice()
l_CR_BNAT1.center = [0., 0.]
l_CR_BNAT1.pitch  = [1.5500]
l_CR_BNAT1.universes = \
       [ [p_CR2_BNAT]*6, [p_CR1_BNAT] ]
l_CR_BNAT1.outer  = p_CR2_NaOU
l_CR_BNAT1.rotation = [0, 0,-30]

c_l_CR1_ABS_UPL_BNAT01 = openmc.Cell( name='c_l_CR1_ABS_UPL_BNAT01')
c_l_CR1_ABS_UPL_BNAT02 = openmc.Cell( name='c_l_CR1_ABS_UPL_BNAT02')
c_l_CR1_ABS_UPL_BNAT03 = openmc.Cell( name='c_l_CR1_ABS_UPL_BNAT03')
c_l_CR1_ABS_UPL_BNAT04 = openmc.Cell( name='c_l_CR1_ABS_UPL_BNAT04')
c_l_CR1_ABS_UPL_BNAT05 = openmc.Cell( name='c_l_CR1_ABS_UPL_BNAT05')

c_l_CR1_ABS_UPL_BNAT01.region = -cyl_CR_WR_IN                       # Absorber
c_l_CR1_ABS_UPL_BNAT02.region = -cyl_CR_WR_OU  & +cyl_CR_WR_IN      # Absorber
c_l_CR1_ABS_UPL_BNAT03.region = -cyl_CR_UPL_IN & +cyl_CR_WR_OU      # Absorber
c_l_CR1_ABS_UPL_BNAT04.region =  hex_CR_UPL_OU & +cyl_CR_UPL_IN    # Upper plenum  
c_l_CR1_ABS_UPL_BNAT05.region = ~hex_CR_UPL_OU                     # Upper plenum  

c_l_CR1_ABS_UPL_BNAT01.fill = l_CR_BNAT1
c_l_CR1_ABS_UPL_BNAT02.fill = Ti316
c_l_CR1_ABS_UPL_BNAT03.fill = Na_CR_Out
c_l_CR1_ABS_UPL_BNAT04.fill = SS
c_l_CR1_ABS_UPL_BNAT05.fill = Na_CR_In

u_CR_ABS_UPL_REGL1 = openmc.Universe()
u_CR_ABS_UPL_REGL1.add_cells([
c_l_CR1_ABS_UPL_BNAT01,
c_l_CR1_ABS_UPL_BNAT02,
c_l_CR1_ABS_UPL_BNAT03,
c_l_CR1_ABS_UPL_BNAT04,
c_l_CR1_ABS_UPL_BNAT05
])

# --- LCO+UPL
c_l_CR1_LCO_UPL_BNAT01 = openmc.Cell( name='c_l_CR1_LCO_UPL_BNAT01')
c_l_CR1_LCO_UPL_BNAT02 = openmc.Cell( name='c_l_CR1_LCO_UPL_BNAT02')
c_l_CR1_LCO_UPL_BNAT03 = openmc.Cell( name='c_l_CR1_LCO_UPL_BNAT03')
c_l_CR1_LCO_UPL_BNAT04 = openmc.Cell( name='c_l_CR1_LCO_UPL_BNAT04')

c_l_CR1_LCO_UPL_BNAT01.region = -cyl_CR_CON_OU                      # Lower connector
c_l_CR1_LCO_UPL_BNAT02.region = -cyl_CR_UPL_IN & +cyl_CR_CON_OU     # Lower connector
c_l_CR1_LCO_UPL_BNAT03.region =  hex_CR_UPL_OU & +cyl_CR_UPL_IN  # Upper plenum  
c_l_CR1_LCO_UPL_BNAT04.region = ~hex_CR_UPL_OU                   # Upper plenum  

c_l_CR1_LCO_UPL_BNAT01.fill = HOMOG_CR_CON
c_l_CR1_LCO_UPL_BNAT02.fill = Na_CR_In
c_l_CR1_LCO_UPL_BNAT03.fill = SS
c_l_CR1_LCO_UPL_BNAT04.fill = Na_CR_In

u_CR_LCO_UPL_REGL1 = openmc.Universe()
u_CR_LCO_UPL_REGL1.add_cells([
c_l_CR1_LCO_UPL_BNAT01,
c_l_CR1_LCO_UPL_BNAT02,
c_l_CR1_LCO_UPL_BNAT03,
c_l_CR1_LCO_UPL_BNAT04 
])

# --- LCO+WRA
c_l_CR1_LCO_WRA_BNAT01 = openmc.Cell( name='c_l_CR1_LCO_WRA_BNAT01')
c_l_CR1_LCO_WRA_BNAT02 = openmc.Cell( name='c_l_CR1_LCO_WRA_BNAT02')
c_l_CR1_LCO_WRA_BNAT03 = openmc.Cell( name='c_l_CR1_LCO_WRA_BNAT03')
c_l_CR1_LCO_WRA_BNAT04 = openmc.Cell( name='c_l_CR1_LCO_WRA_BNAT04')

c_l_CR1_LCO_WRA_BNAT01.region = -cyl_CR_CON_OU                      # Lower connector
c_l_CR1_LCO_WRA_BNAT02.region =  hex_WR_IN     & +cyl_CR_CON_OU     # Lower connector
c_l_CR1_LCO_WRA_BNAT03.region =  hex_WR_OU     & ~hex_WR_IN  # Normal wrapper
c_l_CR1_LCO_WRA_BNAT04.region = ~hex_WR_OU                   # Normal wrapper

c_l_CR1_LCO_WRA_BNAT01.fill = HOMOG_CR_CON
c_l_CR1_LCO_WRA_BNAT02.fill = Na_CR_In
c_l_CR1_LCO_WRA_BNAT03.fill = SS
c_l_CR1_LCO_WRA_BNAT04.fill = Na_CR_In

u_CR_LCO_WRA_REGL1 = openmc.Universe()
u_CR_LCO_WRA_REGL1.add_cells([
c_l_CR1_LCO_WRA_BNAT01,
c_l_CR1_LCO_WRA_BNAT02,
c_l_CR1_LCO_WRA_BNAT03,
c_l_CR1_LCO_WRA_BNAT04 
])

# --- BAF+WRA
c_l_CR1_BAF_WRA_BNAT01 = openmc.Cell( name='c_l_CR1_BAF_WRA_BNAT01')
c_l_CR1_BAF_WRA_BNAT02 = openmc.Cell( name='c_l_CR1_BAF_WRA_BNAT02')
c_l_CR1_BAF_WRA_BNAT03 = openmc.Cell( name='c_l_CR1_BAF_WRA_BNAT03')
c_l_CR1_BAF_WRA_BNAT04 = openmc.Cell( name='c_l_CR1_BAF_WRA_BNAT04')
c_l_CR1_BAF_WRA_BNAT05 = openmc.Cell( name='c_l_CR1_BAF_WRA_BNAT05')

c_l_CR1_BAF_WRA_BNAT01.region =                  -cyl_CR_BAF_IN    # Baffle
c_l_CR1_BAF_WRA_BNAT02.region = +cyl_CR_BAF_IN & -cyl_CR_BAF_OU    # Baffle
c_l_CR1_BAF_WRA_BNAT03.region =  hex_WR_IN     & +cyl_CR_BAF_OU    # Baffle
c_l_CR1_BAF_WRA_BNAT04.region =  hex_WR_OU     & ~hex_WR_IN  # Normal wrapper 
c_l_CR1_BAF_WRA_BNAT05.region = ~hex_WR_OU                   # Normal wrapper 

c_l_CR1_BAF_WRA_BNAT01.fill = Na_CR_In
c_l_CR1_BAF_WRA_BNAT02.fill = Ti316   
c_l_CR1_BAF_WRA_BNAT03.fill = Na_CR_In
c_l_CR1_BAF_WRA_BNAT04.fill = SS
c_l_CR1_BAF_WRA_BNAT05.fill = Na_CR_In

u_CR_BAF_WRA_REGL1 = openmc.Universe()
u_CR_BAF_WRA_REGL1.add_cells([
c_l_CR1_BAF_WRA_BNAT01,
c_l_CR1_BAF_WRA_BNAT02,
c_l_CR1_BAF_WRA_BNAT03,
c_l_CR1_BAF_WRA_BNAT04,
c_l_CR1_BAF_WRA_BNAT05
])

# --- BOT+WRA

c_l_CR1_BOT_WRA_BNAT01 = openmc.Cell( name='c_l_CR1_BOT_WRA_BNAT01')
c_l_CR1_BOT_WRA_BNAT02 = openmc.Cell( name='c_l_CR1_BOT_WRA_BNAT02')
c_l_CR1_BOT_WRA_BNAT03 = openmc.Cell( name='c_l_CR1_BOT_WRA_BNAT03')

c_l_CR1_BOT_WRA_BNAT01.region =  hex_WR_IN                   # Normal wrapper 
c_l_CR1_BOT_WRA_BNAT02.region =  hex_WR_OU     & ~hex_WR_IN  # Normal wrapper
c_l_CR1_BOT_WRA_BNAT03.region = ~hex_WR_OU                   # Normal wrapper

c_l_CR1_BOT_WRA_BNAT01.fill = Na_CR_In
c_l_CR1_BOT_WRA_BNAT02.fill = SS
c_l_CR1_BOT_WRA_BNAT03.fill = Na_CR_In


u_CR_BOT_WRA_REGL1 = openmc.Universe()
u_CR_BOT_WRA_REGL1.add_cells([
c_l_CR1_BOT_WRA_BNAT01,
c_l_CR1_BOT_WRA_BNAT02,
c_l_CR1_BOT_WRA_BNAT03
])



## Regulating Rod 2
# --- Shaft+HEA
c_l_CR2_SHA_HEA_BNAT01 = openmc.Cell( name='c_l_CR2_SHA_HEA_BNAT01')
c_l_CR2_SHA_HEA_BNAT02 = openmc.Cell( name='c_l_CR2_SHA_HEA_BNAT02')
c_l_CR2_SHA_HEA_BNAT03 = openmc.Cell( name='c_l_CR2_SHA_HEA_BNAT03')
c_l_CR2_SHA_HEA_BNAT04 = openmc.Cell( name='c_l_CR2_SHA_HEA_BNAT04')

c_l_CR2_SHA_HEA_BNAT01.region = -cyl_CR_SHAFT_IN                  # Shaft in 
c_l_CR2_SHA_HEA_BNAT02.region = -cyl_CR_HEA_IN & +cyl_CR_SHAFT_IN # Shaft out
c_l_CR2_SHA_HEA_BNAT03.region = -cyl_CR_HEA_OU & +cyl_CR_HEA_IN      # Head connector +gripper
c_l_CR2_SHA_HEA_BNAT04.region = +cyl_CR_HEA_OU                       # Head connector +gripper

c_l_CR2_SHA_HEA_BNAT01.fill = Ti316
c_l_CR2_SHA_HEA_BNAT02.fill = Na_CR_Out
c_l_CR2_SHA_HEA_BNAT03.fill = SS
c_l_CR2_SHA_HEA_BNAT04.fill = Na_CR_In

u_CR_SHA_HEA_REGL2 = openmc.Universe()
u_CR_SHA_HEA_REGL2.add_cells([
c_l_CR2_SHA_HEA_BNAT01, 
c_l_CR2_SHA_HEA_BNAT02,
c_l_CR2_SHA_HEA_BNAT03,
c_l_CR2_SHA_HEA_BNAT04
])

# --- Shaft+HCO
c_l_CR2_SHA_HCO_BNAT01 = openmc.Cell( name='c_l_CR2_SHA_HCO_BNAT01')
c_l_CR2_SHA_HCO_BNAT02 = openmc.Cell( name='c_l_CR2_SHA_HCO_BNAT02')
c_l_CR2_SHA_HCO_BNAT03 = openmc.Cell( name='c_l_CR2_SHA_HCO_BNAT03')
c_l_CR2_SHA_HCO_BNAT04 = openmc.Cell( name='c_l_CR2_SHA_HCO_BNAT04')

c_l_CR2_SHA_HCO_BNAT01.region = -cyl_CR_SHAFT_IN                   # Shaft in 
c_l_CR2_SHA_HCO_BNAT02.region = -cyl_CR_HCO_IN & +cyl_CR_SHAFT_IN  # Shaft out
c_l_CR2_SHA_HCO_BNAT03.region = -cyl_CR_HCO_OU & +cyl_CR_HCO_IN    # Head connector
c_l_CR2_SHA_HCO_BNAT04.region = +cyl_CR_HCO_OU                     # Head connector

c_l_CR2_SHA_HCO_BNAT01.fill = Ti316
c_l_CR2_SHA_HCO_BNAT02.fill = Na_CR_Out
c_l_CR2_SHA_HCO_BNAT03.fill = SS
c_l_CR2_SHA_HCO_BNAT04.fill = Na_CR_In

u_CR_SHA_HCO_REGL2 = openmc.Universe()
u_CR_SHA_HCO_REGL2.add_cells([
c_l_CR2_SHA_HCO_BNAT01, 
c_l_CR2_SHA_HCO_BNAT02,
c_l_CR2_SHA_HCO_BNAT03,
c_l_CR2_SHA_HCO_BNAT04
])

# --- Shaft+TRS
c_l_CR2_SHA_TRS_BNAT01 = openmc.Cell( name='c_l_CR2_SHA_TRS_BNAT01')
c_l_CR2_SHA_TRS_BNAT02 = openmc.Cell( name='c_l_CR2_SHA_TRS_BNAT02')
c_l_CR2_SHA_TRS_BNAT03 = openmc.Cell( name='c_l_CR2_SHA_TRS_BNAT03')
c_l_CR2_SHA_TRS_BNAT04 = openmc.Cell( name='c_l_CR2_SHA_TRS_BNAT04')

c_l_CR2_SHA_TRS_BNAT01.region = -cyl_CR_SHAFT_IN                   # Shaft in 
c_l_CR2_SHA_TRS_BNAT02.region = -cone_CR_PH_IN & +cyl_CR_SHAFT_IN  # Shaft out
c_l_CR2_SHA_TRS_BNAT03.region = -cone_CR_PH_OU & +cone_CR_PH_IN    # Transition
c_l_CR2_SHA_TRS_BNAT04.region = +cone_CR_PH_OU                     # Transition

c_l_CR2_SHA_TRS_BNAT01.fill = Ti316
c_l_CR2_SHA_TRS_BNAT02.fill = Na_CR_Out
c_l_CR2_SHA_TRS_BNAT03.fill = SS
c_l_CR2_SHA_TRS_BNAT04.fill = Na_CR_In

u_CR_SHA_TRS_REGL2 = openmc.Universe()
u_CR_SHA_TRS_REGL2.add_cells([
c_l_CR2_SHA_TRS_BNAT01, 
c_l_CR2_SHA_TRS_BNAT02,
c_l_CR2_SHA_TRS_BNAT03,
c_l_CR2_SHA_TRS_BNAT04
])

# --- Shaft+UPL
c_l_CR2_SHA_UPL_BNAT01 = openmc.Cell( name='c_l_CR2_SHA_UPL_BNAT01')
c_l_CR2_SHA_UPL_BNAT02 = openmc.Cell( name='c_l_CR2_SHA_UPL_BNAT02')
c_l_CR2_SHA_UPL_BNAT03 = openmc.Cell( name='c_l_CR2_SHA_UPL_BNAT03')
c_l_CR2_SHA_UPL_BNAT04 = openmc.Cell( name='c_l_CR2_SHA_UPL_BNAT04')

c_l_CR2_SHA_UPL_BNAT01.region = -cyl_CR_SHAFT_IN                   # Shaft in 
c_l_CR2_SHA_UPL_BNAT02.region = -cyl_CR_UPL_IN & +cyl_CR_SHAFT_IN  # Shaft out
c_l_CR2_SHA_UPL_BNAT03.region =  hex_CR_UPL_OU & +cyl_CR_UPL_IN    # Upper plenum
c_l_CR2_SHA_UPL_BNAT04.region = ~hex_CR_UPL_OU                     # Upper plenum

c_l_CR2_SHA_UPL_BNAT01.fill = Ti316
c_l_CR2_SHA_UPL_BNAT02.fill = Na_CR_Out
c_l_CR2_SHA_UPL_BNAT03.fill = SS
c_l_CR2_SHA_UPL_BNAT04.fill = Na_CR_In

u_CR_SHA_UPL_REGL2 = openmc.Universe()
u_CR_SHA_UPL_REGL2.add_cells([
c_l_CR2_SHA_UPL_BNAT01, 
c_l_CR2_SHA_UPL_BNAT02,
c_l_CR2_SHA_UPL_BNAT03,
c_l_CR2_SHA_UPL_BNAT04
])


# --- UCO+UPL
c_l_CR2_UCO_UPL_BNAT01 = openmc.Cell( name='c_l_CR2_UCO_UPL_BNAT01')
c_l_CR2_UCO_UPL_BNAT02 = openmc.Cell( name='c_l_CR2_UCO_UPL_BNAT02')
c_l_CR2_UCO_UPL_BNAT03 = openmc.Cell( name='c_l_CR2_UCO_UPL_BNAT03')
c_l_CR2_UCO_UPL_BNAT04 = openmc.Cell( name='c_l_CR2_UCO_UPL_BNAT04')

c_l_CR2_UCO_UPL_BNAT01.region = -cyl_CR_CON_OU                      # Upper connector
c_l_CR2_UCO_UPL_BNAT02.region = +cyl_CR_CON_OU & -cyl_CR_UPL_IN     # Upper connector
c_l_CR2_UCO_UPL_BNAT03.region =  hex_CR_UPL_OU & +cyl_CR_UPL_IN     # Upper plenum   
c_l_CR2_UCO_UPL_BNAT04.region = ~hex_CR_UPL_OU                      # Upper plenum

c_l_CR2_UCO_UPL_BNAT01.fill = HOMOG_CR_CON
c_l_CR2_UCO_UPL_BNAT02.fill = Na_CR_Out
c_l_CR2_UCO_UPL_BNAT03.fill = SS
c_l_CR2_UCO_UPL_BNAT04.fill = Na_CR_In

u_CR_UCO_UPL_REGL2 = openmc.Universe()
u_CR_UCO_UPL_REGL2.add_cells([
c_l_CR2_UCO_UPL_BNAT01,
c_l_CR2_UCO_UPL_BNAT02,
c_l_CR2_UCO_UPL_BNAT03,
c_l_CR2_UCO_UPL_BNAT04 
])


# --- PLE+UPL
c_l_CR2_PLE_UPL_BNAT01 = openmc.Cell( name='c_l_CR2_PLE_UPL_BNAT01')
c_l_CR2_PLE_UPL_BNAT02 = openmc.Cell( name='c_l_CR2_PLE_UPL_BNAT02')
c_l_CR2_PLE_UPL_BNAT03 = openmc.Cell( name='c_l_CR2_PLE_UPL_BNAT03')
c_l_CR2_PLE_UPL_BNAT04 = openmc.Cell( name='c_l_CR2_PLE_UPL_BNAT04')
c_l_CR2_PLE_UPL_BNAT05 = openmc.Cell( name='c_l_CR2_PLE_UPL_BNAT05')

c_l_CR2_PLE_UPL_BNAT01.region = -cyl_CR_WR_IN                    # Plenum
c_l_CR2_PLE_UPL_BNAT02.region = -cyl_CR_WR_OU  & +cyl_CR_WR_IN   # Plenum
c_l_CR2_PLE_UPL_BNAT03.region = -cyl_CR_UPL_IN & +cyl_CR_WR_OU   # Plenum
c_l_CR2_PLE_UPL_BNAT04.region =  hex_CR_UPL_OU & +cyl_CR_UPL_IN  # Upper plenum  
c_l_CR2_PLE_UPL_BNAT05.region = ~hex_CR_UPL_OU                   # Upper plenum  

c_l_CR2_PLE_UPL_BNAT01.fill = Na_CR_Out
c_l_CR2_PLE_UPL_BNAT02.fill = Ti316
c_l_CR2_PLE_UPL_BNAT03.fill = Na_CR_Out
c_l_CR2_PLE_UPL_BNAT04.fill = SS
c_l_CR2_PLE_UPL_BNAT05.fill = Na_CR_In

u_CR_PLE_UPL_REGL2 = openmc.Universe()
u_CR_PLE_UPL_REGL2.add_cells([
c_l_CR2_PLE_UPL_BNAT01,
c_l_CR2_PLE_UPL_BNAT02,
c_l_CR2_PLE_UPL_BNAT03,
c_l_CR2_PLE_UPL_BNAT04,
c_l_CR2_PLE_UPL_BNAT05 
])

# --- ABS+UPL,  Natural B4C - regulating rod 2 (u_CR_move_REGL2)
l_CR_BNAT2 = openmc.HexLattice()
l_CR_BNAT2.center = [0., 0.]
l_CR_BNAT2.pitch  = [1.5500]
l_CR_BNAT2.universes = \
       [ [p_CR2_BNAT]*6, [p_CR1_BNAT] ]
l_CR_BNAT2.outer  = p_CR2_NaOU
l_CR_BNAT2.rotation = [0, 0,-30]

c_l_CR2_ABS_UPL_BNAT01 = openmc.Cell( name='c_l_CR2_ABS_UPL_BNAT01')
c_l_CR2_ABS_UPL_BNAT02 = openmc.Cell( name='c_l_CR2_ABS_UPL_BNAT02')
c_l_CR2_ABS_UPL_BNAT03 = openmc.Cell( name='c_l_CR2_ABS_UPL_BNAT03')
c_l_CR2_ABS_UPL_BNAT04 = openmc.Cell( name='c_l_CR2_ABS_UPL_BNAT04')
c_l_CR2_ABS_UPL_BNAT05 = openmc.Cell( name='c_l_CR2_ABS_UPL_BNAT05')

c_l_CR2_ABS_UPL_BNAT01.region = -cyl_CR_WR_IN                       # Absorber
c_l_CR2_ABS_UPL_BNAT02.region = -cyl_CR_WR_OU  & +cyl_CR_WR_IN      # Absorber
c_l_CR2_ABS_UPL_BNAT03.region = -cyl_CR_UPL_IN & +cyl_CR_WR_OU      # Absorber
c_l_CR2_ABS_UPL_BNAT04.region =  hex_CR_UPL_OU & +cyl_CR_UPL_IN    # Upper plenum  
c_l_CR2_ABS_UPL_BNAT05.region = ~hex_CR_UPL_OU                     # Upper plenum  

c_l_CR2_ABS_UPL_BNAT01.fill = l_CR_BNAT2
c_l_CR2_ABS_UPL_BNAT02.fill = Ti316
c_l_CR2_ABS_UPL_BNAT03.fill = Na_CR_Out
c_l_CR2_ABS_UPL_BNAT04.fill = SS
c_l_CR2_ABS_UPL_BNAT05.fill = Na_CR_In

u_CR_ABS_UPL_REGL2 = openmc.Universe()
u_CR_ABS_UPL_REGL2.add_cells([
c_l_CR2_ABS_UPL_BNAT01,
c_l_CR2_ABS_UPL_BNAT02,
c_l_CR2_ABS_UPL_BNAT03,
c_l_CR2_ABS_UPL_BNAT04,
c_l_CR2_ABS_UPL_BNAT05
])

# --- ABS+WRA,  Natural B4C - regulating rod 2 (u_CR_move_REGL2)

c_l_CR2_ABS_WRA_BNAT01 = openmc.Cell( name='c_l_CR2_ABS_WRA_BNAT01')
c_l_CR2_ABS_WRA_BNAT02 = openmc.Cell( name='c_l_CR2_ABS_WRA_BNAT02')
c_l_CR2_ABS_WRA_BNAT03 = openmc.Cell( name='c_l_CR2_ABS_WRA_BNAT03')
c_l_CR2_ABS_WRA_BNAT04 = openmc.Cell( name='c_l_CR2_ABS_WRA_BNAT04')
c_l_CR2_ABS_WRA_BNAT05 = openmc.Cell( name='c_l_CR2_ABS_WRA_BNAT05')

c_l_CR2_ABS_WRA_BNAT01.region = -cyl_CR_WR_IN                       # Absorber
c_l_CR2_ABS_WRA_BNAT02.region = -cyl_CR_WR_OU  & +cyl_CR_WR_IN      # Absorber
c_l_CR2_ABS_WRA_BNAT03.region =  hex_WR_IN     & +cyl_CR_WR_OU      # Absorber
c_l_CR2_ABS_WRA_BNAT04.region =  hex_WR_OU     & ~hex_WR_IN        # Upper plenum  
c_l_CR2_ABS_WRA_BNAT05.region = ~hex_WR_OU                         # Upper plenum  

c_l_CR2_ABS_WRA_BNAT01.fill = l_CR_BNAT2
c_l_CR2_ABS_WRA_BNAT02.fill = Ti316
c_l_CR2_ABS_WRA_BNAT03.fill = Na_CR_Out
c_l_CR2_ABS_WRA_BNAT04.fill = SS
c_l_CR2_ABS_WRA_BNAT05.fill = Na_CR_In

u_CR_ABS_WRA_REGL2 = openmc.Universe()
u_CR_ABS_WRA_REGL2.add_cells([
c_l_CR2_ABS_WRA_BNAT01,
c_l_CR2_ABS_WRA_BNAT02,
c_l_CR2_ABS_WRA_BNAT03,
c_l_CR2_ABS_WRA_BNAT04,
c_l_CR2_ABS_WRA_BNAT05
])

# --- LCO+WRA
c_l_CR2_LCO_WRA_BNAT01 = openmc.Cell( name='c_l_CR2_LCO_WRA_BNAT01')
c_l_CR2_LCO_WRA_BNAT02 = openmc.Cell( name='c_l_CR2_LCO_WRA_BNAT02')
c_l_CR2_LCO_WRA_BNAT03 = openmc.Cell( name='c_l_CR2_LCO_WRA_BNAT03')
c_l_CR2_LCO_WRA_BNAT04 = openmc.Cell( name='c_l_CR2_LCO_WRA_BNAT04')

c_l_CR2_LCO_WRA_BNAT01.region = -cyl_CR_CON_OU                      # Lower connector
c_l_CR2_LCO_WRA_BNAT02.region =  hex_WR_IN     & +cyl_CR_CON_OU     # Lower connector
c_l_CR2_LCO_WRA_BNAT03.region =  hex_WR_OU     & ~hex_WR_IN  # Normal wrapper
c_l_CR2_LCO_WRA_BNAT04.region = ~hex_WR_OU                   # Normal wrapper

c_l_CR2_LCO_WRA_BNAT01.fill = HOMOG_CR_CON
c_l_CR2_LCO_WRA_BNAT02.fill = Na_CR_In
c_l_CR2_LCO_WRA_BNAT03.fill = SS
c_l_CR2_LCO_WRA_BNAT04.fill = Na_CR_In

u_CR_LCO_WRA_REGL2 = openmc.Universe()
u_CR_LCO_WRA_REGL2.add_cells([
c_l_CR2_LCO_WRA_BNAT01,
c_l_CR2_LCO_WRA_BNAT02,
c_l_CR2_LCO_WRA_BNAT03,
c_l_CR2_LCO_WRA_BNAT04 
])

# --- BAF+WRA
c_l_CR2_BAF_WRA_BNAT01 = openmc.Cell( name='c_l_CR2_BAF_WRA_BNAT01')
c_l_CR2_BAF_WRA_BNAT02 = openmc.Cell( name='c_l_CR2_BAF_WRA_BNAT02')
c_l_CR2_BAF_WRA_BNAT03 = openmc.Cell( name='c_l_CR2_BAF_WRA_BNAT03')
c_l_CR2_BAF_WRA_BNAT04 = openmc.Cell( name='c_l_CR2_BAF_WRA_BNAT04')
c_l_CR2_BAF_WRA_BNAT05 = openmc.Cell( name='c_l_CR2_BAF_WRA_BNAT05')

c_l_CR2_BAF_WRA_BNAT01.region =                  -cyl_CR_BAF_IN    # Baffle
c_l_CR2_BAF_WRA_BNAT02.region = +cyl_CR_BAF_IN & -cyl_CR_BAF_OU    # Baffle
c_l_CR2_BAF_WRA_BNAT03.region =  hex_WR_IN     & +cyl_CR_BAF_OU    # Baffle
c_l_CR2_BAF_WRA_BNAT04.region =  hex_WR_OU     & ~hex_WR_IN  # Normal wrapper 
c_l_CR2_BAF_WRA_BNAT05.region = ~hex_WR_OU                   # Normal wrapper 

c_l_CR2_BAF_WRA_BNAT01.fill = Na_CR_In
c_l_CR2_BAF_WRA_BNAT02.fill = Ti316   
c_l_CR2_BAF_WRA_BNAT03.fill = Na_CR_In
c_l_CR2_BAF_WRA_BNAT04.fill = SS
c_l_CR2_BAF_WRA_BNAT05.fill = Na_CR_In

u_CR_BAF_WRA_REGL2 = openmc.Universe()
u_CR_BAF_WRA_REGL2.add_cells([
c_l_CR2_BAF_WRA_BNAT01,
c_l_CR2_BAF_WRA_BNAT02,
c_l_CR2_BAF_WRA_BNAT03,
c_l_CR2_BAF_WRA_BNAT04,
c_l_CR2_BAF_WRA_BNAT05
])

# --- BOT+WRA

c_l_CR2_BOT_WRA_BNAT01 = openmc.Cell( name='c_l_CR2_BOT_WRA_BNAT01')
c_l_CR2_BOT_WRA_BNAT02 = openmc.Cell( name='c_l_CR2_BOT_WRA_BNAT02')
c_l_CR2_BOT_WRA_BNAT03 = openmc.Cell( name='c_l_CR2_BOT_WRA_BNAT03')

c_l_CR2_BOT_WRA_BNAT01.region =  hex_WR_IN                   # Normal wrapper 
c_l_CR2_BOT_WRA_BNAT02.region =  hex_WR_OU     & ~hex_WR_IN  # Normal wrapper
c_l_CR2_BOT_WRA_BNAT03.region = ~hex_WR_OU                   # Normal wrapper

c_l_CR2_BOT_WRA_BNAT01.fill = Na_CR_In
c_l_CR2_BOT_WRA_BNAT02.fill = SS
c_l_CR2_BOT_WRA_BNAT03.fill = Na_CR_In


u_CR_BOT_WRA_REGL2 = openmc.Universe()
u_CR_BOT_WRA_REGL2.add_cells([
c_l_CR2_BOT_WRA_BNAT01,
c_l_CR2_BOT_WRA_BNAT02,
c_l_CR2_BOT_WRA_BNAT03
])



## Shim Rods 
# --- Shaft+HEA
c_l_CR_SHA_HEA_SHIM01 = openmc.Cell( name='c_l_CR_SHA_HEA_SHIM01')
c_l_CR_SHA_HEA_SHIM02 = openmc.Cell( name='c_l_CR_SHA_HEA_SHIM02')
c_l_CR_SHA_HEA_SHIM03 = openmc.Cell( name='c_l_CR_SHA_HEA_SHIM03')
c_l_CR_SHA_HEA_SHIM04 = openmc.Cell( name='c_l_CR_SHA_HEA_SHIM04')

c_l_CR_SHA_HEA_SHIM01.region = -cyl_CR_SHAFT_IN                  # Shaft in 
c_l_CR_SHA_HEA_SHIM02.region = -cyl_CR_HEA_IN & +cyl_CR_SHAFT_IN # Shaft out
c_l_CR_SHA_HEA_SHIM03.region = -cyl_CR_HEA_OU & +cyl_CR_HEA_IN      # Head connector +gripper
c_l_CR_SHA_HEA_SHIM04.region = +cyl_CR_HEA_OU                       # Head connector +gripper

c_l_CR_SHA_HEA_SHIM01.fill = Ti316
c_l_CR_SHA_HEA_SHIM02.fill = Na_CR_Out
c_l_CR_SHA_HEA_SHIM03.fill = SS
c_l_CR_SHA_HEA_SHIM04.fill = Na_CR_In

u_CR_SHA_HEA_SHIM = openmc.Universe()
u_CR_SHA_HEA_SHIM.add_cells([
c_l_CR_SHA_HEA_SHIM01, 
c_l_CR_SHA_HEA_SHIM02,
c_l_CR_SHA_HEA_SHIM03,
c_l_CR_SHA_HEA_SHIM04
])

# --- Shaft+HCO
c_l_CR_SHA_HCO_SHIM01 = openmc.Cell( name='c_l_CR_SHA_HCO_SHIM01')
c_l_CR_SHA_HCO_SHIM02 = openmc.Cell( name='c_l_CR_SHA_HCO_SHIM02')
c_l_CR_SHA_HCO_SHIM03 = openmc.Cell( name='c_l_CR_SHA_HCO_SHIM03')
c_l_CR_SHA_HCO_SHIM04 = openmc.Cell( name='c_l_CR_SHA_HCO_SHIM04')

c_l_CR_SHA_HCO_SHIM01.region = -cyl_CR_SHAFT_IN                   # Shaft in 
c_l_CR_SHA_HCO_SHIM02.region = -cyl_CR_HCO_IN & +cyl_CR_SHAFT_IN  # Shaft out
c_l_CR_SHA_HCO_SHIM03.region = -cyl_CR_HCO_OU & +cyl_CR_HCO_IN    # Head connector
c_l_CR_SHA_HCO_SHIM04.region = +cyl_CR_HCO_OU                     # Head connector

c_l_CR_SHA_HCO_SHIM01.fill = Ti316
c_l_CR_SHA_HCO_SHIM02.fill = Na_CR_Out
c_l_CR_SHA_HCO_SHIM03.fill = SS
c_l_CR_SHA_HCO_SHIM04.fill = Na_CR_In

u_CR_SHA_HCO_SHIM = openmc.Universe()
u_CR_SHA_HCO_SHIM.add_cells([
c_l_CR_SHA_HCO_SHIM01, 
c_l_CR_SHA_HCO_SHIM02,
c_l_CR_SHA_HCO_SHIM03,
c_l_CR_SHA_HCO_SHIM04
])

# --- Shaft+TRS
c_l_CR_SHA_TRS_SHIM01 = openmc.Cell( name='c_l_CR_SHA_TRS_SHIM01')
c_l_CR_SHA_TRS_SHIM02 = openmc.Cell( name='c_l_CR_SHA_TRS_SHIM02')
c_l_CR_SHA_TRS_SHIM03 = openmc.Cell( name='c_l_CR_SHA_TRS_SHIM03')
c_l_CR_SHA_TRS_SHIM04 = openmc.Cell( name='c_l_CR_SHA_TRS_SHIM04')

c_l_CR_SHA_TRS_SHIM01.region = -cyl_CR_SHAFT_IN                   # Shaft in 
c_l_CR_SHA_TRS_SHIM02.region = -cone_CR_PH_IN & +cyl_CR_SHAFT_IN  # Shaft out
c_l_CR_SHA_TRS_SHIM03.region = -cone_CR_PH_OU & +cone_CR_PH_IN    # Transition
c_l_CR_SHA_TRS_SHIM04.region = +cone_CR_PH_OU                     # Transition

c_l_CR_SHA_TRS_SHIM01.fill = Ti316
c_l_CR_SHA_TRS_SHIM02.fill = Na_CR_Out
c_l_CR_SHA_TRS_SHIM03.fill = SS
c_l_CR_SHA_TRS_SHIM04.fill = Na_CR_In

u_CR_SHA_TRS_SHIM = openmc.Universe()
u_CR_SHA_TRS_SHIM.add_cells([
c_l_CR_SHA_TRS_SHIM01, 
c_l_CR_SHA_TRS_SHIM02,
c_l_CR_SHA_TRS_SHIM03,
c_l_CR_SHA_TRS_SHIM04
])

# --- Shaft+UPL
c_l_CR_SHA_UPL_SHIM01 = openmc.Cell( name='c_l_CR_SHA_UPL_SHIM01')
c_l_CR_SHA_UPL_SHIM02 = openmc.Cell( name='c_l_CR_SHA_UPL_SHIM02')
c_l_CR_SHA_UPL_SHIM03 = openmc.Cell( name='c_l_CR_SHA_UPL_SHIM03')
c_l_CR_SHA_UPL_SHIM04 = openmc.Cell( name='c_l_CR_SHA_UPL_SHIM04')

c_l_CR_SHA_UPL_SHIM01.region = -cyl_CR_SHAFT_IN                   # Shaft in 
c_l_CR_SHA_UPL_SHIM02.region = -cyl_CR_UPL_IN & +cyl_CR_SHAFT_IN  # Shaft out
c_l_CR_SHA_UPL_SHIM03.region =  hex_CR_UPL_OU & +cyl_CR_UPL_IN    # Upper plenum
c_l_CR_SHA_UPL_SHIM04.region = ~hex_CR_UPL_OU                     # Upper plenum

c_l_CR_SHA_UPL_SHIM01.fill = Ti316
c_l_CR_SHA_UPL_SHIM02.fill = Na_CR_Out
c_l_CR_SHA_UPL_SHIM03.fill = SS
c_l_CR_SHA_UPL_SHIM04.fill = Na_CR_In

u_CR_SHA_UPL_SHIM = openmc.Universe()
u_CR_SHA_UPL_SHIM.add_cells([
c_l_CR_SHA_UPL_SHIM01, 
c_l_CR_SHA_UPL_SHIM02,
c_l_CR_SHA_UPL_SHIM03,
c_l_CR_SHA_UPL_SHIM04
])


# --- UCO+UPL
c_l_CR_UCO_UPL_SHIM01 = openmc.Cell( name='c_l_CR_UCO_UPL_SHIM01')
c_l_CR_UCO_UPL_SHIM02 = openmc.Cell( name='c_l_CR_UCO_UPL_SHIM02')
c_l_CR_UCO_UPL_SHIM03 = openmc.Cell( name='c_l_CR_UCO_UPL_SHIM03')
c_l_CR_UCO_UPL_SHIM04 = openmc.Cell( name='c_l_CR_UCO_UPL_SHIM04')

c_l_CR_UCO_UPL_SHIM01.region = -cyl_CR_CON_OU                      # Upper connector
c_l_CR_UCO_UPL_SHIM02.region = +cyl_CR_CON_OU & -cyl_CR_UPL_IN     # Upper connector
c_l_CR_UCO_UPL_SHIM03.region =  hex_CR_UPL_OU & +cyl_CR_UPL_IN     # Upper plenum   
c_l_CR_UCO_UPL_SHIM04.region = ~hex_CR_UPL_OU                      # Upper plenum

c_l_CR_UCO_UPL_SHIM01.fill = HOMOG_CR_CON
c_l_CR_UCO_UPL_SHIM02.fill = Na_CR_Out
c_l_CR_UCO_UPL_SHIM03.fill = SS
c_l_CR_UCO_UPL_SHIM04.fill = Na_CR_In

u_CR_UCO_UPL_SHIM = openmc.Universe()
u_CR_UCO_UPL_SHIM.add_cells([
c_l_CR_UCO_UPL_SHIM01,
c_l_CR_UCO_UPL_SHIM02,
c_l_CR_UCO_UPL_SHIM03,
c_l_CR_UCO_UPL_SHIM04 
])


# --- PLE+UPL
c_l_CR_PLE_UPL_SHIM01 = openmc.Cell( name='c_l_CR_PLE_UPL_SHIM01')
c_l_CR_PLE_UPL_SHIM02 = openmc.Cell( name='c_l_CR_PLE_UPL_SHIM02')
c_l_CR_PLE_UPL_SHIM03 = openmc.Cell( name='c_l_CR_PLE_UPL_SHIM03')
c_l_CR_PLE_UPL_SHIM04 = openmc.Cell( name='c_l_CR_PLE_UPL_SHIM04')
c_l_CR_PLE_UPL_SHIM05 = openmc.Cell( name='c_l_CR_PLE_UPL_SHIM05')

c_l_CR_PLE_UPL_SHIM01.region = -cyl_CR_WR_IN                    # Plenum
c_l_CR_PLE_UPL_SHIM02.region = -cyl_CR_WR_OU  & +cyl_CR_WR_IN   # Plenum
c_l_CR_PLE_UPL_SHIM03.region = -cyl_CR_UPL_IN & +cyl_CR_WR_OU   # Plenum
c_l_CR_PLE_UPL_SHIM04.region =  hex_CR_UPL_OU & +cyl_CR_UPL_IN  # Upper plenum  
c_l_CR_PLE_UPL_SHIM05.region = ~hex_CR_UPL_OU                   # Upper plenum  

c_l_CR_PLE_UPL_SHIM01.fill = Na_CR_Out
c_l_CR_PLE_UPL_SHIM02.fill = Ti316
c_l_CR_PLE_UPL_SHIM03.fill = Na_CR_Out
c_l_CR_PLE_UPL_SHIM04.fill = SS
c_l_CR_PLE_UPL_SHIM05.fill = Na_CR_In

u_CR_PLE_UPL_SHIM = openmc.Universe()
u_CR_PLE_UPL_SHIM.add_cells([
c_l_CR_PLE_UPL_SHIM01,
c_l_CR_PLE_UPL_SHIM02,
c_l_CR_PLE_UPL_SHIM03,
c_l_CR_PLE_UPL_SHIM04,
c_l_CR_PLE_UPL_SHIM05 
])

# --- ABS+UPL,  Enriched B4C - shim rod (u_CR_move_SHIM)
l_CR_SHIM = openmc.HexLattice()
l_CR_SHIM.center = [0., 0.]
l_CR_SHIM.pitch  = [1.5500]
l_CR_SHIM.universes = \
       [ [p_CR2_BENR]*6, [p_CR1_BENR] ]
l_CR_SHIM.outer  = p_CR2_NaOU
l_CR_SHIM.rotation = [0, 0,-30]

c_l_CR_ABS_UPL_SHIM01 = openmc.Cell( name='c_l_CR_ABS_UPL_SHIM01')
c_l_CR_ABS_UPL_SHIM02 = openmc.Cell( name='c_l_CR_ABS_UPL_SHIM02')
c_l_CR_ABS_UPL_SHIM03 = openmc.Cell( name='c_l_CR_ABS_UPL_SHIM03')
c_l_CR_ABS_UPL_SHIM04 = openmc.Cell( name='c_l_CR_ABS_UPL_SHIM04')
c_l_CR_ABS_UPL_SHIM05 = openmc.Cell( name='c_l_CR_ABS_UPL_SHIM05')

c_l_CR_ABS_UPL_SHIM01.region = -cyl_CR_WR_IN                       # Absorber
c_l_CR_ABS_UPL_SHIM02.region = -cyl_CR_WR_OU  & +cyl_CR_WR_IN      # Absorber
c_l_CR_ABS_UPL_SHIM03.region = -cyl_CR_UPL_IN & +cyl_CR_WR_OU      # Absorber
c_l_CR_ABS_UPL_SHIM04.region =  hex_CR_UPL_OU & +cyl_CR_UPL_IN    # Upper plenum  
c_l_CR_ABS_UPL_SHIM05.region = ~hex_CR_UPL_OU                     # Upper plenum  

c_l_CR_ABS_UPL_SHIM01.fill = l_CR_SHIM
c_l_CR_ABS_UPL_SHIM02.fill = Ti316
c_l_CR_ABS_UPL_SHIM03.fill = Na_CR_Out
c_l_CR_ABS_UPL_SHIM04.fill = SS
c_l_CR_ABS_UPL_SHIM05.fill = Na_CR_In

u_CR_ABS_UPL_SHIM = openmc.Universe()
u_CR_ABS_UPL_SHIM.add_cells([
c_l_CR_ABS_UPL_SHIM01,
c_l_CR_ABS_UPL_SHIM02,
c_l_CR_ABS_UPL_SHIM03,
c_l_CR_ABS_UPL_SHIM04,
c_l_CR_ABS_UPL_SHIM05
])

# --- LCO+UPL
c_l_CR_LCO_UPL_SHIM01 = openmc.Cell( name='c_l_CR_LCO_UPL_SHIM01')
c_l_CR_LCO_UPL_SHIM02 = openmc.Cell( name='c_l_CR_LCO_UPL_SHIM02')
c_l_CR_LCO_UPL_SHIM03 = openmc.Cell( name='c_l_CR_LCO_UPL_SHIM03')
c_l_CR_LCO_UPL_SHIM04 = openmc.Cell( name='c_l_CR_LCO_UPL_SHIM04')

c_l_CR_LCO_UPL_SHIM01.region = -cyl_CR_CON_OU                      # Lower connector
c_l_CR_LCO_UPL_SHIM02.region = -cyl_CR_UPL_IN & +cyl_CR_CON_OU     # Lower connector
c_l_CR_LCO_UPL_SHIM03.region =  hex_CR_UPL_OU & +cyl_CR_UPL_IN  # Upper plenum  
c_l_CR_LCO_UPL_SHIM04.region = ~hex_CR_UPL_OU                   # Upper plenum  

c_l_CR_LCO_UPL_SHIM01.fill = HOMOG_CR_CON
c_l_CR_LCO_UPL_SHIM02.fill = Na_CR_In
c_l_CR_LCO_UPL_SHIM03.fill = SS
c_l_CR_LCO_UPL_SHIM04.fill = Na_CR_In

u_CR_LCO_UPL_SHIM = openmc.Universe()
u_CR_LCO_UPL_SHIM.add_cells([
c_l_CR_LCO_UPL_SHIM01,
c_l_CR_LCO_UPL_SHIM02,
c_l_CR_LCO_UPL_SHIM03,
c_l_CR_LCO_UPL_SHIM04 
])

# --- LCO+WRA
c_l_CR_LCO_WRA_SHIM01 = openmc.Cell( name='c_l_CR_LCO_WRA_SHIM01')
c_l_CR_LCO_WRA_SHIM02 = openmc.Cell( name='c_l_CR_LCO_WRA_SHIM02')
c_l_CR_LCO_WRA_SHIM03 = openmc.Cell( name='c_l_CR_LCO_WRA_SHIM03')
c_l_CR_LCO_WRA_SHIM04 = openmc.Cell( name='c_l_CR_LCO_WRA_SHIM04')

c_l_CR_LCO_WRA_SHIM01.region = -cyl_CR_CON_OU                      # Lower connector
c_l_CR_LCO_WRA_SHIM02.region =  hex_WR_IN     & +cyl_CR_CON_OU     # Lower connector
c_l_CR_LCO_WRA_SHIM03.region =  hex_WR_OU     & ~hex_WR_IN  # Normal wrapper
c_l_CR_LCO_WRA_SHIM04.region = ~hex_WR_OU                   # Normal wrapper

c_l_CR_LCO_WRA_SHIM01.fill = HOMOG_CR_CON
c_l_CR_LCO_WRA_SHIM02.fill = Na_CR_In
c_l_CR_LCO_WRA_SHIM03.fill = SS
c_l_CR_LCO_WRA_SHIM04.fill = Na_CR_In

u_CR_LCO_WRA_SHIM = openmc.Universe()
u_CR_LCO_WRA_SHIM.add_cells([
c_l_CR_LCO_WRA_SHIM01,
c_l_CR_LCO_WRA_SHIM02,
c_l_CR_LCO_WRA_SHIM03,
c_l_CR_LCO_WRA_SHIM04 
])

# --- BAF+WRA
c_l_CR_BAF_WRA_SHIM01 = openmc.Cell( name='c_l_CR_BAF_WRA_SHIM01')
c_l_CR_BAF_WRA_SHIM02 = openmc.Cell( name='c_l_CR_BAF_WRA_SHIM02')
c_l_CR_BAF_WRA_SHIM03 = openmc.Cell( name='c_l_CR_BAF_WRA_SHIM03')
c_l_CR_BAF_WRA_SHIM04 = openmc.Cell( name='c_l_CR_BAF_WRA_SHIM04')
c_l_CR_BAF_WRA_SHIM05 = openmc.Cell( name='c_l_CR_BAF_WRA_SHIM05')

c_l_CR_BAF_WRA_SHIM01.region =                  -cyl_CR_BAF_IN    # Baffle
c_l_CR_BAF_WRA_SHIM02.region = +cyl_CR_BAF_IN & -cyl_CR_BAF_OU    # Baffle
c_l_CR_BAF_WRA_SHIM03.region =  hex_WR_IN     & +cyl_CR_BAF_OU    # Baffle
c_l_CR_BAF_WRA_SHIM04.region =  hex_WR_OU     & ~hex_WR_IN  # Normal wrapper 
c_l_CR_BAF_WRA_SHIM05.region = ~hex_WR_OU                   # Normal wrapper 

c_l_CR_BAF_WRA_SHIM01.fill = Na_CR_In
c_l_CR_BAF_WRA_SHIM02.fill = Ti316   
c_l_CR_BAF_WRA_SHIM03.fill = Na_CR_In
c_l_CR_BAF_WRA_SHIM04.fill = SS
c_l_CR_BAF_WRA_SHIM05.fill = Na_CR_In

u_CR_BAF_WRA_SHIM = openmc.Universe()
u_CR_BAF_WRA_SHIM.add_cells([
c_l_CR_BAF_WRA_SHIM01,
c_l_CR_BAF_WRA_SHIM02,
c_l_CR_BAF_WRA_SHIM03,
c_l_CR_BAF_WRA_SHIM04,
c_l_CR_BAF_WRA_SHIM05
])

# --- BOT+WRA

c_l_CR_BOT_WRA_SHIM01 = openmc.Cell( name='c_l_CR_BOT_WRA_SHIM01')
c_l_CR_BOT_WRA_SHIM02 = openmc.Cell( name='c_l_CR_BOT_WRA_SHIM02')
c_l_CR_BOT_WRA_SHIM03 = openmc.Cell( name='c_l_CR_BOT_WRA_SHIM03')

c_l_CR_BOT_WRA_SHIM01.region =  hex_WR_IN                   # Normal wrapper 
c_l_CR_BOT_WRA_SHIM02.region =  hex_WR_OU     & ~hex_WR_IN  # Normal wrapper
c_l_CR_BOT_WRA_SHIM03.region = ~hex_WR_OU                   # Normal wrapper

c_l_CR_BOT_WRA_SHIM01.fill = Na_CR_In
c_l_CR_BOT_WRA_SHIM02.fill = SS
c_l_CR_BOT_WRA_SHIM03.fill = Na_CR_In


u_CR_BOT_WRA_SHIM = openmc.Universe()
u_CR_BOT_WRA_SHIM.add_cells([
c_l_CR_BOT_WRA_SHIM01,
c_l_CR_BOT_WRA_SHIM02,
c_l_CR_BOT_WRA_SHIM03
])


#-----------------------------------------------------------------------------------
# --- CR assembly NON-movable part
#-----------------------------------------------------------------------------------
c_l_CR_LSH1 = openmc.Cell( name='c_l_CR_LSH1')
c_l_CR_LSH2 = openmc.Cell( name='c_l_CR_LSH2')
c_l_CR_LSH3 = openmc.Cell( name='c_l_CR_LSH3')
c_l_CR_LSH4 = openmc.Cell( name='c_l_CR_LSH4')

c_l_CR_LSH1.region =  -cyl_CR_LSH
c_l_CR_LSH2.region =  hex_WR_IN & +cyl_CR_LSH
c_l_CR_LSH3.region =  hex_WR_OU & ~hex_WR_IN
c_l_CR_LSH4.region = ~hex_WR_OU

c_l_CR_LSH1.fill = SS 
c_l_CR_LSH2.fill = Na_CR_In
c_l_CR_LSH3.fill = SS   
c_l_CR_LSH4.fill = Na_CR_In

u_CR_LSH = openmc.Universe()
u_CR_LSH.add_cells([
c_l_CR_LSH1,
c_l_CR_LSH2,
c_l_CR_LSH3,
c_l_CR_LSH4
])
# --- RR LATTICES and UNIVERSES
#
# -------------------------------------------------------
# --- Upper shield
c_l_RR_USH1 = openmc.Cell( name='c_l_RR_USH1')
c_l_RR_USH2 = openmc.Cell( name='c_l_RR_USH2')
c_l_RR_USH3 = openmc.Cell( name='c_l_RR_USH3')
c_l_RR_USH4 = openmc.Cell( name='c_l_RR_USH4')

c_l_RR_USH1.region = -cyl_RR_SS_T3
c_l_RR_USH2.region = +cyl_RR_SS_T3 & hex_WR_IN
c_l_RR_USH3.region = ~hex_WR_IN    & hex_WR_OU
c_l_RR_USH4.region = ~hex_WR_OU

c_l_RR_USH1.fill = Ti316
c_l_RR_USH2.fill = Na_RR_In
c_l_RR_USH3.fill = Ti316
c_l_RR_USH4.fill = Na_RR_Out

u_RR_USH = openmc.Universe()
u_RR_USH.add_cells([
c_l_RR_USH1,
c_l_RR_USH2,
c_l_RR_USH3,
c_l_RR_USH4
])

# -------------------------------------------------------
# --- Reflector rods T1 = Type   I(7 rods)
# -------------------------------------------------------                                                                                                                                                                                                                   
l_RR_T1 = openmc.HexLattice()
l_RR_T1.center = [0., 0.]
l_RR_T1.pitch  = [2.07]
l_RR_T1.universes = \
       [ [p_RR_T1]*6, [p_RR_T1] ]
l_RR_T1.outer  = p_RR_NaOU

c_l_RR1_01 = openmc.Cell( name='c_l_RR1_01')
c_l_RR1_02 = openmc.Cell( name='c_l_RR1_02')
c_l_RR1_03 = openmc.Cell( name='c_l_RR1_03')

c_l_RR1_01.region =  hex_WR_IN
c_l_RR1_02.region =  hex_WR_OU & ~hex_WR_IN 
c_l_RR1_03.region = ~hex_WR_OU

c_l_RR1_01.fill = l_RR_T1
c_l_RR1_02.fill = Ti316
c_l_RR1_03.fill = Na_RR_Out

u_RR_T1 = openmc.Universe()
u_RR_T1.add_cells([
c_l_RR1_01,
c_l_RR1_02,
c_l_RR1_03
])

# -------------------------------------------------------
# --- Reflector rods T2 = Type   II (7 rods)
# -------------------------------------------------------                                                                                                                                                                                                                   
l_RR_T2 = openmc.HexLattice()
l_RR_T2.center = [0., 0.]
l_RR_T2.pitch  = [2.07]
l_RR_T2.universes = \
       [ [p_RR_T2]*6, [p_RR_T2] ]
l_RR_T2.outer  = p_RR_NaOU

c_l_RR2_01 = openmc.Cell( name='c_l_RR2_01')
c_l_RR2_02 = openmc.Cell( name='c_l_RR2_02')
c_l_RR2_03 = openmc.Cell( name='c_l_RR2_03')

c_l_RR2_01.region =  hex_WR_IN
c_l_RR2_02.region =  hex_WR_OU & ~hex_WR_IN 
c_l_RR2_03.region = ~hex_WR_OU

c_l_RR2_01.fill = l_RR_T2
c_l_RR2_02.fill = Ti316
c_l_RR2_03.fill = Na_RR_Out

u_RR_T2 = openmc.Universe()
u_RR_T2.add_cells([
c_l_RR2_01,
c_l_RR2_02,
c_l_RR2_03
])

# -------------------------------------------------------
# --- Reflector rods T3 = Type III (Single rod)
# -------------------------------------------------------                                                                                                                                                                                                                   
c_l_RR3_01 = openmc.Cell( name='c_l_RR3_01')
c_l_RR3_02 = openmc.Cell( name='c_l_RR3_02')
c_l_RR3_03 = openmc.Cell( name='c_l_RR3_03')
c_l_RR3_04 = openmc.Cell( name='c_l_RR3_04')

c_l_RR3_01.region =  -cyl_RR_SS_T3
c_l_RR3_02.region =  hex_WR_IN & +cyl_RR_SS_T3
c_l_RR3_03.region =  hex_WR_OU & ~hex_WR_IN
c_l_RR3_04.region = ~hex_WR_OU

c_l_RR3_01.fill = SS_R3
c_l_RR3_02.fill = Na_RR_In
c_l_RR3_03.fill = Ti316
c_l_RR3_04.fill = Na_RR_Out

u_RR_T3 = openmc.Universe()
u_RR_T3.add_cells([
c_l_RR3_01,
c_l_RR3_02,
c_l_RR3_03,
c_l_RR3_04
])

# -------------------------------------------------------
# --- Reflector rods T4 = Type IV (Single rod)
# -------------------------------------------------------                                                                                                                                                                                                                   
c_l_RR4_01 = openmc.Cell( name='c_l_RR4_01')
c_l_RR4_02 = openmc.Cell( name='c_l_RR4_02')
c_l_RR4_03 = openmc.Cell( name='c_l_RR4_03')
c_l_RR4_04 = openmc.Cell( name='c_l_RR4_04')

c_l_RR4_01.region =  -cyl_RR_SS_T3
c_l_RR4_02.region =  hex_WR_IN & +cyl_RR_SS_T3
c_l_RR4_03.region =  hex_WR_OU & ~hex_WR_IN
c_l_RR4_04.region = ~hex_WR_OU

c_l_RR4_01.fill = SS_R4
c_l_RR4_02.fill = Na_RR_In
c_l_RR4_03.fill = Ti316
c_l_RR4_04.fill = Na_RR_Out

u_RR_T4 = openmc.Universe()
u_RR_T4.add_cells([
c_l_RR4_01,
c_l_RR4_02,
c_l_RR4_03,
c_l_RR4_04
])

# -------------------------------------------------------
# --- Na plenum
# -------------------------------------------------------
c_l_RR_SPL2 = openmc.Cell( name='c_l_RR_SPL2')
c_l_RR_SPL3 = openmc.Cell( name='c_l_RR_SPL3')
c_l_RR_SPL4 = openmc.Cell( name='c_l_RR_SPL4')

c_l_RR_SPL2.region =  hex_WR_IN
c_l_RR_SPL3.region =  hex_WR_OU & ~hex_WR_IN
c_l_RR_SPL4.region = ~hex_WR_OU

c_l_RR_SPL2.fill = Na_RR_In
c_l_RR_SPL3.fill = Ti316
c_l_RR_SPL4.fill = Na_RR_Out

u_RR_SPL = openmc.Universe()
u_RR_SPL.add_cells([
c_l_RR_SPL2,
c_l_RR_SPL3,
c_l_RR_SPL4
])

# -------------------------------------------------------
# --- Lower shield
# -------------------------------------------------------
c_l_RR_LSH1 = openmc.Cell( name='c_l_RR_LSH1')
c_l_RR_LSH2 = openmc.Cell( name='c_l_RR_LSH2')
c_l_RR_LSH3 = openmc.Cell( name='c_l_RR_LSH3')
c_l_RR_LSH4 = openmc.Cell( name='c_l_RR_LSH4')

c_l_RR_LSH1.region =  -cyl_CR_LSH
c_l_RR_LSH2.region =  hex_WR_IN & +cyl_CR_LSH
c_l_RR_LSH3.region =  hex_WR_OU & ~hex_WR_IN
c_l_RR_LSH4.region = ~hex_WR_OU

c_l_RR_LSH1.fill = Ti316
c_l_RR_LSH2.fill = Na_RR_In
c_l_RR_LSH3.fill = Ti316
c_l_RR_LSH4.fill = Na_RR_Out

u_RR_LSH = openmc.Universe()
u_RR_LSH.add_cells([
c_l_RR_LSH1,
c_l_RR_LSH2,
c_l_RR_LSH3,
c_l_RR_LSH4
])
# --- Radial shield LATTICES and UNIVERSES
#
# -------------------------------------------------------
# --- Upper SS shield
# -------------------------------------------------------
c_l_RB_USH1 = openmc.Cell( name='c_l_RB_USH1')
c_l_RB_USH2 = openmc.Cell( name='c_l_RB_USH2')
c_l_RB_USH3 = openmc.Cell( name='c_l_RB_USH3')
c_l_RB_USH4 = openmc.Cell( name='c_l_RB_USH4')

c_l_RB_USH1.region =  -cyl_RR_SS_T3
c_l_RB_USH2.region =  hex_WR_IN & +cyl_RR_SS_T3
c_l_RB_USH3.region =  hex_WR_OU & ~hex_WR_IN
c_l_RB_USH4.region = ~hex_WR_OU

c_l_RB_USH1.fill = Ti316
c_l_RB_USH2.fill = Na_RR_In
c_l_RB_USH3.fill = Ti316
c_l_RB_USH4.fill = Na_RR_Out

u_RB_USH = openmc.Universe()
u_RB_USH.add_cells([c_l_RB_USH1,c_l_RB_USH2,c_l_RB_USH3,c_l_RB_USH4])

# -------------------------------------------------------
# --- Radial boron shield (7 rods)
# -------------------------------------------------------                                                                                                                                                                                                                   
l_RB = openmc.HexLattice()
l_RB.center = [0., 0.]
l_RB.pitch  = [2.07]
l_RB.universes = \
       [ [p_RB]*6, [p_RB] ]
l_RB.outer  = p_RB_NaOU

c_l_RB1_01 = openmc.Cell( name='c_l_RB1_01')
c_l_RB1_02 = openmc.Cell( name='c_l_RB1_02')
c_l_RB1_03 = openmc.Cell( name='c_l_RB1_03')

c_l_RB1_01.region =  hex_WR_IN
c_l_RB1_02.region =  hex_WR_OU & ~hex_WR_IN 
c_l_RB1_03.region = ~hex_WR_OU

c_l_RB1_01.fill = l_RB
c_l_RB1_02.fill = Ti316
c_l_RB1_03.fill = Na_RR_Out

u_RB = openmc.Universe()
u_RB.add_cells([c_l_RB1_01,c_l_RB1_02,c_l_RB1_03])

# -------------------------------------------------------
# --- Na plenum
# -------------------------------------------------------
c_l_RB_SPL2 = openmc.Cell( name='c_l_RB_SPL2')
c_l_RB_SPL3 = openmc.Cell( name='c_l_RB_SPL3')
c_l_RB_SPL4 = openmc.Cell( name='c_l_RB_SPL4')

c_l_RB_SPL2.region =  hex_WR_IN
c_l_RB_SPL3.region =  hex_WR_OU & ~hex_WR_IN
c_l_RB_SPL4.region = ~hex_WR_OU

c_l_RB_SPL2.fill = Na_RR_In
c_l_RB_SPL3.fill = Ti316
c_l_RB_SPL4.fill = Na_RR_Out

u_RB_SPL = openmc.Universe()
u_RB_SPL.add_cells([c_l_RB_SPL2,c_l_RB_SPL3,c_l_RB_SPL4])

# -------------------------------------------------------
# --- Lower SS shield
# -------------------------------------------------------
c_l_RB_LSH1 = openmc.Cell( name='c_l_RB_LSH1')
c_l_RB_LSH2 = openmc.Cell( name='c_l_RB_LSH2')
c_l_RB_LSH3 = openmc.Cell( name='c_l_RB_LSH3')
c_l_RB_LSH4 = openmc.Cell( name='c_l_RB_LSH4')

c_l_RB_LSH1.region =  -cyl_CR_LSH
c_l_RB_LSH2.region =  hex_WR_IN & +cyl_CR_LSH
c_l_RB_LSH3.region =  hex_WR_OU & ~hex_WR_IN
c_l_RB_LSH4.region = ~hex_WR_OU

c_l_RB_LSH1.fill = Ti316
c_l_RB_LSH2.fill = Na_RR_In
c_l_RB_LSH3.fill = Ti316
c_l_RB_LSH4.fill = Na_RR_Out

u_RB_LSH = openmc.Universe()
u_RB_LSH.add_cells([c_l_RB_LSH1,c_l_RB_LSH2,c_l_RB_LSH3,c_l_RB_LSH4])
# -------------------------------------------------------
# --- Reflector rods T1 = Type   I(7 rods)
# -------------------------------------------------------                                                                                                                                                                                                                   
l_NS = openmc.HexLattice()
l_NS.center = [0., 0.]
l_NS.pitch  = [2.07]
l_NS.universes = \
       [ [p_RR_T1]*6, [p_NS] ]
l_NS.outer  = p_NS_NaOU

c_l_NS1_01 = openmc.Cell( name='c_l_NS1_01')
c_l_NS1_02 = openmc.Cell( name='c_l_NS1_02')
c_l_NS1_03 = openmc.Cell( name='c_l_NS1_03')

c_l_NS1_01.region =  hex_WR_IN
c_l_NS1_02.region =  hex_WR_OU & ~hex_WR_IN 
c_l_NS1_03.region = ~hex_WR_OU

c_l_NS1_01.fill = l_NS
c_l_NS1_02.fill = Ti316
c_l_NS1_03.fill = Na_RR_Out

u_NS = openmc.Universe()
u_NS.add_cells([c_l_NS1_01,c_l_NS1_02,c_l_NS1_03])
# --- FUEL ASSEMBLY LATTICES for SODIUM VOID 
#
# 11. Head                26.00 cm
# 10. Upper shield        44.00 cm
#  9. Upper connector      6.00 cm
# ------ Fuel pin top ------------
#  8. Top end plug         2.00 cm
#  7. Spring               4.50 cm
#  6. Upper blanket       10.00 cm
#  5. Fissile             45.00 cm
#  4. Lower blanket       25.00 cm
#  3. Lower gas plenum    45.00 cm
#  2. Bottom end plug      3.50 cm
# ------ Fuel pin bottom ---------
#  1. Lower connector     10.00 cm


# -------------------------------------------------------
# --- HEAD
# -------------------------------------------------------
c_l_VO_HEA_01 = openmc.Cell( name='c_l_VO_HEA_01')
c_l_VO_HEA_02 = openmc.Cell( name='c_l_VO_HEA_02')
c_l_VO_HEA_03 = openmc.Cell( name='c_l_VO_HEA_03')

c_l_VO_HEA_01.region =  hex_HEA_IN 
c_l_VO_HEA_02.region = ~hex_HEA_IN & hex_WR_OU
c_l_VO_HEA_03.region = ~hex_WR_OU  

c_l_VO_HEA_01.fill = vacuum
c_l_VO_HEA_02.fill = Ti316
c_l_VO_HEA_03.fill = Na_FU_OUT_bypass

u_VO_HEA = openmc.Universe()
u_VO_HEA.add_cells([c_l_VO_HEA_01, c_l_VO_HEA_02, c_l_VO_HEA_03])

# -------------------------------------------------------
# --- Upper shield (USH)
# -------------------------------------------------------
c_l_VO_USH_01 = openmc.Cell( name='c_l_VO_USH_01')
c_l_VO_USH_02 = openmc.Cell( name='c_l_VO_USH_02')
c_l_VO_USH_03 = openmc.Cell( name='c_l_VO_USH_03')

c_l_VO_USH_01.region = -cyl_USH_hole
c_l_VO_USH_02.region =  hex_WR_OU & +cyl_USH_hole
c_l_VO_USH_03.region = ~hex_WR_OU

c_l_VO_USH_01.fill = vacuum
c_l_VO_USH_02.fill = Ti316
c_l_VO_USH_03.fill = Na_FU_OUT_bypass

u_VO_USH = openmc.Universe()
u_VO_USH.add_cells([c_l_VO_USH_01, c_l_VO_USH_02, c_l_VO_USH_03])

# -------------------------------------------------------
# --- Upper connector (UCN)
# -------------------------------------------------------
c_l_VO_UCN_01 = openmc.Cell( name='c_l_VO_UCN_01')
c_l_VO_UCN_02 = openmc.Cell( name='c_l_VO_UCN_02')
c_l_VO_UCN_03 = openmc.Cell( name='c_l_VO_UCN_03')

c_l_VO_UCN_01.region =  hex_UCN_IN
c_l_VO_UCN_02.region =  hex_WR_OU & ~hex_UCN_IN
c_l_VO_UCN_03.region = ~hex_WR_OU

c_l_VO_UCN_01.fill = vacuum
c_l_VO_UCN_02.fill = Ti316
c_l_VO_UCN_03.fill = Na_FU_OUT_bypass

u_VO_UCN = openmc.Universe()
u_VO_UCN.add_cells([c_l_VO_UCN_01, c_l_VO_UCN_02, c_l_VO_UCN_03])

# -------------------------------------------------------
# --- Top end plug (TEP) 
# -------------------------------------------------------
l_VO_TEP = openmc.HexLattice()
l_VO_TEP.center = [0., 0.]
l_VO_TEP.pitch  = [ 0.695]
l_VO_TEP.universes = \
       [ [p_VO_TEP]*24, [p_VO_TEP]*18, [p_VO_TEP]*12, [p_VO_TEP]*6, [p_VO_TEP] ]
l_VO_TEP.outer  = p_VO_VOU

c_l_VO_TEP_01 = openmc.Cell( name='c_l_VO_TEP_01')
c_l_VO_TEP_02 = openmc.Cell( name='c_l_VO_TEP_02')
c_l_VO_TEP_03 = openmc.Cell( name='c_l_VO_TEP_03')

c_l_VO_TEP_01.region =  hex_WR_IN
c_l_VO_TEP_02.region =  hex_WR_OU & ~hex_WR_IN
c_l_VO_TEP_03.region = ~hex_WR_OU

c_l_VO_TEP_01.fill = l_VO_TEP
c_l_VO_TEP_02.fill = Ti316
c_l_VO_TEP_03.fill = Na_FU_OUT_bypass

u_VO_TEP = openmc.Universe()
u_VO_TEP.add_cells([c_l_VO_TEP_01, c_l_VO_TEP_02, c_l_VO_TEP_03])

# -------------------------------------------------------
# --- Spring (SPR)
# -------------------------------------------------------
l_VO_SPR = openmc.HexLattice()
l_VO_SPR.center = [0., 0.]
l_VO_SPR.pitch  = [ 0.695]
l_VO_SPR.universes = \
       [ [p_VO_SPR]*24, [p_VO_SPR]*18, [p_VO_SPR]*12, [p_VO_SPR]*6, [p_VO_SPR] ]
l_VO_SPR.outer  = p_VO_VOU

c_l_VO_SPR_01 = openmc.Cell( name='c_l_VO_SPR_01')
c_l_VO_SPR_02 = openmc.Cell( name='c_l_VO_SPR_02')
c_l_VO_SPR_03 = openmc.Cell( name='c_l_VO_SPR_03')

c_l_VO_SPR_01.region =  hex_WR_IN
c_l_VO_SPR_02.region =  hex_WR_OU & ~hex_WR_IN
c_l_VO_SPR_03.region = ~hex_WR_OU

c_l_VO_SPR_01.fill = l_VO_SPR
c_l_VO_SPR_02.fill = Ti316
c_l_VO_SPR_03.fill = Na_FU_OUT_bypass

u_VO_SPR = openmc.Universe()
u_VO_SPR.add_cells([c_l_VO_SPR_01, c_l_VO_SPR_02, c_l_VO_SPR_03])

# -------------------------------------------------------
# --- Upper fuel fertile/blanket (UBL)
# -------------------------------------------------------
l_VO_UBL = openmc.HexLattice()
l_VO_UBL.center = [0., 0.]
l_VO_UBL.pitch  = [ 0.695]
l_VO_UBL.universes = \
       [ [p_VO_UBL]*24, [p_VO_UBL]*18, [p_VO_UBL]*12, [p_VO_UBL]*6, [p_VO_UBL] ]
l_VO_UBL.outer  = p_VO_VFE

c_l_VO_UBL_01 = openmc.Cell( name='c_l_VO_UBL_01')
c_l_VO_UBL_02 = openmc.Cell( name='c_l_VO_UBL_02')
c_l_VO_UBL_03 = openmc.Cell( name='c_l_VO_UBL_03')

c_l_VO_UBL_01.region =  hex_WR_IN
c_l_VO_UBL_02.region =  hex_WR_OU & ~hex_WR_IN
c_l_VO_UBL_03.region = ~hex_WR_OU

c_l_VO_UBL_01.fill = l_VO_UBL
c_l_VO_UBL_02.fill = Ti316
c_l_VO_UBL_03.fill = Na_FU_OUT_bypass

u_VO_UBL = openmc.Universe()
u_VO_UBL.add_cells([c_l_VO_UBL_01, c_l_VO_UBL_02, c_l_VO_UBL_03])

# -------------------------------------------------------
# --- Fuel fissile (FIS)
# -------------------------------------------------------
l_VO_FIS = openmc.HexLattice()
l_VO_FIS.center = [0., 0.]
l_VO_FIS.pitch  = [ 0.695]
l_VO_FIS.universes = \
       [ [p_VO_FIS]*24, [p_VO_FIS]*18, [p_VO_FIS]*12, [p_VO_FIS]*6, [p_VO_FIS] ]
l_VO_FIS.outer  = p_VO_VFI

c_l_VO_FIS_01 = openmc.Cell( name='c_l_VO_FIS_01')
c_l_VO_FIS_02 = openmc.Cell( name='c_l_VO_FIS_02')
c_l_VO_FIS_03 = openmc.Cell( name='c_l_VO_FIS_03')

c_l_VO_FIS_01.region =  hex_WR_IN
c_l_VO_FIS_02.region =  hex_WR_OU & ~hex_WR_IN
c_l_VO_FIS_03.region = ~hex_WR_OU

c_l_VO_FIS_01.fill = l_VO_FIS
c_l_VO_FIS_02.fill = Ti316
c_l_VO_FIS_03.fill = Na_FU_FI_bypass

u_VO_FIS = openmc.Universe()
u_VO_FIS.add_cells([c_l_VO_FIS_01, c_l_VO_FIS_02, c_l_VO_FIS_03])

# -------------------------------------------------------
# --- Lower fuel fertile/blanket (LBL)
# -------------------------------------------------------
l_VO_LBL = openmc.HexLattice()
l_VO_LBL.center = [0., 0.]
l_VO_LBL.pitch  = [ 0.695]
l_VO_LBL.universes = \
       [ [p_VO_LBL]*24, [p_VO_LBL]*18, [p_VO_LBL]*12, [p_VO_LBL]*6, [p_VO_LBL] ]
l_VO_LBL.outer  = p_VO_VFE

c_l_VO_LBL_01 = openmc.Cell( name='c_l_VO_LBL_01')
c_l_VO_LBL_02 = openmc.Cell( name='c_l_VO_LBL_02')
c_l_VO_LBL_03 = openmc.Cell( name='c_l_VO_LBL_03')

c_l_VO_LBL_01.region =  hex_WR_IN
c_l_VO_LBL_02.region =  hex_WR_OU & ~hex_WR_IN
c_l_VO_LBL_03.region = ~hex_WR_OU

c_l_VO_LBL_01.fill = l_VO_LBL
c_l_VO_LBL_02.fill = Ti316
c_l_VO_LBL_03.fill = Na_FU_FE_bypass

u_VO_LBL = openmc.Universe()
u_VO_LBL.add_cells([c_l_VO_LBL_01, c_l_VO_LBL_02, c_l_VO_LBL_03])

# -------------------------------------------------------
# --- Lower gas plenum (LGP)
# -------------------------------------------------------
l_VO_LGP = openmc.HexLattice()
l_VO_LGP.center = [0., 0.]
l_VO_LGP.pitch  = [ 0.695]
l_VO_LGP.universes = \
       [ [p_VO_LGP]*24, [p_VO_LGP]*18, [p_VO_LGP]*12, [p_VO_LGP]*6, [p_VO_LGP] ]
l_VO_LGP.outer  = p_VO_VIN

c_l_VO_LGP_01 = openmc.Cell( name='c_l_VO_LGP_01')
c_l_VO_LGP_02 = openmc.Cell( name='c_l_VO_LGP_02')
c_l_VO_LGP_03 = openmc.Cell( name='c_l_VO_LGP_03')

c_l_VO_LGP_01.region =  hex_WR_IN
c_l_VO_LGP_02.region =  hex_WR_OU & ~hex_WR_IN
c_l_VO_LGP_03.region = ~hex_WR_OU

c_l_VO_LGP_01.fill = l_VO_LGP
c_l_VO_LGP_02.fill = Ti316
c_l_VO_LGP_03.fill = Na_FU_In_bypass

u_VO_LGP = openmc.Universe()
u_VO_LGP.add_cells([c_l_VO_LGP_01, c_l_VO_LGP_02, c_l_VO_LGP_03])

# -------------------------------------------------------
# --- Bottop end plug (BEP) 
# -------------------------------------------------------
l_VO_BEP = openmc.HexLattice()
l_VO_BEP.center = [0., 0.]
l_VO_BEP.pitch  = [ 0.695]
l_VO_BEP.universes = \
       [ [p_VO_BEP]*24, [p_VO_BEP]*18, [p_VO_BEP]*12, [p_VO_BEP]*6, [p_VO_BEP] ]
l_VO_BEP.outer  = p_VO_VIN

c_l_VO_BEP_01 = openmc.Cell( name='c_l_VO_BEP_01')
c_l_VO_BEP_02 = openmc.Cell( name='c_l_VO_BEP_02')
c_l_VO_BEP_03 = openmc.Cell( name='c_l_VO_BEP_03')

c_l_VO_BEP_01.region =  hex_WR_IN
c_l_VO_BEP_02.region =  hex_WR_OU & ~hex_WR_IN
c_l_VO_BEP_03.region = ~hex_WR_OU

c_l_VO_BEP_01.fill = l_VO_BEP
c_l_VO_BEP_02.fill = Ti316
c_l_VO_BEP_03.fill = Na_FU_In_bypass

u_VO_BEP = openmc.Universe()
u_VO_BEP.add_cells([c_l_VO_BEP_01, c_l_VO_BEP_02, c_l_VO_BEP_03])

# -------------------------------------------------------
# --- Lower connector (LCN)
# -------------------------------------------------------
c_l_VO_LCN_01 = openmc.Cell( name='c_l_VO_LCN_01')
c_l_VO_LCN_02 = openmc.Cell( name='c_l_VO_LCN_02')
c_l_VO_LCN_03 = openmc.Cell( name='c_l_VO_LCN_03')

c_l_VO_LCN_01.region =  hex_LCN_IN 
c_l_VO_LCN_02.region =  hex_WR_OU & ~hex_LCN_IN
c_l_VO_LCN_03.region = ~hex_WR_OU  

c_l_VO_LCN_01.fill = vacuum   
c_l_VO_LCN_02.fill = Ti316
c_l_VO_LCN_03.fill = Na_FU_OUT_bypass

u_VO_LCN = openmc.Universe()
u_VO_LCN.add_cells([c_l_VO_LCN_01, c_l_VO_LCN_02, c_l_VO_LCN_03])
# -------------------------------------------------------
# --- 3D fuel assembly
# -------------------------------------------------------
#

#cell  c_FU_OUT  a_FU  fill u_FU_HEA  pz_FUEL_HEA                 # 12. Outside             20 deg-C    250 deg-C      
#cell  c_FU_HEA  a_FU  fill u_FU_HEA  pz_FUEL_USH -pz_FUEL_HEA    # 11. Head                26.00 cm    26.108 cm
#cell  c_FU_USH  a_FU  fill u_FU_USH  pz_FUEL_UCN -pz_FUEL_USH    # 10. Upper shield        44.00 cm    44.182 cm
#cell  c_FU_UCN  a_FU  fill u_FU_UCN  pz_FUEL_TEP -pz_FUEL_UCN    #  9. Upper connector      6.00 cm     6.025 cm
#cell  c_FU_TEP  a_FU  fill u_FU_TEP  pz_FUEL_SPR -pz_FUEL_TEP    #  8. Top end plug         2.00 cm     2.008 cm
#cell  c_FU_SPR  a_FU  fill u_FU_SPR  pz_FUEL_UBL -pz_FUEL_SPR    #  7. Spring               4.50 cm     4.519 cm
#cell  c_FU_UBL  a_FU  fill u_FU_UBL  pz_FUEL_FIS -pz_FUEL_UBL    #  6. Upper blanket       10.00 cm    10.023 cm
#cell  c_FU_FIS  a_FU  fill u_FU_FIS  pz_FUEL_LBL -pz_FUEL_FIS    #  5. Fissile             45.00 cm    45.114 cm
#cell  c_FU_LBL  a_FU  fill u_FU_LBL  pz_FUEL_LGP -pz_FUEL_LBL    #  4. Lower blanket       25.00 cm    25.058 cm
#cell  c_FU_LGP  a_FU  fill u_FU_LGP  pz_FUEL_BEP -pz_FUEL_LGP    #  3. Lower gas plenum    45.00 cm    45.186 cm
#cell  c_FU_BEP  a_FU  fill u_FU_BEP  pz_FUEL_LCN -pz_FUEL_BEP    #  2. Bottom end plug      3.50 cm     3.514 cm
#cell  c_FU_LCN  a_FU  fill u_FU_LCN              -pz_FUEL_LCN    #  1. Lower connector     10.00 cm    10.041 cm
                                                    
# 3D Universe - Fuel SA 
c_FU_OUT = openmc.Cell( name='c_FU_OUT')
c_FU_HEA = openmc.Cell( name='c_FU_HEA')
c_FU_USH = openmc.Cell( name='c_FU_USH')
c_FU_UCN = openmc.Cell( name='c_FU_UCN')
c_FU_TEP = openmc.Cell( name='c_FU_TEP')
c_FU_SPR = openmc.Cell( name='c_FU_SPR')
c_FU_UBL = openmc.Cell( name='c_FU_UBL')
c_FU_FIS = openmc.Cell( name='c_FU_FIS')
c_FU_LBL = openmc.Cell( name='c_FU_LBL')
c_FU_LGP = openmc.Cell( name='c_FU_LGP')
c_FU_BEP = openmc.Cell( name='c_FU_BEP')
c_FU_LCN = openmc.Cell( name='c_FU_LCN')

c_FU_OUT.region =                +pz_FUEL_HEA # -pz_TOP & +pz_FUEL_HEA
c_FU_HEA.region = -pz_FUEL_HEA & +pz_FUEL_USH 
c_FU_USH.region = -pz_FUEL_USH & +pz_FUEL_UCN 
c_FU_UCN.region = -pz_FUEL_UCN & +pz_FUEL_TEP 
c_FU_TEP.region = -pz_FUEL_TEP & +pz_FUEL_SPR 
c_FU_SPR.region = -pz_FUEL_SPR & +pz_FUEL_UBL 
c_FU_UBL.region = -pz_FUEL_UBL & +pz_FUEL_FIS 
c_FU_FIS.region = -pz_FUEL_FIS & +pz_FUEL_LBL 
c_FU_LBL.region = -pz_FUEL_LBL & +pz_FUEL_LGP 
c_FU_LGP.region = -pz_FUEL_LGP & +pz_FUEL_BEP 
c_FU_BEP.region = -pz_FUEL_BEP & +pz_FUEL_LCN 
c_FU_LCN.region = -pz_FUEL_LCN                # -pz_FUEL_LCN & +pz_BOT

c_FU_OUT.fill = u_FU_HEA
c_FU_HEA.fill = u_FU_HEA
c_FU_USH.fill = u_FU_USH
c_FU_UCN.fill = u_FU_UCN
c_FU_TEP.fill = u_FU_TEP
c_FU_SPR.fill = u_FU_SPR
c_FU_UBL.fill = u_FU_UBL
c_FU_FIS.fill = u_FU_FIS
c_FU_LBL.fill = u_FU_LBL
c_FU_LGP.fill = u_FU_LGP
c_FU_BEP.fill = u_FU_BEP
c_FU_LCN.fill = u_FU_LCN

c_FU_OUT.rotation = [0, 0, 90]
c_FU_HEA.rotation = [0, 0, 90]
c_FU_USH.rotation = [0, 0, 90]
c_FU_UCN.rotation = [0, 0, 90]
c_FU_TEP.rotation = [0, 0, 90]
c_FU_SPR.rotation = [0, 0, 90]
c_FU_UBL.rotation = [0, 0, 90]
c_FU_FIS.rotation = [0, 0, 90]
c_FU_LBL.rotation = [0, 0, 90]
c_FU_LGP.rotation = [0, 0, 90]
c_FU_BEP.rotation = [0, 0, 90]
c_FU_LCN.rotation = [0, 0, 90]

a_FU = openmc.Universe()
a_FU.add_cells([c_FU_OUT,
                c_FU_HEA,
                c_FU_USH,
                c_FU_UCN,
                c_FU_TEP,
                c_FU_SPR,
                c_FU_UBL,
                c_FU_FIS,
                c_FU_LBL,
                c_FU_LGP,
                c_FU_BEP,
                c_FU_LCN ])
# -------------------------------------------------------
# --- RR assemblies
# -------------------------------------------------------
# --- RR1 - Type I 
# -------------------------------------------------------

c_R1_OUT = openmc.Cell( name='c_R1_OUT')
c_R1_SHU = openmc.Cell( name='c_R1_SHU')
c_R1_USP = openmc.Cell( name='c_R1_USP')
c_R1_SSR = openmc.Cell( name='c_R1_SSR')
c_R1_LSP = openmc.Cell( name='c_R1_LSP')
c_R1_SHL = openmc.Cell( name='c_R1_SHL')

c_R1_OUT.region =               +pz_RR1_SHU  # Outside        
c_R1_SHU.region = -pz_RR1_SHU & +pz_RR1_USP  # Upper shield                 
c_R1_USP.region = -pz_RR1_USP & +pz_RR1_SSR  # Na plenum                    
c_R1_SSR.region = -pz_RR1_SSR & +pz_RR1_LSP  # SS rods cluster              
c_R1_LSP.region = -pz_RR1_LSP & +pz_RR1_SHL  # Na plenum                    
c_R1_SHL.region = -pz_RR1_SHL                # Lower shield   

c_R1_OUT.fill = u_RR_USH
c_R1_SHU.fill = u_RR_USH
c_R1_USP.fill = u_RR_SPL
c_R1_SSR.fill = u_RR_T1 
c_R1_LSP.fill = u_RR_SPL
c_R1_SHL.fill = u_RR_LSH

c_R1_OUT.rotation = [0, 0, 90]
c_R1_SHU.rotation = [0, 0, 90]
c_R1_USP.rotation = [0, 0, 90]
c_R1_SSR.rotation = [0, 0, 90]
c_R1_LSP.rotation = [0, 0, 90]
c_R1_SHL.rotation = [0, 0, 90]

a_R1 = openmc.Universe()
a_R1.add_cells([c_R1_OUT,
                c_R1_SHU,
                c_R1_USP,
                c_R1_SSR,
                c_R1_LSP,
                c_R1_SHL])


# -------------------------------------------------------
# --- RR2 - Type II
# -------------------------------------------------------
#
c_R2_OUT = openmc.Cell( name='c_R2_OUT')
c_R2_SHU = openmc.Cell( name='c_R2_SHU')
c_R2_USP = openmc.Cell( name='c_R2_USP')
c_R2_SSR = openmc.Cell( name='c_R2_SSR')
c_R2_LSP = openmc.Cell( name='c_R2_LSP')
c_R2_SHL = openmc.Cell( name='c_R2_SHL')

c_R2_OUT.region =               +pz_RR1_SHU  # Outside        
c_R2_SHU.region = -pz_RR1_SHU & +pz_RR1_USP  # Upper shield                 
c_R2_USP.region = -pz_RR1_USP & +pz_RR1_SSR  # Na plenum                    
c_R2_SSR.region = -pz_RR1_SSR & +pz_RR1_LSP  # SS rods cluster              
c_R2_LSP.region = -pz_RR1_LSP & +pz_RR1_SHL  # Na plenum                    
c_R2_SHL.region = -pz_RR1_SHL                # Lower shield   

c_R2_OUT.fill = u_RR_USH
c_R2_SHU.fill = u_RR_USH
c_R2_USP.fill = u_RR_SPL
c_R2_SSR.fill = u_RR_T2 
c_R2_LSP.fill = u_RR_SPL
c_R2_SHL.fill = u_RR_LSH

c_R2_OUT.rotation = [0, 0, 90]
c_R2_SHU.rotation = [0, 0, 90]
c_R2_USP.rotation = [0, 0, 90]
c_R2_SSR.rotation = [0, 0, 90]
c_R2_LSP.rotation = [0, 0, 90]
c_R2_SHL.rotation = [0, 0, 90]

a_R2 = openmc.Universe()
a_R2.add_cells([c_R2_OUT,
                c_R2_SHU,
                c_R2_USP,
                c_R2_SSR,
                c_R2_LSP,
                c_R2_SHL])

# -------------------------------------------------------
# --- RR3 - Type III 
# -------------------------------------------------------
#
c_R3_OUT = openmc.Cell( name='c_R3_OUT')
c_R3_RR3 = openmc.Cell( name='c_R3_RR3')
c_R3_LSP = openmc.Cell( name='c_R3_LSP')
c_R3_SHL = openmc.Cell( name='c_R3_SHL')

c_R3_OUT.region =               +pz_RR2_SHU   # Outside
c_R3_RR3.region = -pz_RR2_SHU & +pz_RR2_LSP   # Upper shield
c_R3_LSP.region = -pz_RR2_LSP & +pz_RR2_SHL   # Na plenum
c_R3_SHL.region = -pz_RR2_SHL                 # Lower shield

c_R3_OUT.fill = u_RR_USH
c_R3_RR3.fill = u_RR_T3 
c_R3_LSP.fill = u_RR_SPL
c_R3_SHL.fill = u_RR_LSH

c_R3_OUT.rotation = [0, 0, 90]
c_R3_RR3.rotation = [0, 0, 90]
c_R3_LSP.rotation = [0, 0, 90]
c_R3_SHL.rotation = [0, 0, 90]

a_R3 = openmc.Universe()
a_R3.add_cells([c_R3_OUT,
                c_R3_RR3,
                c_R3_LSP,
                c_R3_SHL])

# -------------------------------------------------------
# --- RR4 - Type IV 
# -------------------------------------------------------
#
c_R4_OUT = openmc.Cell( name='c_R4_OUT')
c_R4_RR3 = openmc.Cell( name='c_R4_RR3')
c_R4_LSP = openmc.Cell( name='c_R4_LSP')
c_R4_SHL = openmc.Cell( name='c_R4_SHL')

c_R4_OUT.region =               +pz_RR2_SHU   # Outside
c_R4_RR3.region = -pz_RR2_SHU & +pz_RR2_LSP   # Upper shield
c_R4_LSP.region = -pz_RR2_LSP & +pz_RR2_SHL   # Na plenum
c_R4_SHL.region = -pz_RR2_SHL                 # Lower shield

c_R4_OUT.fill = u_RR_USH
c_R4_RR3.fill = u_RR_T4 
c_R4_LSP.fill = u_RR_SPL
c_R4_SHL.fill = u_RR_LSH

c_R4_OUT.rotation = [0, 0, 90]
c_R4_RR3.rotation = [0, 0, 90]
c_R4_LSP.rotation = [0, 0, 90]
c_R4_SHL.rotation = [0, 0, 90]

a_R4 = openmc.Universe()
a_R4.add_cells([c_R4_OUT,
                c_R4_RR3,
                c_R4_LSP,
                c_R4_SHL])

# -------------------------------------------------------
# --- Radial boron shield assemblies
# -------------------------------------------------------
#

c_RB_OUT  = openmc.Cell( name='c_RB_OUT')
c_RB_SHU2 = openmc.Cell( name='c_RB_SHU2')
c_RB_USP  = openmc.Cell( name='c_RB_USP')
c_RB_SHU1 = openmc.Cell( name='c_RB_SHU1')
c_RB_RB   = openmc.Cell( name='c_RB_RB')
c_RB_SHL2 = openmc.Cell( name='c_RB_SHL2')
c_RB_LSP  = openmc.Cell( name='c_RB_LSP')
c_RB_SHL1 = openmc.Cell( name='c_RB_SHL1')

c_RB_OUT.region  =               +pz_RB_SHU2 # Outside    
c_RB_SHU2.region = -pz_RB_SHU2 & +pz_RB_USP  # Upper shield
c_RB_USP.region  = -pz_RB_USP  & +pz_RB_SHU1 # Na plenum
c_RB_SHU1.region = -pz_RB_SHU1 & +pz_RB_RB   # Upper shield
c_RB_RB.region   = -pz_RB_RB   & +pz_RB_SHL2 # Rod cluster
c_RB_SHL2.region = -pz_RB_SHL2 & +pz_RB_LSP  # Lower shield
c_RB_LSP.region  = -pz_RB_LSP  & +pz_RB_SHL1 # Na plenum
c_RB_SHL1.region = -pz_RB_SHL1               # Lower shield

c_RB_OUT.fill  = u_RB_USH
c_RB_SHU2.fill = u_RB_USH
c_RB_USP.fill  = u_RB_SPL
c_RB_SHU1.fill = u_RB_USH
c_RB_RB.fill   = u_RB    
c_RB_SHL2.fill = u_RB_LSH
c_RB_LSP.fill  = u_RB_SPL
c_RB_SHL1.fill = u_RB_LSH

c_RB_OUT.rotation  = [0, 0, 90]
c_RB_SHU2.rotation = [0, 0, 90]
c_RB_USP.rotation  = [0, 0, 90]
c_RB_SHU1.rotation = [0, 0, 90]
c_RB_RB.rotation   = [0, 0, 90]
c_RB_SHL2.rotation = [0, 0, 90]
c_RB_LSP.rotation  = [0, 0, 90]
c_RB_SHL1.rotation = [0, 0, 90]

a_RB = openmc.Universe()
a_RB.add_cells([c_RB_OUT,
                c_RB_SHU2,
                c_RB_USP,
                c_RB_SHU1,
                c_RB_RB,
                c_RB_SHL2,
                c_RB_LSP,
                c_RB_SHL1])

# -------------------------------------------------------
# --- Neutron Source assembly
# -------------------------------------------------------
                                                            

c_NS_OUT = openmc.Cell( name='c_NS_OUT')
c_NS_SHU = openmc.Cell( name='c_NS_SHU')
c_NS_USP = openmc.Cell( name='c_NS_USP')
c_NS_SSR = openmc.Cell( name='c_NS_SSR')
c_NS_NSR = openmc.Cell( name='c_NS_NSR')
c_NS_LSP = openmc.Cell( name='c_NS_LSP')
c_NS_SHL = openmc.Cell( name='c_NS_SHL')

c_NS_OUT.region =              +pz_NS_SHU  # Outside
c_NS_SHU.region = -pz_NS_SHU & +pz_NS_USP  # Upper shield
c_NS_USP.region = -pz_NS_USP & +pz_NS_SSR  # Na plenum 
c_NS_SSR.region = -pz_NS_SSR & +pz_NS_NSR  # SS rods cluster
c_NS_NSR.region = -pz_NS_NSR & +pz_NS_LSP  # NS rods cluster
c_NS_LSP.region = -pz_NS_LSP & +pz_NS_SHL  # Na plenum  
c_NS_SHL.region = -pz_NS_SHL               # Lower shield 

c_NS_OUT.fill = u_RR_USH
c_NS_SHU.fill = u_RR_USH
c_NS_USP.fill = u_RR_SPL
c_NS_SSR.fill = u_RR_T1 
c_NS_NSR.fill = u_NS    
c_NS_LSP.fill = u_RR_SPL
c_NS_SHL.fill = u_RR_LSH

c_NS_OUT.rotation = [0, 0, 90]
c_NS_SHU.rotation = [0, 0, 90]
c_NS_USP.rotation = [0, 0, 90]
c_NS_SSR.rotation = [0, 0, 90]
c_NS_NSR.rotation = [0, 0, 90]
c_NS_LSP.rotation = [0, 0, 90]
c_NS_SHL.rotation = [0, 0, 90]

a_NS = openmc.Universe()
a_NS.add_cells([c_NS_OUT,
                c_NS_SHU,
                c_NS_USP,
                c_NS_SSR,
                c_NS_NSR,
                c_NS_LSP,
                c_NS_SHL])

# -------------------------------------------------------
# --- Mock-up assembly
# -------------------------------------------------------

# -- Quite approximate model !!!
#same as Serpent#                                                           
c_l_filter1 = openmc.Cell( name='c_l_filter1')
c_l_filter2 = openmc.Cell( name='c_l_filter2')
c_l_filter3 = openmc.Cell( name='c_l_filter3')

c_l_filter1.region = -cyl_CR_BAF_IN
c_l_filter2.region = +cyl_CR_BAF_IN & -cyl_CR_BAF_OU 
c_l_filter3.region =                  +cyl_CR_BAF_OU

c_l_filter1.fill = Na_CR_In
c_l_filter2.fill = Ti316
c_l_filter3.fill = Na_CR_In

u_MU_FIL = openmc.Universe()
u_MU_FIL.add_cells([
c_l_filter1,
c_l_filter2,
c_l_filter3
])

# Add duct

#c_l_filter1 = openmc.Cell( name='c_l_filter1')
#c_l_filter2 = openmc.Cell( name='c_l_filter2')
#c_l_filter3 = openmc.Cell( name='c_l_filter3')
#c_l_filter4 = openmc.Cell( name='c_l_filter4')
#c_l_filter5 = openmc.Cell( name='c_l_filter5')
#
#c_l_filter1.region = -cyl_CR_BAF_IN
#c_l_filter2.region = +cyl_CR_BAF_IN & -cyl_CR_BAF_OU 
#c_l_filter3.region = +cyl_CR_BAF_OU & hex_WR_IN
#c_l_filter4.region = ~hex_WR_IN     & hex_WR_OU 
#c_l_filter5.region = ~hex_WR_OU
#
#c_l_filter1.fill = Na_CR_In
#c_l_filter2.fill = Ti316
#c_l_filter3.fill = Na_CR_In
#c_l_filter4.fill = Ti316
#c_l_filter5.fill = Na_FU_OUT_bypass
#
#u_MU_FIL = openmc.Universe()
#u_MU_FIL.add_cells([
#c_l_filter1,
#c_l_filter2,
#c_l_filter3,
#c_l_filter4, 
#c_l_filter5
#])


# -- Stack Assembly

c_MU_OUT = openmc.Cell( name='c_MU_OUT')
c_MU_SHU = openmc.Cell( name='c_MU_SHU')
c_MU_USP = openmc.Cell( name='c_MU_USP')
c_MU_SSR = openmc.Cell( name='c_MU_SSR')
c_MU_NSR = openmc.Cell( name='c_MU_NSR')

c_MU_OUT.region =              +pz_MU_SHU   # Outside
c_MU_SHU.region = -pz_MU_SHU & +pz_MU_USP   # Upper shield
c_MU_USP.region = -pz_MU_USP & +pz_MU_SSR   # Na plenum
c_MU_SSR.region = -pz_MU_SSR & +pz_MU_SHL   # Filter  
c_MU_NSR.region = -pz_MU_SHL                # Lower shield

c_MU_OUT.fill = u_FU_USH
c_MU_SHU.fill = u_FU_USH
c_MU_USP.fill = u_RR_SPL
c_MU_SSR.fill = u_MU_FIL
c_MU_NSR.fill = u_RR_LSH

c_MU_OUT.rotation = [0, 0, 90]
c_MU_SHU.rotation = [0, 0, 90]
c_MU_USP.rotation = [0, 0, 90]
c_MU_SSR.rotation = [0, 0, 90]
c_MU_NSR.rotation = [0, 0, 90]

a_MU = openmc.Universe()
a_MU.add_cells([c_MU_OUT,
                c_MU_SHU,
                c_MU_USP,
                c_MU_SSR,
                c_MU_NSR])


# -------------------------------------------------------
# --- 3D fuel assembly
# -------------------------------------------------------
#

#cell  c_VO_OUT  a_VO  fill u_VO_HEA  pz_FUEL_HEA                 # 12. Outside             20 deg-C    250 deg-C      
#cell  c_VO_HEA  a_VO  fill u_VO_HEA  pz_FUEL_USH -pz_FUEL_HEA    # 11. Head                26.00 cm    26.108 cm
#cell  c_VO_USH  a_VO  fill u_VO_USH  pz_FUEL_UCN -pz_FUEL_USH    # 10. Upper shield        44.00 cm    44.182 cm
#cell  c_VO_UCN  a_VO  fill u_VO_UCN  pz_FUEL_TEP -pz_FUEL_UCN    #  9. Upper connector      6.00 cm     6.025 cm
#cell  c_VO_TEP  a_VO  fill u_VO_TEP  pz_FUEL_SPR -pz_FUEL_TEP    #  8. Top end plug         2.00 cm     2.008 cm
#cell  c_VO_SPR  a_VO  fill u_VO_SPR  pz_FUEL_UBL -pz_FUEL_SPR    #  7. Spring               4.50 cm     4.519 cm
#cell  c_VO_UBL  a_VO  fill u_VO_UBL  pz_FUEL_FIS -pz_FUEL_UBL    #  6. Upper blanket       10.00 cm    10.023 cm
#cell  c_VO_FIS  a_VO  fill u_VO_FIS  pz_FUEL_LBL -pz_FUEL_FIS    #  5. Fissile             45.00 cm    45.114 cm
#cell  c_VO_LBL  a_VO  fill u_VO_LBL  pz_FUEL_LGP -pz_FUEL_LBL    #  4. Lower blanket       25.00 cm    25.058 cm
#cell  c_VO_LGP  a_VO  fill u_VO_LGP  pz_FUEL_BEP -pz_FUEL_LGP    #  3. Lower gas plenum    45.00 cm    45.186 cm
#cell  c_VO_BEP  a_VO  fill u_VO_BEP  pz_FUEL_LCN -pz_FUEL_BEP    #  2. Bottom end plug      3.50 cm     3.514 cm
#cell  c_VO_LCN  a_VO  fill u_VO_LCN              -pz_FUEL_LCN    #  1. Lower connector     10.00 cm    10.041 cm
                                                    
# 3D Universe - Fuel SA 
c_VO_OUT = openmc.Cell( name='c_VO_OUT')
c_VO_HEA = openmc.Cell( name='c_VO_HEA')
c_VO_USH = openmc.Cell( name='c_VO_USH')
c_VO_UCN = openmc.Cell( name='c_VO_UCN')
c_VO_TEP = openmc.Cell( name='c_VO_TEP')
c_VO_SPR = openmc.Cell( name='c_VO_SPR')
c_VO_UBL = openmc.Cell( name='c_VO_UBL')
c_VO_FIS = openmc.Cell( name='c_VO_FIS')
c_VO_LBL = openmc.Cell( name='c_VO_LBL')
c_VO_LGP = openmc.Cell( name='c_VO_LGP')
c_VO_BEP = openmc.Cell( name='c_VO_BEP')
c_VO_LCN = openmc.Cell( name='c_VO_LCN')

c_VO_OUT.region =                +pz_FUEL_HEA # -pz_TOP & +pz_FUEL_HEA
c_VO_HEA.region = -pz_FUEL_HEA & +pz_FUEL_USH 
c_VO_USH.region = -pz_FUEL_USH & +pz_FUEL_UCN 
c_VO_UCN.region = -pz_FUEL_UCN & +pz_FUEL_TEP 
c_VO_TEP.region = -pz_FUEL_TEP & +pz_FUEL_SPR 
c_VO_SPR.region = -pz_FUEL_SPR & +pz_FUEL_UBL 
c_VO_UBL.region = -pz_FUEL_UBL & +pz_FUEL_FIS 
c_VO_FIS.region = -pz_FUEL_FIS & +pz_FUEL_LBL 
c_VO_LBL.region = -pz_FUEL_LBL & +pz_FUEL_LGP 
c_VO_LGP.region = -pz_FUEL_LGP & +pz_FUEL_BEP 
c_VO_BEP.region = -pz_FUEL_BEP & +pz_FUEL_LCN 
c_VO_LCN.region = -pz_FUEL_LCN                # -pz_FUEL_LCN & +pz_BOT

c_VO_OUT.fill = u_VO_HEA
c_VO_HEA.fill = u_VO_HEA
c_VO_USH.fill = u_VO_USH
c_VO_UCN.fill = u_VO_UCN
c_VO_TEP.fill = u_VO_TEP
c_VO_SPR.fill = u_VO_SPR
c_VO_UBL.fill = u_VO_UBL
c_VO_FIS.fill = u_VO_FIS
c_VO_LBL.fill = u_VO_LBL
c_VO_LGP.fill = u_VO_LGP
c_VO_BEP.fill = u_VO_BEP
c_VO_LCN.fill = u_VO_LCN

c_VO_OUT.rotation = [0, 0, 90]
c_VO_HEA.rotation = [0, 0, 90]
c_VO_USH.rotation = [0, 0, 90]
c_VO_UCN.rotation = [0, 0, 90]
c_VO_TEP.rotation = [0, 0, 90]
c_VO_SPR.rotation = [0, 0, 90]
c_VO_UBL.rotation = [0, 0, 90]
c_VO_FIS.rotation = [0, 0, 90]
c_VO_LBL.rotation = [0, 0, 90]
c_VO_LGP.rotation = [0, 0, 90]
c_VO_BEP.rotation = [0, 0, 90]
c_VO_LCN.rotation = [0, 0, 90]

a_VO = openmc.Universe()
a_VO.add_cells([c_VO_OUT,
                c_VO_HEA,
                c_VO_USH,
                c_VO_UCN,
                c_VO_TEP,
                c_VO_SPR,
                c_VO_UBL,
                c_VO_FIS,
                c_VO_LBL,
                c_VO_LGP,
                c_VO_BEP,
                c_VO_LCN ])
#  Non-movable    Movable    Uppler B   ARO       What's in ARO
#  pz_CR_HEA      -          219.405    -         SHA_HEA
#  pz_CR_HCO      -          206.451    -         SHA_HCO
#  pz_CR_TRS      -          198.518    -         SHA_TRS
#  pz_CR_UPL      -          197.514    -         SHA_UPL
#  pz_CR_WRA      -          130.839    -         UCO_UPL
#  -              pz_CR_UCO  68.32      193.183   PLE_UPL
#  -              pz_CR_PLE  61.794     186.657   ABS_UPL
#  -              pz_CR_ABS  58.681     183.544   LCO_UPL
#  -              pz_CR_LCO  7.631      132.494   LCO_WRA
#  -              pz_CR_BAF  4.217      129.08    BAF_WRA
#  -              pz_CR_BOT  0          124.863   BOT_WRA
#  pz_CR_SHL      -          65.872     -         -      

#  pz_CR_BOT ~ pz_CR_UCO = pz_CR_SHL+8.991+pz_CR_XXX

# --- Enriched B4C - Safety rod (u_CR_move_SAFT)

# --- Moving CR1 (B4C enr) by changing Z-coordinate in trans. Z=0 --> bottom of the system
#trans u_CR_move_SAFT 0.0 0.0 124.863 % Based on 250 deg-C
pz_CR1_SHA_HEA = openmc.ZPlane( z0= 219.405, name='pz_CR1_SHA_HEA')
pz_CR1_SHA_HCO = openmc.ZPlane( z0= 206.451, name='pz_CR1_SHA_HCO')
pz_CR1_SHA_TRS = openmc.ZPlane( z0= 198.518, name='pz_CR1_SHA_TRS')
pz_CR1_SHA_UPL = openmc.ZPlane( z0= 197.514, name='pz_CR1_SHA_UPL')
pz_CR1_UCO_UPL = openmc.ZPlane( z0= 193.183, name='pz_CR1_UCO_UPL')
pz_CR1_PLE_UPL = openmc.ZPlane( z0= 186.657, name='pz_CR1_PLE_UPL')
pz_CR1_ABS_UPL = openmc.ZPlane( z0= 183.544, name='pz_CR1_ABS_UPL')
pz_CR1_LCO_UPL = openmc.ZPlane( z0= 132.494, name='pz_CR1_LCO_UPL')
pz_CR1_LCO_WRA = openmc.ZPlane( z0= 130.839, name='pz_CR1_LCO_WRA')
pz_CR1_BAF_WRA = openmc.ZPlane( z0= 129.080, name='pz_CR1_BAF_WRA')
pz_CR1_BOT_WRA = openmc.ZPlane( z0= 124.863, name='pz_CR1_BOT_WRA')
pz_CR1_SHL     = openmc.ZPlane( z0=  65.872, name='pz_CR1_SHL')    


# --- Inside wrapper cells
c_CR1_00 = openmc.Cell( name='c_CR1_00')
c_CR1_01 = openmc.Cell( name='c_CR1_01')
c_CR1_02 = openmc.Cell( name='c_CR1_02')
c_CR1_03 = openmc.Cell( name='c_CR1_03')
c_CR1_04 = openmc.Cell( name='c_CR1_04')
c_CR1_05 = openmc.Cell( name='c_CR1_05')
c_CR1_06 = openmc.Cell( name='c_CR1_06')
c_CR1_07 = openmc.Cell( name='c_CR1_07')
c_CR1_08 = openmc.Cell( name='c_CR1_08')
c_CR1_09 = openmc.Cell( name='c_CR1_09')
c_CR1_10 = openmc.Cell( name='c_CR1_10')
c_CR1_11 = openmc.Cell( name='c_CR1_11')
c_CR1_12 = openmc.Cell( name='c_CR1_12')

# --- ARO
c_CR1_00.region =                   +pz_CR1_SHA_HEA
c_CR1_01.region = -pz_CR1_SHA_HEA & +pz_CR1_SHA_HCO
c_CR1_02.region = -pz_CR1_SHA_HCO & +pz_CR1_SHA_TRS
c_CR1_03.region = -pz_CR1_SHA_TRS & +pz_CR1_SHA_UPL
c_CR1_04.region = -pz_CR1_SHA_UPL & +pz_CR1_UCO_UPL
c_CR1_05.region = -pz_CR1_UCO_UPL & +pz_CR1_PLE_UPL
c_CR1_06.region = -pz_CR1_PLE_UPL & +pz_CR1_ABS_UPL
c_CR1_07.region = -pz_CR1_ABS_UPL & +pz_CR1_LCO_UPL
c_CR1_08.region = -pz_CR1_LCO_UPL & +pz_CR1_LCO_WRA
c_CR1_09.region = -pz_CR1_LCO_WRA & +pz_CR1_BAF_WRA
c_CR1_10.region = -pz_CR1_BAF_WRA & +pz_CR1_BOT_WRA
c_CR1_11.region = -pz_CR1_BOT_WRA & +pz_CR1_SHL    
c_CR1_12.region = -pz_CR1_SHL     

c_CR1_00.fill = u_CR_SHA_HEA_SAFT
c_CR1_01.fill = u_CR_SHA_HEA_SAFT
c_CR1_02.fill = u_CR_SHA_HCO_SAFT
c_CR1_03.fill = u_CR_SHA_TRS_SAFT
c_CR1_04.fill = u_CR_SHA_UPL_SAFT
c_CR1_05.fill = u_CR_UCO_UPL_SAFT
c_CR1_06.fill = u_CR_PLE_UPL_SAFT
c_CR1_07.fill = u_CR_ABS_UPL_SAFT
c_CR1_08.fill = u_CR_LCO_UPL_SAFT
c_CR1_09.fill = u_CR_LCO_WRA_SAFT
c_CR1_10.fill = u_CR_BAF_WRA_SAFT
c_CR1_11.fill = u_CR_BOT_WRA_SAFT
c_CR1_12.fill = u_CR_LSH

c_CR1_00.rotation = [0, 0, 90]
c_CR1_01.rotation = [0, 0, 90]
c_CR1_02.rotation = [0, 0, 90]
c_CR1_03.rotation = [0, 0, 90]
c_CR1_04.rotation = [0, 0, 90]
c_CR1_05.rotation = [0, 0, 90]
c_CR1_06.rotation = [0, 0, 90]
c_CR1_07.rotation = [0, 0, 90]
c_CR1_08.rotation = [0, 0, 90]
c_CR1_09.rotation = [0, 0, 90]
c_CR1_10.rotation = [0, 0, 90]
c_CR1_11.rotation = [0, 0, 90]
c_CR1_12.rotation = [0, 0, 90]

a_C1 = openmc.Universe()
a_C1.add_cells([c_CR1_00,
                c_CR1_01,
                c_CR1_02,
                c_CR1_03,
                c_CR1_04,
                c_CR1_05,
                c_CR1_06,
                c_CR1_07,
                c_CR1_08,
                c_CR1_09,
                c_CR1_10,
                c_CR1_11,
                c_CR1_12])

# --- Natural B4C - Regulating rod 1 (u_CR_move_REGL11)

# --- Moving CR2-1 (B4C nat) by changing Z-coordinate in trans. Z=0 --> bottom of the system
#trans u_CR_move_REGL1 0.0 0.0 124.863 % Based on 250 deg-C 
pz_CR21_SHA_HEA = openmc.ZPlane( z0= 219.405, name='pz_CR21_SHA_HEA')
pz_CR21_SHA_HCO = openmc.ZPlane( z0= 206.451, name='pz_CR21_SHA_HCO')
pz_CR21_SHA_TRS = openmc.ZPlane( z0= 198.518, name='pz_CR21_SHA_TRS')
pz_CR21_SHA_UPL = openmc.ZPlane( z0= 197.514, name='pz_CR21_SHA_UPL')
pz_CR21_UCO_UPL = openmc.ZPlane( z0= 193.183, name='pz_CR21_UCO_UPL')
pz_CR21_PLE_UPL = openmc.ZPlane( z0= 186.657, name='pz_CR21_PLE_UPL')
pz_CR21_ABS_UPL = openmc.ZPlane( z0= 183.544, name='pz_CR21_ABS_UPL')
pz_CR21_LCO_UPL = openmc.ZPlane( z0= 132.494, name='pz_CR21_LCO_UPL')
pz_CR21_LCO_WRA = openmc.ZPlane( z0= 130.839, name='pz_CR21_LCO_WRA')
pz_CR21_BAF_WRA = openmc.ZPlane( z0= 129.080, name='pz_CR21_BAF_WRA')
pz_CR21_BOT_WRA = openmc.ZPlane( z0= 124.863, name='pz_CR21_BOT_WRA')
pz_CR21_SHL     = openmc.ZPlane( z0=  65.872, name='pz_CR21_SHL')    


# --- Inside wrapper cells
c_CR21_00 = openmc.Cell( name='c_CR21_00')
c_CR21_01 = openmc.Cell( name='c_CR21_01')
c_CR21_02 = openmc.Cell( name='c_CR21_02')
c_CR21_03 = openmc.Cell( name='c_CR21_03')
c_CR21_04 = openmc.Cell( name='c_CR21_04')
c_CR21_05 = openmc.Cell( name='c_CR21_05')
c_CR21_06 = openmc.Cell( name='c_CR21_06')
c_CR21_07 = openmc.Cell( name='c_CR21_07')
c_CR21_08 = openmc.Cell( name='c_CR21_08')
c_CR21_09 = openmc.Cell( name='c_CR21_09')
c_CR21_10 = openmc.Cell( name='c_CR21_10')
c_CR21_11 = openmc.Cell( name='c_CR21_11')
c_CR21_12 = openmc.Cell( name='c_CR21_12')

# --- ARO
c_CR21_00.region =                   +pz_CR21_SHA_HEA
c_CR21_01.region = -pz_CR21_SHA_HEA & +pz_CR21_SHA_HCO
c_CR21_02.region = -pz_CR21_SHA_HCO & +pz_CR21_SHA_TRS
c_CR21_03.region = -pz_CR21_SHA_TRS & +pz_CR21_SHA_UPL
c_CR21_04.region = -pz_CR21_SHA_UPL & +pz_CR21_UCO_UPL
c_CR21_05.region = -pz_CR21_UCO_UPL & +pz_CR21_PLE_UPL
c_CR21_06.region = -pz_CR21_PLE_UPL & +pz_CR21_ABS_UPL
c_CR21_07.region = -pz_CR21_ABS_UPL & +pz_CR21_LCO_UPL
c_CR21_08.region = -pz_CR21_LCO_UPL & +pz_CR21_LCO_WRA
c_CR21_09.region = -pz_CR21_LCO_WRA & +pz_CR21_BAF_WRA
c_CR21_10.region = -pz_CR21_BAF_WRA & +pz_CR21_BOT_WRA
c_CR21_11.region = -pz_CR21_BOT_WRA & +pz_CR21_SHL    
c_CR21_12.region = -pz_CR21_SHL     

c_CR21_00.fill = u_CR_SHA_HEA_REGL1
c_CR21_01.fill = u_CR_SHA_HEA_REGL1
c_CR21_02.fill = u_CR_SHA_HCO_REGL1
c_CR21_03.fill = u_CR_SHA_TRS_REGL1
c_CR21_04.fill = u_CR_SHA_UPL_REGL1
c_CR21_05.fill = u_CR_UCO_UPL_REGL1
c_CR21_06.fill = u_CR_PLE_UPL_REGL1
c_CR21_07.fill = u_CR_ABS_UPL_REGL1
c_CR21_08.fill = u_CR_LCO_UPL_REGL1
c_CR21_09.fill = u_CR_LCO_WRA_REGL1
c_CR21_10.fill = u_CR_BAF_WRA_REGL1
c_CR21_11.fill = u_CR_BOT_WRA_REGL1
c_CR21_12.fill = u_CR_LSH

c_CR21_00.rotation = [0, 0, 90]
c_CR21_01.rotation = [0, 0, 90]
c_CR21_02.rotation = [0, 0, 90]
c_CR21_03.rotation = [0, 0, 90]
c_CR21_04.rotation = [0, 0, 90]
c_CR21_05.rotation = [0, 0, 90]
c_CR21_06.rotation = [0, 0, 90]
c_CR21_07.rotation = [0, 0, 90]
c_CR21_08.rotation = [0, 0, 90]
c_CR21_09.rotation = [0, 0, 90]
c_CR21_10.rotation = [0, 0, 90]
c_CR21_11.rotation = [0, 0, 90]
c_CR21_12.rotation = [0, 0, 90]

a_C21 = openmc.Universe()
a_C21.add_cells([c_CR21_00,
                 c_CR21_01,
                 c_CR21_02,
                 c_CR21_03,
                 c_CR21_04,
                 c_CR21_05,
                 c_CR21_06,
                 c_CR21_07,
                 c_CR21_08,
                 c_CR21_09,
                 c_CR21_10,
                 c_CR21_11,
                 c_CR21_12])




# --- Natural B4C - Regulating rod 2 (u_CR_move_REGL2)

# WP1 movable
# --- Moving CR2-2 (B4C nat) by changing Z-coordinate in trans. Z=0 --> bottom of the system
#trans u_CR_move_REGL2 0.0 0.0 81.863 % Based on 250 deg-C 
pz_CR22_SHA_HEA = openmc.ZPlane( z0= 219.405, name='pz_CR22_SHA_HEA')
pz_CR22_SHA_HCO = openmc.ZPlane( z0= 206.451, name='pz_CR22_SHA_HCO')
pz_CR22_SHA_TRS = openmc.ZPlane( z0= 198.518, name='pz_CR22_SHA_TRS')
pz_CR22_SHA_UPL = openmc.ZPlane( z0= 197.514, name='pz_CR22_SHA_UPL')
pz_CR22_UCO_UPL = openmc.ZPlane( z0= 193.183, name='pz_CR22_UCO_UPL')
pz_CR22_PLE_UPL = openmc.ZPlane( z0= 186.657, name='pz_CR22_PLE_UPL')
pz_CR22_ABS_UPL = openmc.ZPlane( z0= 183.544, name='pz_CR22_ABS_UPL')
pz_CR22_ABS_WRA = openmc.ZPlane( z0= 132.494, name='pz_CR22_ABS_WRA')
pz_CR22_LCO_WRA = openmc.ZPlane( z0= 130.839, name='pz_CR22_LCO_WRA')
pz_CR22_BAF_WRA = openmc.ZPlane( z0= 129.080, name='pz_CR22_BAF_WRA')
pz_CR22_BOT_WRA = openmc.ZPlane( z0= 124.863, name='pz_CR22_BOT_WRA')
pz_CR22_SHL     = openmc.ZPlane( z0=  65.872, name='pz_CR22_SHL')    

# --- Inside wrapper cells
c_CR22_00 = openmc.Cell( name='c_CR22_00')
c_CR22_01 = openmc.Cell( name='c_CR22_01')
c_CR22_02 = openmc.Cell( name='c_CR22_02')
c_CR22_03 = openmc.Cell( name='c_CR22_03')
c_CR22_04 = openmc.Cell( name='c_CR22_04')
c_CR22_05 = openmc.Cell( name='c_CR22_05')
c_CR22_06 = openmc.Cell( name='c_CR22_06')
c_CR22_07 = openmc.Cell( name='c_CR22_07')
c_CR22_08 = openmc.Cell( name='c_CR22_08')
c_CR22_09 = openmc.Cell( name='c_CR22_09')
c_CR22_10 = openmc.Cell( name='c_CR22_10')
c_CR22_11 = openmc.Cell( name='c_CR22_11')
c_CR22_12 = openmc.Cell( name='c_CR22_12')

# --- ARO
c_CR22_00.region =                   +pz_CR22_SHA_HEA
c_CR22_01.region = -pz_CR22_SHA_HEA & +pz_CR22_SHA_HCO
c_CR22_02.region = -pz_CR22_SHA_HCO & +pz_CR22_SHA_TRS
c_CR22_03.region = -pz_CR22_SHA_TRS & +pz_CR22_SHA_UPL
c_CR22_04.region = -pz_CR22_SHA_UPL & +pz_CR22_UCO_UPL
c_CR22_05.region = -pz_CR22_UCO_UPL & +pz_CR22_PLE_UPL
c_CR22_06.region = -pz_CR22_PLE_UPL & +pz_CR22_ABS_UPL
c_CR22_07.region = -pz_CR22_ABS_UPL & +pz_CR22_ABS_WRA
c_CR22_08.region = -pz_CR22_ABS_WRA & +pz_CR22_LCO_WRA
c_CR22_09.region = -pz_CR22_LCO_WRA & +pz_CR22_BAF_WRA
c_CR22_10.region = -pz_CR22_BAF_WRA & +pz_CR22_BOT_WRA
c_CR22_11.region = -pz_CR22_BOT_WRA & +pz_CR22_SHL    
c_CR22_12.region = -pz_CR22_SHL     

c_CR22_00.fill = u_CR_SHA_HEA_REGL2
c_CR22_01.fill = u_CR_SHA_HEA_REGL2
c_CR22_02.fill = u_CR_SHA_HCO_REGL2
c_CR22_03.fill = u_CR_SHA_TRS_REGL2
c_CR22_04.fill = u_CR_SHA_UPL_REGL2
c_CR22_05.fill = u_CR_UCO_UPL_REGL2
c_CR22_06.fill = u_CR_PLE_UPL_REGL2
c_CR22_07.fill = u_CR_ABS_UPL_REGL2
c_CR22_08.fill = u_CR_ABS_WRA_REGL2
c_CR22_09.fill = u_CR_LCO_WRA_REGL2
c_CR22_10.fill = u_CR_BAF_WRA_REGL2
c_CR22_11.fill = u_CR_BOT_WRA_REGL2
c_CR22_12.fill = u_CR_LSH

c_CR22_00.rotation = [0, 0, 90]
c_CR22_01.rotation = [0, 0, 90]
c_CR22_02.rotation = [0, 0, 90]
c_CR22_03.rotation = [0, 0, 90]
c_CR22_04.rotation = [0, 0, 90]
c_CR22_05.rotation = [0, 0, 90]
c_CR22_06.rotation = [0, 0, 90]
c_CR22_07.rotation = [0, 0, 90]
c_CR22_08.rotation = [0, 0, 90]
c_CR22_09.rotation = [0, 0, 90]
c_CR22_10.rotation = [0, 0, 90]
c_CR22_11.rotation = [0, 0, 90]
c_CR22_12.rotation = [0, 0, 90]

a_C22 = openmc.Universe()
a_C22.add_cells([c_CR22_00,
                 c_CR22_01,
                 c_CR22_02,
                 c_CR22_03,
                 c_CR22_04,
                 c_CR22_05,
                 c_CR22_06,
                 c_CR22_07,
                 c_CR22_08,
                 c_CR22_09,
                 c_CR22_10,
                 c_CR22_11,
                 c_CR22_12])



# --- Enriched B4C - Shim rod (u_CR_move_SHIM)

# --- Moving CR3 (B4C enr) by changing Z-coordinate in trans. Z=0 --> bottom of the system
#trans u_CR_move_SHIM 0.0 0.0 124.863 %  Based on 250 deg-C
pz_CR3_SHA_HEA = openmc.ZPlane( z0= 219.405, name='pz_CR3_SHA_HEA')
pz_CR3_SHA_HCO = openmc.ZPlane( z0= 206.451, name='pz_CR3_SHA_HCO')
pz_CR3_SHA_TRS = openmc.ZPlane( z0= 198.518, name='pz_CR3_SHA_TRS')
pz_CR3_SHA_UPL = openmc.ZPlane( z0= 197.514, name='pz_CR3_SHA_UPL')
pz_CR3_UCO_UPL = openmc.ZPlane( z0= 193.183, name='pz_CR3_UCO_UPL')
pz_CR3_PLE_UPL = openmc.ZPlane( z0= 186.657, name='pz_CR3_PLE_UPL')
pz_CR3_ABS_UPL = openmc.ZPlane( z0= 183.544, name='pz_CR3_ABS_UPL')
pz_CR3_LCO_UPL = openmc.ZPlane( z0= 132.494, name='pz_CR3_LCO_UPL')
pz_CR3_LCO_WRA = openmc.ZPlane( z0= 130.839, name='pz_CR3_LCO_WRA')
pz_CR3_BAF_WRA = openmc.ZPlane( z0= 129.080, name='pz_CR3_BAF_WRA')
pz_CR3_BOT_WRA = openmc.ZPlane( z0= 124.863, name='pz_CR3_BOT_WRA')
pz_CR3_SHL     = openmc.ZPlane( z0=  65.872, name='pz_CR3_SHL')    


# --- Inside wrapper cells
c_CR3_00 = openmc.Cell( name='c_CR3_00')
c_CR3_01 = openmc.Cell( name='c_CR3_01')
c_CR3_02 = openmc.Cell( name='c_CR3_02')
c_CR3_03 = openmc.Cell( name='c_CR3_03')
c_CR3_04 = openmc.Cell( name='c_CR3_04')
c_CR3_05 = openmc.Cell( name='c_CR3_05')
c_CR3_06 = openmc.Cell( name='c_CR3_06')
c_CR3_07 = openmc.Cell( name='c_CR3_07')
c_CR3_08 = openmc.Cell( name='c_CR3_08')
c_CR3_09 = openmc.Cell( name='c_CR3_09')
c_CR3_10 = openmc.Cell( name='c_CR3_10')
c_CR3_11 = openmc.Cell( name='c_CR3_11')
c_CR3_12 = openmc.Cell( name='c_CR3_12')

# --- ARO
c_CR3_00.region =                   +pz_CR3_SHA_HEA
c_CR3_01.region = -pz_CR3_SHA_HEA & +pz_CR3_SHA_HCO
c_CR3_02.region = -pz_CR3_SHA_HCO & +pz_CR3_SHA_TRS
c_CR3_03.region = -pz_CR3_SHA_TRS & +pz_CR3_SHA_UPL
c_CR3_04.region = -pz_CR3_SHA_UPL & +pz_CR3_UCO_UPL
c_CR3_05.region = -pz_CR3_UCO_UPL & +pz_CR3_PLE_UPL
c_CR3_06.region = -pz_CR3_PLE_UPL & +pz_CR3_ABS_UPL
c_CR3_07.region = -pz_CR3_ABS_UPL & +pz_CR3_LCO_UPL
c_CR3_08.region = -pz_CR3_LCO_UPL & +pz_CR3_LCO_WRA
c_CR3_09.region = -pz_CR3_LCO_WRA & +pz_CR3_BAF_WRA
c_CR3_10.region = -pz_CR3_BAF_WRA & +pz_CR3_BOT_WRA
c_CR3_11.region = -pz_CR3_BOT_WRA & +pz_CR3_SHL    
c_CR3_12.region = -pz_CR3_SHL     

c_CR3_00.fill = u_CR_SHA_HEA_SHIM
c_CR3_01.fill = u_CR_SHA_HEA_SHIM
c_CR3_02.fill = u_CR_SHA_HCO_SHIM
c_CR3_03.fill = u_CR_SHA_TRS_SHIM
c_CR3_04.fill = u_CR_SHA_UPL_SHIM
c_CR3_05.fill = u_CR_UCO_UPL_SHIM
c_CR3_06.fill = u_CR_PLE_UPL_SHIM
c_CR3_07.fill = u_CR_ABS_UPL_SHIM
c_CR3_08.fill = u_CR_LCO_UPL_SHIM
c_CR3_09.fill = u_CR_LCO_WRA_SHIM
c_CR3_10.fill = u_CR_BAF_WRA_SHIM
c_CR3_11.fill = u_CR_BOT_WRA_SHIM
c_CR3_12.fill = u_CR_LSH

c_CR3_00.rotation = [0, 0, 90]
c_CR3_01.rotation = [0, 0, 90]
c_CR3_02.rotation = [0, 0, 90]
c_CR3_03.rotation = [0, 0, 90]
c_CR3_04.rotation = [0, 0, 90]
c_CR3_05.rotation = [0, 0, 90]
c_CR3_06.rotation = [0, 0, 90]
c_CR3_07.rotation = [0, 0, 90]
c_CR3_08.rotation = [0, 0, 90]
c_CR3_09.rotation = [0, 0, 90]
c_CR3_10.rotation = [0, 0, 90]
c_CR3_11.rotation = [0, 0, 90]
c_CR3_12.rotation = [0, 0, 90]

a_C3 = openmc.Universe()
a_C3.add_cells([c_CR3_00,
                c_CR3_01,
                c_CR3_02,
                c_CR3_03,
                c_CR3_04,
                c_CR3_05,
                c_CR3_06,
                c_CR3_07,
                c_CR3_08,
                c_CR3_09,
                c_CR3_10,
                c_CR3_11,
                c_CR3_12])

#CORE Lattice
l_core = openmc.HexLattice()
l_core.center = [0., 0.]
l_core.pitch  = [6.12525]
# List of universes in the map:
# OpenMC -Serpent- Explain                      | Amount
# a_FU   - a_FU  - Fuel Assembly                | 78   
# a_R1   - a_R1  - 1-Steel Shielding Assembly   | 2    
# a_R2   - a_R2  - 2-Steel Shielding Assembly   | 37   
# a_R3   - a_R3  - 3-Steel Shielding Assembly   | 132  
# a_R4   - a_R4  - 4-Steel Shielding Assembly   | 223  
# a_RB   - a_RB  - Boron Shielding Assembly     | 230  
# a_C1   - a_C1  - Safety Rod Assembly, SA1     | 1    
# a_C1   - a_C1  - Safety Rod Assembly, SA1     | 1    
# a_C1   - a_C1  - Safety Rod Assembly, SA3     | 1    
# a_C21  - a_C21 - Regulating Rod Assembly, RE1 | 1    
# a_C22  - a_C22 - Regulating Rod Assembly, RE2 | 1    
# a_C3   - a_C3  - Shim Rod Assembly, SH1       | 1    
# a_C3   - a_C3  - Shim Rod Assembly, SH2       | 1    
# a_C3   - a_C3  - Shim Rod Assembly, SH3       | 1    
# a_NS   - a_NS  - Neutron Source Assembly      | 1    
# a_OU   - a_OU                                 | 515  
# a_VO   - a_VO  - Na Void Assembly             | 1    
# a_MU   - a_MU  - Mock-up Assembly             | 0    
# 
l_core.universes = \
       [ 
         [a_OU]*102,
         [a_OU]*4 +[a_R4]   +[a_RB]*8 +[a_OU]*7 +[a_RB]*9 +[a_OU]*7 +[a_RB]*3 +[a_OU]*19+[a_RB]*3 +[a_OU]*7 +[a_RB]*9 +[a_OU]*7 +[a_RB]*8 +[a_R4]   +[a_OU]*3 ,
         [a_OU]*2 +[a_R4]*3 +[a_RB]*3 +[a_R4]*5 +[a_RB]   +[a_OU]*3 +[a_RB]   +[a_R4]*10+[a_RB]   +[a_OU]*3 +[a_RB]   +[a_R4]*3 +[a_RB]*2 +[a_OU]*15+[a_RB]*2 +[a_R4]*3 +[a_RB]   +[a_OU]*3 +[a_RB]   +[a_R4]*10+[a_RB]   +[a_OU]*3 +[a_RB]   +[a_R4]*5 +[a_RB]*3 +[a_R4]*3 +[a_OU]   ,
         [a_R4]*5 +[a_RB]*7 +[a_R4]*2 +[a_RB]   +[a_R4]*2 +[a_RB]*9 +[a_R4]*2 +[a_RB]   +[a_R4]*2 +[a_RB]*5 +[a_R4]   +[a_OU]*11+[a_R4]   +[a_RB]*5 +[a_R4]*2 +[a_RB]   +[a_R4]*2 +[a_RB]*9 +[a_R4]*2 +[a_RB]   +[a_R4]*2 +[a_RB]*7 +[a_R4]*4 ,
         [a_R4]*5 +[a_RB]*8 +[a_R4]   +[a_RB]*12+[a_R4]   +[a_RB]*6 +[a_R4]*3 +[a_OU]*7 +[a_R4]*3 +[a_RB]*6 +[a_R4]   +[a_RB]*12+[a_R4]   +[a_RB]*8 +[a_R4]*4 ,
         [a_R4]*5 +[a_RB]*25+[a_R4]*5 +[a_OU]*3 +[a_R4]*5 +[a_RB]*25+[a_R4]*4 ,
         [a_R4]*9 +[a_RB]*5 +[a_R4]*6 +[a_RB]*5 +[a_R4]*17+[a_RB]*5 +[a_R4]*6 +[a_RB]*5 +[a_R4]*8 ,
         [a_R4]*3 +[a_R3]*2 +[a_R4]*5 +[a_RB]   +[a_R4]*2 +[a_R3]*2 +[a_R4]*5 +[a_RB]   +[a_R4]*2 +[a_R3]*2 +[a_R4]*8 +[a_R3]*2 +[a_R4]*5 +[a_RB]   +[a_R4]*2 +[a_R3]*2 +[a_R4]*5 +[a_RB]   +[a_R4]*2 +[a_R3]*2 +[a_R4]*5 , 
         [a_R4]*2 +[a_R3]*5 +[a_R4]*4 +[a_R3]*5 +[a_R4]*4 +[a_R3]*5 +[a_R4]*4 +[a_R3]*5 +[a_R4]*4 +[a_R3]*5 +[a_R4]*4 +[a_R3]*5 +[a_R4]*2 ,
         [a_R3]*48,
         [a_R3]*42,
         [a_R2]*8 +[a_C21]  +[a_R2]*19+[a_C22]  +[a_R2]*7 ,
         [a_FU]*5 +[a_R2]   +[a_FU]*9 +[a_R2]   +[a_FU]*9 +[a_R2]   +[a_FU]*4 ,
         [a_C1]  +[a_FU]   +[a_VO]  +[a_FU]*3 +[a_R1]   +[a_FU]   +[a_C1]  +[a_FU]*7 +[a_C1]    +[a_FU]   +[a_R1]   +[a_FU]*5 ,
         [a_FU]*18,                                     
         [a_FU]*2 +[a_C3]  +[a_FU]*3 +[a_C3]  +[a_FU]*3 +[a_C3]  +[a_FU]   ,
         [a_FU]*6 ,
         [a_NS]
       ]

l_core.outer = a_OU 

cell1000 = openmc.Cell(name='cell1000')

cell1000.region = hexcore & -pz_TOP & +pz_BOT

cell1000.fill = l_core

root = openmc.Universe(name='root universe')
root.add_cells([cell1000])
# Instantiate a Geometry, register the root Universe, and export to XML
geometry = openmc.Geometry(root)                                       
geometry.export_to_xml()                                               
###############################################################################
#                   Exporting to OpenMC settings.xml file
###############################################################################

# Instantiate a Settings object, set all runtime parameters, and export to XML
settings_file = openmc.Settings()
settings_file.batches   = 1050   # sum of active & inactive cycles
settings_file.inactive  = 50     
settings_file.particles = 100000
settings_file.ptables   = True
#Settings_file.temperature=openmc.stats(multipole, True)
# Create an initial uniform spatial source distribution over fissionable zones
bounds = [-50.0, -50.0, 120.0, 50.0,  50.0, 120.0]
uniform_dist = openmc.stats.Box(bounds[:3], bounds[3:], only_fissionable=True )
settings_file.source = openmc.source.Source(space=uniform_dist)

settings_file.export_to_xml()
###############################################################################
#                   Exporting to OpenMC plots.xml file
###############################################################################

plot_xy = openmc.Plot()
plot_xy.filename = 'plot_xy_x00y00z080'
plot_xy.origin = [0, 0,  80]
plot_xy.width = [200.0, 200.0]
plot_xy.pixels = [2000, 2000]
plot_xy.color_by = 'material'
plot_xy.colors={
UOF             :(150,   0,   0),
UOB             :(  0,   0, 150),
SS              :(150, 150, 150),
Ti316           :(101, 100, 100),
B4Cenr          :(100, 180, 245),
B4Cnat1         :( 80,  80,  80),
B4Cnat2         :( 80,  80,  80),
He              :(249, 249, 249),
vacuum          :(254, 254, 254), #(255, 153,  51), 
Na_FU_Out       :(230, 255, 255),
Na_FU_FI        :(230, 255, 255),
Na_FU_FE        :(230, 255, 255),
Na_FU_In        :(230, 255, 255),
Na_FU_OUT_bypass:(230, 255, 255),
Na_FU_FI_bypass :(230, 255, 255),
Na_FU_FE_bypass :(230, 255, 255),
Na_FU_In_bypass :(230, 255, 255),
Na_CR_Out       :(230, 255, 255),
Na_CR_In        :(230, 255, 255),
Na_RR_In        :(230, 255, 255),
Na_RR_Out       :(230, 255, 255),
SS_R1           :(255, 255,   0),
SS_R2           :( 36, 255,  36),
SS_R3           :( 88, 199, 255),
SS_R4           :(230, 153, 255),
HOMOG_SPR_FU    :(  0, 248,   0),
HOMOG_CR_CON    :(100, 100, 100) 
}

plot_xy2 = openmc.Plot()
plot_xy2.filename = 'plot_xy_x00y00z120'
plot_xy2.origin = [0, 0, 120]
plot_xy2.width = [200., 200.]
plot_xy2.pixels = [2000, 2000]
plot_xy2.color_by = 'material'
plot_xy2.colors={
UOF             :(150,   0,   0),
UOB             :(  0,   0, 150),
SS              :(150, 150, 150),
Ti316           :(101, 100, 100),
B4Cenr          :(100, 180, 245),
B4Cnat1         :( 80,  80,  80),
B4Cnat2         :( 80,  80,  80),
He              :(249, 249, 249),
vacuum          :(254, 254, 254), #(255, 153,  51), 
Na_FU_Out       :(230, 255, 255),
Na_FU_FI        :(230, 255, 255),
Na_FU_FE        :(230, 255, 255),
Na_FU_In        :(230, 255, 255),
Na_FU_OUT_bypass:(230, 255, 255),
Na_FU_FI_bypass :(230, 255, 255),
Na_FU_FE_bypass :(230, 255, 255),
Na_FU_In_bypass :(230, 255, 255),
Na_CR_Out       :(230, 255, 255),
Na_CR_In        :(230, 255, 255),
Na_RR_In        :(230, 255, 255),
Na_RR_Out       :(230, 255, 255),
SS_R1           :(255, 255,   0),
SS_R2           :( 36, 255,  36),
SS_R3           :( 88, 199, 255),
SS_R4           :(230, 153, 255),
HOMOG_SPR_FU    :(  0, 248,   0),
HOMOG_CR_CON    :(100, 100, 100) 
}

plot_mat = openmc.Plot()
plot_mat.filename = 'plot_xy_x00y00z135'
plot_mat.origin = [0, 0, 135]
plot_mat.width = [200., 200.]
plot_mat.pixels = [2000, 2000]
plot_mat.color_by = 'material'
plot_mat.colors={
UOF             :(150,   0,   0),
UOB             :(  0,   0, 150),
SS              :(150, 150, 150),
Ti316           :(101, 100, 100),
B4Cenr          :(100, 180, 245),
B4Cnat1         :( 80,  80,  80),
B4Cnat2         :( 80,  80,  80),
He              :(249, 249, 249),
vacuum          :(254, 254, 254), #(255, 153,  51), 
Na_FU_Out       :(230, 255, 255),
Na_FU_FI        :(230, 255, 255),
Na_FU_FE        :(230, 255, 255),
Na_FU_In        :(230, 255, 255),
Na_FU_OUT_bypass:(230, 255, 255),
Na_FU_FI_bypass :(230, 255, 255),
Na_FU_FE_bypass :(230, 255, 255),
Na_FU_In_bypass :(230, 255, 255),
Na_CR_Out       :(230, 255, 255),
Na_CR_In        :(230, 255, 255),
Na_RR_In        :(230, 255, 255),
Na_RR_Out       :(230, 255, 255),
SS_R1           :(255, 255,   0),
SS_R2           :( 36, 255,  36),
SS_R3           :( 88, 199, 255),
SS_R4           :(230, 153, 255),
HOMOG_SPR_FU    :(  0, 248,   0),
HOMOG_CR_CON    :(100, 100, 100) 
}

plot_xz = openmc.Plot()
plot_xz.filename = 'plot_xz_x00y00z095'
plot_xz.origin = [0, 0,95]
plot_xz.width = [200., 200.]
plot_xz.basis = 'xz'
plot_xz.pixels = [2000, 2000]
plot_xz.color_by = 'material'
plot_xz.colors={
UOF             :(150,   0,   0),
UOB             :(  0,   0, 150),
SS              :(150, 150, 150),
Ti316           :(101, 100, 100),
B4Cenr          :(100, 180, 245),
B4Cnat1         :( 80,  80,  80),
B4Cnat2         :( 80,  80,  80),
He              :(249, 249, 249),
vacuum          :(254, 254, 254), #(255, 153,  51), 
Na_FU_Out       :(230, 255, 255),
Na_FU_FI        :(230, 255, 255),
Na_FU_FE        :(230, 255, 255),
Na_FU_In        :(230, 255, 255),
Na_FU_OUT_bypass:(230, 255, 255),
Na_FU_FI_bypass :(230, 255, 255),
Na_FU_FE_bypass :(230, 255, 255),
Na_FU_In_bypass :(230, 255, 255),
Na_CR_Out       :(230, 255, 255),
Na_CR_In        :(230, 255, 255),
Na_RR_In        :(230, 255, 255),
Na_RR_Out       :(230, 255, 255),
SS_R1           :(255, 255,   0),
SS_R2           :( 36, 255,  36),
SS_R3           :( 88, 199, 255),
SS_R4           :(230, 153, 255),
HOMOG_SPR_FU    :(  0, 248,   0),
HOMOG_CR_CON    :(100, 100, 100) 
}

plot_xz1 = openmc.Plot()
plot_xz1.filename = 'plot_xz_x00-y30z095'
plot_xz1.origin = [0, -30,95]
plot_xz1.width = [200., 200.]
plot_xz1.basis = 'xz'
plot_xz1.pixels = [2000, 2000]
plot_xz1.color_by = 'material'
plot_xz1.colors={
UOF             :(150,   0,   0),
UOB             :(  0,   0, 150),
SS              :(150, 150, 150),
Ti316           :(101, 100, 100),
B4Cenr          :(100, 180, 245),
B4Cnat1         :( 80,  80,  80),
B4Cnat2         :( 80,  80,  80),
He              :(249, 249, 249),
vacuum          :(254, 254, 254), #(255, 153,  51), 
Na_FU_Out       :(230, 255, 255),
Na_FU_FI        :(230, 255, 255),
Na_FU_FE        :(230, 255, 255),
Na_FU_In        :(230, 255, 255),
Na_FU_OUT_bypass:(230, 255, 255),
Na_FU_FI_bypass :(230, 255, 255),
Na_FU_FE_bypass :(230, 255, 255),
Na_FU_In_bypass :(230, 255, 255),
Na_CR_Out       :(230, 255, 255),
Na_CR_In        :(230, 255, 255),
Na_RR_In        :(230, 255, 255),
Na_RR_Out       :(230, 255, 255),
SS_R1           :(255, 255,   0),
SS_R2           :( 36, 255,  36),
SS_R3           :( 88, 199, 255),
SS_R4           :(230, 153, 255),
HOMOG_SPR_FU    :(  0, 248,   0),
HOMOG_CR_CON    :(100, 100, 100) 
}

plot_xz2 = openmc.Plot()
plot_xz2.filename = 'plot_xz_x00-y15z095'
plot_xz2.origin = [0, -15,95]
plot_xz2.width = [200., 200.]
plot_xz2.basis = 'xz'
plot_xz2.pixels = [2000, 2000]
plot_xz2.color_by = 'material'
plot_xz2.colors={
UOF             :(150,   0,   0),
UOB             :(  0,   0, 150),
SS              :(150, 150, 150),
Ti316           :(101, 100, 100),
B4Cenr          :(100, 180, 245),
B4Cnat1         :( 80,  80,  80),
B4Cnat2         :( 80,  80,  80),
He              :(249, 249, 249),
vacuum          :(254, 254, 254), #(255, 153,  51), 
Na_FU_Out       :(230, 255, 255),
Na_FU_FI        :(230, 255, 255),
Na_FU_FE        :(230, 255, 255),
Na_FU_In        :(230, 255, 255),
Na_FU_OUT_bypass:(230, 255, 255),
Na_FU_FI_bypass :(230, 255, 255),
Na_FU_FE_bypass :(230, 255, 255),
Na_FU_In_bypass :(230, 255, 255),
Na_CR_Out       :(230, 255, 255),
Na_CR_In        :(230, 255, 255),
Na_RR_In        :(230, 255, 255),
Na_RR_Out       :(230, 255, 255),
SS_R1           :(255, 255,   0),
SS_R2           :( 36, 255,  36),
SS_R3           :( 88, 199, 255),
SS_R4           :(230, 153, 255),
HOMOG_SPR_FU    :(  0, 248,   0),
HOMOG_CR_CON    :(100, 100, 100) 
}

plot_xz3 = openmc.Plot()
plot_xz3.filename = 'plot_xz_x00y15z095'
plot_xz3.origin = [0, 15,95]
plot_xz3.width = [200., 200.]
plot_xz3.basis = 'xz'
plot_xz3.pixels = [2000, 2000]
plot_xz3.color_by = 'material'
plot_xz3.colors={
UOF             :(150,   0,   0),
UOB             :(  0,   0, 150),
SS              :(150, 150, 150),
Ti316           :(101, 100, 100),
B4Cenr          :(100, 180, 245),
B4Cnat1         :( 80,  80,  80),
B4Cnat2         :( 80,  80,  80),
He              :(249, 249, 249),
vacuum          :(254, 254, 254), #(255, 153,  51), 
Na_FU_Out       :(230, 255, 255),
Na_FU_FI        :(230, 255, 255),
Na_FU_FE        :(230, 255, 255),
Na_FU_In        :(230, 255, 255),
Na_FU_OUT_bypass:(230, 255, 255),
Na_FU_FI_bypass :(230, 255, 255),
Na_FU_FE_bypass :(230, 255, 255),
Na_FU_In_bypass :(230, 255, 255),
Na_CR_Out       :(230, 255, 255),
Na_CR_In        :(230, 255, 255),
Na_RR_In        :(230, 255, 255),
Na_RR_Out       :(230, 255, 255),
SS_R1           :(255, 255,   0),
SS_R2           :( 36, 255,  36),
SS_R3           :( 88, 199, 255),
SS_R4           :(230, 153, 255),
HOMOG_SPR_FU    :(  0, 248,   0),
HOMOG_CR_CON    :(100, 100, 100) 
}

plot_xz4 = openmc.Plot()
plot_xz4.filename = 'plot_xz_x00y30z095'
plot_xz4.origin = [0, 30,95]
plot_xz4.width = [200., 200.]
plot_xz4.basis = 'xz'
plot_xz4.pixels = [2000, 2000]
plot_xz4.color_by = 'material'
plot_xz4.colors={
UOF             :(150,   0,   0),
UOB             :(  0,   0, 150),
SS              :(150, 150, 150),
Ti316           :(101, 100, 100),
B4Cenr          :(100, 180, 245),
B4Cnat1         :( 80,  80,  80),
B4Cnat2         :( 80,  80,  80),
He              :(249, 249, 249),
vacuum          :(254, 254, 254), #(255, 153,  51), 
Na_FU_Out       :(230, 255, 255),
Na_FU_FI        :(230, 255, 255),
Na_FU_FE        :(230, 255, 255),
Na_FU_In        :(230, 255, 255),
Na_FU_OUT_bypass:(230, 255, 255),
Na_FU_FI_bypass :(230, 255, 255),
Na_FU_FE_bypass :(230, 255, 255),
Na_FU_In_bypass :(230, 255, 255),
Na_CR_Out       :(230, 255, 255),
Na_CR_In        :(230, 255, 255),
Na_RR_In        :(230, 255, 255),
Na_RR_Out       :(230, 255, 255),
SS_R1           :(255, 255,   0),
SS_R2           :( 36, 255,  36),
SS_R3           :( 88, 199, 255),
SS_R4           :(230, 153, 255),
HOMOG_SPR_FU    :(  0, 248,   0),
HOMOG_CR_CON    :(100, 100, 100) 
}

plot_xz5 = openmc.Plot()
plot_xz5.filename = 'plot_xz_x00y45z095'
plot_xz5.origin = [0, 45,95]
plot_xz5.width = [200., 200.]
plot_xz5.basis = 'xz'
plot_xz5.pixels = [2000, 2000]
plot_xz5.color_by = 'material'
plot_xz5.colors={
UOF             :(150,   0,   0),
UOB             :(  0,   0, 150),
SS              :(150, 150, 150),
Ti316           :(101, 100, 100),
B4Cenr          :(100, 180, 245),
B4Cnat1         :( 80,  80,  80),
B4Cnat2         :( 80,  80,  80),
He              :(249, 249, 249),
vacuum          :(254, 254, 254), #(255, 153,  51), 
Na_FU_Out       :(230, 255, 255),
Na_FU_FI        :(230, 255, 255),
Na_FU_FE        :(230, 255, 255),
Na_FU_In        :(230, 255, 255),
Na_FU_OUT_bypass:(230, 255, 255),
Na_FU_FI_bypass :(230, 255, 255),
Na_FU_FE_bypass :(230, 255, 255),
Na_FU_In_bypass :(230, 255, 255),
Na_CR_Out       :(230, 255, 255),
Na_CR_In        :(230, 255, 255),
Na_RR_In        :(230, 255, 255),
Na_RR_Out       :(230, 255, 255),
SS_R1           :(255, 255,   0),
SS_R2           :( 36, 255,  36),
SS_R3           :( 88, 199, 255),
SS_R4           :(230, 153, 255),
HOMOG_SPR_FU    :(  0, 248,   0),
HOMOG_CR_CON    :(100, 100, 100) 
}

plot_yz = openmc.Plot()
plot_yz.filename = 'plot_yz_x00y00z095'
plot_yz.origin = [0, 0,95]
plot_yz.width = [200., 200.]
plot_yz.basis = 'yz'
plot_yz.pixels = [2000, 2000]
plot_yz.color_by = 'material'
plot_yz.colors={
UOF             :(150,   0,   0),
UOB             :(  0,   0, 150),
SS              :(150, 150, 150),
Ti316           :(101, 100, 100),
B4Cenr          :(100, 180, 245),
B4Cnat1         :( 80,  80,  80),
B4Cnat2         :( 80,  80,  80),
He              :(249, 249, 249),
vacuum          :(254, 254, 254), #(255, 153,  51), 
Na_FU_Out       :(230, 255, 255),
Na_FU_FI        :(230, 255, 255),
Na_FU_FE        :(230, 255, 255),
Na_FU_In        :(230, 255, 255),
Na_FU_OUT_bypass:(230, 255, 255),
Na_FU_FI_bypass :(230, 255, 255),
Na_FU_FE_bypass :(230, 255, 255),
Na_FU_In_bypass :(230, 255, 255),
Na_CR_Out       :(230, 255, 255),
Na_CR_In        :(230, 255, 255),
Na_RR_In        :(230, 255, 255),
Na_RR_Out       :(230, 255, 255),
SS_R1           :(255, 255,   0),
SS_R2           :( 36, 255,  36),
SS_R3           :( 88, 199, 255),
SS_R4           :(230, 153, 255),
HOMOG_SPR_FU    :(  0, 248,   0),
HOMOG_CR_CON    :(100, 100, 100) 
}

plot_yz1 = openmc.Plot()
plot_yz1.filename = 'plot_yz_x06y00z095'
plot_yz1.origin = [6.12, 0,95]
plot_yz1.width = [200., 200.]
plot_yz1.basis = 'yz'
plot_yz1.pixels = [2000, 2000]
plot_yz1.color_by = 'material'
plot_yz1.colors={
UOF             :(150,   0,   0),
UOB             :(  0,   0, 150),
SS              :(150, 150, 150),
Ti316           :(101, 100, 100),
B4Cenr          :(100, 180, 245),
B4Cnat1         :( 80,  80,  80),
B4Cnat2         :( 80,  80,  80),
He              :(249, 249, 249),
vacuum          :(254, 254, 254), #(255, 153,  51), 
Na_FU_Out       :(230, 255, 255),
Na_FU_FI        :(230, 255, 255),
Na_FU_FE        :(230, 255, 255),
Na_FU_In        :(230, 255, 255),
Na_FU_OUT_bypass:(230, 255, 255),
Na_FU_FI_bypass :(230, 255, 255),
Na_FU_FE_bypass :(230, 255, 255),
Na_FU_In_bypass :(230, 255, 255),
Na_CR_Out       :(230, 255, 255),
Na_CR_In        :(230, 255, 255),
Na_RR_In        :(230, 255, 255),
Na_RR_Out       :(230, 255, 255),
SS_R1           :(255, 255,   0),
SS_R2           :( 36, 255,  36),
SS_R3           :( 88, 199, 255),
SS_R4           :(230, 153, 255),
HOMOG_SPR_FU    :(  0, 248,   0),
HOMOG_CR_CON    :(100, 100, 100) 
}

plot_yz2 = openmc.Plot()
plot_yz2.filename = 'plot_yz_x18y00z095'
plot_yz2.origin = [18, 0,95]
plot_yz2.width = [200., 200.]
plot_yz2.basis = 'yz'
plot_yz2.pixels = [2000, 2000]
plot_yz2.color_by = 'material'
plot_yz2.colors={
UOF             :(150,   0,   0),
UOB             :(  0,   0, 150),
SS              :(150, 150, 150),
Ti316           :(101, 100, 100),
B4Cenr          :(100, 180, 245),
B4Cnat1         :( 80,  80,  80),
B4Cnat2         :( 80,  80,  80),
He              :(249, 249, 249),
vacuum          :(254, 254, 254), #(255, 153,  51), 
Na_FU_Out       :(230, 255, 255),
Na_FU_FI        :(230, 255, 255),
Na_FU_FE        :(230, 255, 255),
Na_FU_In        :(230, 255, 255),
Na_FU_OUT_bypass:(230, 255, 255),
Na_FU_FI_bypass :(230, 255, 255),
Na_FU_FE_bypass :(230, 255, 255),
Na_FU_In_bypass :(230, 255, 255),
Na_CR_Out       :(230, 255, 255),
Na_CR_In        :(230, 255, 255),
Na_RR_In        :(230, 255, 255),
Na_RR_Out       :(230, 255, 255),
SS_R1           :(255, 255,   0),
SS_R2           :( 36, 255,  36),
SS_R3           :( 88, 199, 255),
SS_R4           :(230, 153, 255),
HOMOG_SPR_FU    :(  0, 248,   0),
HOMOG_CR_CON    :(100, 100, 100) 
}

plot_yz3 = openmc.Plot()
plot_yz3.filename = 'plot_yz_x30y00z095'
plot_yz3.origin = [30, 0,95]
plot_yz3.width = [200., 200.]
plot_yz3.basis = 'yz'
plot_yz3.pixels = [2000, 2000]
plot_yz3.color_by = 'material'
plot_yz3.colors={
UOF             :(150,   0,   0),
UOB             :(  0,   0, 150),
SS              :(150, 150, 150),
Ti316           :(101, 100, 100),
B4Cenr          :(100, 180, 245),
B4Cnat1         :( 80,  80,  80),
B4Cnat2         :( 80,  80,  80),
He              :(249, 249, 249),
vacuum          :(254, 254, 254), #(255, 153,  51), 
Na_FU_Out       :(230, 255, 255),
Na_FU_FI        :(230, 255, 255),
Na_FU_FE        :(230, 255, 255),
Na_FU_In        :(230, 255, 255),
Na_FU_OUT_bypass:(230, 255, 255),
Na_FU_FI_bypass :(230, 255, 255),
Na_FU_FE_bypass :(230, 255, 255),
Na_FU_In_bypass :(230, 255, 255),
Na_CR_Out       :(230, 255, 255),
Na_CR_In        :(230, 255, 255),
Na_RR_In        :(230, 255, 255),
Na_RR_Out       :(230, 255, 255),
SS_R1           :(255, 255,   0),
SS_R2           :( 36, 255,  36),
SS_R3           :( 88, 199, 255),
SS_R4           :(230, 153, 255),
HOMOG_SPR_FU    :(  0, 248,   0),
HOMOG_CR_CON    :(100, 100, 100) 
}

plot_yz4 = openmc.Plot()
plot_yz4.filename = 'plot_yz_x42y00z095'
plot_yz4.origin = [42, 0,95]
plot_yz4.width = [200., 200.]
plot_yz4.basis = 'yz'
plot_yz4.pixels = [2000, 2000]
plot_yz4.color_by = 'material'
plot_yz4.colors={
UOF             :(150,   0,   0),
UOB             :(  0,   0, 150),
SS              :(150, 150, 150),
Ti316           :(101, 100, 100),
B4Cenr          :(100, 180, 245),
B4Cnat1         :( 80,  80,  80),
B4Cnat2         :( 80,  80,  80),
He              :(249, 249, 249),
vacuum          :(254, 254, 254), #(255, 153,  51), 
Na_FU_Out       :(230, 255, 255),
Na_FU_FI        :(230, 255, 255),
Na_FU_FE        :(230, 255, 255),
Na_FU_In        :(230, 255, 255),
Na_FU_OUT_bypass:(230, 255, 255),
Na_FU_FI_bypass :(230, 255, 255),
Na_FU_FE_bypass :(230, 255, 255),
Na_FU_In_bypass :(230, 255, 255),
Na_CR_Out       :(230, 255, 255),
Na_CR_In        :(230, 255, 255),
Na_RR_In        :(230, 255, 255),
Na_RR_Out       :(230, 255, 255),
SS_R1           :(255, 255,   0),
SS_R2           :( 36, 255,  36),
SS_R3           :( 88, 199, 255),
SS_R4           :(230, 153, 255),
HOMOG_SPR_FU    :(  0, 248,   0),
HOMOG_CR_CON    :(100, 100, 100) 
}

plot_yz5 = openmc.Plot()
plot_yz5.filename = 'plot_yz_x54y00z095'
plot_yz5.origin = [54, 0,95]
plot_yz5.width = [200., 200.]
plot_yz5.basis = 'yz'
plot_yz5.pixels = [2000, 2000]
plot_yz5.color_by = 'material'
plot_yz5.colors={
UOF             :(150,   0,   0),
UOB             :(  0,   0, 150),
SS              :(150, 150, 150),
Ti316           :(101, 100, 100),
B4Cenr          :(100, 180, 245),
B4Cnat1         :( 80,  80,  80),
B4Cnat2         :( 80,  80,  80),
He              :(249, 249, 249),
vacuum          :(254, 254, 254), #(255, 153,  51), 
Na_FU_Out       :(230, 255, 255),
Na_FU_FI        :(230, 255, 255),
Na_FU_FE        :(230, 255, 255),
Na_FU_In        :(230, 255, 255),
Na_FU_OUT_bypass:(230, 255, 255),
Na_FU_FI_bypass :(230, 255, 255),
Na_FU_FE_bypass :(230, 255, 255),
Na_FU_In_bypass :(230, 255, 255),
Na_CR_Out       :(230, 255, 255),
Na_CR_In        :(230, 255, 255),
Na_RR_In        :(230, 255, 255),
Na_RR_Out       :(230, 255, 255),
SS_R1           :(255, 255,   0),
SS_R2           :( 36, 255,  36),
SS_R3           :( 88, 199, 255),
SS_R4           :(230, 153, 255),
HOMOG_SPR_FU    :(  0, 248,   0),
HOMOG_CR_CON    :(100, 100, 100) 
}

plot_yz6 = openmc.Plot()
plot_yz6.filename = 'plot_yz_x66y00z095'
plot_yz6.origin = [66, 0,95]
plot_yz6.width = [200., 200.]
plot_yz6.basis = 'yz'
plot_yz6.pixels = [2000, 2000]
plot_yz6.color_by = 'material'
plot_yz6.colors={
UOF             :(150,   0,   0),
UOB             :(  0,   0, 150),
SS              :(150, 150, 150),
Ti316           :(101, 100, 100),
B4Cenr          :(100, 180, 245),
B4Cnat1         :( 80,  80,  80),
B4Cnat2         :( 80,  80,  80),
He              :(249, 249, 249),
vacuum          :(254, 254, 254), #(255, 153,  51), 
Na_FU_Out       :(230, 255, 255),
Na_FU_FI        :(230, 255, 255),
Na_FU_FE        :(230, 255, 255),
Na_FU_In        :(230, 255, 255),
Na_FU_OUT_bypass:(230, 255, 255),
Na_FU_FI_bypass :(230, 255, 255),
Na_FU_FE_bypass :(230, 255, 255),
Na_FU_In_bypass :(230, 255, 255),
Na_CR_Out       :(230, 255, 255),
Na_CR_In        :(230, 255, 255),
Na_RR_In        :(230, 255, 255),
Na_RR_Out       :(230, 255, 255),
SS_R1           :(255, 255,   0),
SS_R2           :( 36, 255,  36),
SS_R3           :( 88, 199, 255),
SS_R4           :(230, 153, 255),
HOMOG_SPR_FU    :(  0, 248,   0),
HOMOG_CR_CON    :(100, 100, 100) 
}

plot_core = openmc.Plot()
plot_core.filename = 'plot_core_x00y00z120'
plot_core.origin = [0, 0, 120]
plot_core.width = [100.0, 100.0]
plot_core.pixels = [2000, 2000]
plot_core.color_by = 'material'
plot_core.colors={
UOF             :(150,   0,   0),
UOB             :(  0,   0, 150),
SS              :(150, 150, 150),
Ti316           :(101, 100, 100),
B4Cenr          :(100, 180, 245),
B4Cnat1         :( 80,  80,  80),
B4Cnat2         :( 80,  80,  80),
He              :(249, 249, 249),
vacuum          :(254, 254, 254), #(255, 153,  51), 
Na_FU_Out       :(230, 255, 255),
Na_FU_FI        :(230, 255, 255),
Na_FU_FE        :(230, 255, 255),
Na_FU_In        :(230, 255, 255),
Na_FU_OUT_bypass:(230, 255, 255),
Na_FU_FI_bypass :(230, 255, 255),
Na_FU_FE_bypass :(230, 255, 255),
Na_FU_In_bypass :(230, 255, 255),
Na_CR_Out       :(230, 255, 255),
Na_CR_In        :(230, 255, 255),
Na_RR_In        :(230, 255, 255),
Na_RR_Out       :(230, 255, 255),
SS_R1           :(255, 255,   0),
SS_R2           :( 36, 255,  36),
SS_R3           :( 88, 199, 255),
SS_R4           :(230, 153, 255),
HOMOG_SPR_FU    :(  0, 248,   0),
HOMOG_CR_CON    :(100, 100, 100) 
}


# Instantiate a Plots collection, add plots, and export to XML
plot_file = openmc.Plots([
plot_xy,
plot_xy2,
plot_mat,
plot_xz,
plot_xz1,
plot_xz2,
plot_xz3,
plot_xz4,
plot_xz5,
plot_yz,
plot_yz1,
plot_yz2,
plot_yz3,
plot_yz4,
plot_yz5,
plot_yz6,
plot_core
])

plot_file.export_to_xml()

###############################################################################
#                   Exporting to OpenMC tallies.xml File
###############################################################################

# Instantiate a distribcell Tally
tallyF = openmc.Tally(tally_id=1)
tallyF.filters = [openmc.DistribcellFilter(c_FU_UBL)]
tallyF.scores = ['kappa-fission', 'flux', 'fission-q-recoverable']

# Instantiate a distribcell Tally
tallyBB = openmc.Tally(tally_id=2)
tallyBB.filters = [openmc.DistribcellFilter(c_FU_FIS)]
tallyBB.scores = ['kappa-fission', 'flux', 'fission-q-recoverable']

# Instantiate a distribcell Tally
tallyBT = openmc.Tally(tally_id=3)
tallyBT.filters = [openmc.DistribcellFilter(c_FU_LBL)]
tallyBT.scores = ['kappa-fission', 'flux', 'fission-q-recoverable']

# Instantiate a distribcell Tally
tallyE = openmc.Tally(tally_id=4)
energy_filter = openmc.EnergyFilter([
1.0000000000E-05, 
1.0000000000E-04,
5.0000000000E-04,
7.5000000000E-04,
1.0000000000E-03,
1.2000000000E-03,
1.5000000000E-03,
2.0000000000E-03,
2.5000000000E-03,
3.0000000000E-03,
4.0000000000E-03,
5.0000000000E-03,
7.5000000000E-03,
1.0000000000E-02,
2.5300000000E-02,
3.0000000000E-02,
4.0000000000E-02,
5.0000000000E-02,
6.0000000000E-02,
7.0000000000E-02,
8.0000000000E-02,
9.0000000000E-02,
1.0000000000E-01,
1.2500000000E-01,
1.5000000000E-01,
1.7500000000E-01,
2.0000000000E-01,
2.2500000000E-01,
2.5000000000E-01,
2.7500000000E-01,
3.0000000000E-01,
3.2500000000E-01,
3.5000000000E-01,
3.7500000000E-01,
4.0000000000E-01,
4.5000000000E-01,
5.0000000000E-01,
5.5000000000E-01,
6.0000000000E-01,
6.2500000000E-01,
6.5000000000E-01,
7.0000000000E-01,
7.5000000000E-01,
8.0000000000E-01,
8.5000000000E-01,
9.0000000000E-01,
9.2500000000E-01,
9.5000000000E-01,
9.7500000000E-01,
1.0000000000E+00,
1.0100000000E+00,
1.0200000000E+00,
1.0300000000E+00,
1.0400000000E+00,
1.0500000000E+00,
1.0600000000E+00,
1.0700000000E+00,
1.0800000000E+00,
1.0900000000E+00,
1.1000000000E+00,
1.1100000000E+00,
1.1200000000E+00,
1.1300000000E+00,
1.1400000000E+00,
1.1500000000E+00,
1.1750000000E+00,
1.2000000000E+00,
1.2250000000E+00,
1.2500000000E+00,
1.3000000000E+00,
1.3500000000E+00,
1.4000000000E+00,
1.4500000000E+00,
1.5000000000E+00,
1.5900000000E+00,
1.6800000000E+00,
1.7700000000E+00,
1.8600000000E+00,
1.9400000000E+00,
2.0000000000E+00,
2.1200000000E+00,
2.2100000000E+00,
2.3000000000E+00,
2.3800000000E+00,
2.4700000000E+00,
2.5700000000E+00,
2.6700000000E+00,
2.7700000000E+00,
2.8700000000E+00,
2.9700000000E+00,
3.0000000000E+00,
3.0500000000E+00,
3.1500000000E+00,
3.5000000000E+00,
3.7300000000E+00,
4.0000000000E+00,
4.7500000000E+00,
5.0000000000E+00,
5.4000000000E+00,
6.0000000000E+00,
6.2500000000E+00,
6.5000000000E+00,
6.7500000000E+00,
7.0000000000E+00,
7.1500000000E+00,
8.1000000000E+00,
9.1000000000E+00,
1.0000000000E+01,
1.1500000000E+01,
1.1900000000E+01,
1.2900000000E+01,
1.3750000000E+01,
1.4400000000E+01,
1.5100000000E+01,
1.6000000000E+01,
1.7000000000E+01,
1.8500000000E+01,
1.9000000000E+01,
2.0000000000E+01,
2.1000000000E+01,
2.2500000000E+01,
2.5000000000E+01,
2.7500000000E+01,
3.0000000000E+01,
3.1250000000E+01,
3.1750000000E+01,
3.3250000000E+01,
3.3750000000E+01,
3.4600000000E+01,
3.5500000000E+01,
3.7000000000E+01,
3.8000000000E+01,
3.9100000000E+01,
3.9600000000E+01,
4.1000000000E+01,
4.2400000000E+01,
4.4000000000E+01,
4.5200000000E+01,
4.7000000000E+01,
4.8300000000E+01,
4.9200000000E+01,
5.0600000000E+01,
5.2000000000E+01,
5.3400000000E+01,
5.9000000000E+01,
6.1000000000E+01,
6.5000000000E+01,
6.7500000000E+01,
7.2000000000E+01,
7.6000000000E+01,
8.0000000000E+01,
8.2000000000E+01,
9.0000000000E+01,
1.0000000000E+02,
1.0800000000E+02,
1.1500000000E+02,
1.1900000000E+02,
1.2200000000E+02,
1.8600000000E+02,
1.9250000000E+02,
2.0750000000E+02,
2.1000000000E+02,
2.4000000000E+02,
2.8500000000E+02,
3.0500000000E+02,
5.5000000000E+02,
6.7000000000E+02,
6.8300000000E+02,
9.5000000000E+02,
1.1500000000E+03,
1.5000000000E+03,
1.5500000000E+03,
1.8000000000E+03,
2.2000000000E+03,
2.2900000000E+03,
2.5800000000E+03,
3.0000000000E+03,
3.7400000000E+03,
3.9000000000E+03,
6.0000000000E+03,
8.0300000000E+03,
9.5000000000E+03,
1.3000000000E+04,
1.7000000000E+04,
2.5000000000E+04,
3.0000000000E+04,
4.5000000000E+04,
5.0000000000E+04,
5.2000000000E+04,
6.0000000000E+04,
7.3000000000E+04,
7.5000000000E+04,
8.2000000000E+04,
8.5000000000E+04,
1.0000000000E+05,
1.2830000000E+05,
1.5000000000E+05,
2.0000000000E+05,
2.7000000000E+05,
3.3000000000E+05,
4.0000000000E+05,
4.2000000000E+05,
4.4000000000E+05,
4.7000000000E+05,
4.9952000000E+05,
5.5000000000E+05,
5.7300000000E+05,
6.0000000000E+05,
6.7000000000E+05,
6.7900000000E+05,
7.5000000000E+05,
8.2000000000E+05,
8.6110000000E+05,
8.7500000000E+05,
9.0000000000E+05,
9.2000000000E+05,
1.0100000000E+06,
1.1000000000E+06,
1.2000000000E+06,
1.2500000000E+06,
1.3170000000E+06,
1.3560000000E+06,
1.4000000000E+06,
1.5000000000E+06,
1.8500000000E+06,
2.3540000000E+06,
2.4790000000E+06,
3.0000000000E+06,
4.3040000000E+06,
4.8000000000E+06,
6.4340000000E+06,
8.1873000000E+06,
1.0000000000E+07,
1.2840000000E+07,
1.3840000000E+07,
1.4550000000E+07,
1.5683000000E+07,
1.7333000000E+07,
2.0000000000E+07
]) # serpent det ed scale238_ext SCALE 238-group structure
tallyE.filters = [openmc.DistribcellFilter(cell1000),energy_filter]
tallyE.scores = ['flux']

# Instantiate a Tallies collection and export to XML
tallies_file = openmc.Tallies([tallyF,tallyBB,tallyBT,tallyE])
tallies_file.export_to_xml()

