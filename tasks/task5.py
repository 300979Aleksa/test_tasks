'''Условие задачи "Палиндром":
Помогите Васе понять, будет ли фраза палиндромом.
Учитываются только буквы и цифры, заглавные и строчные буквы считаются одинаковыми.
'''

'''Формат ввода:
В единственной строке записана фраза или слово. Буквы могут быть только латинские.
Фраза может состоять из строчных и прописных латинских букв, цифр, знаков препинания.
'''

'''Формат вывода:
Выведите «True», если фраза является палиндромом, и «False», если не является.
'''

# Пример ввода -> вывода:
inputs = [
    'A man, a plan, a canal: Panama',  # -> True
    'zo',                              # -> False
    '10001',                           # -> True
    '123'                              # -> False
]
##
# тут ваше решение:

#word = input () 

#if str(word) == ''.join(reversed(word)):
 #   print("Its palindrome")
#else:
#    print("Its not palindrome")

for string in inputs:
    new_string=[]
    for char in string:
        if char.isalnum():
            new_string.append(char.lower())
    print(new_string)
    new_string="".join(new_string)
    if new_string==new_string[::-1]:
        print(True)
    else:
        print(False)