
from validation.playername import playerNameValidation
from game_control.game import Game


print("Create a Username")

while True:
    name = input("Enter your preferred username here: ").strip()
    nameValidationMessage = playerNameValidation(name)
    if nameValidationMessage == "valid":
        mystery_island = Game(name)
        break
    else:
        for error in nameValidationMessage:
            print(error)
        continue

print("THE MYSTERY ISLAND GAME")
print("=" * 27)



        
instruction = f"Hello {mystery_island.player_name}!, \nWelcome to Mystery Island after the great storm of the sea.\nThe lighthouse is dark, the bridge is locked, and a rescue boat will arrive only if you restore the beacon.\nYou will need a rope and a lantern to cross the bridge and light the lighthouse.\npress 1 to start your journey through the Island.\nPress 2 to Quit.\n\n"

print(f"***INSTRUCTION:***\n{" "*5}{instruction}")

players_choice = input("Decide your Choice:  ").strip()


if players_choice == "1":
    started = mystery_island.start_game()
    print(started)

if players_choice == "2":
    print(mystery_island.quit_game())
    
