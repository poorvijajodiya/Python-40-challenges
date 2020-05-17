import random
print("--------------------Power-Ball Simulator--------------------\n")
white_balls = int(input("How many white-balls to draw from for the 5 winning numbers (Normally 69): "))
if white_balls<5:
    white_balls = 5
red_balls = int(input("How many white-balls to draw from for the 5 winning numbers (Normally 69): "))
if red_balls<1:
    red_balls = 1
odds = 1
for i in range(5):
    odds *= white_balls-i
odds *=red_balls/120
print("You have a 1 in {} chance of winning this lottery.".format(float(odds)))
ticket_interval = int(input("Purchase tickets in what interval: "))
winning_numbers = []
while len(winning_numbers)<5:
    r = random.randint(1,white_balls)
    if r not in winning_numbers:
        winning_numbers.append(r)
winning_numbers.sort()
r = random.randint(1,red_balls)
winning_numbers.append(r)
print("---------Welcome to the Power-Ball-----------")
print("\nTonight's winning numbers are: ", end="")
for i in winning_numbers:
    print(i,end=' ')
input("\nPress 'Enter' to begin purchasing tickets!!!")
tickets_purchased = 0
flag= True
tickets_sold = []
while winning_numbers not in tickets_sold and flag == True:
    lottery_numbers = []
    while len(lottery_numbers) < 5:
        r = random.randint(1, white_balls)
        if r not in lottery_numbers:
            lottery_numbers.append(r)
    lottery_numbers.sort()
    r = random.randint(1, red_balls)
    lottery_numbers.append(r)
    if lottery_numbers not in tickets_sold:
        tickets_purchased +=1
        tickets_sold.append(lottery_numbers)
        print(lottery_numbers)
    else:
        print("Losing ticket generated; disregard...")
    if tickets_purchased % ticket_interval==0:
        print(" {} tickets purchased so far with no winners...".format(tickets_purchased))
        res = input("keep purchasing tickets (y/n): ").lower()
        if res.startswith('n'):
            flag = False
if lottery_numbers==winning_numbers:
    print("Winning tickets number:",end=' ')
    for num in lottery_numbers:
        print("{}".format(num), end = ' ')
    print("Purchased a total of {} tickets.".format(tickets_purchased))
else:
    print("You bought {} tickets and still lost!\nBetter luck next time!".format(tickets_purchased))

