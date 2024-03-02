# программа корректно работает, однако нуждается в оптимизации
# (вынести повторяющийся код в функции и продумать как улучшить выполнение)
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

need_to_crypt = True
while need_to_crypt:
    way_to = input('Введи 1, если нужно зашифровать текст и 2, если расшифровать: ')
    lang = input('Выбери язык шифровки - eng 1, rus 2: ')
    rot = int(input('Введи шаг сдвига: '))
    if way_to == '1':
        if lang in ['1', 'eng', 'англ']:
            rot = rot % 26
            text = input('Input your text: ')
            new_text = ''
            for c in text:
                if c.isupper():
                    idx = eng_upper_alphabet.index(c) + rot
                    if idx >= 26:
                        idx -= 26
                    new_text += eng_upper_alphabet[idx]
                elif c.islower():
                    idx = eng_lower_alphabet.index(c) + rot
                    if idx >= 26:
                        idx -= 26
                    new_text += eng_lower_alphabet[idx]
                else:
                    new_text += c
            print(f'Your text: {new_text}')

        elif lang in ['2', 'rus', 'рус']:
            rot = rot % 32
            text = input('Введи свой текст: ')
            new_text = ''
            for c in text:
                if c.isupper():
                    idx = rus_upper_alphabet.index(c) + rot
                    if idx >= 32:
                        idx -= 32
                    new_text += rus_upper_alphabet[idx]
                elif c.islower():
                    idx = rus_lower_alphabet.index(c) + rot
                    if idx >= 32:
                        idx -= 32
                    new_text += rus_lower_alphabet[idx]
                else:
                    new_text += c
            print(f'Ваш текст: {new_text}')
        else:
            print('Предусмотрены только русский и английский языки!')
            continue
    elif way_to == '2':
        if lang in ['1', 'eng', 'англ']:
            rot = rot % 26
            text = input('Input your text: ')
            new_text = ''
            for c in text:
                if c.isupper():
                    idx = eng_upper_alphabet.index(c) - rot
                    if idx < 0:
                        idx += 26
                    new_text += eng_upper_alphabet[idx]
                elif c.islower():
                    idx = eng_lower_alphabet.index(c) - rot
                    if idx < 0:
                        idx += 26
                    new_text += eng_lower_alphabet[idx]
                else:
                    new_text += c
            print(f'Your text: {new_text}')

        elif lang in ['2', 'rus', 'рус']:
            rot = rot % 32
            text = input('Введи свой текст: ')
            new_text = ''
            for c in text:
                if c.isupper():
                    idx = rus_upper_alphabet.index(c) - rot
                    if idx < 0:
                        idx += 32
                    new_text += rus_upper_alphabet[idx]
                elif c.islower():
                    idx = rus_lower_alphabet.index(c) - rot
                    if idx < 0:
                        idx += 32
                    new_text += rus_lower_alphabet[idx]
                else:
                    new_text += c
            print(f'Ваш текст: {new_text}')
        else:
            print('Предусмотрены только русский и английский языки!')
            continue
    still_crypt = input('Продолжаем работать: ')
    if still_crypt not in ['yes', 'да']:
        need_to_crypt = False
