import cmath
print("Welcome to the Quadratic Equation Solver App.\n")
print("A quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solution can b real or complex numbers")
print("A complex number has two parts: a + bj\nWhere a is the real portion and bj is the imaginary portion")
q = int(input("How many equations would you like to solve today: "))
for i in range(1,q+1):
    print("Solving equation #{}---------------------------------------------------------------".format(i))
    a = float(input("Please enter your value of a (coefficient of x^2): "))
    b = float(input("Please enter your value of b (coefficient of x): "))
    c = float(input("Please enter your value of c (coefficient): "))
    print("The solutions to {}x^2 + {}x + {} = 0 are:".format(a,b,c))
    x1 = (-b + cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print("x1 = {}".format(x1))
    print("x2 = {}".format(x2))
print("Thank you for using the Quadratic Equation Solver App. Goodbye.")