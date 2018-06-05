class Rectangle:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("created")

    def calculate_perimeter(self):
        return self.a * 2 + self.b *2

class Square:
    
    def __init__(self,a):
        self.a = a
        print("created")

    def calculate_perimeter(self):
        return self.a * 4

  
a = Rectangle(10,12)
b = Square(12)
print(a.calculate_perimeter())

print(b.calculate_perimeter())
