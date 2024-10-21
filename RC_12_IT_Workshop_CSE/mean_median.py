n = int(input("Enter number of terms:"))
x = []
x.sort()
for i in range(n):
    x.append(int(input("Enter a number:")))

def average(x):
    k = 0
    for i in x:
        k = k + i
    avg = k/n
    return avg

def median(x):
    if(n%2==0):
        return x[int(((n-1)/2)+1)]
    else:
        return x[int(((n-1)+1)/2)]
mean = average(x)
median = median(x)

print("The average is:", mean)
print("The median is:", median)

    
