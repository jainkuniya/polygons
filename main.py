from circle import find_area, find_circumference
from square import find_area as find_square_area

r = 5
area = find_area(5)
circumference = find_circumference(5)

print(f'Area of cicle with radius {r} is {area}')
print(f'Circumference of cicle with radius {r} is {circumference}')

s = 5
area = find_square_area(5)

print(f'Area of square with side {s} is {area}')