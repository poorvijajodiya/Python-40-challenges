import time
print("Welcome to the Prime Number App")
flag = True
while flag:
    print("Enter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")
    choice = int(input("Enter your choice 1 or 2: "))
    if choice == 1:
        num = int(input("Enter a number to determine if it is prime or not: "))
        prime_status = True
        for i in range(2,num):
            if num%i==0:
                prime_status = False
                break
        if prime_status == True:
            print("{} is prime".format(num))
        else:
            print("{} is not prime".format(num))
    elif choice == 2:
        lower = int(input("Enter the lower bound of your range: "))
        upper = int(input("Enter the upper bound of your range: "))
        prime = []
        start_time = time.time()
        for j in range(lower,upper+1):
            if j > 1:
                prime_status = True
                for i in range(2, j):
                    if j % i == 0:
                        prime_status = False
                        break
            else:
                prime_status = False
            if prime_status:
                prime.append(j)
        end_time = time.time()
        total_time = round(start_time-end_time,4)
        print("Calculations took a total of {} seconds".format(total_time))
        print("The following numbers between {} and {} are prime:".format(lower,upper))
        for k in prime:
            print(k)
    else:
        print("That is not a valid option.")
    res = input("Would you like to run the program again (y/n): ")
    if res.startswith('n'):
        flag = False
        print("Thank you for using the program. Goodbye.")