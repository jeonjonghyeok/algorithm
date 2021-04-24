#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            print(i, end=' ')
            dfs(graph,i,visited)


visited = [False]*9
graph = [
    [],
    [2, 3 ,8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
dfs(graph,1,visited)
