import math

m = float(input("The mass of objcet(in kg):"))
g = 9.8 #m/s^2
h = float(input("The constant height of the object at the fall(in m):"))

PE = m*g*h

print("The Kinetic energy of the object in motion is",round(PE,2),"J")