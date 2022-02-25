import sys

T = range(1, 1001)
R = range(1, 9)
result = []

T = int(sys.stdin.readline())
RS = [sys.stdin.readline().strip() for i in range(T)]

for i in range(T):
    a = int(RS[i][0])
    b = RS[i][2:]
    for j in range(len(b)):
        result.append(RS[i][j+2] * a)
    string = "".join(result)
    print(string)
    result = []

"""
https://velog.io/@ecvheo1/%EC%9E%85%EB%A0%A5-%EB%B0%9B%EB%8A%94-%EB%B0%A9%EB%B2%95-sys.stdin.readline
"""

"""
t = int(input())

for _ in range(t):
    r, s = input().split()
    for i in s:
        print(i * int(r), end='')
    print()

for 문의 반복조건에 문자열이 들어갈 수 있음을 알게 됨
"""
