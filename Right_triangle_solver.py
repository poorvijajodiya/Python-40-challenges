import math
print("Welcome to the Right Triangle Solver App")
print()
a = float(input("What is the first leg of the triangle: "))
b = float(input("What is the second leg of the triangle: "))
c = math.sqrt(a**2 + b**2)
c = round(c,3)
area = 0.5*a*b
area = round(area,3)
print("For a triangle with legs of {} and {} the hypotenuse is {}.".format(a,b,c))
print("For a triangle with legs of {} and {} the area is {}.".format(a,b,area))