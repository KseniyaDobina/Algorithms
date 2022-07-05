N = int(input())
set_yes = set(i for i in range(1, N + 1))

while True:
    answer = input()
    if answer == 'HELP':
        break
    a = set(map(int, answer.split()))
    answer = input()
    if answer == 'YES':
        set_yes &= a
    else:
        set_yes -= a
list_yes = list(set_yes)
for i in sorted(list_yes):
    print(i, end=' ')
