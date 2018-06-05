class Shape():

    def what_am_i(self):
        print("I am a shape.")

class Square(Shape):

    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1,self.s1,self.s1,self.s1)

def Compare(a,b):
    return a is b


a_square = Square(29)
b_square = a_square
another_square = Square(93)

print(Compare(a_square,b_square))
print(Compare(a_square,another_square))

