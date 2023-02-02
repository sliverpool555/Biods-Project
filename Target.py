# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 11:30:12 2022

@author: 253364
"""

import random

class Target():
    
    def __init__(self,x, y, width, height):
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)
        
        
    