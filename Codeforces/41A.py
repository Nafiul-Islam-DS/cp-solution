#https://codeforces.com/problemset/problem/41/A

x = input().lower()
y = input().lower()

if x== y[::-1]:
    print("YES")
else:
    print("NO")
