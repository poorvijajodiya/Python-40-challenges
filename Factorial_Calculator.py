import math
print("Welcome to the Factorial Calculator App")
print()
fact = int(input("What number would you like to compute the factorial of? "))
print("{}! = ".format(fact),end = "")
for i in range(1,fact):
    print(str(i), end = "*")
print(fact)
print("\nHere is the result from the math library:")
a = math.factorial(fact)
print("The factorial of {} is: {}".format(fact,a))
print()
print("Here is the result from my own algorithm:")
b = 1
for j in range(1,fact+1):
    b = b*j
print("The factorial of {} is: {}".format(fact,b))
if a == b:
    print("It is shown twice that {}! = {} (with excitement)".format(fact,a))