# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 10:42:07 2022

@author: 253364
"""

import random
import math


class Boid():
    
    def __init__(self, x, y, width, height, border_top, border_bottom, border_left, border_right):
        
        self.x = x                              #initialise the parameters for size and boarders
        self.y = y
        self.width = width
        self.height = height
        self.border_top = border_top
        self.border_bottom = border_bottom
        self.border_left = border_left
        self.border_right = border_right
        self.colour = (255, 100, 0)             #set the colour
        self.list_x = []
        self.list_y = []
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.perception = (self.x + 50, self.y + 50, self.width + 50, self.height + 50) #create the preception and proximity areas larger then the object
        self.proximity = (self.x + 50, self.y + 50, self.width + 50, self.height + 50)  
        self.speed = 3                                                          #set the speed and the legit variables
        self.legit = 5 
        
        
        
    def check_walls(self, x, y):                #check if the object has reached a wall
        if y > self.border_bottom:
            self.y = self.border_bottom - 10    #if it has reached the bottom wall put object back
        elif y < self.border_top:
            self.y = self.border_top + 10
        else:
            self.y = self.y + random.randint(-1, 1) #if on screen add some random
            
        if x > self.border_right:
            self.x = self.border_right - 10
            
        elif x < self.border_left:
            self.x = self.border_left  + 10
        else:
            self.x = self.x + random.randint(-1, 1)
            
        self.hitbox = (self.x, self.y, self.width, self.height) #update the hitbox
        
    def movement_rand(self):
        x = self.x + random.randint(-1, 1)  #add random movement 
        y = self.y + random.randint(-1, 1) 
        
        self.check_walls(x, y)              #check the walls
        
    def seperation(self, bird_ranges_x, bird_ranges_y, bird_ranges_width, bird_ranges_height):
        
        for i in range(len(bird_ranges_x)):     #loop through the indexs of the birds to then find the index paramters of the bird for finding if it is within the proximity area
            if self.proximity[1] - self.proximity[3] < bird_ranges_y[i] + bird_ranges_height[3] and self.proximity[1] + self.proximity[3] > bird_ranges_y[i]:
                if self.proximity[0] + self.proximity[2] > bird_ranges_x[i] and self.proximity[0] - self.proximity[2] < bird_ranges_x[i] + bird_ranges_width[i]:
                    
                    #If it is a direct match then it isself
                    
                    if self.x == bird_ranges_x[i] and self.y == bird_ranges_y[i]: #if it shares the same coordinates it is the same bird so pass
                        pass
                    else:
                        
                        difference_x = self.x - bird_ranges_x[i]    #if bird is in the range find the x and y difference
                        difference_y = self.y - bird_ranges_y[i]
                        
                        if difference_x < self.x:           #takeaway or add to get closer on both x and y
                            x = self.x - 1 * self.speed
                        elif difference_x > self.x:
                            x = self.x + 1 * self.speed
                        else:
                            x = self.x
                            
                        if difference_y < self.x:
                            y = self.y - 1 * self.speed
                        elif difference_y > self.x:
                            y = self.y + 1 * self.speed
                        else:
                            y = self.y
                            
                            
    def cohesion(self, bird_ranges_x, bird_ranges_y, bird_ranges_width, bird_ranges_height):
        
        zone_avg_x = 0      #reset the zone averages and the total of birds in zone
        zone_avg_y = 0
        tots = 0
        
        for i in range(len(bird_ranges_x)): #find if there are other birds within the perception
            if self.perception[1] - self.perception[3] < bird_ranges_y[i] + bird_ranges_height[3] and self.perception[1] + self.perception[3] > bird_ranges_y[i]:
                if self.perception[0] + self.perception[2] > bird_ranges_x[i] and self.perception[0] - self.perception[2] < bird_ranges_x[i] + bird_ranges_width[i]:
                    
                    #If it is a direct match then it isself
                    
                    if self.x == bird_ranges_x[i] and self.y == bird_ranges_y[i]: #if it is the same bird pass
                        pass
                    else:
                        zone_avg_x = zone_avg_x + bird_ranges_x[i] + 5 #add the middle of the objects average and add one to the total amount of bird in area
                        zone_avg_y = zone_avg_y + bird_ranges_y[i] + 5
                        tots = tots + 1
               
        try:
            zone_avg_x = zone_avg_x / tots  #find the average
            zone_avg_y = zone_avg_y / tots
            
            if zone_avg_x < self.x:         #Move closer to the average
                x = self.x - 1 
            elif zone_avg_x > self.x:
                x = self.x + 1 
            else:
                x = self.x
                            
            if zone_avg_y < self.x:
                y = self.y - 1 
            elif zone_avg_y > self.x:
                y = self.y + 1 
            else:
                y = self.y
                
        except:
            pass        #if there are no birds in the area then just pass
        
        
    def alignment(self, target):
        if target.x < self.x:               #move closer to the coordinates of the target
            x = self.x - 1 * self.speed
        elif target.x > self.x:
            x = self.x + 1 * self.speed
        else:
            x = self.x
            
        self.x = x
        
                            
        if target.y < self.x:
            y = self.y - 1 * self.speed
        elif target.y > self.x:
            y = self.y + 1 * self.speed
        else:
            y = self.y
                
        self.y = y
        
    def avoid(self, pred_ranges_x, pred_ranges_y, pred_ranges_width, pred_ranges_height, predators):
        vectors = []
        for i in range(len(predators)):         #find if there are preditors in the area
            if self.proximity[1] - self.proximity[3] < pred_ranges_y[i] + pred_ranges_height[3] and self.proximity[1] + self.proximity[3] > pred_ranges_y[i]:
                if self.proximity[0] + self.proximity[2] > pred_ranges_x[i] and self.proximity[0] - self.proximity[2] < pred_ranges_x[i] + pred_ranges_width[i]:
                    vectors.append(math.sqrt(((self.x + 5) - (pred_ranges_x[i] + 5))**2 + ((self.y + 5)- (pred_ranges_y[i] + 5))**2)) #Using Pythagorean Therom to find vector for all inside of proximity
        try:
            if vectors == None:                 #if there arebirds in area just pass
                pass
            
            else:
                lowest = min(vectors)           #find the nearest preditor
                index = vectors.index(lowest)   #find the nearest index of preditor
                
                pred_x = pred_ranges_x[index]   #find the x and y of nearest predator
                pred_y = pred_ranges_y[index]
                
                if self.x > pred_x:             #move away from the predator
                    self.x = self.x + 5
                elif self.x < pred_x:
                    self.x = self.x - 5
                else:
                    self.x = self.x + random.randint(-self.speed, self.speed) #if no predator add some random
                        
                if self.y > pred_y:
                    self.y = self.y + 5 
                elif self.y < pred_y:
                    self.y = self.y - 5
                else:
                    self.y = self.y + random.randint(-self.speed, self.speed)
                
                
        except:
            pass #Dont add any input here
        
    def log_coordinates(self):      #log the coordindates
        self.list_x.append(self.x)
        self.list_y.append(self.y)
        
    def eaten(self):
        print("Eaten")      #If eaten print eat
                            
            
        
        
        
    