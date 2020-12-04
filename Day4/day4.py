#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:16:35 2020

@author: danielgellerman
"""

# %% PART 1

passports = []
passport = {}

with open('input.txt', 'r') as f:
    for l in f.readlines():
        
        if l == '\n':
            passports.append(passport)
            passport = {}

            continue

        l_split = l.split()
        
        for field in l_split:
            k, v = field.split(':')
            passport[k] = v
passports.append(passport)

nbr_valid_passports = 0
valid_passports = []
for p in passports:
    
    if len(p.keys()) == 8:
        nbr_valid_passports += 1
        valid_passports.append(p)
        
    if len(p.keys()) == 7:
        if 'cid' not in p.keys():
            valid_passports.append(p)
            nbr_valid_passports += 1
        
# %% Part 2

nbr_valid = 0
for p in valid_passports:
    correct = 0
    for k, v in p.items():
        
        if k == 'byr':
            if len(v) != 4 or not (1920 <= int(v) <= 2002):
                break
        if k == 'iyr':
            if len(v) != 4 or not (2010 <= int(v) <= 2020):
                break
        if k == 'eyr':
            if len(v) != 4 or not (2020 <= int(v) <= 2030):
                break
            
            
        if k == 'hgt':
            if 'c' in v:
                try:
                    if not (150 <= int(v[0:3]) <= 193):
                        break
                except:
                    break
                
            if 'i' in v:
                if not (59 <= int(v[0:2]) <= 76):
                    break
                
                
                
                
        if k == 'hcl':
            
            if v[0] != '#':
                break
            if len(v[1:]) != 6: # möjligt fel
                break
            v_split = v.split()
            for c in v_split:
                print(c)
                if not (c.isalpha() or c.isnumber()):
                    break
                    
            
            
            
        if k == 'ecl':
            if v not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                break
            
        if k == 'pid':
            try:
                if len(v) != 9 or int(v) < -100: # möjligt fel
                    break
            except:
                break
            
        correct += 1
        
    if correct == 7 or correct == 8:
        nbr_valid += 1