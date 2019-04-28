from circle import find_area, find_circumference
from square import find_area as find_square_area, find_perimeter as find_square_perimeter
from rectangle import find_area as find_rectangle_area, find_perimeter as find_rectangle_perimeter

r = 5
area = find_area(5)
circumference = find_circumference(5)

print(f'Area of cicle with radius as {r} is {area}')
print(f'Circumference of cicle with radius as {r} is {circumference}')
print("--------------------------------------------------------------------------------")

s = 5
area = find_square_area(5)
perimeter = find_square_perimeter(5)

print(f'Area of square with side as {s} is {area}')
print(f'Perimeter of square with side as {s} is {perimeter}')
print("--------------------------------------------------------------------------------")

l = 5
b = 10
area = find_rectangle_area(5, 10)
perimeter = find_rectangle_perimeter(5, 10)

print(f'Area of rectangle with sides as {l} and {b} is {area}')
print(f'Perimeter of rectangle with sides as {l} and {b} is {perimeter}')
print("--------------------------------------------------------------------------------")