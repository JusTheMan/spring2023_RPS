# File created by: Justin Edusada

# import libraries

from time import sleep

from random import randint

import pygame as pg

import os

# setup asset folders - images and sounds
game_folder = os.path.dirname(__file__)
print(game_folder)

#computer option
cpu_choice = ""
# game settings of the width, height, and frames the computer handles. 
WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
#tuples are immutable - cannot be changed once created
WHITE = (255, 255, 255)
#defines rgb values of black 
BLACK = (0, 0, 0)
#defines rgb values of Red 
RED = (255, 0, 0)
#defines rgb values of Green 
GREEN = (255, 255, 255)
#defines rgb values of Blue 
BLUE = (255, 255, 255)

# initializes pygame and create a window 
pg.init()
#initializes sound 
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock Paper Scissors...")
#processing time 
clock = pg.time.Clock()

# sounds
scissors_sound = pg.mixer.Sound(os.path.join(game_folder, "scissors.wav"))
#gets the image from folder and stores pixels
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
#gets the image from folder and stores pixels
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
#gets the image from folder and stores pixels
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
# creates transparency 
rock_image.set_colorkey(GREEN)
paper_image.set_colorkey(GREEN)
scissors_image.set_colorkey(GREEN)

# gets the geometry of the image
rock_rect = rock_image.get_rect()   
paper_rect = paper_image.get_rect()
scissors_rect = scissors_image.get_rect()
paper_rect.y = HEIGHT/2
scissors_rect.x = WIDTH/2

running = True
while running:
    clock.tick(FPS)
   
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            #when clicking x running is false. 
            running = False
            #mouse button up means once releasing the click. 
        if event.type == pg.MOUSEBUTTONUP:
            # gets the coords of mouse position of where you click
            mouse_coords = pg.mouse.get_pos()
            # print(mouse_coords)
            # print(mouse_coords[0])
            # print(mouse_coords[1])
            if rock_rect.collidepoint(mouse_coords):
                print("you clicked on rock")
                #rock drawn on screen
                userchoice = "rock"
                cpu_choice = "paper"
            elif paper_rect.collidepoint(mouse_coords):
                print("you clicked on paper")
            elif scissors_rect.collidepoint(mouse_coords):
                print("you clicked on scissors")
                pg.mixer.Sound.play(scissors_sound)
            else:
                print("you clicked on nothing...")
            # if mouse_coords[0] <= 300 and mouse_coords[1] <= 300:
            # # if mouse_coords == pg.mouse.get_pos():
            #     print("I clicked on the rock...")
    
    # get input from player...

    # update    
    # rock_rect.y += 1
    # paper_rect.y += 1
    # scissors_rect.x += 1
    # scissors_rect.y += 1
    
    # draw
    screen.fill(WHITE)

    screen.blit(scissors_image, scissors_rect)
    if cpu_choice == "paper":
        screen.blit(paper_image, paper_rect)
    screen.blit(rock_image, rock_rect)
    pg.display.flip()
    

pg.quit()