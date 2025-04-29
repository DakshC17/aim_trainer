# Aim Trainer Game
import pygame
import random 
import math
import time
pygame.init()

WIDTH, HEIGHT = 1600, 1200
#FPS = 60  #
### Set up the display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")


TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT 

TARGET_PADDING = 30

BG_COLOR = (0, 10, 40)


class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.3
    #GROWTH_RATE = 0.5
    COLOR = "red"
    SECOND_coLOOR = "white"


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True


    def update(self):
        if self.grow:
            self.size += self.GROWTH_RATE
            if self.size >= self.MAX_SIZE:
                self.grow = False
        else:
            self.size -= self.GROWTH_RATE

            


    
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), int(self.size))
        pygame.draw.circle(win, self.SECOND_coLOOR, (self.x, self.y), int(self.size*0.8))
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), int(self.size*0.6))
        pygame.draw.circle(win, self.SECOND_coLOOR, (self.x, self.y), int(self.size*0.4))


    def collide(self,x,y): 
        dis = math.sqrt((self.x-x)**2 + (self.y-y)**2)
        return dis <= self.size



def draw(win,targets):
    win.fill(BG_COLOR)  #fill the window with the background color
    for target in targets:
        target.draw(win)
    pygame.display.update()  #update the display
### set up of the window and close functionality 
def main():
    run = True
    targets = []   #run is true for now and till it is true the window will run
    clock = pygame.time.Clock()
    
    target_pressed = 0
    clicks = 0
    misses = 0
    start_time = time.time()
    
      #clock is created to control the frame rate
    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)  #set timer for target event


    while run:

        clock.tick(60)  #set the frame rate to 60 FPS
        click = False

        mouse_pos = pygame.mouse.get_pos()  #get the position of the mouse

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False    #here it becomes false and the window closes
                break

            if event.type == TARGET_EVENT:

                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1


        for target in targets:
            target.update()

            if target.size <= 0:
                targets.remove(target)
                misses += 1

            if click and target.collide(*mouse_pos):
                
                targets.remove(target)
                target_pressed += 1

                

        draw(WIN, targets)  #draw the targets on the window
    pygame.quit()


if __name__=="__main__":  #main function is called when the script is run
    main()
    