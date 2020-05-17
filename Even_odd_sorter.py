print("Welcome to the Even Odd Number Sorter App\n")
flag = True
while flag:
    num_list = (input("Enter in a string of numbers separated by a comma (,) :").replace(" ","")).split(',')
    #inp = inp.split(',')
    even = []
    odd = []
    print("---- Result Summary ----")
    for i in num_list:
        i = int(i)
        if i%2==0:
            even.append(i)
            print("{} is even".format(i))
        else:
            odd.append(i)
            print("{} is odd".format(i))
    even.sort()
    odd.sort()
    print("The following {} numbers are even".format(len(even)))
    for i in range(len(even)):
        print(even[i])
    print("The following {} numbers are odd".format(len(odd)))
    for i in range(len(odd)):
        print(odd[i])
    res = input("Would you like to run the program again (y/n): ")
    if res.startswith('n'):
        flag = False
        print("Thank you for using the program. Goodbye.")
