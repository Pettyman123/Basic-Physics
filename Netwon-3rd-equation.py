import math
#S = ut + 1/2at^2


u = float(input("Enter the initial velocity(in m/s):"))
t = float(input("Enter the time period(in sec):"))
a = float(input("The accelaration of the object(in m/s^2):"))
s =  0.5 * a * t * t
print("The distance travelled is",s,"m")
    


