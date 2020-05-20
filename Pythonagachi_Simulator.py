import random
class Creature:
    def __init__(self,name):
        self.name = name.title()
        self.hunger, self.boredom, self.tiredness, self.dirtiness = 0,0,0,0
        self.food = 2
        self.is_sleeping = False
        self.is_alive = True

    def eat(self):
        if self.food > 0:
            self.food -= 1
            self.hunger -= random.randint(1,4)
            print("Yum! " + self.name + " ate a great meal!")
        else:
            print(self.name + " doesn't have any food! Better forage for some.")
        if self.hunger<0:
            self.hunger = 0

    def play(self):
        r = random.randint(0,2)
        print("{} wants to play a game.".format(self.name))
        print("{} is thinking of a number 0, 1, or 2.".format(self.name))
        guess = int(input("What is your guess: "))
        if r == guess:
            print("That is correct!!!")
            self.boredom -= 3
        else:
            print("That is an incorrect!!!")
            self.boredom -=1
        if self.boredom<0:
            self.boredom=0

    def sleep(self):
        self.is_sleeping = True
        self.tiredness -=3
        self.boredom -=2
        print("Zzzzzz....Zzzzzz....Zzzzzz")
        if self.tiredness<0:
            self.tiredness = 0
        if self.boredom<0:
            self.boredom = 0

    def awake(self):
        r = random.randint(0,2)
        if r==0:
            print("{} just woke up".format(self.name))
            self.is_sleeping = False
            self.boredom = 0
        else:
            print("{} would not woke up".format(self.name))
            self.sleep()

    def clean(self):
        self.dirtiness = 0
        print("{} took a bath".format(self.name))

    def forage(self):
        food_found = random.randint(0,4)
        self.food +=food_found
        self.dirtiness +=2
        print("{} found {} pieces of food!".format(self.name,food_found))

    def show_values(self):
        print("Creature Name: {}\nHunger (0-10): {}\nBoredom (0-10): {}\nTiredness (0-10): {}\nDirtiness (0-10): {}\n".format(self.name,self.hunger,self.boredom,self.tiredness,self.dirtiness))
        print("Food Inventory: {} pieces\n".format(self.food))
        if self.is_sleeping:
            print("Current Status: Sleeping")
        else:
            print("Current Status: Awake")

    def incriment_values(self,game_difficulty):
        self.hunger += random.randint(0,game_difficulty)
        if self.is_sleeping == False:
            self.boredom = random.randint(0,game_difficulty)
            self.tiredness = random.randint(0,game_difficulty)
        self.dirtiness += random.randint(0,game_difficulty)

    def kill(self):
        if self.hunger>=10:
            print(self.name + " has starved to death...")
            self.is_alive = False
        elif self.dirtiness>=10:
            print(self.name + " has suffered from infection and died...")
            self.is_alive = False
        elif self.boredom>=10:
            self.boredom = 10
            print(self.name + " has bored and feeling asleep")
            self.is_sleeping = True
        elif self.tiredness >= 10:
            self.tiredness = 10
            print(self.name + " is sleepy and feeling asleep")
            self.is_sleeping = True

def show_menu(Creature):
    if Creature.is_sleeping:
        choice = input("\nEnter (6) to try and wake up: ")
        choice = '6'
    else:
        print("Enter 1 to eat.\nEnter 2 to play.\nEnter 3 to sleep.\nEnter 4 to take a bath.\nEnter 5 to forage for food.")
        choice = int(input("What is your choice: "))
    return choice

def call_action(Creature,choice):
    if choice == 1:
        Creature.eat()
    elif choice == 2:
        Creature.play()
    elif choice == 3:
        Creature.sleep()
    elif choice == 4:
        Creature.clean()
    elif choice == 5:
        Creature.forage()
    elif choice == 6:
        Creature.awake()
    else:
        print("not a valid choice")

print("Welcome to the Pythonagachi Simulator App")
diff = int(input("Please choose a difficulty level (1-5): "))
if diff>5:
    diff = 5
elif diff<1:
    diff = 1
active = True
while active:
    name = input("What name would you like to give your pet Pythonogachi: ")
    player = Creature(name)
    rounds = 1
    while player.is_alive:
        print("\n--------------------------------------------------------------------------------")
        print("Round #" + str(rounds))
        player.show_values()
        choice = show_menu(player)
        call_action(player,choice)
        print("Round #{} Summary:".format(rounds))
        player.show_values()
        input("Press (enter) to continue...")
        player.incriment_values(diff)
        player.kill()
        rounds +=1
    print("R.I.P")
    print(player.name + " survived a total of " + str(rounds - 1) + " rounds.")
    choice = input("Would you like to play again (y/n): ").lower()
    if choice != 'y':
        active = False
        print("Thank you for playing Pythonagachi!")
