import time
import os
import datetime
def sleep(s:int):
    x = datetime.datetime.now()
    while 1:
        xx = datetime.datetime.now()
    
        xx=xx-x
        xx=xx.seconds
        if xx>=s:
            break

print("\033c\033[40;37m\n please wait")
sleep(5)


