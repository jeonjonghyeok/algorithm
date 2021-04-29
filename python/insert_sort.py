#!/usr/bin/env python
# -*- coding: utf-8 -*-

items = [5,4,6,7,2,1,8,9,3]

for i in range(1,len(items)):
    for j in range(i,0,-1):
        if items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]

print(items)



