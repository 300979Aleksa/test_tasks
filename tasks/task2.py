'''Условие задачи "Чётные и нечётные числа":
Представьте себе онлайн-игру для поездки в метро: игрок нажимает на кнопку, и на экране появляются три случайных числа.
Если все три числа оказываются одной чётности, игрок выигрывает.
Напишите программу, которая по трём числам определяет, выиграл игрок или нет.
'''

'''Формат ввода:
На вход через пробел подаются три случайных целых числа a, b и c.
'''

'''Формат вывода:
Выведите «WIN», если игрок выиграл, и «FAIL» в противном случае.
'''

# Пример ввода -> вывода:
inputs = [
    '1 2 -3',  # -> FAIL
    '7 11 7',  # -> WIN
    '6 -2 0'   # -> WIN
]

#a=in(input())
#b=in(input())
#c=in(input())


# тут ваше решение:

#from random import randint
#a=randint(-10,10)
#b=randint(-10,10)
#c=randint(-10,10)
#print(a,b,c)
#if (a%2==1) and (b%2==1) and (c%2==1) or (a%2==0) and (b%2==0) and (c%2==0):
#    print("Win")
#else:
#    print("Fale")
for input in inputs:
    number_list = input.split()
    values = list(map(int, number_list))
    n=0
    enum_nambers=0
    for value in values:
        if value %2==0:
            enum_nambers+=1
        n+=1
    if (enum_nambers==n or enum_nambers==0):
        print('win')
    else:
        print('fail')