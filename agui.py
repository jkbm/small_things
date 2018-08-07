import pyautogui

#pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True

w, h = pyautogui.size()

for i in range(3):
      pyautogui.moveTo(100, 100, duration=0.25)
      pyautogui.moveTo(200, 100, duration=0.25)
      pyautogui.moveTo(200, 200, duration=0.25)
      pyautogui.moveTo(100, 200, duration=0.25)
      
pyautogui.moveTo(w/2, h/2, duration=1)
cpos = pyautogui.position()
print(cpos)