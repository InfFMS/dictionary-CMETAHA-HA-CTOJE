# Нужно считать файл parameters.txt. 
# Это файл с настройками расчетной модели.
# Формат в файле следующий первое слово в строке - это ключ, 
# потом после пробела - значение (может быть строкой, числом, или набором чисел),
# все, что после символа "//" это комментарий  должно игнорироваться.
# Реализуйте считывание значений из файла и запись этих значений в словарь.
variables = {}
with open('parameters.txt', encoding='utf-8') as file:
    for line in file:
        variable = str()
        value = str()
        lineSplit = line.split()
        for i in range(len(lineSplit)):
            if lineSplit[i][0] == '/' and lineSplit[i][1] == '/':
                lineSplit = lineSplit[:i]
                break
        if len(lineSplit) != 0:
            variables.update({f'{lineSplit[0]}':f'{lineSplit[1]}'})
print(variables)

