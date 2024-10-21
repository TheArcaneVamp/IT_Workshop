import math
def f1(x,y):
    if y<=x:
        return f1(x-y,y)+1
    else:
        return 0
def f2(n,r):
    if n>1:
        return f2(n-1,r)+f2(n-1,r-1)
    else:
        return 1
def f3(n):
    if n>1:
        return f3(n/2)+1
    else:
        return 0
def f4(m,n):
    if(m==0 or m>=n>=1):
        return 1
    else:
        return f4(m-1,n) + f4(m-1,n-1)
def f5(m,x):
    if m>x:
        return math.factorial(m)/(math.factorial(x)*math.factorial(m-x))
    else:
        return f5(m,x-1)*int((m-x+1)/x)

    
