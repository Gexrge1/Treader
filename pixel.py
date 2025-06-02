import pyautogui
import mouse
import time
# import keyboard
def pix():
    
    #pixel coordinates
    x1,y1,x2,y2 = 0,0,0,0
    """

    version #1 

    while y2 == 0:
        event = keyboard.read_event()
        if event.event_type == "down":    
            if event.name == "a":
                x1,y1 = pyautogui.position()
            elif event.name == "s":
                x2,y2 = pyautogui.position()
            else:
                print("ERROR")

    """
    
    """

    # version #2

    while y2 == 0:
        event = keyboard.read_event()
        if event.event_type == "down":
                if event.name == "a":
                    if x1 == 0:
                        x1,y1 = pyautogui.position()
                        print(x1,y1)
                    else:
                        x2,y2 = pyautogui.position()      
                        print(x2,y2)
    
    input()
    x1,y1 = pyautogui.position()
    input()
    x2,y2 = pyautogui.position()

    """

    #version 3

    while not mouse.is_pressed("left"):
        time.sleep(0.01)
    x1,y1 = pyautogui.position()
    print(x1,y1)
    while mouse.is_pressed("left"):
        time.sleep(0.01)
    x2,y2 = pyautogui.position()
    print(x2,y2)
    
    return x1,y1,x2,y2
    


def main():
    x1,y1,x2,y2 = pix()
    print(x1,y1,x2,y2)
    

if __name__=="__main__":
    main()
