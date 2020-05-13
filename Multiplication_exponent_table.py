print("Welcome to the Multiplication/Exponent Table App")
a = input("What is your name: ").title()
num = float(input("What number would you like to work with: "))
message ="{}, Math is cool".format(a)
print()
print("Multiplication table for {}".format(num))
for i in range(1,10):
    mul = i * num
    mul = round(mul,4)
    print(str(i) + "*" + str(num) + "="+ str(mul))
print()
print("Exponent table for" + str(num))
for j in range(1,10):
    exp = num**j
    exp = round(exp,4)
    print(str(num) + "**" + str(j) + "="+ str(exp))
print()
print(message)
print("\t{}".format(message.lower()))
print("\t\t{}".format(message.title()))
print("\t\t\t{}".format(message.upper()))