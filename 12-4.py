
class Hexagon:
    
    def __init__(self,a):
        self.a = a
        print("created")

    def calculate_perimeter(self):
        return self.a * 6
    
T = Hexagon(10)
print(T.calculate_perimeter())
