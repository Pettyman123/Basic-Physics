import math
import numpy as np

u = float(input("Enter the initial velocity(in m/s):"))
t = float(input("Enter the time period(in sec):"))
a = float(input("The accelaration of the object(in m/s^2):"))
s = float(input("The distance (in m):"))
v = math.sqrt(u*u + 2*a*s)

print("The final velocity is",v,"m/s")