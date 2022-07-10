with open('input.txt', 'r') as file:
    name_dict = {}
    for i in file:
        a = i.split()
        if a[0] in name_dict.keys():
            new_val = name_dict.get(a[0])
            name_dict[a[0]] = new_val + int(a[1])
        else:
            name_dict[a[0]] = int(a[1])

new = sorted(name_dict.keys())

for i in new:
    print(i, name_dict[i])
