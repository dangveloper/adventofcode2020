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
        seats.append(l.replace('\n', ''))
# %% Part 1
def get_pos(seat_code, seat_pos):

    
    if (len(seat_pos)) == 1:
        return seat_pos[0]
    
    if seat_code[0] in ['F', 'L']:
        seat_pos_remaining = seat_pos[:len(seat_pos)//2]
        return get_pos(seat_code[1:], seat_pos_remaining)
        
    if seat_code[0] in ['B', 'R']:
        seat_pos_remaining = seat_pos[len(seat_pos)//2:]
        return get_pos(seat_code[1:], seat_pos_remaining)


max_value = 0
for seat in seats:
    
    row = get_pos(seat[0:-3], list(range(128)))
    column = get_pos(seat[-3:], list(range(8)))
    
    value = row * 8 + column
    
    if value > max_value:
        max_value = value


# %% Part 2
        
seat_ids = []
    
for seat in seats:

    row = get_pos(seat[0:-3], list(range(128)))
    column = get_pos(seat[-3:], list(range(8)))
    
    value = row * 8 + column
    
    seat_ids.append(value)
    
sorted_seats = sorted(seat_ids)

new = 0
old = 0

for i in sorted_seats:
    if not (i+1 in sorted_seats and i-1 in sorted_seats):
        new = i
        
        if new - old == 2:
            my_seat = old +1
            print(my_seat)
        old = new
        