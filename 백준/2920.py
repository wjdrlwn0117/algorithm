a = list(map(int, input().split()))

if a == sorted(a):
    print('ascending')
elif a == sorted(a, reverse=True):
    print('descending')
else:
    print('mixed')

"""
여기 if문에서 a.sort()를 사용하면 제대로 되지 않는다 a.sort()와 sorted(a)의 차이는 리스트 본체가 정렬이 되냐 안되냐 인데
이것이 이유라면 이유가 될 수 있을것 같다
결론 : a.sort()는 본체 자체가 정렬, sorted(a)는 본체 자체는 변하지 않고 정렬된 결과만 반환 
"""