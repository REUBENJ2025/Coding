#Greg Allcock
#Reuben Joseph
#22/10/25
#for in
#Computer science

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
