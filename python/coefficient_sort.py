#!/usr/bin/env python
# -*- coding: utf-8 -*-

array = [7,5,9,0,3,1,6,2,0]

count = [0]*(max(array)+1)

for i in array:
    count[i] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end='')
    
