player = [[1, 45],
          [2, 30],
          [2, 46],
          [1, 31],
          [1, 10],
          [1, 32],
          [2, 2]
          ]

green_score = 0

red_score = 0

for i in range(0,7):
    if player[i][0] == 1:
        green_score = green_score + player[i][1]
    if player[i][0] == 2:
        red_score = red_score + player[i][1]

print(f"The score for the red team was {red_score} and the score for the green team was {green_score}")