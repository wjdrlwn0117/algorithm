"""
변수 : 케이스 수, 테스트, 점수, 총 점수
"""
OX = range(1, 80)

case = int(input())
for _ in range(case):
    score = 0
    sum = 0
    total = 0
    OX = list(input())

    for i in range(len(OX)):
        if OX[i] == "O":
            score += 1
            OX[i] = score
            # print(OX)
        else:
            sum += score
            score = 0
            # print(OX)
        if i == len(OX) - 1:
            if OX[i] == "O":
                sum += score
                # print(OX)
    for j in range(len(OX)):
        if str(type(OX[j])) == "<class 'int'>":
            total += int(OX[j])
    print(total)

"""
<다른 코딩 참고>
n = int(input())
for _ in range(n):
    ox_list = list(input())
    score = 0
    sum_score = 0
    for ox in ox_list:
        if ox =='O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)
: 여기서 배울 점은 for문을 쓰는데 있어서 너무 정수값에 의존한다는 점, 이 코딩은 for문의 매개체가 리스트와 문자열이다.

다른코딩 중 이해가 안되는 코딩이 있다

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    case = input().rstrip()
    score = [0] * len(case)
    if case[0] == 'O':
        score[0] = 1
    for i in range(1, len(score)):
        if case[i] == 'O':
            score[i] += score[i - 1] + 1
    print(sum(score))



"""