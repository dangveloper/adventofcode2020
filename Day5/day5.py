#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 21:07:11 2020

@author: danielgellerman
"""


# %%
seats = []
with open('input.txt', 'r') as f:
    for l in f.readlines():
        seats.append(l)

def get_pos(seat_code, seat_pos):
    print(seat_code)
    if seat_code[0] in ['F', 'L']:
        seat_pos_remaining = seat_pos[:len(seat_pos)]
        
    if seat_code[0] in ['B', 'R']:
        seat_pos_remaining = seat_pos[:len(seat_pos)]
    print(seat_pos_remaining)
    
    if len(seat_pos_remaining) != 1:
        seat_pos_remaining = get_pos(seat_code[1:], seat_pos_remaining)
        
    return seat_pos_remaining

print(get_pos(seats[0][0:-3], [range(128)]))
    
    