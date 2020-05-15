import random
Thesaurus = {
"hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
"cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'],
"happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
"sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],
}
print("Welcome to the Thesaurus App!\n\nChoose a word from the thesaurus and I will give you a synonym.")
print("Here are the words in the thesaurus:")
for i in Thesaurus.keys():
    print("\t{}".format(i))
word = input("What word would you like a synonym for: ").lower()
if word in Thesaurus.keys():
    r = random.randint(0,4)
    print("A synonym for {} is {}.".format(word,Thesaurus[word][r]))
else:
    print("I'm sorry, that word is not currently in the thesaurus.")
inp = input("Would you like to see the whole thesaurus (yes/no): ")
if inp.startswith('y'):
    for k,v in Thesaurus.items():
        print("{} synonyms are".format(k.title()))
        for val in v:
            print("\t{}".format(val))
else:
    print("I hope you enjoyed the program. Thank you!")
