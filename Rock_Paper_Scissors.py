import random
print("Welcome to a game of Rock, Paper, Scissors\n")
n = int(input("How many rounds would you like to play: "))
moves = ['rock','paper','scissors']
player = 0
comp = 0
for i in range(n):
    print("Round {}".format(i+1))
    print("Player: {}\tcomputer: {}".format(player,comp))
    choose = input("Time to pick...rock, paper, scissors: ")
    players = choose.lower()
    if players in moves:
        comput = random.randint(0,2)
        computer = moves[comput]
        print("\tComputer:{}".format(computer))
        print("\tplayer: {}".format(players))
        if players=='rock' and computer=='scissors':
            print("\tRock beats scissor")
            winner = 'player'
            player +=1
        elif players=='scissors' and computer =='paper':
            print("\tscissors beats paper")
            winner = 'player'
            player +=1
        elif players =='paper' and computer=='rock':
            print("\tpaper beats rock")
            winner = 'player'
            player +=1
        elif computer=='rock' and players=='scissors':
            print("\tRock beats scissor")
            winner = 'computer'
            comp +=1
        elif computer=='scissors' and players =='paper':
            print("\tscissors beats paper")
            winner = 'computer'
            comp +=1
        elif computer =='paper' and players =='rock':
            print("\tpaper beats rock")
            winner = 'computer'
            comp +=1
        else:
            print("\tIt is a tie, how boring!\n\tThis round was a tie.")
        if winner == 'player':
            print("You win round{}".format(i+1))
        else:
            print("Computer win round{}".format(i+1))
    else:
            print("That is not a valid game option!")
            print("Computer gets the point!")
            comp +=1
print()
print("Final game results: ")
print("\tRounds Played: {}\n\tPlayer Score: {}\n\tComputer Score: {}".format(n, player, comp))
if player>comp:
    print("Winner: PLAYER!!!!!")
else:
    print("Winner: COMPUTER!!!!!")



