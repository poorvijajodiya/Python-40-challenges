import random
print("Welcome to the Guess My Number App\n")
name = input("Hello! What is your name: ").title()
print("Well {}, I am thinking of a number between 1 and 20".format(name))
num = random.randint(1,20)
for i in range(5):
    guess = int(input("Enter a guess: "))
    if num<guess:
        print("Your guess is too high... ")
    elif num>guess:
        print("Your guess is too low...")
    else:
        break
if guess == num:
    print("Good job, {}! You guessed my number in {} guesses!".format(name,i+1))
else:
    print("Game Over. The number I was thinking of was {}".format(num))