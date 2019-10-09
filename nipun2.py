"""
Author    : co_devil Chirag Garg
Institute : JIIT
"""
from math import *
from sys import stdin, stdout
import itertools, os, sys, threading
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import *
#from math import ceil, floor, log, sqrt, factorial, pow, pi, gcd
# from bisect import bisect_left,bisect_right
# from decimal import *,threading
from fractions import Fraction
def ii(): return int(input())
def si(): return str(input())
def mi(): return map(int, input().split())
def li(): return list(mi())
def fii(): return int(stdin.readline())
def fsi(): return str(stdin.readline())
def fmi(): return map(int, stdin.readline().split())
def fli(): return list(fmi())
abd = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
       'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
       'z': 25}
def getKey(item): return item[0]
def sort2(l): return sorted(l, key=getKey)
def d2(n, m, num): return [[num for x in range(m)] for y in range(n)]
def isPowerOfTwo(x): return (x and (not (x & (x - 1))))
def decimalToBinary(n): return bin(n).replace("0b", "")
def ntl(n): return [int(i) for i in str(n)]
def powerMod(x, y, p):
    res = 1
    x %= p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res
graph = defaultdict(list)
visited = [0] * 1000000
col = [-1] * 1000000
def bfs(d, v):
    q = []
    q.append(v)
    visited[v] = 1
    while len(q) != 0:
        x = q[0]
        q.pop(0)
        for i in d[x]:
            if visited[i] != 1:
                visited[i] = 1
                q.append(i)
        print(x)
