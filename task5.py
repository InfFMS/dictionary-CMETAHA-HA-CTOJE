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
word = input('eng to rus >> ')
outWord = eng_rusWords.get(word)
if outWord:
    print(outWord)
else:
    print('translation is not available')
