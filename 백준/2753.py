import sys

year = int(input())
if (1 > year) | (4000 < year): sys.exit("연도의 범위는 1 <= year <= 4000입니다")
# print("연도의 범위는 1 <= year <= 4000입니다"), quit()
# 파이썬 프로그램 종료 방식에는 4가지가 있음
# quit(), exit(), sys.exit(), os.exit()
# 참고 : https://www.delftstack.com/ko/howto/python/python-exit-program/

if (year % 4 == 0) & ((year % 100 != 0) | (year % 400 == 0)): print(1)
else: print(0)
