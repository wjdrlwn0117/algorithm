Max = 0
index_Max = 0
num = range(1, 100)
input_num = list()

for i in range(9):
    num = int(input())
    input_num.append(num)

for i in range(9):
    if input_num[i] > Max:
        Max = input_num[i]
        index_Max = i+1


print(Max)
print(index_Max)

"""번외 다른 코딩 참고"""
"""
b=[]                        빈리스트 b 생성
for i in range(0,9):        입력과 동시에 리스트b에 추가하는 for문
    a=int(input())
    b.append(a)
print(max(b))               파이썬 리스트 자료형의 최댓값추출함수 max (새로알게됨)
print(b.index(max(b))+1)    b의 최대값의 인덱스에 1을 더한 수 출력 (인덱스가 0부터 시작하기 때문)
"""

"""
lst = []
for i in range(1, 10):
    number = int(input())
    lst.append((number, i))
lst.sort(reverse=True)
print(*lst[0], sep="\n")
"""
# https://www.daleseo.com/python-lists-print/ 참고