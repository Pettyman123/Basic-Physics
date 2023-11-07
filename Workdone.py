import math

m = float(input("The mass of objcet(in kg):"))
v = float(input("The constant velocity of the object during motion(in m/s):"))
g = 9.8 #m/s^2
h = float(input("The constant height of the object at the fall(in m):"))

KE = (1/2)*m*v*v
PE = m*g*h

WD = KE+PE

print("The workdone by the object in the whole motion is", round(WD,2),"J")