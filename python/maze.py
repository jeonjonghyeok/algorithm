#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque

n,m = map(int, input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x,y):
    i=0
    print("start bfs")
    queue = deque()
    queue.append((x,y))
    while queue:
        i+=1
        print("i=",i)
        print("queue=",queue)
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
        for j in range(5):
            print(graph[j])
    return graph[n-1][m-1]
    
print(bfs(0,0))
