#!/usr/bin/env python
# -*- coding: utf-8 -*-

def numeric(n):
    q,r = divmod(n-1,3)
    if n<=3:
        return '123'[r]
    return numeric(q)+'123'[r]
print(numeric(100))
