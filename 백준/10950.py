import sys

A = B = range(1, 10)

result = list()

T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split(' '))
    result.append(A+B)

for i in range(len(result)):
    print(result[i])