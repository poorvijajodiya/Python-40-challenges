from collections import Counter
print("Welcome to the Frequency Analysis App\n")
non_letters1 = []
phrase1 = input("Enter a word or phrase to count the occurrence of each letter: ").lower()
for i in phrase1:
    if  i.isalpha():
        continue
    else:
        non_letters1.append(i)
for j in non_letters1:
    phrase1 = phrase1.replace(j,'')
total_occurrences1 = len(phrase1)
letter_count1 = Counter(phrase1)
print("Here is the frequency analysis from key phrase 1:")
print("\tletter\toccurences\tpercentage")
for k,v in sorted(letter_count1.items()):
    percent1 = 100*v/total_occurrences1
    percent1 = round(percent1,2)
    print("\t\t{}\t\t{}\t\t{}%".format(k,v,percent1))
print("Letters ordered from highest occurrence to lowest:")
sorted1 = letter_count1.most_common()
sorted_ls1 = []
for h in sorted1:
    sorted_ls1.append(h[0])
for key in sorted_ls1:
    print(key,end = '')
print()
non_letters2 = []
phrase2 = input("Enter a word or phrase to count the occurrence of each letter: ").lower()
for i in phrase2:
    if  i.isalpha():
        continue
    else:
        non_letters2.append(i)
for j in non_letters2:
    phrase2 = phrase2.replace(j,'')
total_occurrences2 = len(phrase2)
letter_count2 = Counter(phrase2)
print("Here is the frequency analysis from key phrase 2:")
print("\tletter\toccurences\tpercentage")
for k,v in sorted(letter_count2.items()):
    percent2 = 100*v/total_occurrences2
    percent2 = round(percent2,2)
    print("\t\t{}\t\t{}\t\t{}%".format(k,v,percent2))
print("Letters ordered from highest occurrence to lowest:")
sorted2 = letter_count2.most_common()
sorted_ls2 = []
for h in sorted2:
    sorted_ls2.append(h[0])
for key in sorted_ls2:
    print(key,end = '')

