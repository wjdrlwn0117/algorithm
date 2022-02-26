import sys

a, b = map(int, sys.stdin.readline().split())
a = int(str(a)[::-1])
b = int(str(b)[::-1])

if a > b:
    print(a)
else:
    print(b)

"""
if문을 이렇게 대체가 가능함
print(max(a,b))
"""