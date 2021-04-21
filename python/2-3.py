#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_data = input()

steps = [(-1,-2),(1,-2),(-1,2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1)]
count=0

for step in steps:
    x = int(ord(input_data[0]))-96
    y = int(input_data[1])
    
    x += step[0]
    y += step[1]

    if x>=1 and x<=8 and y >=1 and y<=8:
        count += 1
print(count)

