alpabet = list(range(65, 91))
bin = [0] * len(alpabet)
num = 0

word = [str(a) for a in input()]

for i in range(len(word)):
    word[i] = word[i].upper()
    word[i] = ord(word[i])

for j in range(len(word)):
    for k in range(len(alpabet)):
        if word[j] == alpabet[k]:
            bin[k] += 1

fre = sorted(bin, reverse=True)
if fre[0] == fre[1]:
    print("?")
else:
    num = fre[0]
    print(chr(alpabet[bin.index(num)]))


"""
https://hogni.tistory.com/119
upper(), lower(), capitalize() 함수

<다른코딩 참고>

words = input().upper()
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])
"""