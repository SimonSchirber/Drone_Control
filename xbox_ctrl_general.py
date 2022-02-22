import pygame
from pygame.locals import *

##initialize pygame
pygame.init()
dispay = pygame.display.set_mode((600,600), 0,32)
clock = pygame.time.Clock()

#intialize joystick
pygame.joystick.init()
joystick = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
print(joystick)

keepPlaying = True

while keepPlaying:
    #check for events in pygame from controller
    for event in pygame.event.get():
        #click button then leave (print(event to see what the event is called and all details))
        #print(event)
        print(event)
        #button up/down are for binary buttons, button number indicates which button
        if event.type ==JOYBUTTONDOWN:
            #Buttons
            if (event.button == 0):
                print('a pressed')
            if (event.button == 1):
                print('b pressed')
            if (event.button == 2):
                print('x pressed')
            if (event.button == 3):
                print('y pressed')
            #Bumpers
            if (event.button == 4):
                print('left bumper pressed')
            if (event.button == 5):
                print('right bumper pressed')
        if event.type ==JOYBUTTONUP:
            print('button released')


        if event.type == JOYAXISMOTION:
            #Left Joystick
            if event.axis < 2:
                print("left joystick")
                if (event.axis == 0):
                    if (event.value > 0):
                        print('up')
                    if (event.value < 0):
                        print('down')
                if (event.axis == 1):
                    if (event.value > 0):
                        print('right')
                    if (event.value < 0):
                        print('left')

            #Right Joystick
            if (event.axis >1) and (event.axis< 4):
                print('right joystick')
                if (event.axis == 2):
                    if (event.value > 0):
                        print('up')
                    if (event.value < 0):
                        print('down')
                if (event.axis == 3):
                    if (event.value > 0):
                        print('right')
                    if (event.value < 0):
                        print('left')
            #Left Trigger
            if (event.axis == 4):
                print('left trigger')
            #Right Trigger
            if (event.axis == 5):
                print('right trigger')
        
        if event.type == JOYHATMOTION:
            print(event.value)
            #DPAD up,down,left,right
            if (event.value == (1,0)):
                print('right dpad')
            if (event.value == (-1,0)):
                print('left dpad')
            if (event.value == (0,1)):
                print('up dpad')
            if (event.value == (0,-1)):
                print('down dpad')

        #exitx button on py display
        if event.type == QUIT:
            pygame.quit()
        
        



#Xbox controller pygame
#JOTBUTTON (DOWN/UP) event
    #ABXY .button->
        #a = 0
        #b = 1
        #y = 3
        #x = 2

    #Bumpers .button -> 
        #left : 4
        #right : 5

#JOYAXISMOTION event

    #Right joystick: .axis ->
        #  up/down  2:(up:pos, down:neg)  
        # left/right  3: (left:neg, right:pos)

    #Left joystick: .axis -> 
        #  up/down  0: .value(down:neg, up:pos)  
        # left/right  1: .value(left:neg, right:pos)

    #Triggers Left and Right .axis ->
        #right trig (5): .value (1 =pulldown, -1 = letup)
        #left trig  (4): .value (1 =pulldown, -1 = letup)

#JOYHATMOTION event
    # DPAD .value ->
        # right:(1,0)
        # left: (-1,0)
        # up: (0,1)
        # down: (0,-1)           
         
        

        

       
