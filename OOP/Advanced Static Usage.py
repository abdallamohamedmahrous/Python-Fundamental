class Shape:
    counter=0
    def __init__(self) -> None:
         Shape.counter+=1
    @staticmethod
    def get_counter():
        return Shape.counter
    
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    counter=0
    def __init__(self) -> None:
        super().__init__() 
        Circle.counter+=1

    @staticmethod
    def get_counter():
        return Circle.counter
    
    def draw(self):
        print("Drawing a shape")

class Rectangle(Shape):
    counter=0
    def __init__(self) -> None:
        super().__init__() 
        Rectangle.counter+=1

    @staticmethod
    def get_counter():
        return Rectangle.counter
    
    def draw(self):
        print("Drawing a shape")


shape1 = Shape()
shape2 = Shape()
shape3 = Shape()

circle1 = Circle()
circle2 = Circle()
circle3 = Circle()

rectangle1 = Rectangle()
rectangle2 = Rectangle()
rectangle3 = Rectangle()

shape1.draw()
circle1.draw()
rectangle1.draw()

print(f"Total Shapes: {Shape.get_counter()}")
print(f"Total Circles: {Circle.get_counter()}")
print(f"Total Rectangles: {Rectangle.get_counter()}")