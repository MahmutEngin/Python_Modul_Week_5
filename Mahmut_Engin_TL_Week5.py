class Rectangle():
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return  2* (self.width + self.height)
rect = Rectangle(int(input("1.Kenar")), int(input("2.Kenar")))

print("Area:", rect.area())
print("Perimeter:", rect.perimeter())