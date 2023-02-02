# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 16:25:01 2022

@author: 253364
"""

import pygame
import matplotlib.pyplot as plt
import random


from Boid import Boid
from Predator import Predator
from Target import Target
from Logger import Logger

screen_x = 1000         #set the y axis of the screen size
screen_y = 1000         #set the x axis screen size

pygame.init()                                           #Initisal the game enviroment
screen = pygame.display.set_mode((screen_x, screen_y))  #Pu the screen on screen
done = False                                            #Set the done to False
pygame.display.set_caption('Bird Flock Simulation')     #Put teh caption on the top of the window
Icon = pygame.image.load("images\\birdicon.png")        #load the image into pygame
pygame.display.set_icon(Icon)                           #Put the icon on the screen

clock = pygame.time.Clock()                             #Start the clock on the screen

log = Logger()          #Start the log

amount_birds = []

birds = []              #Stores all the birds within this list
eaten = []              #all the eaten birds are stored here


bird_width = 5          #set the width of the birds
bird_height = 5         #set the height of the birds

i = 0       #set the i and j paramters for locations of birds to swan in
j = 999

for b in range(30):                                                         #Iterate a set amount of time
    i = random.randint(1, 999)                                              #Find a random x and y within the space
    j = random.randint(1, 999)
    bird = Boid(i, j, bird_width, bird_height, 0, screen_y, 0, screen_x)    #create the bird
    birds.append(bird)                                                      #Add the bird to the list


predators = []                                                  

i = 0
j = 999

for p in range(4):
    i = random.randint(400, 600)                                #find a random coordindates for x and y in the middle of the screen
    j = random.randint(400, 600)
    pred = Predator(i, j, 5, 5,  0, screen_y, 0, screen_x)      #create the predator
    predators.append(pred)                                      #add the predator to the list
    


targets = []

targets.append(Target(50, 50, 10, 10))      #Create the targets at the coordindates
targets.append(Target(50, 950, 10, 10)) 
targets.append(Target(950, 950, 10, 10))
targets.append(Target(950, 50, 10, 10))

current_target = targets[0]                 #set the current target to the first target
counts = 0                                  #Initize the count and the tar
tar = 0

while(done == False):                       #Loop through all the object and methods
    counts = counts + 1                     #add one to the count
    current_target = targets[tar]           #Set the current target to the target in index
    
    for event in pygame.event.get():        #Check the events
        if event.type == pygame.QUIT:       #if the event is Quit
            ind = 0                         #set the variable to 0
            
            print("Amount of living", len(birds))
            
            for b in birds:                                 #Loop through the birds
                ind = ind + 1
                log.add_bird_log(b.list_x, b.list_y, ind)   #Add the bird coordinates to the list
            
                
            ind = 0
            print("eaten amount", len(eaten))
            
            for e in eaten:                                 #loop through eaten
                ind = ind + 1
                log.add_eaten_log(e.list_x, e.list_y, ind)  #log the eaten coordinates
                
            ind = 0
            for p in predators:                             #loop through the predators
                ind = ind + 1
                log.add_pred_log(p.list_x, p.list_y, ind)   #log the predators
            
            log.add_to_csv()                                #Add the data to the csv
            
            plt.title("Amount of birds at each iteration")
            plt.plot(amount_birds)
            plt.xlabel("Iterations")
            plt.ylabel("Amount of birds")
            plt.show()
            print(amount_birds)
            
            done = True                                     #close the game down
            pygame.quit()
            
    
    #find out where all the birds are
    
    bird_ranges_x = []                          #Initilise the ranges to store the data
    bird_ranges_y = []
    bird_ranges_width = []
    bird_ranges_height = []
    
    for bird in birds:                              #loop through each bird and add the x, y, width and height to the list
        bird_ranges_x.append(bird.x)
        bird_ranges_y.append(bird.y)
        bird_ranges_width.append(bird.width)
        bird_ranges_height.append(bird.height)
        
    
    pred_ranges_x = []                                  #initilse the list for the predators
    pred_ranges_y = []
    pred_ranges_width = []
    pred_ranges_height = []
    
    for pred in predators:                              #Loop through the predators and add the coordinates
        pred_ranges_x.append(pred.x)                    
        pred_ranges_y.append(pred.y)
        pred_ranges_width.append(pred.width)
        pred_ranges_height.append(pred.height)
        
    
    screen.fill((0,0,0))                                                                                #Emtpy the screen
    for bird in birds:
        bird.movement_rand()                                                                            #add the movement functions
        bird.cohesion(bird_ranges_x, bird_ranges_y, bird_ranges_width, bird_ranges_height)              
        bird.seperation(bird_ranges_x, bird_ranges_y, bird_ranges_width, bird_ranges_height)            
        bird.alignment(current_target)                                                                  
        bird.avoid(pred_ranges_x, pred_ranges_y, pred_ranges_width, pred_ranges_height, predators)
        pygame.draw.rect(screen, bird.colour, pygame.Rect(bird.x, bird.y, bird.width, bird.height))     #draw the bird on the screen
        bird.log_coordinates()                                                                          #Log the coordinates
        
    for pred in predators:                                                                              #Loop through the predators
        pred.movement_rand()                                                                            #Run the movement function
        pred.track_down(bird_ranges_x, bird_ranges_y, bird_ranges_width, bird_ranges_height, birds)
        pygame.draw.rect(screen, pred.colour, pygame.Rect(pred.x, pred.y, pred.width, pred.height))
        pred.log_coordinates()                                                                          #log the coordindates
        
    #Now if the bird and preditor met
    
    for pred in predators:                                                                                          #Loop through the predators
        for bird in birds:                                                                                          #Loop through the birds
            if pred.y - pred.height < bird.hitbox[1] + bird.hitbox[3] and pred.y + pred.height > bird.hitbox[1]:    #Find if a bird and predator overlap
                if pred.x + pred.width > bird.hitbox[0] and pred.x - pred.width < bird.hitbox[0] + bird.hitbox[2]:  #
                    bird.eaten()                    #Bird is eaten
                    eaten.append(bird)              #Bird added to the eaten list
                    birds.pop(birds.index(bird))    #removes the bird from list at index
                    pred.add_kill()                 #Add the kill to the predator
    
    
    if counts == 100:   #if the count reaches 100
        counts = 0      #reset the count
        tar = tar + 1   #add one to the tar
        if tar == 4:    #if the tar does equal 4
            tar = 0     #reset the index
            
    amount_birds.append(len(birds))
    pygame.display.flip()   #reset the display
    clock.tick(30)          #puase the clock
    
    



    