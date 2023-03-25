from time import sleep
from bhaptics import haptic_player
import keyboard
from random import shuffle
import pandas as pd



player = haptic_player.HapticPlayer()
sleep(0.4)

dictionary = ["PedestrianLeft", "PedestrianMiddle", "PedestrianRight", "CarLeft", "CarMiddle", "CarRight", "TruckLeft", "TruckMiddle", "TruckRight"]
# 1 = Pedestrian, 2 = Car, 3 = Truck
category = [1, 1, 1, 2, 2, 2, 3, 3, 3]
# 4 = Left, 5 = Middle, 6 = Right
location = [4, 5, 6, 4, 5, 6, 4, 5, 6]
place = None
category_guess = None

# Registering the dictionary
for i in range(9):
    player.register(dictionary[i], dictionary[i] + ".tact")

def playDictionary():
    lst = list(range(18))
    shuffle(lst)
    locations_guessed = []
    actual_locations = []
    categories_guessed = []
    actual_categories = []
    locations_correct = []
    categories_correct = []
    for i in lst:
        trial_number = i%9
        player.submit_registered(dictionary[trial_number])
        print("Location:")
        event = keyboard.read_event()
        place = event.name
        print("Category:")
        sleep(0.05)
        event = keyboard.read_event()
        if event.event_type != keyboard.KEY_DOWN:
            event = keyboard.read_event()
        category_guess = event.name
        if int(place) < 4 and int(category_guess) > 3:
            temp = place
            place = category_guess
            category_guess = temp
        locations_guessed.append(place)
        actual_locations.append(location[trial_number])
        categories_guessed.append(category_guess)
        actual_categories.append(category[trial_number])
        locations_correct.append(location[trial_number] == int(place))
        categories_correct.append(category[trial_number] == int(category_guess))
        print(f"Place: Actual: {location[trial_number]}, Guessed: {place}\nCategory: Actual: {category[trial_number]}, Guessed: {category_guess}")
        sleep(2)
    data = pd.DataFrame({'ActualLocation': actual_locations, 'GuessedLocations': locations_guessed, 'LocationCorrect': locations_correct, 'ActualCategory': actual_categories, 'GuessedCategory':categories_guessed, 'CategoryCorrect': categories_correct})
    data.to_csv("Category_Guesses.csv", index_label='TrialNumber')


playDictionary()



