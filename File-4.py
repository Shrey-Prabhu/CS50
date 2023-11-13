import random

a = random.choice([100,90]) #choice([a,b,c]) any one from the list

b = random.randint(0,10)    #randint(a,b) any one a onwards upto b both inclusive

letters = ["a", "b", "c"]
random.shuffle(letters)     #parameter is a variable that is a list which is updated after shuffling

print(a)
print(b)
for i in letters:
    print(i, end = " ")