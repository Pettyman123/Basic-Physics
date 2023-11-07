import math

m = float(input("The mass of objcet(in kg):"))
s = float(input("The displacement of the object during motion(in m):"))
a = float(input("The constant accelaration of the object (in m/s^2):"))
F = m*a
WD = F*s

print("The workdone by the object in the whole motion is", round(WD,2),"J")