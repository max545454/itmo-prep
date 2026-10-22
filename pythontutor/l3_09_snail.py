import math

h = int(input())
a = int(input())
b = int(input())
x = a - b
y = ((h - b) / x)
y1 = math.ceil(y)
print(y1)