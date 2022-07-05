n = int(input())
num = []

for _ in range(n):
    a = set(i for i in input())
    num.append(a)

n = int(input())
b = {}

for _ in range(n):
    a = input()
    check_num = set(i for i in a)
    number = 0
    for val in num:
        check_set = check_num & val
        if len(val) == len(check_set):
            number += 1
    if number in b.keys():
        new_val = [i for i in b[number]]
        new_val.append(a)
        b[number] = new_val
    else:
        b[number] = [a]
f = max(b.keys())
m = b[f]
for i in m:
    print(i)
