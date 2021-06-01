#!/usr/bin/env python
# -*- coding: utf-8 -*-

a1 = (1,1)
b1 = (0,0)
a2 = (2,2)
b2 = (1,1)

x1, y1 = 1,1
x2, y2 = 0,0
x3, y3 = 2,2
x4, y4 = 1,1
## case1 오른쪽으로 벗어나 있는 경우
if x2 < x3:
    print(0)

## case2 왼쪽으로 벗어나 있는 경우
if x1 > x4:
    print(0)

    ## case3 위쪽으로 벗어나 있는 경우
if  y2 < y3:
    print(0)

    ## case4 아래쪽으로 벗어나 있는 경우
if  y1 > y4:
    print(0)

left_up_x = max(x1, x3)
left_up_y = max(y1, y3)
right_down_x = min(x2, x4)
right_down_y = min(y2, y4)

width = right_down_x - left_up_x
height =  right_down_y - left_up_y
  
print(width * height)
