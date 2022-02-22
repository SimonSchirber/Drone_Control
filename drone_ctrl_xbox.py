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
            #Right Joystick
            if (event.axis >1) and (event.axis< 4):
                print('right joystick')
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

        #exit x button on py display
        if event.type == QUIT:
            pygame.quit()
        
 
        

        

       
