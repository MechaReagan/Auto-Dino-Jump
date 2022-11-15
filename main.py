import pyautogui
from PIL import ImageGrab


screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.


# pyautogui.moveTo(850, 438) # Move the mouse to XY coordinates.
#
# pyautogui.click()
#
# pyautogui.press('space')

def is_cactus(data):
    for x in reversed(range(775, 820)):
        for y in reversed(range(400, 430)):
            if data[x, y] < 100:
                pyautogui.press('space')
                return


while True:
    image = ImageGrab.grab().convert("L")
    data = image.load()
    is_cactus(data)
