mas = [2, 4, 10, 3, 10, 1, 11]
count = 0
max_count = 1
number = 0
max_number = 0
for i in range(len(mas)):
    count = 0
    for j in range(len(mas)):
        if mas[i] == mas[j]:
            count += 1
    if count > max_count:
        max_count = count
        number = mas[i]
    elif max_count == count and count != 1 and number < mas[i]:
        max_number = mas[i]
if max_count == 1:
    print("Повторяющихся чисел нет")
elif max_number > 0:
    print("Наибольшее число из часто встречающихся:", max_number)
else:
    print("Наиболее часто встречающееся число: ", number)
