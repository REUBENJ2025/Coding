#As Computer Science
#16/10/25
#Student Lottery
#Greg Allcock
#Student Lottery

import random

def main():
    names = ["Reuben", "Lukas", "Alfie"]
    last_names = ["Joseph", "Deli", "Herring"]
    middle_names = ["Edward", "Deli", "Herring"] # Don't know middle names

    choices1 = random.choice(names)
    choices2 = random.choice(last_names)
    choices3 = random.choice(middle_names)

    print(f"A winner is a player with the first name {choices1}!")
    print(f"The second winner is a player with the last name {choices2}!")
    print(f"The third winner is a player with middle name {choices3}!")

main()