a = int(input())
b = int(input())

b_one = b % 10
b_ten = (b % 100 - b_one)
b_back = (b - (b_one + b_ten))

print(a * b_one)
print(int(a * (b_ten) / 10))
print(int(a * (b_back / 100)))
print(a * b)


"""
a = input()
b = input()
int_a = int(a)
int_b = int(b)

print(int(b[2]) * int_a)
print(int(b[1]) * int_a)
print(int(b[0]) * int_a)
print(int_a * int_b)

굳이 b의 값을 정수로 만들어서 자릿수를 하는 것이 아닌 문자열로 입력받아서 print함수에서 문자열의 인덱스값을
int()해서 하는 방법
"""