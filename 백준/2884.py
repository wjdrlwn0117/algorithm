import sys

H = range(0, 24)
M = range(0, 60)

H, M = map(int, sys.stdin.readline().split(" "))

M = M - 45          # 문제에서 제기한 45분을 앞서는 시간에 집중한 것
if M < 0:
    H = H - 1
    M = 60 + M
if H < 0:
    H = 23

print(H, M)

""" if M > 45:      # 45분을 앞서는 시간에 집중한 것이 아닌 출력결과에만 집중한 것
    M = M - 45
else:
    M = M + 15
    H = H - 1
    if H == -1:
        H = 23

print(H, M) """