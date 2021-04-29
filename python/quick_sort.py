#!/usr/bin/env python
# -*- coding: utf-8 -*-

array = [1,5,8,2,4,9,7,3,6]

def quick_sort(array, start, end):
    if start >= end:
        return
    left = start+1
    right = end
    pivot = start

    while left <= right:
        while left <= end and array[left] < array[pivot]:
            left += 1
    
        while right > start and array[right] > array[pivot]:
            right -= 1

        if left > right:
            array[pivot],array[right] = array[right],array[pivot]
        else:
            array[left],array[right] = array[right],array[left]
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)



