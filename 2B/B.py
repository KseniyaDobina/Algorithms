a = list(map(int, input().split()))

home = [id_count for id_count, val in enumerate(a) if val == 1]
shop = [id_count for id_count, val in enumerate(a) if val == 2]

min_list = []

for i in home:
    min_number = float('inf')
    for j in shop:
        mod = abs(j - i)
        if mod < min_number:
            min_number = mod
    min_list.append(min_number)

print(max(min_list))
