#https://codeforces.com/problemset/problem/231/A

n = int(input())
lis = []
for i in range(n):
    x = input()
    lis.append(x)
    
def count(arr):
    c = 0
    for i in arr:
        if i.count("1")>1:
            c+=1
        else:
            pass
    return c

x = count(lis)
print(x)
