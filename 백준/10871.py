import sys
import math

X = range(10000)
N = math.inf
numbers = range(1, 10001)
result = list()

N, X = map(int, sys.stdin.readline().split(" "))

numbers = list(map(int, input().split()))

for i in range(0, N):
    if numbers[i] < X:
        result.append(numbers[i])

for i in range(len(result)):
    print(result[i], end=' ')

"""
https://bamdal.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%ACpython-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EA%B3%B5%EB%B0%B1%EC%9C%BC%EB%A1%9C-%EA%B5%AC%EB%B6%84%ED%95%98%EC%97%AC-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0
파이썬 리스트 공백으로 구분하여 출력하기
"""
