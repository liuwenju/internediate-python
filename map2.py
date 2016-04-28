#!/usr/bin/env python
# encoding: utf-8

def multiply(x):
    return (x * x)

def add(x):
    return (x + x)


funcs = [multiply, add]
for i in range(5):
    value = map(lambda x: x(i),funcs)
    print list(value)
