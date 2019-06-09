import pyautogui
import PIL.ImageGrab
import time
pyautogui.pause = 2.5

#Change the hotkeys but make sure to keep them in quotes
othersHealthKey = '9'
myManaKey = '7'
print("Welcome to Jared's Dominando Bot:")
print("Please select from the following: ")
print("1: Auto Refill Mana")
print("2: Auto Heal Other Person")
print("3: Both")
result = input(">> ")

def get_color(x, y):
    rgb = PIL.ImageGrab.grab().load()[x, y]
    return rgb

input("Press enter when Tibia is loaded and colors will be grabbed in 5 seconds")
for i in range(0,4):
    print(str(i+1) + " ")
    time.sleep(1)
print("Bot is LIVE!!!")

#These are the X,Y coordinates to get the color
othersHealth = [1321, 484]
myMana = [1299,160]

startOthersHealth = get_color(othersHealth[0],othersHealth[1])
startMyMana = get_color(myMana[0],myMana[1])
#startAnyThing = get_color('1244', '300')

if result is '1':
    while True:
        newMyMana = get_color(myMana[0],myMana[1])
        if startMyMana != newMyMana:
            pyautogui.press(myManaKey)
            time.sleep(1)
if result is '2':
    while True:
        newOthersHealth=get_color(othersHealth[0],othersHealth[1])
        if startOthersHealth != newOthersHealth:
            pyautogui.press(othersHealthKey)
            time.sleep(1)
if result is '3':
    while True:
        newOthersHealth = get_color(othersHealth[0],othersHealth[1])
        newMyMana = get_color(myMana[0],myMana[1])
        if startOthersHealth != newOthersHealth:
            pyautogui.press(othersHealthKey)
            time.sleep(1)
        if startMyMana != newMyMana:
            pyautogui.press(myManaKey)
            time.sleep(1)
        time.sleep(0.8)
