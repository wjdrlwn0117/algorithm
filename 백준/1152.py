# sentence = input()
# a = list(map(str, sentence))
# if (a[0] == ' ') or (a[-1] == ' '):
#     word = 0
# elif (a[0] == ' ') and (a[-1] == ' '):
#     word = 0
# else:
#     word = 1
#
# for i in range(len(a)):
#     if (a[i] == ' '):
#         word += 1
#
# print(word)

word = input().split()
print(len(word))

"""split을 사용할 때 split(" ")과 split()이 다르다
https://somjang.tistory.com/entry/Python-%EB%AC%B8%EC%9E%90%EC%97%B4-split-%EA%B3%BC-split-%EC%B0%A8%EC%9D%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0"""