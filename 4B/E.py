n = int(input())

list_number = [0]*n
list_t = ['']*n
dict_t = {-1: -1}

for i in range(n):
    number = int(input())
    if number == 0:
        t = input()
        input()
        list_number[i] = i
        list_t[i] = t
    else:
        input()
        list_number[i] = list_number[number - 1]

dict_str = {}
max_values = 0

for i in list_number:
    if i not in dict_str.keys():
        dict_str[i] = 0
    else:
        new_val = dict_str.get(i) + 1
        dict_str[i] = new_val
        if max_values < new_val:
            max_values = new_val

for i in dict_str.keys():
    if dict_str[i] == max_values:
        print(list_t[i])
        break
