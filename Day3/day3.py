#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:13:09 2020

@author: daniel
"""

# %% Part 1

maps = []


with open('input.txt', 'r') as f:
    for l in f.readlines():
        maps.append(l)

# %%
row_len = len(maps[0]) - 1
right_step = 3
down_step = 1

# %%

pos_x = 0
pos_y = 0
nbr_trees = 1 if maps[pos_y][pos_x] == '#' else 0
for i in range(len(maps)-1):
    pos_x += right_step
    pos_y += down_step
    
    if pos_x >= row_len:
        pos_x -= row_len
    if maps[pos_y][pos_x] == '#':
        nbr_trees += 1

print(nbr_trees)


# %% Part 2

step_x = [1, 3, 5, 7, 1]
step_y = [1, 1, 1, 1, 2]

trees = 1
for j in range(len(step_x)):
    right_step = step_x[j]
    down_step = step_y[j]
    nbr_trees = 0
    pos_x = 0
    pos_y = 0
    
    for i in range(len(maps)-1):
        pos_x += right_step
        pos_y += down_step
        
        if pos_x >= row_len:
            pos_x -= row_len
            
        if pos_y > len(maps) -1:
            break
            
        if maps[pos_y][pos_x] == '#':
            nbr_trees += 1
    trees *= nbr_trees

print(trees)
            
        
        
    