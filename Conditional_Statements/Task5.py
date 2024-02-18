a, b, c = int(input()), int(input()), int(input())
print('Самое большое число:', max(a, b, c))

# 2й способ решения через if
if a > b:
    if a > c:
        print('Самое большое число:', a)
if b > a:
    if b > c:
        print('Самое большое число:', b)
if c > a:
    if c > b:
        print('Самое большое число:', c)
