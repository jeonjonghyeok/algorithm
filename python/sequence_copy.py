#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import time
start = time.time()

n = int(input())
s = list(map(int, input().split()))
op = list(map(int, input().split()))

arr = []
per = []
m=0
for i in range(4):
    for j in range(op[i]):
        m=m+1
        arr.append(i)
per = list(itertools.permutations(arr,m))

    
result = 0
results=[]

for operate in per:
    result = s[0]
    for i in range(m):
        if operate[i]==0:
            result += s[i+1]
        elif operate[i] ==1:
            result -= s[i+1]
        elif operate[i] == 2:
            result *= s[i+1]
        elif operate[i] ==3:
            result = int(result / s[i+1])
            result
    results.append(result)

print(max(results))
print(min(results))

print("time: ", time.time()-start)
