import sys

T = int(input())

for i in range(T):
    apt = map(int, sys.stdin.readline().split())
    apt = list(apt)
    H = (apt[2] % apt[0]) * 100
    W = apt[2] / apt[0] + 1
    print((int)(H + W))
    apt = []