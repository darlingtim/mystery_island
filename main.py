from player_control import player
from validation.playername import playerNameValidation
from game_control.game import start_game, quit_game


print("Create a Username")
new_player = player
while True:
    name = input("Enter your preferred username here: ").strip()
    nameValidationMessage = playerNameValidation(name)
    if nameValidationMessage == "valid":
        new_player.name = name
        break
    else:
        for error in nameValidationMessage:
            print(error)
        continue

print("THE MYSTERY ISLAND GAME")
print("=" * 27)



        
instruction = f"Hello {new_player.name}!, \nWelcome to Mystery Island after the great storm of the sea.\nThe lighthouse is dark, the bridge is locked, and a rescue boat will arrive only if you restore the beacon.\nYou will need a rope and a lantern to cross the bridge and light the lighthouse.\npress 1 to start your journey through the Island.\nPress 2 to Quit.\n\n"

print(f"***INSTRUCTION:***\n{" "*5}{instruction}")

players_choice = input("Decide your Choice:  ").strip()

if players_choice == "1":
    started =start_game()
    print(started)

if players_choice == "2":
    print(quit_game())
    
