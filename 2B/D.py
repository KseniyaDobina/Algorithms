N = list(map(int, input().split()))[0]
a = list(map(int, input().split()))
list_number = [val for val in range(N)]

if N % 2 == 0:
    right_number = N // 2
    b = list_number[:right_number]
    for i in b[::-1]:
        if i in a:
            left_number = i
            break
    for i in list_number[-right_number:]:
        if i in a:
            right_number = i
            break
    print(left_number, right_number)

else:
    center_number = N // 2
    if center_number in a:
        print(center_number)
    else:
        left_number = float('inf')
        right_number = float('inf')
        b = list_number[:center_number]
        for i in b[::-1]:
            if i in a:
                left_number = i
                break
        for i in list_number[-center_number:]:
            if i in a:
                right_number = i
                break
        print(left_number, right_number)
