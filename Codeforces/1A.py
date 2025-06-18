#https://codeforces.com/problemset/problem/1/A


import math
x = input()
l = x.strip().split()
h = int(l[0])/int(l[2])
h= math.ceil(h)
w = int(l[1])/int(l[2])

w= math.ceil(w)

print(h*w)
