num = range(1, 1000001)
Selnum = range(-1000000, 1000001)

num = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

print(numbers[0], numbers[num-1])

""" 
https://choichumji.tistory.com/64
 파이썬 공백 구분해 정수 입력 받기 
"""