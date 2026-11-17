import random

def is_valid(num_2):
    if not num_2.isdigit():
        return None
    num_3=int(num_2)
    if num_3<1 or num_3>100:
        return None
    return num_3


target_num=random.randint(1, 100)
print('Добро пожаловать в числовую угадайку!')
print('Я загадал число от 1 до 100. Попробуй угадать его!')

user_num=None

while user_num!=target_num:
    while True:
        guess_str=input('Введите число от 1 до 100: ')
        result=is_valid(guess_str)
        if result is not None:
            user_num=result
            break
        print('Ошибка! Нужно ввести число от 1 до 100. Попробуйте еще раз.')
    if user_num>target_num:
        print('Слишком много, попробуйте еще раз')
    elif user_num<target_num:
        print('Слишком мало, попробуйте еще раз')
print('Вы угадали, поздравляем!')
print('Спасибо, что играли в числовую угадайку. Еще увидимся.')






