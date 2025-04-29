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
LIVES = 3
TOP_BAR_HEIGHT = 50
LABEL_FONT = pygame.font.SysFont("comicsans", 45)


class Target:
    MAX_SIZE = 50
    GROWTH_RATE = 0.5
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
      
### set up of the window and close functionality 
def format_time(secs):
    milli = math.floor(int(secs*1000%1000)/100)
    seconds = int(round(secs%60,1))
    minutes = int(secs//60)



    return f"{minutes:02d}:{seconds:02d}:{milli}"


def draw_top_bar(win,elapsed_time,targets_pressed,misses):
    pygame.draw.rect(win,"grey",(0,0,WIDTH,TOP_BAR_HEIGHT))
    time_label = LABEL_FONT.render(

        f"Time: {format_time(elapsed_time)}",1,"black")
    speed = round(targets_pressed/elapsed_time,1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s",1,"black")
    hits_label = LABEL_FONT.render(f"Hits: {targets_pressed}",1,"black")
    lives_label = LABEL_FONT.render(f"Lives: {LIVES-misses}",1,"black")




    win.blit(time_label,(15,15))
    win.blit(speed_label,(350,15))

    win.blit(hits_label,(650,15))
    win.blit(lives_label,(850,15))



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

        mouse_pos = pygame.mouse.get_pos() 
         #get the position of the mouse
        elapsed_time = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False    #here it becomes false and the window closes
                break

            if event.type == TARGET_EVENT:

                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING+TOP_BAR_HEIGHT, HEIGHT - TARGET_PADDING)
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

                
        if misses >= LIVES:
            pass #end game
        draw(WIN, targets)  #draw the targets on the window
        draw_top_bar(WIN, elapsed_time,target_pressed,misses)  #draw the top bar with the elapsed time and targets pressed
        pygame.display.update()  #update the display
    pygame.quit()


if __name__=="__main__":  #main function is called when the script is run
    main()
    