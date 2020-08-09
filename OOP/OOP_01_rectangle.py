class Shapes:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def area(self):
        return self.x * self.y
    
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    
    
    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale
        
rect = Shapes(50, 30)


#finding the area of your rectangle:
print(rect.area())

#finding the perimeter of your rectangle:
print(rect.perimeter())
 
#making the rectangle 40% smaller
rect.scaleSize(0.4)
#re-printing the new area of the rectangle
print(rect.area())

