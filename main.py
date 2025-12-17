import pyautogui
import time

StartPic = "pic/start.png"
BattlePic = "pic/battle.png"
EndPic = "pic/end.png"

# confidence
StartCon = 0.4
BattleCon = 0.5
EndCon = 0.4

StartReg = (787, 761, 290, 182)
StartCli = (959,870)
EndReg = (834, 896, 192, 104)
EndCli = (964, 963)

Card = (817, 945)
Drop = (854, 788)

def click(pos):
    pyautogui.moveTo(pos, duration=0.05)
    pyautogui.mouseDown()
    time.sleep(0.15)
    pyautogui.mouseUp()

time.sleep(3)
print("3s begin")
#check until click start
while True:
    while True:
        try:
            start_pos = pyautogui.locateOnScreen(StartPic, confidence=StartCon, region=StartReg)
        except pyautogui.ImageNotFoundException:
            start_pos = None
        if start_pos:
            click(StartCli)
            time.sleep(1)
        else:
            break

    #loading
    while True:
        try:
            king_pos = pyautogui.locateOnScreen(BattlePic, confidence=BattleCon)
        except pyautogui.ImageNotFoundException:
            king_pos = None
        if king_pos:
            break
        time.sleep(0.5)
    #battle
    king_missing = 0
    maxtime = 180
    starttime = time.time()
    while True:
        click(Card)
        time.sleep(3)
        click(Drop)
        time.sleep(3)
        try:
            king_pos = pyautogui.locateOnScreen(
                BattlePic, confidence=BattleCon
            )
        except pyautogui.ImageNotFoundException:
            king_pos = None
        #try to end
        if king_pos:
            king_missing = 0
        else:
            king_missing += 1
        #check it more time to avoid the king be shelter
        if king_missing >= 3:
            break
        try:
            end_pos = pyautogui.locateOnScreen(
                EndPic, confidence=EndCon, region=EndReg
            )
        except pyautogui.ImageNotFoundException:
            end_pos = None

        if end_pos:
            break

        #overtime
        if time.time() - starttime > maxtime:
            break
        time.sleep(0.5)
    #end
    while True:
        try:
            end_pos = pyautogui.locateOnScreen(
                EndPic, confidence=EndCon, region=EndReg
            )
        except pyautogui.ImageNotFoundException:
            end_pos = None
        if end_pos:
            click(EndCli)
            time.sleep(2)
        else:
            break