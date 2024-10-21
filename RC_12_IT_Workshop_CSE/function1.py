x = int(input("Enter a number:"))
def fact(x):
    pro = 1
    for i in range(1, x+1):
        pro*=i
    return pro
def factrec(x):
    if x==1:
        return 1
    else:
        return x*factrec(x-1)
product = fact(x)
product2 = factrec(x)
print("Factorial is:", product)
print("Reccursive Factorial is:", product2)
