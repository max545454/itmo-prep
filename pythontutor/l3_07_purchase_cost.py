a = int(input())
b = int(input())
n = int(input())
x = a * n
y = b * n
if y >= 100:
    print(x + (y // 100), y % 100)
else:
    print(x, y)