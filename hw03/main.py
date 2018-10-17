class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

class Square(Rectangle):

    def __init__(self, width):
        self.width  = width
        self.height = width

class Ellipse(Rectangle):

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height*3.14

class Circle(Ellipse):
        
    def __init__(self,width):
        self.width = width
        self.height = width


def compute_area(shapes):
    current=0
    s=0
    while current<len(shapes):
        #print(shapes[current].area())
        s+=shapes[current].area()
        #print(s)
        current+=1
    return s

   







 
