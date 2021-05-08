#!/usr/bin/env python
# -*- coding: utf-8 -*-

n,m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

answer = 0
while start <= end:
    result = 0
    mid = (start+end)//2
    for x in array:
        if x-mid > 0:
            result += x-mid
    if result == m:
        answer = mid
        break
    elif result < m:
        end = mid-1
    else:
        start = mid+1
        answer = mid

print(answer)
