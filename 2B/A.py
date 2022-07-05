a = 0
b = 0
while True:
    n = int(input())
    if n > b:
        a = 1
        b = n
    elif n == b:
        a += 1
    elif n == 0:
        break
print(a)
