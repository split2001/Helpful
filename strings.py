a = '!!----qweretY12345-----!!!'
print(a.swapcase())  # меняет местами строчные и заглавные
print(a.rfind('q'))  # поиск по индексу
print(a.find('w'))  # поиск по индексу
print(a.replace('q', 'o'))
print(a.count('e'))
print(a.isdigit())  # содержит только цифры
print(a.islower())  # строчные
print(a.isupper())  # заглавные
print(a.isalnum())  #  содержит буквы и цифры
print(a.isalpha())  # содержит только буквы
print(a.istitle())  # содержит заглавные
print(a.ljust(15,'-'))  # добавить символы слева
print(a.rjust(15,'!'))  # добавить символы справа
print(a.center(15,'_'))  # добавить символы с обеих сторон
print(a.zfill(10))  # добавить 0 слева
print(a.endswith('5'))
print(a.startswith('q'))
print(a.rstrip('-, _, !, ?'))
print(a.strip('-, _, !, ?'))
print(a.lstrip('-, _, !, ?'))









# string = input()
# # print(string.replace('w','').replace('z',''))
# # print(string.replace(' ',','))
# before = string.lower()
# first = (before.replace('a','').replace('o','').replace('y','').
#          replace('e','').replace('u','').replace('i',''))
# second = '.'.join(first)
# print('.' + second)




# print('/\\_/\\\n>^,^<\n / \\\n(|_|)_/\n')
# print('_ /~~~\\\n //^ ^\\\\\n(/(_*_)\)\n_/\'\'*\'\'\_\n(/_)^(_\)')
#
# S.rpartition(sep)