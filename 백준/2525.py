m, s = map(int, input().split())
time = int(input())

s = s + time

a = s % 60
b = s // 60

if s >= 60:
    s = a
    m += int(b)
    if m >= 24:
        m -= 24

print(m, s)