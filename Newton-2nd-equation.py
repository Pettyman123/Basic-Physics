import math
import numpy as np

u = float(input("Enter the initial velocity(in m/s):"))
t = float(input("Enter the time period(in sec):"))
a = float(input("The accelaration of the object(in m/s^2):"))
v = u + a*t
print("The final velocity is",v,"m/s")