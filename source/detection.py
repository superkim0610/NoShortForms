# from pyautogui import locateAllOnScreen
# from PIL import ImageGrab, imread
import time
import pyautogui
import cv2 as cv
from PIL import ImageGrab

# screenshot = ImageGrab.grab()
# screenshot.save("screenshot.png")
# screenshot.close()

def detect():
    thumb_up_icon1 = cv.imread("resource/thumb_up_icon1.png")
    thumb_up_icon2 = cv.imread("resource/thumb_up_icon2.png")
    thumb_up_icon3 = cv.imread("resource/thumb_up_icon3.png")
    thumb_up_icon4 = cv.imread("resource/thumb_up_icon4.png")
    images = [thumb_up_icon1, thumb_up_icon2, thumb_up_icon3, thumb_up_icon4]
    
    screenshot = ImageGrab.grab()
    result = []
    
    for image in images:
        try:
            result.append(pyautogui.locate(image, screenshot, step=2, confidence=0.9))
        except:
            pass
        
        try:
            result.append(pyautogui.locate(image, screenshot, step=2, confidence=0.9, grayscale=True))
        except:
            pass
        
    print(len(result)/8)
    
    # try:
    #     g = [pyautogui.locate(thumb_up_icon1, screenshot, confidence=0.9),\
    #         pyautogui.locate(thumb_up_icon2, screenshot, confidence=0.9), \
    #         pyautogui.locate(thumb_up_icon1, screenshot, confidence=0.9, grayscale=True), \
    #         pyautogui.locate(thumb_up_icon2, screenshot, confidence=0.9, grayscale=True)], \
    #     print(g)
    # except:
    #     pass
    
    # try:
    #     for _g in g:
    #         for _ in _g:
    #             pass
    # except:
    #     pass
    
    # for _ in pyautogui.locateAllOnScreen(thumb_up_icon1, confidence=0.9):
    #     print(_)
    #     pyautogui.moveTo((_.left, _.top))

def get_image():
    pass

while True:
    t0 = time.time()
    detect()
    # print(time.time()-t0)
    # time.sleep(1)