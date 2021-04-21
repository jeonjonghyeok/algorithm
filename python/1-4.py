#!/usr/bin/env python
# -*- coding: utf-8 -*-

n,k = map(int, input().split())
count=0
while(n>1):
    if n >= k:
        count += n % k
    n = n // k
    count += 1
print(count)


