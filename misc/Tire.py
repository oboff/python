from Circle import Circle

class Tire(Circle):

    def perimeter(self):
        return Circle.perimeter(self) * 1.25
