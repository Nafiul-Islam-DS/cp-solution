# https://codeforces.com/contest/2104/problem/A

n = int(input())

for i in range(n):
    x = input()
    lis = x.split(" ")
    total = int(lis[0]) + int(lis[1]) + int(lis[2])
    if total % 3==0:
        if total//3>= int(lis[1]):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    