#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:24:28 2020

@author: daniel
"""
# %%
import numpy as np
 
# %% Load data

data = np.loadtxt('input.txt')

#%% Part 1

for i in data:
    for j in data:
        if j + i == 2020:
            print(i*j)
            
            
# %% Part 2


for i in data:
    for j in data:
        for k in data:
            if j + i + k== 2020:
                print(i*j*k)
                