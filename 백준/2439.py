num = range(1, 101)
num = int(input())

for i in range(1, num+1):
    if(num != i):
        print(" " * (num-i-1), "*" * i)
    else:
        print("*"*i)

# 2중 포문을 써서 공백을 채우려고 했지만 num과 i가 같아 지는 시점에서 공백의 수가 -1이 되는 경우가 생겨 if문을 사용

# for i in range(1, num+1):
#     print(" " * (num-i) + "*" * i)

# 참고 : https://twinstarinfo.blogspot.com/2018/10/backjoon-2439-python.html