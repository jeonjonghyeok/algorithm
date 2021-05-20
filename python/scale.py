#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

n = 3
arr = []
for i in range(1,n+1):
    arr.append(2**i)

result = list(itertools.permutations(arr,3))
print(result)
print(len(result))

for i in result:
    print(list(itertools.combinations(i,2)))



