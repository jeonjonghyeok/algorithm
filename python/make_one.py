#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())

cnt = 0
while n != 1:
    cnt+=1
    if n%5 == 0:
        n=n//5
    elif n%3 == 0:
        n=n//3
    else:
        n=n-1

print(cnt)
