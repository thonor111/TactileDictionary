from time import sleep
from bhaptics import haptic_player
import keyboard
from random import shuffle
import pandas as pd



player = haptic_player.HapticPlayer()
sleep(0.4)

dictionary = ["PedestrianLeft", "PedestrianMiddle", "PedestrianRight", "CarLeft", "CarMiddle", "CarRight", "TruckLeft", "TruckMiddle", "TruckRight"]
# 0 = Pedestrian, 1 = Car, 2 = Truck
category = [0, 0, 0, 1, 1, 1, 2, 2, 2]
# 0 = Left, 1 = Middle, 2 = Right
location = [0, 1, 2, 0, 1, 2, 0, 1, 2]
place = None
category_guess = None

# Registering the dictionary
for i in range(9):
    player.register(dictionary[i], dictionary[i] + ".tact")

def audiovisualVibration():
    while True:
        lst = list(range(9))
        shuffle(lst)
        for trial_number in lst:
            player.submit_registered(dictionary[trial_number])
            sleep(2)


audiovisualVibration()