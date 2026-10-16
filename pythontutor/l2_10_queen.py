a = int(input())
a1 = int(input())
b = int(input())
b1 = int(input())
if a == b or a1 == b1:
    print("YES")
elif (a + a1) == (b + b1) or (a - a1) == (b - b1):
    print("YES")
else:
    print("NO")
