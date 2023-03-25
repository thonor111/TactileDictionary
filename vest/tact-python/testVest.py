from time import sleep
from bhaptics import haptic_player
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from random import shuffle
import keyboard



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

def testVest():
    # playing the whole dictionary once
    im = plt.imshow(np.zeros((384, 576)), cmap='gray')
    plt.axis('off')
    plt.ion()
    plt.draw()
    plt.pause(0.1)
    plt.show()
    sleep(0.1)
    event = keyboard.read_event()
    sleep(2)
    lst = list(range(9))
    for i in range(2):
        for trial_number in lst:
            im.set_data(mpimg.imread(f'images/{dictionary[trial_number % 9]}.png'))
            plt.draw()
            plt.pause(0.1)
            player.submit_registered(dictionary[trial_number])
            sleep(2)
        sleep(4)
    im.set_data(mpimg.imread(f'images/InstructionsTraining.png'))
    plt.draw()
    plt.pause(0.1)
    sleep(4)
    shuffle(lst)
    for trial_number in lst:
        im.set_data(mpimg.imread(f'images/InstructionsTraining.png'))
        plt.draw()
        plt.pause(0.1)
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
        if int(place) == location[trial_number] and int(category_guess) == category[trial_number]:
            im.set_data(mpimg.imread(f'images/{dictionary[trial_number % 9]}Correct.png'))
        else:
            im.set_data(mpimg.imread(f'images/{dictionary[trial_number % 9]}Wrong.png'))
        plt.draw()
        plt.pause(0.1)
        sleep(2)



testVest()