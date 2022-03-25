import sys

x, y, w, h = map(int, sys.stdin.readline().split())
num = min(x, y, (w-x), (h-y))
print(num)