import pygame
import utils
import sys


LENGTH = 800
S_COLOR = (0, 191, 255)
I_COLOR = (190, 80, 80)
R_COLOR = (145, 195, 80)
FPS = 30


file = open("C:\\Users\Ignacy\\Desktop\python\\algorytmy_genetyczne_2\\epidemie\\magistrala.txt", "r")

DIM = int(utils.readUntilChar(file, "d"))
#print(DIM) #
block_length = LENGTH // DIM
steps = []
while True:
    step = utils.readOneStep(file)
    #print(step) #
    steps.append(step)
    if not step:
        break

#print(steps) #    
pygame.init()
window = pygame.display.set_mode((LENGTH, LENGTH)) 
clock = pygame.time.Clock()   
def drawBoard(step):
    i = 0
    for point in step:
        if(point == "s"):
            color = S_COLOR
        elif(point == "i"):
            color = I_COLOR
        else:
            color = R_COLOR        
        pygame.draw.rect(window, color, pygame.Rect((i % DIM) * block_length, (i // DIM) * block_length, block_length, block_length)) 
        i += 1 
    pygame.display.update()  

for step in steps:
    pygame.event.get()
    drawBoard(step)
    clock.tick(FPS) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()   

#def makeBoard(file):
#    dim = int(file.read(1))

#while run:
#    clock.tick(3)