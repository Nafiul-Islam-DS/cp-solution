#https://codeforces.com/contest/2117/problem/A

def can_reach_exit(n, x, doors):
    for i in range(n):
        time = 0
        is_open = doors[:] 
        pressed = False
        while time < n:
            if is_open[time] == 0:
                time += 1
            else:
                if not pressed:
                    pressed = True
                    for j in range(time, min(time + x, n)):
                        is_open[j] = 0
                else:
                    return "NO"
        return "YES"
    return "NO"

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    doors = list(map(int, input().split()))
    print(can_reach_exit(n, x, doors))
 
