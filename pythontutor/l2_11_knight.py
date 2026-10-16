a = int(input()) # решено с подсказкой: abs
a1 = int(input())
b = int(input())
b1 = int(input())
if ((a + 1) == b or (a + 2) == b or (a - 1) == b or (a - 2) == b) and ((a1 - 1) == b1 or (a1 - 2) == b1 or (a1 + 1) == b1 or (a1 + 2) == b1) and not ((a + 1 == b or a - 1 == b or a == b) and (a1 + 1 == b1 or a1 - 1 == b1 or a1 == b1)) and (a + a1) % 2 != (b + b1) % 2:
    print("YES")
else:
    print("NO")
