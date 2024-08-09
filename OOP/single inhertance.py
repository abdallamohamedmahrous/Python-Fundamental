import math as ma

class Shape:
    def __init__(self, width=0, height=0) -> None:
        self.__width = width
        self.__height = height
    
    def set_width(self, width):
        self.__width = width
    
    def get_width(self):
        return self.__width
    
    def set_height(self, height):
        self.__height = height
    
    def get_height(self):
        return self.__height
    
    def area_shape(self):
        pass

class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__(radius, radius) 
        self.__radius = radius  
    
    def get_radius(self):
        return self.__radius
    
    def area_Circle(self):
        return "{:.3f}".format(ma.pi * self.__radius ** 2) 

Circle1 = Circle(radius=float(input("Enter The Radius Of Circle: ")))
print(f"The area of the circle is {Circle1.area_Circle()}")
