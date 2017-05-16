from visual import *

#first create the object
class astro(sphere):
    def __init__(radius, mass):
        self.radius = radius
        self.mass = mass
    def setPos(x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def getMass():
        return self.mass
    def getRadius():
        return self.radius
    def getPos():
        return self.x, self.y, self.z
def e(sci, power):
    return sci * math.pow(10, power)

SUN_MASS = e(1.989, 30)
SUN_RADIUS = e(695.7, 6)

sun = astro(SUN_RADIUS, SUN_MASS)
    
    