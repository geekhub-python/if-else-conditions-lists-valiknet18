#!/usr/bin/env python3

n = int(input())
m = int(input())
k = int(input())

calc = n*m - k

if ((calc % n) == 0 or (calc % m) == 0) and calc > 0:
    print("Yes")
else:
    print("No")
