#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())
array = list(map(int, input().split()))

array.sort()
d = [0]*n

d[0] = array[0]
result = d[0]
for i in range(1,n):
    d[i] = d[i-1] + array[i]
    result += d[i]

print(result)

