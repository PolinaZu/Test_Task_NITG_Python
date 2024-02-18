a = 11
mas = []
for i in range(a):
    mas.append([i] * a)
for j in range(0, len(mas)):
    for k in range(0, len(mas[j])):
        if j == k:
            print(mas[j][k], end=' ')
        else:
            print(end=' ')
    print()
