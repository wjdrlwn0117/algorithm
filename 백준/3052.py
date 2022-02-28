n = range(0,)
n = [int(input()) for _ in range(10)]

dif_num = 1

for i in range(10):
    n[i] = n[i] % 42

n = sorted(n)

for i in range(9):
    if n[i] != n[i + 1]:
        dif_num += 1

print(dif_num)

"""
서로 다른 수를 담는 변수가 1로 선언되는 이유 : 만약 모든 수가 같다면 그 하나의 수가 있기 때문에 1로 시작
n리스트의 수들이 크기 비교가 뒤죽박죽일 때 구하는 것이 정렬한 후 구하면 쉬워지므로 정렬을 사용

<다른코딩 참고>
list = []
c = 0

for i in range(10):
  a = int(input())
  list.append(a % 42)

for i in range(42):
  if i in list:
    c += 1
print(c)

나머지는 나눈 수보다 무조건 작다는 걸 이용한 예시

a=set()

for i in range(10):
    n=int(input())
    a.add(n%42)

print(len(a))

set함수를 사용한 예시 set함수는 집합의 개념과 비슷하며 기본적으로 중복된 값을 제거하는 기능이 있어 이 문제에 최적화된 함수
중복된 값을 제거한 후 리스트에 원소들을 넣어 길이를 구한 예시
"""