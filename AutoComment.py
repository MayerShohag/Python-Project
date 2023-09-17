import pyautogui
import time

comment = ["Nice", "Good", "Not Bad", "Excellent", "Nice Caption", "Good Pose", "Wish You Good Luck", "Best of Luck"]



time.sleep(3)
try:

    for i in range(1, 20):
        pyautogui.typewrite(comment[i%8])
        pyautogui.typewrite("\n")
        time.sleep(2)
        pyautogui.press("Enter")
except:
    print("Loop is over....!")