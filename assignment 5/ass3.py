st = input("Enter a string:")
if (" " in st):
    raise Exception("No spaces allowed!")
if (len(st)<3 or len(st)>4):
    raise Exception("Must be between 3 or 4 characters!")
list = [*st]
if (len(st)==3):
    for i in st:
        for j in st:
            if j != i:
                for k in st:
                  if k != i and k!=j:
                      print(i,j,k)
if (len(st)==4):
    for i in st:
        for j in st:
            if j != i:
                for k in st:
                    if k != i and k != j:
                        for l in st:
                            if l != k and l !=j and l != k:
                                print(i,j,k,l)
