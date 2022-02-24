import keyboard
import pyautogui
import time
import _thread

flag = False


def loopAttack(name):
    global flag
    print(name)
    while True:
        time.sleep(0.1)
        if flag:
            pyautogui.mouseDown(button='right')
            time.sleep(0.65)
            pyautogui.mouseUp(button='right')
            print('activated')




_thread.start_new_thread(loopAttack, ('1',))


def callback(x):
    if x.name == 'shift':
        pyautogui.mouseDown(button='right')
        time.sleep(0.65)
        pyautogui.mouseUp(button='right')
    global flag
    if x.name == 'x':
        flag = not flag
        print('changed')


keyboard.on_press(callback)
keyboard.wait()
