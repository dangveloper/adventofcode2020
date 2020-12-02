#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:05:08 2020

@author: daniel
"""

# %% Part 1

nbr_pw_part1 = 0
with open('input.txt', 'r') as file:
    
    for line in file.readlines():
        parts = line.split()
        min, max = parts[0].split('-')
        letter = parts[1].replace(':', '')
        password = parts[2]
        
        occurences = password.count(letter)
        
        if int(min) <= occurences <= int(max):
            nbr_pw_part1 += 1
            
# %% Part 2
nbr_pw_part2 = 0
with open('input.txt', 'r') as file:
    
    for line in file.readlines():
        parts = line.split()
        pos1, pos2 = parts[0].split('-')
        letter = parts[1].replace(':', '')
        password = parts[2]
        
        
        try:
            if password[int(pos1)-1] == letter and password[int(pos2)-1] != letter:
                nbr_pw_part2 += 1
            if password[int(pos1)-1] != letter and password[int(pos2)-1] == letter:
                nbr_pw_part2+= 1
        except: 
            continue
                