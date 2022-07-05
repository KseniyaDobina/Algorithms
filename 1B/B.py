c = list(map(int, input().split()))

if c[2] > c[1]:
    a = c[2] - c[1] - 1
    b = c[0] - c[2] + c[1] - 1
else:
    a = c[1] - c[2] - 1
    b = c[0] - c[1] + c[2] - 1

if a < b:
    print(a)
elif a == -1 or b == -1:
    print(0)
else:
    print(b)
