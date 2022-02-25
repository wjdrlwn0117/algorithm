a = b = c = d = e = f = g = h = i = j = 0
mul = 1
for x in range(3):
    mul *= int(input())

for z in range(len(str(mul))):
    if str(mul)[z] == "0":
        a += 1
    elif str(mul)[z] == "1":
        b += 1
        continue
    elif str(mul)[z] == "2":
        c += 1
        continue
    elif str(mul)[z] == "3":
        d += 1
        continue
    elif str(mul)[z] == "4":
        e += 1
        continue
    elif str(mul)[z] == "5":
        f += 1
        continue
    elif str(mul)[z] == "6":
        g += 1
        continue
    elif str(mul)[z] == "7":
        h += 1
        continue
    elif str(mul)[z] == "8":
        i += 1
        continue
    else:
        j += 1
        continue

print(a, b, c, d, e, f, g, h, i, j, sep='\n')
"""
n = [int(input()) for _ in range(3)]         for _ in range(3)에서 쓰인 _는 _의 많은 역할 중 값을 무시하기 위한 _이며 단순히 입력문을 반복하는 것이므로 _을 사용한 것이다.            
m = str(n[0]*n[1]*n[2])
for i in range(10):
    print(m.count(str(i)))                  ** 문자열 count함수가 사용된 것으로 특정 문자, 혹은 문자열이 포함되어 있는지 계산해서 반환하는 함수
https://blockdmask.tistory.com/410
"""