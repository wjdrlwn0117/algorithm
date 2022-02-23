A = B = range(1, 10)

while 1:
    try:
        A, B = map(int, input().split())
        if (A + B) == 0:
            break
        print(A + B)
    except:
        break