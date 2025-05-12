# Создайте программу-переводчик, которая хранит перевод
#  слов с русского языка на английский.
# После запуска программа выводит список слов в словаре 
# и предлагает пользователю ввести слово для перевода. 
# Если введенного слова нет в словаре выводится сообщение "нет такого слова".
# Используйте словари для словаря:)
engWords = 'animal, apple, arm, baby, badminton, bag, ball, balloon, banana, bear, bed, bee, bike, bird, blackboard, block, book, box'
engWords = engWords.split(', ')

rusWords = 'животное яблоко рука малыш бадминтон сумка мяч воздушный шар банан медведь кровать пчела велосипед птица доска кубик книга коробка'
rusWords = rusWords.split()

eng_rusWords = dict(zip(engWords, rusWords))
rus_engWords = dict(zip(rusWords, engWords))


def eng_rus(word):
    outRusWord = eng_rusWords.get(word)
    if outRusWord:
        return outRusWord
    else:
        return 'translation is not available'


def rus_eng(word):
    outEngWord = rus_engWords.get(word)
    if outEngWord:
        return outEngWord
    else:
        return 'перевод не имеется'


fl = input('eng to rus (write eng), руское в английское? (напишите рус) >> ')
if fl == 'eng':
    word = input('word >> ')
    print(eng_rus(word))
if fl == 'рус':
    word = input('слово >> ')
    print(rus_eng(word))
