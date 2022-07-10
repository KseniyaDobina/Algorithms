n = int(input())

color_dict = {}

for _ in range(n):
    a = list(map(int, input().split()))
    if a[0] in color_dict.keys():
        new_val = color_dict.get(a[0])
        color_dict[a[0]] = new_val + a[1]
    else:
        color_dict[a[0]] = a[1]

new = sorted(color_dict.keys())

for i in new:
    print(i, color_dict[i])
