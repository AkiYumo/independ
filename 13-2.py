class Square:
    
    def __init__(self,a):
        self.a = a
        print("created")

    def change_size(self,x):
        self.a = self.a + x
        print("self.a value is {}".format(self.a))
        

  
b = Square(12)
b.change_size(-4)

