# Clash Royale UI Automation Script (Python)

This is a Python script for basic game UI automation using **PyAutoGUI**.


# what it does
Automatically repeats the game flow:
  - start match
  - play battle
  - end match
Uses image detection to identify game states and simulates human-like mouse clicks


# how it works
getpos.py:  use to get the fixed position 
test.py: use to test the screenshot confidence
main.py: The script determines the current game stage by comparing screenshots of visual scene features (such as start buttons or in-game buildings) with the game screen, and then performs actions based on the detected stage.

# Notes
Image files used for detection are environment-specific
(screen resolution, UI scale, theme) and are not included in this repository