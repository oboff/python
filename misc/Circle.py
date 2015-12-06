import math

class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    @classmethod
    def from_bbd(cls, bbd):
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)
    
#    @classmethod
    def from_ccd(self, ccd):
        radius = ccd+10
        return self(radius)

'''
class Tire(Circle):

    def perimeter(self):
        return Circle.perimeter(self) * 1.25
'''
