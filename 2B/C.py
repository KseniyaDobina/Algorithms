a = input()
b = len(a)
summa = 0
count = 0

if b % 2 == 0:
    while count <= (b // 2) - 1:
        if a[count] != a[b - 1 - count]:
            summa += 1
        count += 1
else:
    while count <= b // 2:
        if a[count] != a[b - 1 - count]:
            summa += 1
        count += 1
print(summa)
