P = int(input())
X = int(input())
Y = int(input())
m = (((X * 100) + Y) * (P + 100)) // 100
print(m // 100, (m % 100))
