#https://codeforces.com/problemset/problem/546/A


x = input().strip().split()
    
k = int(x[0])
n = int(x[1])
w = int(x[2])
total = 0

for i in range(1,w+1):
    total+= i*k
if k and w!=1 and total>n:    
    print(total-n)
else:
    print(0)

    
    
