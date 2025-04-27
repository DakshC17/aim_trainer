import pygame
import random 
import math
import time
pygame.init()

WIDTH, HEIGHT = 800, 600
#FPS = 60  #
### Set up the display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")


class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR = "red"
    SECOND_coLOOR = "blue"


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True


    def update(self):
        if self.size + self.GROWTH_RATE < self.MAX_SIZE:
            self.grow = False


        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE
            


    
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), int(self.size))
        pygame.draw.circle(win, self.SECOND_coLOOR, (self.x, self.y), int(self.size)*0.8)
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), int(self.size)*0.6)
        pygame.draw.circle(win, self.SECOND_coLOOR, (self.x, self.y), int(self.size)*0.4)



### set up of the window and close functionality 
def main():
    run = True   #run is true for now and till it is true the window will run


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False    #here it becomes false and the window closes
                break
    pygame.quit()


if __name__=="__main__":  #main function is called when the script is run
    main()

