score = [10]

numscore = len(score)
print(numscore)
total = 0


for i in range(len(score)):
    total = total + score[i]
    print("Score ",score[i])

averagescore = total/numscore
total = 0
for items in range(len(score)):
    total = score[items]
    if total > averagescore:
        print("Score ",items + 1, "Is above average")
    elif total < averagescore:
        print("Socre ",items + 1, "Is below average")
    elif total == averagescore:
        print("Score ", items + 1,"Is the average")

print("Average candidate score ",averagescore)


