# Представьте, что вы шпионы)
# Придумайте шифр, в котором буквы заменяются на какие-то символы
# и реализуйте шифроватор и дешифроватор
import string
import random
eng = list(string.ascii_lowercase)
eng_copy = eng.copy()
engEncrypted = []
for word in eng:
    randint = random.randint(0, len(eng_copy) - 1)
    engEncrypted.append(eng_copy[randint])
    eng_copy.pop(randint)
orig_encrypt = dict(zip(eng, engEncrypted))
encrypt_orig = dict(zip(engEncrypted, eng))

while True:
    message = input('message >> ')
    print('encryption or decryption?')
    cryption = input('print: "en" or "de" >> ')
    answer = []
    if cryption == 'en':
        for sym in message:
            answer.append(orig_encrypt[sym])
    elif cryption == 'de':
        for sym in message:
            answer.append(encrypt_orig[sym])
    print(str(answer))



