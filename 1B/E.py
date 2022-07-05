d = int(input())

x, y = map(int, input().split())

a = x ** 2 + y ** 2
b = (d - x) ** 2 + y ** 2
c = x ** 2 + (d - y) ** 2

if x < d and y < d:
    if x >= 0 and y >= 0:
        if d - y >= x:
            print(0)
        else:
            if min(a, b, c) == a:
                print(1)
            elif min(a, b, c) == b:
                print(2)
            else:
                print(3)
    elif x < 0 or y < 0:
        if min(a, b, c) == a:
            print(1)
        elif min(a, b, c) == b:
            print(2)
        else:
            print(3)
elif x == d or y == d:
    if x == d:
        if y == 0:
            print(0)
        elif y < 0:
            print(2)
        elif y == d:
            print(2)
    elif y == d:
        if x == 0:
            print(0)
        elif x < 0:
            print(3)
        elif y == d:
            print(2)
else:
    if min(a, b, c) == a:
        print(1)
    elif min(a, b, c) == b:
        print(2)
    else:
        print(3)
