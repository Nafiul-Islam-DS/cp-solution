#https://codeforces.com/problemset/problem/71/A

n = int(input())

for i in range(n):
    x = input()
    if len(x)<11:
        print(x)
    else:
        print(x[0]+str(len(x)-2)+x[-1])
