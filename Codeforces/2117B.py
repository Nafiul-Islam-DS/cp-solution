#https://codeforces.com/problemset/problem/2117/B

def shrink(n):
    left = 1
    right = n
    result = []

    flag = True
    while left <= right:
        if flag:
            result.append(left)
            left += 1
        else:
            result.append(right)
            right -= 1
        flag =False

    return result

t = int(input())
for _ in range(t):
    n = int(input())
    res = shrink(n)
    print(' '.join(map(str, res)))
 
