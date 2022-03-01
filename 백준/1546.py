sub_num = int(input())

score = [int(x) for x in input().split()]
new_score = []
sum = 0

for i in range(len(score)):
    new_score.append(score[i] / max(score) * 100)

for j in range(len(new_score)):
    sum += new_score[j]

print(sum / len(new_score))