#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())
array = [0] * 1000
for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for j in x:
    if array[j] == 1:
        print("yes")
    else:
        print("no")


        






