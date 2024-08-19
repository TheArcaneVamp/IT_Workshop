st = input("Enter a string").upper()
old = []
for i in st:
    count = 0
    if(i in old):
        continue
    else:
        for j in st:
            if j == i:
                count = count + 1
        print("The frequency of {0} is {1}".format(i, count))
        old.append(i)

        
    
