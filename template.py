#!usr/bin/env python3
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
from itertools import permutations, accumulate
from logging.config import valid_ident
from multiprocessing.sharedctypes import Value
import sys
import math
import bisect

input = sys.stdin.readline
istr = lambda: input().strip()
inum = lambda: int(input().strip())
imap = lambda: map(int,input().strip().split())
ilist = lambda: list(map(int, input().strip().split()))
 
# sys.setrecursionlimit(1000000)
mod = 1000000007

def matrix(n, m):
    return [[0] * (m) for _ in range(n)]
 
def go(k):
    return 0

def primes(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    print(primes)

def main():
    a, b, c = imap()
    print(a+b+c)
           
if __name__ == "__main__":
    main()