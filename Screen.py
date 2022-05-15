from pynput.mouse import Listener
import pyautogui
global a
a=0
def on_click(x, y, button, pressed):
    if pressed:
        global a
        a=a+1
        n2=str(a)
        n=" .png"
        name=n2+n
        pyautogui.screenshot(name)

        with Listener(on_click=on_click) as listener:
            listener.join()
