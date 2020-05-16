print("Welcome to the Yes or No Issue Polling App\n")
inp = input("What is the yes or no issue you will be voting on today: ")
n = int(input("What is the number of voters you will allow on the issue: "))
inp1 = input("Enter a password for polling results: ")
yes = 0
no = 0
dict = {}
for i in range(n):
    name = input("Enter your full name: ").title()
    if name in dict:
        print("Already voted..")
    else:
        print("Here is our issue: {}".format(inp))
        l = input("What do you think...yes or no: ").lower()
        if l.startswith('y') or l.startswith('n'):
            if l.startswith('y'):
                l = 'yes'
                yes +=1
            else:
                l ='no'
                no +=1
        else:
            print("That is not a yes or no answer, but okay...")
        print("Thank you {}! Your vote of {} has been recorded.".format(name, l))
        dict[name] = l
print("The following {} people voted:".format(yes+no))
for m in dict.keys():
    print(m)
print("On the following issue: {}".format(inp))
if yes>no:
    print("YES wins!!!",end = ' ')
    print("{} votes to {}".format(yes,no))
elif no>yes:
    print("No wins!!!", end=' ')
    print("{} votes to {}".format(no, yes))
else:
    print("It was a tie!!! {} votes to {} ".format(yes,no))
g = input("To see the voting results enter the admin password: ")
if inp1 == g:
    for key,value in dict.items():
        print("Voter:{}\t\tVote:{}".format(key,value))
else:
    print("Sorry, that is not the correct password. Goodbye...")
print("Thank you for using the Yes or No Issue Polling App.")




