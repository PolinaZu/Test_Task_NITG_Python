import math

n = int(input())
s = math.factorial(n)
print(s)

# 2й способ решения через for
s = 1
for i in range(1, n + 1):
    s *= i
print(s)