#Greg Allcock
#ReubenJoseph#
#26/10/25
#Game leaderboard
#Computer Science


import json
import sys
import time



def main():
    return [
    {"Player": "Alex", "Game": "Minecraft", "Score": 54},
    {"Player": "Ben", "Game": "Fortnite", "Score": 88},
    {"Player": "Chloe", "Game": "Fifa", "Score": 42},
    {"Player": "Dylan", "Game": "Minecraft", "Score": 71},
    {"Player": "Ella", "Game": "Fifa", "Score": 95},

]


def save_leaderboard(data):
    with open("leaderboard.json", "w") as file: #Creates a Json file and writes over file to include data
        json.dump(data, file, indent=10)



def print_scores(data): #Prints player score from data
    print("Current Leaderboard")
    for values in data:
        print(f"{values['Player']}: {values['Score']}")

 
def user_input(data): #Looks for  user from json file
    choice = input("\nWhat game would you like to view? ")
    found = False
    print(f"\nPlayers who play {choice}:")
    for entry in data:
        if entry['Game'].lower() == choice.lower():
            print(f"{entry['Player']}")
            found = True
    if found:
        highest_score(data, choice)
    else:
        print("No players found for that game")

def highest_score(data, game_choice): #Finds the player with the highest score in that game 
    players_in_game = [p for p in data if p['Game'].lower() == game_choice.lower()]
    if not players_in_game:
        print(f"No players found for {game_choice}")
        return
    
    highest_player = max(players_in_game, key=lambda x:x['Score'])
    print(f"\nThe Player with the highest score for {game_choice} is {highest_player['Player']}")
    print(f"\nTheir Score is {highest_player['Score']} points.")


def continue_program(data): #Continues program if user decided
        program = False
        while program == False:
            decision = input("\nPlease press y to continue to view another player or n to stop the program: ")
            decision = decision.lower()
            if decision == "y":
                user_input(leaderboard)
            else:
                print("\n \nThanks for checking the leaderboard!")
                program = True

            for i in range(10,0, -1):
                unit = "second" if i == 1 else "seconds" #Avoids print the last character twice
                print(f"\rExiting in {i} {unit} ", end = "", flush=True) #Prints on one line countdown
                time.sleep(1)
            sys.exit()


                

### Running program with functions ###n

leaderboard = main()
save_leaderboard(leaderboard)
print_scores(leaderboard)
user_input(leaderboard)
continue_program(leaderboard)
