with open('input.txt', 'r') as file:

    party_list = []
    summa = 0
    
    for i in file:
        a = i.split()
        b = [val for val in a[:-1]]
        party_list.append([' '.join(b), int(a[len(a) - 1])])
        summa += int(a[len(a) - 1])

check_sum = 450
k = summa / 450

for id_c, i in enumerate(party_list):
    win_card = int(i[1] // k)
    check_sum -= win_card
    party_list[id_c].append(win_card)
    party_list[id_c].append(i[1] % k)
new_list = party_list.copy()
new_list = sorted(new_list, key=lambda x: x[3], reverse=True)

for id_c, i in enumerate(new_list):
    if check_sum == 0:
        break
    else:
        new_list[id_c][2] = i[2] + 1
        check_sum -= 1

for i in party_list:
    print(i[0], i[2])
