mas = [[9, 2, 12, 21, 5], [11, 23, 2, 4, 31], [5, 8, 16, 30, 1], [23, 4, 18, 13, 21], [17, 8, 14, 56, 6]]
sm = 0
max_sm = 0
for i in range(len(mas)):
    for k in range(len(mas[i])):
        sm += mas[k][i]
    if sm > max_sm:
        max_sm = sm
        sm = 0
print(max_sm)
