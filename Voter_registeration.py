print("Welcome to the Voter Registration App\n")
name = input("Please enter your name: ").title()
age = int(input("Please enter your age: "))
ls = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]
if age>=18:
    print("Congratulations {}! You are old enough to register to vote.".format(name))
    print("Here is a list of political parties to join.")
    for i in ls:
        print("-{}".format(i))
    p = input("What party would you like to join: ").title()
    print("Congratulations {}! You have joined the {} party!".format(name, p))
    if p == ls[0] or p == ls[1]:
        print("It is a major party!")
    elif p ==ls[2]:
        print("An independent person")
    else:
        print("Not a major party!")
else:
    print("You are not old enough to register to vote")
