# Напишите программу, которая получает на вход две строки, и формирует из них словарь. 
# Ключами служат слова из первой строки, значениями – целые числа из второй.
# Пример ввода
# яблоки сливы груши персики манго киви апельсины
# 34 56 23 89 55 32 11

lst1 = 'яблоки сливы груши персики манго киви апельсины'.split()
lst2 = list(map(int, '34 56 23 89 55 32 11'.split()))
print(dict(zip(lst1, lst2)))
