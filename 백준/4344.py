import sys

case = int(input())
avg = []

for i in range(case):
    over_avr_stu = 0
    score = list(map(int, sys.stdin.readline().split()))
    for j in range(score[0]):
        if sum(score[1:]) / (len(score) - 1) < score[j+1]:
            over_avr_stu += 1
    answer = round((over_avr_stu / score[0]), 5) * 100
    print("{:.3f}%".format(answer))


"""
score = list(map(int, sys.stdin.readline().split()))
== map함수를 이용한 숫자 입력을 리스트구조에 바로 넣는 코드

소수점표현 관련 문서
https://blockdmask.tistory.com/534

문자열 서식 지정자와 포매팅 사용
https://dojang.io/mod/page/view.php?id=2300
"""





