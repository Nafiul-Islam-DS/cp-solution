#https://codeforces.com/problemset/problem/791/A


n  = input().strip().split()
limak = int(n[0])
bob = int(n[1])
year = 0
while True:
    limak*=3
    bob*=2
    year+=1
    if limak>bob:
        break
    
print(year)
    
