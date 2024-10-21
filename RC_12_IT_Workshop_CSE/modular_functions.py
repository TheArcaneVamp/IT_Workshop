import mod

x = int(input("x="))
y = int(input("y="))
while True:
    ch = int(input("Enter function number:"))
    if(ch == 1):
        print(mod.f1(x,y))
    if(ch == 2):
        print(mod.f2(x,y))
    if(ch == 3):
        print(mod.f3(x))
    if(ch == 4):
        print(mod.f4(x,y))
    if(ch == 5):
        print(mod.f5(x,y))
    else:
        print("Bye!")
        exit()
        
