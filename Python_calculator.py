def add(num1,num2):
    a = round(num1+num2,4)
    print("The sum of "+str(num1)+ " and " +str(num2)+ " is " +str(a)+ ".")
    return str(num1)+"+"+str(num2)+"="+str(a)
def subtract(num1,num2):
    a = round(num1-num2,4)
    print("The subtraction of "+str(num1)+ " and " +str(num2)+ " is " +str(a)+ ".")
    return str(num1)+"-"+str(num2)+"="+str(a)

def mul(num1,num2):
    a = round(num1*num2,4)
    print("The product of "+str(num1)+ " and " +str(num2)+ " is " +str(a)+ ".")
    return str(num1)+"*"+str(num2)+"="+str(a)

def division(num1,num2):
    if num2!=0:
        a = round(num1/num2,4)
        print("The division of "+str(num1)+ " and " +str(num2)+ " is " +str(a)+ ".")
        return str(num1)+"/"+str(num2)+"="+str(a)
    else:
        print("Cannot divide by zero")
        return "DIV ERROR"

def exp(num1,num2):
    a = round(num1**num2,4)
    print("The exp of "+str(num1)+ " and " +str(num2)+ " is " +str(a)+ ".")
    return str(num1)+"**"+str(num2)+"="+str(a)


def perform_again():
    res = input("Would you like to perform again(y/n)")
    if res.startswith('n'):
        flag = False
        print("Thank you for using the Python calculator .")
    else:
        flag =True
    return flag



print("Welcome to The Python Calculator App")
print("Enter two numbers and an operation and the desired operation will be performed")
flag = True
ls = []
while flag:
    num1 = float(input("Enter a number "))
    num2 = float(input("Enter a number "))
    opr = input("Enter an operation (addition, subtraction, multiplication, division, or exponentiation): ").lower()
    if opr.startswith('add'):
        res = add(num1,num2)
    elif opr.startswith('sub'):
        res = subtract(num1,num2)
    elif opr.startswith('mul'):
        res = mul(num1,num2)
    elif opr.startswith('div'):
        res = division(num1,num2)
    elif opr.startswith('exp'):
        res = exp(num1,num2)
    else:
        print("Not a valid operator")
        res = "OPR ERROR"
    ls.append(res)
    flag = perform_again()
print("Calculation Summary:")
for i in ls:
    print(i)