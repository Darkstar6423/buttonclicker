from pynput.keyboard import Key, Listener, Controller
import threading
import sys
import time
import os
import random

isActive = True
keepPressing = True
args = sys.argv
keyboard = Controller()
isRandom = False

if len(args) < 2 :
    print('Error requires at least one argument \n')
    print('args are [letter to press] <interval> <random interval y/n>')
    os._exit(0)
    
if len(args) > 3:
    if args[3] == 'y':
        isRandom = True
        if int(args[2]) < 2:
            print('Error: randomness requires an interval greater than 1')
            os._exit(0)
        
    else:
        isRandom = False

def theLoop():
    global isActive
    global args
    global keyboard
    delay = 0
    key = 'n'
    if args[1] == 'space':
        key = Key.space
    elif args[1] == 'shift':
        key = Key.shift
    else:
        key = args[1]
    
    
    if len(args) < 3 :
        delay = 1
    else:
        delay = float(args[2])
        
    while isActive:
        if keepPressing == False:
            continue
            
        
        if isRandom == True:
            time.sleep(random.randrange(1, delay))
        else:    
            time.sleep(delay)
        keyboard.press(key)
        time.sleep(.001)
        keyboard.release(key)   


thread = threading.Thread(target=theLoop)
thread.start()

def on_press(key):
    print('{0} pressed ' .format(key))


def on_release(key):
    global isActive
    global keepPressing
    #turn on and off thread
    if key == Key.esc:
        if keepPressing == True:
            keepPressing = False
        else:
            keepPressing = True

    #program exit
    if key == Key.f1:
        isActive = False
        return False


with Listener(
        on_press=on_press,
        on_release=on_release
) as listener:
    listener.join()

    
    
