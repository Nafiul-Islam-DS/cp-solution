#https://codeforces.com/problemset/problem/282/A


n = int(input())

lis = []
for i in range(n):
    x = input()
    lis.append(x)

def returncount(arr):
    count = 0
    for i in arr:
        if "++" in i:
            count+=1
        else:
            count-=1
    return count
            
            
count = returncount(lis)
print(count)
