#https://codeforces.com/problemset/problem/339/A

x = input().strip().split("+")
for i in x:
    i = int(i)
x = sorted(x)
output = str(x[0])
for i in range(1,len(x)):
    output = output +"+"+ str(x[i])
    
    
print(output)
