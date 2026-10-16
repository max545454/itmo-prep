N = int(input())
M = int(input())
x = int(input())
y = int(input())
if N > M:
    if (N - y) <= (M - x) and (N - y) <= y and (N - y) <= x:
        print(N - y)
    elif (M - x) <= (N - y) and (M - x) <= y and (M - x) <= x:
        print(M - x)
    elif y <= x and y <= (M - x) and y <= (N - y):
        print(y)
    elif x <= y and x <= (M - x) and x <= (N - y):
        print(x)
else:
    if (M - y) <= (N - x) and (M - y) <= y and (M - y) <= x:
        print(M - y)
    elif (N - x) <= (M - y) and (N - x) <= y and (N - x) <= x:
        print(N - x)
    elif y <= x and y <= (N - x) and y <= (M - y):
        print(y)
    elif x <= y and x <= (N - x) and x <= (M - y):
        print(x)
