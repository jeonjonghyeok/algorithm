#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())
array=[]

for i in range(n):
    array.append(int(input()))
array = sorted(array, reverse=True)
print(array)

