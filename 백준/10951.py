A = B = range(1, 10)

while 1:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break

"""
https://pchild.tistory.com/2
"""