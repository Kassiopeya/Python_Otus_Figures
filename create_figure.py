from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle

new_rectangle = Rectangle(3, 2)
print("New Rectangle:")
print(new_rectangle.get_area)
print(new_rectangle.get_perimeter)

new_circle = Circle(3)
print("New Circle:")
print(new_circle.get_area)
print(new_circle.get_perimeter)

new_triangle = Triangle(20.1,14.1,12.1)
print("New Triangle:")
print(new_triangle.get_area)
print(new_circle.get_perimeter)

new_square = Square(6)
print("New Square:")
print(new_square.get_area)
print(new_square.get_perimeter)

