with open('input.txt', 'r') as file:
    words_dict = {}
    for i in file:
        for j in i.split():
            if j in words_dict.keys():
                new_val = words_dict.get(j)
                words_dict[j] = new_val + 1
            else:
                words_dict[j] = 1

list_word = [(words_dict[i], i) for i in words_dict.keys()]

list_word = sorted(list_word)

for i in sorted(list_word, key=lambda x: x[0], reverse=True):
    print(i[1])
 
