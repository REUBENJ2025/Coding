#Greg Allcock
#Reuben Joseph
#22/10/25
#for in
#Computer science
import random, string
nlist = [10, 20, 30, 40]

for x in range(0, len(nlist)):
    print(nlist[x], end=' ')

print(' ')
for item in nlist:
    print(item,end=' ')

num = 20

print(' ')

if num in nlist:
    print("Found")

while num in nlist:
    print("still repeating")
    nlist.remove(20)

new_list = []

for i in range(100000):
    new_list.append(1 + i)

#print(new_list)

character = string.ascii_letters + string.digits + string.punctuation + string.



password = [random.choice(character) for x in range(0,200)]


print(' '.join(password))
