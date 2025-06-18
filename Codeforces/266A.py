#https://codeforces.com/problemset/problem/266/A

n = int(input())

x = input()
count = 0
for i in range(1,n):
    x = x[:n]
    if x[i]==x[i-1]:
        count+=1
        
print(count)
