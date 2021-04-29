#!/usr/bin/env python
# -*- coding: utf-8 -*-

items = [5,2,4,3,9,1,6,7,8]


for i in range(len(items)):
    min_idx=i
    for j in range(i+1,len(items)):
        if items[min_idx] > items[j]:
            min_idx = j
    items[min_idx], items[i] = items[i], items[min_idx]

print(items)
        
