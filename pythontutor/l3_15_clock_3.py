a = float(input())
H = (a // 30)
M = (a % 30) * 2
S = (a % 30) % 0.5 * 120
print(int(H), int(M), int(S))