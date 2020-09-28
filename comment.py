import requests
import time
from pyautogui import *
def check_connetion():
    try:
        if requests.get("http://google.com").status_code == 200:
            return "ok"
        else:
            return "stop"
    except:
        return "stop"
 
#use bellow comments to grab information about your window sizes, here i used mine

#comment button(970,686)
#comment_box start(436,691)
#terminal minimize(1264,48)
#window_somewhere(231,420)

def comment(a):
    com_bu_x = 970  #place here your comment button x value
    com_bu_y = 686  #place here your comment button y value
    com_bx_x = 436  #place here your comment box starting x value    
    com_bx_y = 691  #place here your comment box starting y value
    moveTo(com_bx_x,com_bx_y)
    click()
    write(a)
    moveTo(com_bu_x,com_bu_y)
    click()

def work(a,b,c):
    if b==0:
        print("done")
    else:
        if check_connetion() == "ok":
            comment(a)
            time.sleep(c)
            work(a,b-1,c)
        else:
            pass

work(input("message:\n"),int(input("times: ")),int(input("how many seconds wait?: ")))
