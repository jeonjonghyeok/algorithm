#!/usr/bin/env python
# -*- coding: utf-8 -*-

n=1020

money = [500,100,50,10]
count =0

for i in money:
    count += n//i
    n %= i

print(count)
