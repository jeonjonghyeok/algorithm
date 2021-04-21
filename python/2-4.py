#!/usr/bin/env python
# -*- coding: utf-8 -*-
n,m = map(int, input().split()) 
x,y,direction = map(int, input().split())
o_map = []
g_map = [[0]*n for _ in range(m)] 

dx =[0,1,0,-1]
dy =[-1,0,1,0]

for _ in range(n):
    o_map.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        g_map[i][j] = o_map[i][j]
        
g_map[y][x] = 1
turn_cnt,cnt=0,0

while(True):
    if direction==0:
        direction=3
    else:
        direction+=-1
    turn_cnt+=1

    nx = x+dx[direction]
    ny = y+dy[direction]
    rnx = x-dx[direction]
    rny = y-dy[direction]

    if turn_cnt==4:
        if o_map[rny][rnx]==0 and rnx>=0 and rnx<=n and rny>=0 and rny<=n:
            x,y = rnx,rny
            turn_cnt=0
            cnt+=1
            continue
        else:
            break

    if g_map[ny][nx]==0 and nx>=0 and nx<=n and ny>=0 and ny<=n:
        x,y = nx,ny
        g_map[ny][nx] = 1
        cnt+=1
        turn_cnt=0

print(cnt)



