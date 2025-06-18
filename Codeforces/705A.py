#https://codeforces.com/problemset/problem/705/A


n = int(input())

def fun(n):
    output = "I hate that I love it"
    if n==1:
        print("I hate it")
    elif n==2:
        print(output)
    else:
        for i in range(3,n+1):
            if i%2==0:
                output = output.replace("it","that")
                output += " I love it"
            else:
                output = output.replace("it","that")
                output += " I hate it"
        
        print(output)
    
fun(n)
