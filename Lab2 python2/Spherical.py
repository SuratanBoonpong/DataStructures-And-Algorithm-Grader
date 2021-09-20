'''สร้าง class Spherical โดยต้อง

มี function [changeR , findVolume , findArea]

มี ตัวแปร radius



*สามารถใช้ from math import pi  หรือ math.pi  ได้*

class Spherical:

    def __init__(self,r):

        ### Enter Your Code Here ###

    def changeR(self,Radius):

        ### Enter Your Code Here ###

    def findVolume(self):

        ### Enter Your Code Here ###

    def findArea(self):

        ### Enter Your Code Here ###

    def __str__(self):

        ### Enter Your Code Here ###

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)'''

import math
class Spherical:

    def __init__(self,r):
        self.radius = r

    def changeR(self,Radius):
        self.radius = Radius

    def findVolume(self):
        return (4/3)*math.pi*math.pow(self.radius,3)

    def findArea(self):
        return 4*math.pi*math.pow(self.radius,2)

    def __str__(self):
        return "Radius ="+str(self.radius)+" Volumn = "+str(self.findVolume())+" Area = "+str(self.findArea())

r1,r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)