#!/usr/bin/env python
# -*- coding: utf-8 -*-

n,m,k = map(int, input().split())

array = list(map(int, input().split()))

array.sort()
max_item = array[len(array)-1]
second_item = array[len(array)-2]

m_count = m//(k+1) *k
m_count += m%(k+1)
s_count = m%k

result = m_count*max_item + s_count*second_item
print(result)


