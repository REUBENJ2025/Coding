#Template
# Power of code
# ReubenJoseph
# 09/10/25
# AS Computer Science
# Greg Allcock

def main():
    result = 0
    user_input = int(input("Please enter a number: "))
    iterator = 0

    for x in range(1, user_input + 1):
        iterator += 1
        result = result + ((user_input - iterator ** 2))
