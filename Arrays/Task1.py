l = [1, 2, -4, -10, 3, -2, 1]
positive = 0
negative = 0
for i in range(len(l)):
    if l[i] < 0:
        negative += 1
    else:
        positive += 1
print(positive)
print(negative)
