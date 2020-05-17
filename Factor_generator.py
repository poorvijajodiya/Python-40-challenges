print("Welcome to the Factor Generator App\n")
Flag = True
while Flag:
    num = int(input("Enter a number to determine all factors of that number: "))
    factors = []
    for i in range(1,num+1):
        if num%i == 0:
            factors.append(i)
    print("Factors of 44 are:")
    for i in range(len(factors)):
        print(factors[i])
    print("In summary:")
    for j in  range(int(len(factors)/2)):
        print("{}*{}={}".format(factors[j],factors[-j-1],num))
    inp = input("Run again y/n: ")
    if inp.startswith('n'):
        Flag = False
        print("Thank you for using the program. Have a great day")