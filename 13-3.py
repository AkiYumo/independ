class Shape:
    
    def what_am_i(self):
        print("I im a shape")
        
class Rectangle(Shape):
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("created")

    def calculate_perimeter(self):
        return self.a * 2 + self.b *2

class Square(Shape):
    
    def __init__(self,a):
        self.a = a
        print("created")

    def calculate_perimeter(self):
        return self.a * 4

  
a_rectangle = Rectangle(20, 50)

a_square = Square(29)



a_rectangle.what_am_i()

a_square.what_am_i()
