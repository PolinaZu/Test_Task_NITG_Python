l = [22, 11, -16, -11, 31, 12, 1]
sm = 0
for i in range(len(l)):
    if l[i] % 2 == 0:
        sm += l[i]
print(sm)
