import pyautogui # import pyautogui
import time # import time

comment = ["Nice", "Good", "Not Bad", "Excellent", "Nice Caption", "Good Pose", "Wish You Good Luck", "Best of Luck"] # your commment



time.sleep(3) #program run time
try:

    for i in range(1, 20): # loop is running 20 times
        pyautogui.typewrite(comment[i%8]) # loop variable % comment index
        pyautogui.typewrite("\n") # new line
        time.sleep(2) # comment sent after 2 second
        pyautogui.press("Enter") # automatically pressed enter button loop running time
except:
    print("Loop is over....!") 
