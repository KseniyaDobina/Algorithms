a = list(map(int, input().split()))

b = {val: 'NO' for val in a}
for i in a:
    if i in b.keys():
        print(b[i])
        b[i] = 'YES'
