a = int(input())
a1 = int(input())
b = int(input())
b1 = int(input())
if (a + a1) % 2 == 0 and (b + b1) % 2 == 0:
    print("YES")
elif (a + a1) % 2 != 0 and (b + b1) % 2 != 0:
    print("YES")
else:
    print("NO")