word = input()
alpabet = list(range(97, 123)) #알팝젯의 아스키코드 숫자 범위

for x in alpabet:
    print(word.find(chr(x)))

"""
리스트의 find함수와 index함수의 공통점 및 차이
https://ooyoung.tistory.com/78
"""