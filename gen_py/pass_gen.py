from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambiguous = 'il1Lo0O'


def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += choice(chars)
    return password


chars = ''

cnt_pass = int(input('Укажите количество паролей для генерации: '))
len_pass = int(input('Укажите длину одного пароля: '))
dig = input('Включать ли цифры? (да/нет) ')
upp = input('Включать ли прописные буквы? (да/нет) ')
low = input('Включать ли строчные буквы? (да/нет) ')
punc = input('Включать ли символы? (да/нет) ')
amb = input('Исключать ли неоднозначные символы? (да/нет) Речь о символах il1Lo0O ')
if dig.lower() in ['y', 'yes', 'да']:
    chars += digits
if upp.lower() in ['y', 'yes', 'да']:
    chars += uppercase_letters
if low.lower() in ['y', 'yes', 'да']:
    chars += lowercase_letters
if punc.lower() in ['y', 'yes', 'да']:
    chars += punctuation
if amb.lower() in ['y', 'yes', 'да']:
    for c in ambiguous:
        chars = chars.replace(c, '')
lst_pass = []

for i in range(1, cnt_pass + 1):
    lst_pass.append(generate_password(len_pass, chars))
print(*lst_pass, sep='\n')
