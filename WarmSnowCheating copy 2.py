import keyboard
import pyautogui
import time
import _thread
#from pynput.mouse import Listener

flag = False
Lflag = False


def loopAttack(name):
    global flag
    print(name)
    while True:
        time.sleep(0.1)
        if flag:
            pyautogui.mouseDown(button='right')
            time.sleep(0.65)
            pyautogui.mouseUp(button='right')


def AutoSmash(name):
    '''
    def on_click(x, y, button, pressed):  # 监听鼠标点击
        global Lflag
        if Lflag:
            time.sleep(0.05)
            pyautogui.click(button='right')
    with Listener(on_click=on_click) as listener:
        listener.join()
    '''
    global Lflag
    print(name)
    while True:
        time.sleep(0.15)
        if Lflag:
            pyautogui.click(button='left')
            time.sleep(0.18)
            pyautogui.mouseDown(button='right')
            pyautogui.mouseUp(button='right')


_thread.start_new_thread(loopAttack, ('1',))
_thread.start_new_thread(AutoSmash, ('2',))


def callback(x):
    if x.name == 'shift':
        pyautogui.mouseDown(button='right')
        time.sleep(0.65)
        pyautogui.mouseUp(button='right')
    global flag
    global Lflag
    if x.name == 'x':
        flag = not flag
    if x.name == 'z':
        Lflag = not Lflag


keyboard.on_press(callback)
keyboard.wait()
