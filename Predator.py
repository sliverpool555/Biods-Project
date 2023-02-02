# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 21:12:42 2022

@author: 253364
"""

import random
import math


class Predator():
    
    def __init__(self, x, y, width, height, border_top, border_bottom, border_left, border_right):
        self.x = x                                                  #initisialise the variables for the size of the objects
        self.y = y
        self.width = width
        self.height = height
        self.colour = (0, 100, 255)                                 #set the colour of the predator
        self.list_x = []                                            #initialise the lists
        self.list_y = []
        self.border_top = border_top
        self.border_bottom = border_bottom
        self.border_left = border_left
        self.border_right = border_right
        self.hitbox = (self.x, self.y, self.width, self.height)     #Set the hitbox to the dimenions of the object
        self.kills = 0                                              #set the kills to 0
        self.angle = 0
        self.proximity = (self.x + 150, self.y + 150, self.width + 150, self.height + 150)  #set the size of the proximity
        self.speed = 3                                                                      #set the speed
      
    def check_walls(self, x, y):
        if y > self.border_bottom:              #if the y coordinate is greater then the bottom then put the pred back on the screen
            self.y = self.border_bottom - 10
            
        elif y < self.border_top:               
            self.y = self.border_top + 10       #if the y coordinate is less then the bottom then put the pred back on the screen
        else:
            self.y = self.y + random.randint(-1, 1) #add some random to reduce the confussion when the predator has to pick between two pray
            
        if x > self.border_right:
            self.x = self.border_right - 10 
        elif x < self.border_left:
            self.x = self.border_left  + 10
        else:
            self.x = self.x + random.randint(-1, 1)
            
        self.hitbox = (self.x, self.y, self.width, self.height)
        
    def movement_rand(self):
        x = self.x + random.randint(-1, 1)  #randomise the movements by 1
        y = self.y + random.randint(-1, 1) 
        
        self.check_walls(x, y)              #run the check rules function
            
        
    def track_down(self, bird_ranges_x, bird_ranges_y, bird_ranges_width, bird_ranges_height, birds):
        vectors = []
        for i in range(len(birds)):
            if self.proximity[1] - self.proximity[3] < bird_ranges_y[i] + bird_ranges_height[3] and self.proximity[1] + self.proximity[3] > bird_ranges_y[i]:       #check if the bird is within the proximity
                if self.proximity[0] + self.proximity[2] > bird_ranges_x[i] and self.proximity[0] - self.proximity[2] < bird_ranges_x[i] + bird_ranges_width[i]:
                    vectors.append(math.sqrt(((self.x + 5) - (bird_ranges_x[i] + 5))**2 + ((self.y + 5)- (bird_ranges_y[i] + 5))**2)) #Using Pythagorean Therom to find vector for all inside of proximity
                
        try:
            lowest = min(vectors)           #find the smallest vector
            index = vectors.index(lowest)   #find the index of the smallest vector
            
            prey_x = bird_ranges_x[index]   #find x and y of the smallest vector
            prey_y = bird_ranges_y[index]
        except:
            prey_x = self.y + random.randint(-self.speed, self.speed) #randomise the speed if no vector is found
            prey_y = self.y + random.randint(-self.speed, self.speed)
            
            
        if self.x > prey_x:                         #Move towards the nearest pray by adding or -1 to the coordinates and times by speed
            self.x = self.x - 1 * self.speed
        elif self.x < prey_x:
            self.x = self.x + 1 * self.speed
        else:
            self.x = self.x + random.randint(-self.speed, self.speed)
                
        if self.y > prey_y:
            self.y = self.y - 1 * self.speed
        elif self.y < prey_y:
            self.y = self.y + 1 * self.speed
        else:
            self.y = self.y + random.randint(-self.speed, self.speed)


            
        

    def add_kill(self):                 #add one to the kills
        self.kills = self.kills + 1
     
    def log_coordinates(self):          #log the coordinates for graphing
        self.list_x.append(self.x)
        self.list_y.append(self.y)
                        
        