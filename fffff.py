# a = input()
# if len(a) >= 6 and len(a) % 2 == 0:
#     print('четная большая')
# elif len(a) < 6 and len(a) % 2 == 0:
#     print('четная короткая')
# elif len(a) >= 6 and len(a) % 2 != 0:
#     print('нечетная большая')
# elif len(a) < 6 and len(a) % 2 != 0:
#     print('нечетная короткая')


# first_string = input().lower()
# second_string = input().lower()
# if first_string < second_string:
#     print('-1')
# elif second_string < first_string:
#     print('1')
# else:
#     print('0')


# number_of_guests = int(input())
# if number_of_guests == 1:
#     print(0)
# elif number_of_guests % 2 == 0:
#     print(number_of_guests//2)
# else:
#     print(number_of_guests)
#
#
# salary = int(input().split())


# age = int(input())
# member = bool(int(input()))
#
# if age > 18 and member:
#     print("Цена билета 75")
# elif age > 18 and  not member:
#     print("Цена билета 100")
# elif age < 18 and member:
#     print("Цена билета 25")
# elif age < 18 and not member:
#     print("Цена билета 50")

# number = int(input())
#
# if number % 3 == 0 and number % 5 == 0:
#     print('FizzBuzz')
# elif number % 3 == 0:
#     print('Fizz')
# elif number % 5 == 0:
#     print('Buzz')
# else:
#     print(number)

# number_1 = int(input())
# number_2 = int(input())
# number_3 = int(input())
#
# if number_3 == number_1 == number_2:
#     print(3)
# elif number_1 == number_2 or number_3 == number_2 or number_1 == number_3:
#     print(2)
# else:
#     print(0)

# sentence = input()
#
# if sentence[-1] == '.':
#     print('Законченное')
# elif sentence[-1] == '?':
#     print('Вопросительное')
# elif sentence[-1] == '!':
#     print('Восклицательное')
# elif sentence[-1] == ',':
#     print('Незаконченное')
# else:
#     print('Неопределенное')


# n = int(input())
#
# if n ==1 :
#     print('Январь')
# elif n == 2:
#     print('Февраль')
# elif n == 3:
#     print('Март')
# elif n == 4:
#     print('Апрель')
# elif n == 5:
#     print('Май')
# elif n == 6:
#     print('Июнь')
# elif n == 7:
#     print('Июль')
# elif n == 8:
#     print('Август')
# elif n == 9:
#     print('Сентябрь')
# elif n == 10:
#     print('Октябрь')
# elif n == 11:
#     print('Ноябрь')
# elif n == 12:
#     print('Декабрь')


# n = int(input())
#
# if n < 2 :
#     print('Младенец')
# elif 2 <= n < 4:
#     print('Малыш')
# elif 4 <= n < 12:
#     print('Ребенок')
# elif 12 <= n < 19:
#     print('Подросток')
# elif 19 <= n < 65:
#     print('Взрослый человек')
# else:
#     print('Пожилой человек')

# a = float(input())
# b = float(input())
# c = input()
#
# if  c not in ('+','-','*','/'):
#     print('Неизвестно')
# elif c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '*':
#     print(a * b)
# elif c == '/':
#     if a == 0 or b == 0:
#         print('Неизвестно')
#     else:
#         print(a / b)


#
#     password = input()
#     password_2 = input()
#
#     if len(password) < 7:
#         print('Short')
#     elif password != password_2:
#         print('Difference')
#     else:
#         print('OK')

# number = int(input())
# match number:
#     case 1:
#         print('Совсем еще зеленый студентик')
#
#     case 2:
#         print('Джун-студент')
#     case 3:
#         print('Мидл - студент')
#     case 4:
#         print('Сеньор - студент')
#     case 5:
#         print('Босс качалки')
#     case _:
#         print('Неизвестный курс')


# number = int(input())
# match number:
#     case 1|3|5|7|8|10|11:
#         print(31)
#     case 4|6|9|12:
#         print(30)
#     case _:
#         print(28)
#
# sign = input()
# match sign:
#     case 'Овен'|'Лев'|'Стрелец':
#         print('Огненный')
#     case 'Телец'|'Дева'|'Козерог':
#         print('Земной')
#     case 'Близнецы' | 'Весы' | 'Водолей':
#         print('Воздушный')
#     case 'Рак' | 'Скорпион' | 'Рыбы':
#         print('Водный')
#     case _:
#         print('Неизвестный знак зодиака')

# i_love_none = [None] * 50
# print(i_love_none)
#
# my_tuple = (-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)
# print(min(my_tuple), max(my_tuple))

# my_tuple = (-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)
# print(sum(my_tuple) / len(my_tuple))
#
#
# a = (1,)
# b = ('R',)
# c = ('A',)
# d = (2,)
# result = (a * 3) + (b * 5) + (c * 8) + (d * 5)
# print(result)


# a = int(input())
# b = int(input())
#
# print(tuple(range(a,b + 1)))


# n = int(input())
# list_ = []
# for i in range(n, n**2+ 1):
#     if i % 2 !=0:
#         list_.append(i)
# print(tuple(list_))


# my_tuple = (32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45, 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34, 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68, 56, 26, 39, 34, 50, 10, 12, 3, 27)
# print(my_tuple[44])
# print(my_tuple[-9])

# my_tuple = (32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45, 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34, 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68, 56, 26, 39, 34, 50, 10, 12, 3, 27)
#
# slice_5_10 = my_tuple[5:10]
# slice_from_20 = my_tuple[20:]
# slice_to_35 = my_tuple[:35]
#
# print(slice_5_10)
# print(slice_from_20)
# print(slice_to_35)

# my_tuple = (32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45, 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34, 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68, 56, 26, 39, 34, 50, 10, 12, 3, 27)
#
# print(my_tuple[::-1])



# my_tuple = (32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45, 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34, 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68, 56, 26, 39, 34, 50, 10, 12, 3, 27)
#
# print(my_tuple.count(50))
#
# words_tuple = ('quaint', 'leftovers', 'thesis', 'density', 'retired', 'weak', 'tolerate',
#                'sensitivity', 'primary', 'definition', 'determine', 'bring', 'monstrous',
#                'hurl', 'timetable', 'month', 'advocate', 'provoke', 'stress', 'omission')
# for i in words_tuple:
#     print(f'Длина слова {i} = {len(i)}')
#
# my_tuple = (
# -214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759,
# -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493,
# -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493,
# -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357,
# 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)
#
# list_ = []
# for i in my_tuple:
#     if i % 2 != 0:
#         list_.append(i)
# print(sum(list_)/ len(list_))

# players = [("Alice", 10), ("Bob", 15), ("Charlie", 20), ("Dave", 25)]
# max_difference = 6
#
# # for i in range(len(players)):
# #     print(i)
# # print(players[2])
#
# for i in players:
#     print(i[1] + 1)

# for i in players:
#     if i[1] - i[1] < max_difference:
#         print(f'{i[0]} vs {i[0]}')

# bank = float(input())
# bank *= 1.5
# print(bank)

print('''Районы, кварталы, жилые массивы
Я ухожу, ухожу красиво''')



