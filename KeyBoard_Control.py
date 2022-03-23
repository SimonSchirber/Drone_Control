from djitellopy import tello
import pygame_input_check as ic
import time
import cv2

drone = tello.Tello()
drone.connect()
print(f"Battery at {drone.get_battery()}%")

#Sdrone.stream_on()



def getInput():
    
    lr, fb, ud, yv = 0,0,0,0
    speed = 75
    
    if ic.getKey("LEFT"):
        lr = -speed
    elif ic.getKey("RIGHT"):
        lr = speed
    
    elif ic.getKey("UP"):
        fb = speed
    elif ic.getKey("DOWN"):
        fb = -speed
    
    elif ic.getKey("w"):
        ud = speed
    elif ic.getKey("s"):
        ud = -speed 
    
    elif ic.getKey("d"):
        yv = speed
    elif ic.getKey("a"):
        yv = -speed

    #land
    if ic.getKey("q"):
        drone.land()
        time.sleep(3)
    #takeoff
    if ic.getKey("e"):
        drone.takeoff()
    #take a photo, save it uniquely
    if ic.getKey('z'):
        cv2.imwrite(f"Images/{time.time()}.jpg")
        time.sleep(.3)
    
    return [lr, fb, ud, yv]
    
    

#use pygame)input_check script to check for keys
ic.init()
while True:
    vals = getInput()
    drone.send_rc_control(vals[0],vals[1],vals[2],vals[3])

    #stream drone
    img = drone.get_frame_read().frame
    img = img = cv2.resize(img, (360,420))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    time.sleep(.05)