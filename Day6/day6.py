#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:19:51 2020

@author: daniel
"""

# %% Part 1
nbr_yes = 0
answers = ''
with open('input.txt', 'r') as f:
    for line in f.readlines():
        
        if line == '\n':
            nbr_yes += len(set(answers))
            answers = ''
        
        answers += line.replace('\n','')
                
    nbr_yes += len(set(answers))
    
    print(f'Part 1: {nbr_yes}')
# %% Part 2

from collections import Counter

nbr_yes = 0
answers = ''
group_size = 0
with open('input.txt', 'r') as f:
    
    for line in f.readlines():
        
        if line == '\n':
            c = Counter(answers)
            
            for k,v in c.items():
                if v == group_size:
                    nbr_yes += 1
            answers = ''
            group_size = 0
            
            continue
        
        answers += line.replace('\n','')
        group_size += 1
                
    c = Counter(answers)
    
    for k,v in c.items():
        if v == group_size:
            nbr_yes += 1
    print(f'Part 2: {nbr_yes}')