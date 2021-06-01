#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())
array = []

for i in range(n):
    name, s = input().split(" ")
    name.lower()
    s = s.lower()
    name= name[0].upper()+name[1:]
    s = s[0].upper()+s[1:]
    array.append((name,s))

for i in range(n):
    print("Case #%d"% i)
    print(array[i][0],array[i][1])
