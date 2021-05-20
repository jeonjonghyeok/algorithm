#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
def perm(arr, depth, n):
    if (depth == n):
        per.append(list(arr))
        return
    for idx in range(depth, n):
        arr[idx], arr[depth] = arr[depth], arr[idx]
        perm(arr, depth+1,n)
        arr[idx], arr[depth] = arr[depth], arr[idx]
    
perm(arr, 0, m)
result = 0
max_result=-999999999
min_result=99999999

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
    max_result = max(max_result,result)
    min_result = min(min_result,result)

print(max_result)
print(min_result)

print("time: ", time.time() - start)