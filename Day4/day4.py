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
            
            height = ''
            unit = ''
            for c in v:
                if c.isnumeric():
                    height += c
                if c.isalpha():
                    unit += c

            if 'cm' == unit:
                
                if not (150 <= int(height) <= 193):
                    break
                
            if 'in' == unit:
                
                if not (59 <= int(height) <= 76):
                    
                    break
                
                
                
                
        if k == 'hcl':
            
            if len(v[1:]) != 6:
                break
            if v[0] != '#':
                break
            

            for c in v[1:]:
                if not (c.isnumeric() or c in 'abcdef'):
                    break
            
            
            
            
        if k == 'ecl':
            if v not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                break
            
        if k == 'pid':
            if len(v) != 9:
                # möjligt fel
                break
            if not v.isnumeric():
                print(v)
                break

            
        correct += 1
    
    if correct == 7 or correct == 8:
        nbr_valid += 1