print("Welcome to the Binary/Hexadecimal Converter App")
print()
a = int(input("Compute binary and hexadecimal values up to the following decimal number: "))
B_V = []
H_V = []
decimal = list(range(1, a+1))
for i in decimal:
    B_V.append(bin(i))
    H_V.append(hex(i))
print("Generating lists complete...")
print()
print("Using slices, we will now show a portion of each list")
start = int(input("What decimal number would you like to start at:"))
stop = int(input("What decimal number would you like to stop at:"))
print("Decimal values from {} to {}:".format(start, stop))
for j in decimal[start-1:stop]:
    print(j)
print("Binary values from {} to {}:".format(start, stop))
for k in B_V[start-1:stop]:
    print(k)
print("Hexadecimal values from {} to {}:".format(start, stop))
for l in H_V[start-1:stop]:
    print(l)
print("press enter to see all values from 1 to 12.")
print("Decimal----Binary----Hexadecimal\n----------------------------------------------------------")
for d in range(0,a):
    print("{}----{}----{}".format(decimal[d], B_V[d], H_V[d]))