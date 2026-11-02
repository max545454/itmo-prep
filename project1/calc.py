a = float(input())
b = (input())
c = float(input())
if b == "+":
    print(a + c)
elif (b == '/' or b == '//' or b == '%') and c == 0:
    print('На ноль делить нельзя')
elif b == '-':
    print(a - c)
elif b == '*':
    print(a * c)
elif b == '/':
    print(a / c)
elif b == '//':
    print(a // c)
elif b == '%':
    print(a % c)
elif b == '**' and a == 0 and c < 0:
    print('выражение не имеет смысла')
elif b == '**':
    print(a ** c)
else:
    print('неизвестная операция')