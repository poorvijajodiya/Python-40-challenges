import random
def dice_sides():
    sides = int(input("How many sides would you like on your dice: "))
    return sides
def dice_number():
    no_of_dice_to_roll = int(input("How many dice would you like to roll: "))
    return no_of_dice_to_roll
def roll_dice(sides,no_of_dice_to_roll):
    dice = []
    print("You rolled {} {} sided dice".format(no_of_dice_to_roll,sides))
    for i in range(no_of_dice_to_roll):
        dice.append(random.randint(1,sides))
    return dice
def sum_dice(dice):
    s = sum(dice)
    print("The total value of your roll is {}".format(s))
def roll_again():
    res = input("Would you like to roll again(y/n)")
    if res.startswith('n'):
        flag = False
        print("Thank you for using the Python Dice App.")
    else:
        flag = True
    return flag



print("Welcome to the Python Dice App")
flag = True
while flag:
    a = dice_sides()
    b = dice_number()
    ls = roll_dice(a,b)
    print("-----Results are as followed-----")
    for i in ls:
        print(i)
    sum_dice(ls)
    flag = roll_again()