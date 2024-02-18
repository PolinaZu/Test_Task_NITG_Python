positive = 0
negative = 0
for i in range(4):
    n = int(input())
    if n > 0:
        positive += 1
    else:
        negative += 1
print(positive)
print(negative)
