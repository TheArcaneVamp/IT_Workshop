st = input("Enter a string:")
if (" " in st):
    raise Exception("No spaces allowed!")
list = [*st]
print(list)