a = int(input())
b = int(input())
c = int(input())
if a > b:
    if c < b:
        print(c)
    else:
        print(b)
else:
    if a < c:
        print(a)
    else:
        print(c)
