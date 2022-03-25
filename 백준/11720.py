case = range(1,101)
case = int(input())

sum = 0

num = [int(x) for x in input().strip()]

for i in range(len(num)):
    sum += num[i]

print(sum)

"""
<다른코딩 참고>
n = input()
print(sum(map(int, input())))

**숫자의 개수를 지정하고 그 개수만큼 반복문을 쓴다고만 생각함 ==> 그럴 필요 없었음**

https://www.acmicpc.net/board/view/32535
"""