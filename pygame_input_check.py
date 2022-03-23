import pygame


def init():
    pygame.init()
    win = pygame.display.set_mode((400,400))

def getKey(keyName):
    #return true if the keyname is what was pressed
    ans = False 
    for event in pygame.event.get(): pass 
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if getKey("LEFT"):
        print("left pressed")
    if getKey("RIGHT"):
        print("right pressed")
    if getKey('a'):
        print("a pressed")
    

if __name__ == "__main__":
    init()
    while True:
        main()

