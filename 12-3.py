
class Triangle:
    
    def __init__(self,a,h):
        self.a = a
        self.h = h
        print("created")

    def area(self):
        return self.a * self.h * 0.5
    
T = Triangle(10,10)
print(T.area())
