a = 11
mas = []
for i in range(a):
    mas.append([i] * a)
for j in range(0, len(mas)):
    for k in range(len(mas[j])):
        if j + k == 10:
            print(mas[j][k], end=' ')
        else:
            print(end=' ')
    print()