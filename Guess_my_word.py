import random
print("Welcome to the Guess My Word App\n")
game_dict = {
"sports":['basketball', 'baseball', 'soccer', 'football', 'tennis','curling'],
"colors":['orange', 'yellow', 'purple', 'aquamarine', 'violet', 'gold'],
"fruits":['apple', 'banana', 'watermelon', 'peach', 'mango', 'strawberry'],
"classes":['english', 'history', 'science', 'mathematics', 'art', 'health'],
}
game_keys = []
for i in game_dict.keys():
    game_keys.append(i)
flag = True
while flag:
    g1 = random.randint(0,3)
    game_category = game_keys[g1]
    g2 = random.randint(0, 5)
    game_word = game_dict[game_category][g2]
    blank_word = []
    for j in game_word:
        blank_word.append("-")
    print("Guess a {} letter word from the following category: {}".format(len(blank_word),game_category))
    guess_count = 0
    guess = ""
    while guess!=game_word:
        print("".join(blank_word))
        guess = input("Enter your guess: ").lower()
        guess_count +=1
        if guess==game_word:
            print("Correct! You guessed the word in {} guesses".format(guess_count))
            break
        else:
            print("The guess is not correct. let us reveal a letter to help you!")
            s =True
            while s:
                g3 = random.randint(0,len(blank_word)-1)
                if blank_word[g3] == '-':
                    blank_word[g3]=game_word[g3]
                    s = False
    res = input("Would you like to run the program again (y/n): ")
    if res.startswith('n'):
        flag = False
        print("Thank you for using the program. Goodbye.")