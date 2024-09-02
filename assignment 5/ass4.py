st = input("Enter a string:").upper()
list1 = st.split(" ")
list2=[]
for i in range(0,len(list1)):
    list2.append(list1[i][0])
print("".join(list2))
