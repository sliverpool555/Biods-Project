# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 17:17:26 2022

@author: 253364
"""

import os
import pandas as pd


class Logger():
    
    def __init__(self):
        
        self.file_num = len(os.listdir("results_logs\\"))                               #Find the amount of files within the folder
        self.file_name = str("results_logs\\log_entry_{}.csv".format(self.file_num))    #Find the file name within the folder
        self.birds = {}                                                                 #create the dictionaries
        self.eaten = {}
        self.predators = {}
        
        
    def add_bird_log(self, list_bird_x, list_bird_y, num):      
        key_num_x = "bird{}_x".format(num)                  #find the name for the key
        key_num_y = "bird{}_y".format(num)
        self.birds[key_num_x] = list_bird_x                 #add the data to the dictionary
        self.birds[key_num_y] = list_bird_y
        
    def add_eaten_log(self, list_bird_x, list_bird_y, num):
        key_num_x = "eaten{}_x".format(num)
        key_num_y = "eaten{}_y".format(num)
        
        self.eaten[key_num_x] = list_bird_x
        self.eaten[key_num_y] = list_bird_y
        
    def add_pred_log(self, list_bird_x, list_bird_y, num):
        key_num_x = "pred{}_x".format(num)
        key_num_y = "pred{}_y".format(num)
        
        self.predators[key_num_x] = list_bird_x
        self.predators[key_num_y] = list_bird_y
        
    
    def add_to_csv(self):
        
        maxium = 0                          
        
        for k, d in self.birds.items():     #loop through the dictionary
            lenght = len(d)                 #Set the lenght to the lenght of the list
            if maxium < lenght:             #If the maxium is less then the lenght
                maxium = lenght             #set the maxium to the lenght 
        
        for k, d in self.eaten.items():     #loop through keys and data in the eaten
            len_eaten = len(d)              #Find the lenght of the eaten
            if len_eaten < maxium:          #If the eaten is less then the maxium
                amount = maxium - len_eaten #find the difference in the lengths
                for a in range(amount):     #add 0 to the end to make the lists the same size
                    d.append(0)
                
            self.birds[k] = d               #add the new dictionary key with data
            
        for k, d in self.predators.items(): #Same as loop above with the predators instead
            len_eaten = len(d)
            if len_eaten < maxium:
                amount = maxium - len_eaten
                for a in range(amount):
                    d.append(0)
                
            self.birds[k] = d               #add another bit of data to the dictionary
            
        
        self.df_birds = pd.DataFrame(self.birds)            #convert the data to pandas dataframe
        self.df_birds.to_csv(self.file_name, index=False)   #Put pandas dataframe into .csv file
        
