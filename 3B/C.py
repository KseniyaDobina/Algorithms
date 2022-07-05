a = list(map(int, input().split()))

b = []
c = []

for id_count, i in enumerate(a):
    if i not in b and i not in c:
        b.append(i)
    else:
        if i in b:
            b.pop(b.index(i))
            c.append(i)
for i in b:
    print(i, end=" ")
