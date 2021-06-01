#!/usr/bin/env python
# -*- coding: utf-8 -*-

arr= [1,2,1,1,0]

cnt=1
temp = 0
for i in range(1,len(arr)):
    if arr[i-1] != arr[i]:
        print(i-temp,end=' ')
        print(arr[i-1],end=' ')
        temp = i
