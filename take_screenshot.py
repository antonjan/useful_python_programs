# Using PyAutoGUI library
# pip install PyAutoGUI
import pyautogui
ss = pyautogui.screenshot ()
ss.save("image1.png")
# Using PIL library
# pip install Pillow
from PIL import ImageGrab
ss = ImageGrab.grab()
ss.save("image2.png")
