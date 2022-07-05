r = int(input())
i = int(input())
c = int(input())
if i == 2 or i == 3 or i == 5:
    print(i)
else:
    if i == 1:
        print(c)
    elif i == 6:
        print(0)
    elif i == 7:
        print(1)
    elif i == 0:
        if r == 0:
            print(c)
        else:
            print(3)
    else:
        if r == 0:
            print(4)
        else:
            print(3)
