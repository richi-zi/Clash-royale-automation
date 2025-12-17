import pyautogui
import keyboard
import time

while True:
    if keyboard.is_pressed("F8"):
        print(pyautogui.position())
        time.sleep(0.3)