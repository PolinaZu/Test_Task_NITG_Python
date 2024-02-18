n = int(input())
n1 = 1
n2 = 0
for i in range(n):
    n2 = n1 + n2
    n1 = n2 - n1
print(n2)