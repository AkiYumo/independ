import math

class Circle:
    
    def __init__(self,r):
        self.r = r
        print("created")

    def area(self):
        return (self.r ** 2) * math.pi
    
circle = Circle(10)
print(circle.area())
