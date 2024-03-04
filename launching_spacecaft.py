# Amir Abu Hani
# This is the fourth module. from this module, the app will run. it includes the other three modules and
# another 2 built-in modules(time and json)
import time, json
from handling_events import handling_space_events, spacecraft
from exploring_galaxy import exploring_the_galaxy

exploring_the_galaxy()
player_name = input("Enter your name: ")
print(f"Welcome {player_name} to the space exploring game. we decided to launch you to the galaxy. here is your "
      f"spacecraft: ")
print(spacecraft.__str__())
print("You are launching successfully. The game has started")
print()
time.sleep(2)
handling_space_events()


# Saving the spacecraft details in info.json file
def save_game_data(filename, data):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


essential_information = spacecraft.spaceship_details()

save_game_data("info.json", essential_information)
