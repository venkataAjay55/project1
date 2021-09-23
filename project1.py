#first code
#printing area of circle
r=float(input("enter the radius of circle : "))
from math import pi
area=pi*r*r
print(area)



#second code
#printing the extension of taken file from user
filename=input("input the filename :")
f_extension=filename.split(".")
print("the extension of file is : " +repr(f_extension[-1]))
