import sys
import math

numbers = [], range(1, 30001)
while True:
    numbers = map(int, sys.stdin.readline().split())
    numbers2 = sorted(numbers)
    if numbers2[0] == 0 and numbers2[1] == 0 and numbers2[2] == 0:
        break
    if math.pow(numbers2[0], 2) + math.pow(numbers2[1], 2) == math.pow(numbers2[2], 2):
        print("right")
    else:
        print("wrong")