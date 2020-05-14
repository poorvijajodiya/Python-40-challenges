import random
print("Welcome to the Coin Toss App\n\nI will flip a coin a set number of times")
flip = int(input("How many times would you like me to flip the coin: "))
res = input("Would you like to see the result of each flip (y/n): ").lower()
head_count = 0
tail_count = 0
for i in range(0,flip):
    r = random.randint(0,1)
    if r == 1:
        head_count +=1
        if res.startswith('y'):
            print("HEADS")
    else:
        tail_count +=1
        if res.startswith('y'):
            print("TAILS")
    if head_count == tail_count:
        print("At {} flips, the number of heads and tails were equal at {} each.".format(i+1,(i+1)/2))
print("Results Of Flipping A Coin {} Times:".format(flip))
per1 = round(100*head_count/flip,2)
per2 = round(100*tail_count/flip,2)
print("Side\t\tCount\t\tpercentage\nHEADS\t\t{}\t\t\t{}\nTAILS\t\t{}\t\t\t{}".format(head_count, per1, tail_count, per2))
