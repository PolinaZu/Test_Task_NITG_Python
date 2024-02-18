l = [22, 14, -16, -10, 31, -2, 1]
sm = 0
for i in range(len(l)):
    if i % 2 == 0:
        sm += l[i]
print(sm)
