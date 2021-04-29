#!/usr/bin/env python
# -*- coding: utf-8 -*-

def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start+end)//2
    print("start=",start,"end=",end,"mid=",mid)

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

array = [1,3,5,6,9,11]

print(binary_search(array, 3, 0, 5))

