# This is a comment.  Python will ignore these lines (starting with #) when running

import math as ma
# To use a math function, write "ma." in front of it.  Example:  ma.sin(3.146)
data=open('planet_data.dat','r')
print("This function will find the weight of an explorer on a chosen celestial body. ")
mass=float(raw_input("Please input the mass of the astronaut in kilograms (don't write the units): "))
planetliststr=[]
planetlist=[]
q=data.readlines()
radiilist=[]
densitylist=[]
explorerweight=0
gees=0
earthaccel=9.807 #m/s^2
planetmass=0
univerconst=6.674e-11 #m^3/(kg*s^2)

for linnum in (q):
    if linnum[0]!="#":
        loc=linnum.find(";")
        planetliststr.append(linnum[0:loc]) #building up the planetlist
        planetlist.append(linnum[0:loc])
        loc2=linnum.find(";",loc+1)
        radiilist.append(float(linnum[loc+2:linnum.find("km",loc+1)])) #building radiilist
        densitylist.append(float(linnum[loc2+2:linnum.find("g/cm^3",loc2+1)]))
print('\n'+"Celestial body options are: "+', '.join(planetlist))
planet=(raw_input("Please choose a planet or celestial body from the given list: "))
altinit=float(raw_input("Please input the altitude above the planet's average radius in meters (don't write the units): "))
for pointer in range(len(planetlist)):
    radiilist[pointer]=radiilist[pointer]*1000 #Turning km measurements into meters.
    densitylist[pointer]=densitylist[pointer]*(1000000/1000) #conversion of g/cm^3 to kg/m^3

if planet in planetlist:
    print("You've picked "+planetlist[planetlist.index(planet)])
    location=planetlist.index(planet)
    planetmass=(4/3.0)*ma.pi*((radiilist[location])**3)*densitylist[location]
    force=univerconst*planetmass*mass/((altinit+radiilist[location])**2)
    accel=force/mass
    gees=round(accel/earthaccel,3)
    print('\n'+"The astronaut weighs "+str(force)+" Newtons while on "+planetlist[planetlist.index(planet)])
    print('\n'+"The acceleration due to gravity on "+planetlist[planetlist.index(planet)]+" is "+str(accel)+" m/s^2, or "+str(gees)+" Gs.")
else:
    print('\n'+"OH NO! You seem to have misspelled something. Please check your spelling, and try again. If you need to, you can copy from the list above.")



















