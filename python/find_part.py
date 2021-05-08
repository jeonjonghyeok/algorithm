#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())
array_n = map(int, input().split())

m = int(input())
array_m = map(int, input().split())

def binary_search(array, target, start, end):
    if start > end:
        return "no"
    mid = (start+end)//2
    if array[mid] == target:
        return "yes"
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)
for i in array_m:
    print(binary_search(array_n, i, 0, n-1))

    


