print("Welcome to the Fibonacci Calculator App")
print()
f = int(input("How many digits of the Fibonacci Sequence would you like to compute: "))
ls = [1,1]
rat = [1]
print("The first {} numbers of the Fibonacci sequence are:".format(f))
for i in range(2,f):
    sum = ls[-1]+ls[-2]
    ls.append(sum)
for num in ls:
    print(num)
print()
print("The corresponding Golden Ratio values are:")
for i in range(1,f-1):
    p = float(ls[i+1]/ls[i])
    rat.append(p)
for j in rat:
    print(j)
print("The ratio of consecutive Fibonacci terms approaches Phi; 1.618...")