import pyautogui
import time
a = input("Enter Message")
while True:
    pyautogui.typewrite(a)
    time.sleep()
    pyautogui.press("enter")