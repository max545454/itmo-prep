m = int(input())
a = m // 100
b = (m % 100) // 10
c = (m % 100) % 10
print(a, b, c, sep="")
print(a, c, b, sep="")
print(b, a, c, sep="")
print(b, c, a, sep="")
print(c, a, b, sep="")
print(c, b, a, sep="")

