# Amir Abu Hani
# This is the third module. This module is attendant with the various events, that player can encounter in the space
import random
import time
import space_explorations

events = ["Asteroid Field", "SpacePirates", "Alien Diplomacy", "Black Hole"]

spacecraft = space_explorations.Spaceship("apollo", 200, "power system")

numbers_of_events = 4


def handling_space_events():
    global numbers_of_events
    while numbers_of_events > 0:
        random_event = random.choice(events)
        if random_event == "Asteroid Field":
            print("You are encountering an asteroid field!")
            print("you have to navigate between the asteroids in the field cautiously.")
            spacecraft.fuel -= 30
            if spacecraft.fuel <= 0:
                break
            numbers_of_events -= 1
            time.sleep(2)
            print("You have successfully crossed the Asteroid Field. Let's continue ")
            print()
            time.sleep(1)
        elif random_event == "SpacePirates":
            print("You are encountering a space pirates!")
            print("You have to kill all the pirates. ")
            spacecraft.fuel -= 40
            time.sleep(3)
            print("You have successfully crossed the space pirates. Let's continue..")
            print()
            if spacecraft.fuel <= 0:
                break
            numbers_of_events -= 1
            time.sleep(1)
        elif random_event == "Alien Diplomacy":
            print("You are encountering an aliens! ")
            print("You have to use alien diplomacy to convince the aliens that you have to cross them.")
            spacecraft.fuel -= 50
            time.sleep(4)
            print("You have successfully crossed the alien, Let's continue..")
            print()
            if spacecraft.fuel <= 0:
                break
            numbers_of_events -= 1
            time.sleep(1)
        elif random_event == "Black Hole":
            print("You are encountering a black hole!")
            print("You have to get around the black hole")
            spacecraft.fuel -= 35
            time.sleep(3)
            print("You have successfully crossed the black hole, Let's continue..")
            print()
            if spacecraft.fuel <= 0:
                break
            numbers_of_events -= 1
            time.sleep(1)
    if numbers_of_events == 0:
        print("Congratulations! You were able to complete the space explorations mission")
    else:
        print(f"The spacecraft fuel is over. you could not complete the mission. You lost!")



