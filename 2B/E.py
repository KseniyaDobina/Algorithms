N = int(input())
a = list(map(int, input().split()))

b = [(i + 1, a[i]) for i in range(N)]
b = sorted(b, key=lambda x: x[1])
c = len(a)
time = 0
count = 0
while c > 1:
    for i in range(b[count][1]):
        time += 1
    count += 1
    c -= 1
print(time)
