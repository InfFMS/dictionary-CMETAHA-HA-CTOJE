# Даны два словаря. Напишите программу, которая объединит эти словари. 
# Если ключи встречаются в обоих исходных словарях, значения, 
# которые хранятся по этим ключам складываются.
# Пример:

# Первый словарь: {'a': 100, 'b': 200, 'c':300}
# Второй словарь: {'a': 300, 'b': 200, 'd':400}
# Результат: {'a': 400, 'b': 400, 'd': 400, 'c': 300}

slov1 = {'a': 100, 'b': 200, 'c':300}
slov2 = {'a': 300, 'b': 200, 'd':400}
slov2_copy = slov2.copy()
slov3 = {}
for i in slov1:
    if i in slov2_copy:
        slov3.update({str(i):str(slov1[i]+slov2[i])})
        slov2_copy.pop(i)
    else:
        slov3.update({str(i):str(slov1[i])})
for i in slov2_copy:
    slov3.update({str(i):str(slov2_copy[i])})
print(slov3)

