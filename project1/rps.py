import random
comp = random.randint(1, 3)   # случайное целое от 1 до 3 включительно
p = input()
if comp == 1:
    print('ножницы')
    compw = 'ножницы'
elif comp == 2:
    print('камень')
    compw = 'камень'
elif comp == 3:
    print('бумага')
    compw = 'бумага'
if (p == 'камень' and comp == 1) or (p == 'ножницы' and comp == 3) or (p == 'бумага' and comp == 2):
    print('Ты победил')
elif (p == 'ножницы' and comp == 2) or (p == 'бумага' and comp == 1) or (p == 'камень' and comp == 3):
    print('Ты проиграл')
elif p == compw:
    print('Ничья')
else:
    print('ошибка')