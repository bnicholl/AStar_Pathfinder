#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 17:49:44 2017

@author: bennicholl
"""
  #  please cite algorithm if used
  
  #  Algorithm changes the integer values of the grid array being used


import numpy as np


nmap = np.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,0,1,1,1,1,1,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,0,1,1,1,1,1,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,1,1,1,1,1,1,1,0,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

class AStar():
    
    def __init__(self, grid, x, y, goal_x, goal_y)    :
        self.grid = grid
        self.initial_x = x  #  never changes
        self.initial_y = y  #  never changes
        self.x = self.initial_x  #  does change
        self.y = self.initial_y  #  does change
        self.goal_x = goal_x  # never changes
        self.goal_y = goal_y  #  never changes
        self.neighbors = []
        self.neighbor()
   
    def neighbor(self):
        #  if x and y == goal_x and goal_y, algo is complete
        if self.x == self.goal_x and self.y == self.goal_y:
            print('your done')
            return 'your done'
        
        #  sets the x and y coordinates to 1 so they are not revisited
        self.grid[self.x][self.y] = 1 
        
        #  the below if statements give you the coordinates of 
        #  the neighbors that have a value of 0            
        if self.x > 0:  #  if X will be on the grid if it moves UP 1 node
            if self.grid[self.x-1] [self.y] == 0:
                self.neighbors.append([self.x - 1, self.y])  
                
        if self.x < self.grid.shape[0] - 1:  #  if X will be on the grid if it moves DOWN 1 node
            if self.grid[self.x+1][self.y] == 0: 
                self.neighbors.append([self.x+1,self.y]) 
                
        if self.y > 0: #  If Y will be on grid if it moves LEFT 1 node
            if self.grid[self.x][self.y - 1] == 0:
                self.neighbors.append([self.x, self.y - 1]) #  
        
        if self.y < self.grid.shape[1] - 1: #  If Y will be on grid if it moves RIGHT 1 node
            if self.grid[self.x][self.y + 1] == 0:
                self.neighbors.append([self.x, self.y + 1]) 
                
        self.f_value()
       
    #  this method gives you the f_value off all the neighbors    
    def f_value(self):
        h_values = []
        g_values = []  
        
        #  calculate distance from the neighboring X, Y to end X, Y value using Manhattan distance 
        for i in self.neighbors:     
            x_distance = abs(i[0] - self.goal_x)  
            y_distance = abs(i[1] - self.goal_y)  
            h_value = (x_distance + y_distance)
            h_values.append(h_value)
        
        #  calculate distance from the neighboring X, Y to the initial X, Y values   
        for i in self.neighbors:
            x_distance = abs(i[0] - self.initial_x)  
            y_distance = abs(i[1] - self.initial_y)
            g_value = (x_distance + y_distance)
            g_values.append(g_value)
        
        #  add g_value and h_value 
        self.f_values = [h + g for h, g in zip(h_values, g_values)]
        self.path()
              
    #  gets the lowest f_value, then pops that f_value and coresponding neighbor
    #  the neighbor always has the same index as the f_values
    def path(self):
               
        for coordinate, i in enumerate(self.f_values):
            if i <= min(self.f_values):
                value = i
                index = coordinate 
                
        self.x = self.neighbors[index][0]        
        self.y = self.neighbors[index][1]
        
        print('f_values:', self.f_values)
        print('neighbors:', self.neighbors)  
        print('x:', self.x)
        print('y:', self.y)
        
        self.neighbors.pop(index)
        self.f_values.pop(index)
    
        self.neighbor()    

        

            
                         
        
        




        







