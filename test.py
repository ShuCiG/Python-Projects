# [print(int(i)**3, end=' ') for i in input().split()]

#print(''.join(ch for ch in input() if ch.isdigit()))

#[print(i**2, end=' ') for i in input().split() if ((i % 2 == 0) and ((i**2 % 10) != 4))]

'''
a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

n = len(a)

# реализация алгоритма сортировки выбором
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print(a)
'''
'''
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)

for i in range(1, n): 
    elem = a[i]  # берем первый элемент из неотсортированной части списка
    j = i
    
    # пока элемент слева существует и больше нашего текущего элемента
    while j >= 1 and a[j - 1] > elem:
        # смещаем j-1-й элемент отсортированной части вправо
        a[j] = a[j - 1]
        # сами идём влево, дальше ищем место для нашего текущего элемента
        j -= 1

    # нашли место для нащего текущего элемента из неотсортированной части
    # и вставляем его на индекс j в отсортированной части
    a[j] = elem


print('Отсортированный список:', a)
'''

#[print((i + 1) * 2) for i in range(int(input()) // 2)]

'''
L = input().split()

M = input().split()

R = []

for i in range(len(L)):
    R.append(int(L[i]) + int(M[i]))

print(R)
'''

# elements = input().split()

# print(*elements, sep='+', end='=' + str(elements.sum()))

#print(*[i[1:] + i[0] * 2 + 'ки' for i in input().split()], sep = ' ')

'''
# объявление функции
def print_digit_sum(num):
    print(sum(int(i) for i in list(str(num))))

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
'''

'''
target = 'abcdabcaaa'
symbol = 'a'
    
while target.find(symbol) >= 0:
    print(target.find(symbol))
    target = target[target.find(symbol) + 1:]
    print(target)
'''

'''
# объявление функции
def draw_triangle():
    for i in range(1, 9):
        print(' ' * (8 - i) + '*' * ((i - 1) * 2 + 1))
        

# основная программа
draw_triangle()  # вызов функции
'''

'''
import random

def is_valid(str_num):
    if len(str_num) > 3:
        return False
    elif not str_num.isdigit():
        return False
    elif not (0 < int(str_num) <= 100):
        return False
    else:
        return True

random_int = random.randint(1, 101)
print('Добро пожаловать в числовую угадайку :', random_int)
user_count = 0

while True:
    user_num = input("Введите число от 1 до 100 :")

    if not is_valid(user_num):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue

    user_int = int(user_num)
    user_count += 1

    if user_int > random_int:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif user_int < random_int:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали за', user_count, 'раз, поздравляем!')
        break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
'''

'''
import random

answers = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай',
           'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет',
           'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет',
           'Определённо да', 'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
		   'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно'
           ]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')

user_name = input('Как вас зовут? : ')
print('Привет', user_name)
			
while True:
    user_ask = input('Задай свой вопрос ' + user_name + ' на который можно ответить "да" или "нет" : ')
    print(random.choice(answers))
    
    user_follow = input('Хочет спросить что-то еще ("Да"/"Нет")? ')
    if user_follow.lower() == 'да':
        continue
    else:
        break

print('Возвращайся, если возникнут вопросы!')
'''			

'''
import random as rnd

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
STRANGE_CHARS = 'ilI1Lo0O'

def generate_password(length, chars):
    result = ''
    for i in range(int(length)):
        result += rnd.choice(chars)

    return result

chars = ''

passwords_count = input('Количество паролей для генерации ')
password_length = input('Длина одного пароля ')
is_digits = input('Включать ли цифры 0123456789 (да/нет) ')
is_lowercase_letters = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ (да/нет) ')
is_uppercase_letters = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz (да/нет) ')
is_punctuation = input('Включать ли символы !#$%&*+-=?@^_ (да/нет) ')
is_strange_chars = input('Исключать ли неоднозначные символы il1Lo0O (да/нет) ')

if is_digits == 'да' or is_digits == '':
    chars += DIGITS

if is_lowercase_letters == 'да' or is_lowercase_letters == '':
    chars += LOWERCASE_LETTERS

if is_uppercase_letters == 'да' or is_uppercase_letters == '':
    chars += UPPERCASE_LETTERS

if is_punctuation == 'да' or is_punctuation == '':
    chars += PUNCTUATION

if is_strange_chars == 'да' or is_strange_chars == '':
    chars = list([i for i in chars if i not in STRANGE_CHARS])

for i in range(int(passwords_count)):
    print(generate_password(password_length, chars))
'''

'''
# русский алфавит без «ё»
ALPHABET_RUS = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# английский алфавит
ALPHABET_ENG = 'abcdefghijklmnopqrstuvwxyz'

def caesar_code(text, lang, k):
    res = []
    if lang == 'eng':
        alphabet = ALPHABET_ENG
    else:
        alphabet = ALPHABET_RUS

    for ch in text:
        low = ch.lower()
        if low in alphabet:
            idx = alphabet.index(low)
            new_idx = (idx + k) % len(alphabet)
            new_ch = alphabet[new_idx]
            res.append(new_ch.upper() if ch.isupper() else new_ch)
        else:
            res.append(ch)
    return ''.join(res)

#shift = input('Введи сдвиг : ')
lang = input('Введи язык (eng/rus) : ')
msg = input('Введи сообщение : ')
for i in range(26):
    cipher = caesar_code(msg, lang, int(i))
    print(i, cipher)
'''

# print(1 * 16**3 + 10 * 16**2 + 15 * 16 + 2)
# print(int('1AF2', 16))
# print(int('1000', 16))

"""
import random as rnd

word_list = ['человек', 'работа', 'вопрос', 'сторона', 'страна', 'случай', 'голова', 'ребенок', 'система',
             'отношение', 'женщина', 'деньги', 'машина', 'проблема', 'решение', 'история', 'власть', 'тысяча',
             'возможность', 'результат', 'область', 'статья', 'компания', 'группа', 'развитие', 'процесс', 'условие',
             'средство', 'начало', 'уровень', 'минута', 'качество', 'дорога', 'действие', 'государство', 'любовь',
             'взгляд', 'общество', 'деятельность', 'организация', 'президент', 'комната', 'порядок', 'момент',
             'письмо', 'помощь', 'ситуация', 'состояние', 'квартира', 'внимание', 'смерть', 'программа', 'задача',
             'предприятие', 'разговор', 'правительство', 'производство', 'информация', 'положение', 'интерес',
             'федерация', 'правило', 'управление', 'мужчина', 'партия', 'сердце', 'движение', 'материал', 'неделя',
             'чувство', 'газета', 'причина', 'основа', 'товарищ', 'культура', 'данные', 'мнение', 'документ',
             'институт', 'проект', 'встреча', 'директор', 'служба', 'судьба', 'девушка', 'очередь', 'состав',
             'количество', 'событие', 'объект', 'создание', 'значение', 'период', 'искусство', 'структура', 'пример',
             'исследование', 'гражданин', 'начальник', 'принцип', 'воздух', 'характер', 'борьба', 'использование',
             'размер', 'образование', 'мальчик', 'представитель', 'участие', 'девочка', 'политика', 'картина', 'доллар',
             'территория', 'изменение', 'направление', 'рисунок', 'течение', 'церковь', 'население', 'большинство',
             'музыка', 'правда', 'свобода', 'память', 'команда', 'договор', 'дерево', 'хозяин', 'природа', 'телефон',
             'позиция', 'писатель', 'самолет', 'солнце', 'спектакль', 'способ', 'журнал', 'руководитель', 'специалист',
             'оценка', 'регион', 'процент', 'родитель', 'требование', 'основание', 'половина', 'анализ', 'автомобиль',
             'экономика', 'литература', 'бумага', 'степень', 'господин', 'надежда', 'предмет', 'вариант', 'министр',
             'граница', 'модель', 'операция', 'название', 'старик', 'миллион', 'счастье', 'ребята', 'кабинет',
             'магазин', 'пространство', 'знание', 'защита', 'руководство', 'площадь', 'сознание', 'возраст', 'участник',
             'участок', 'желание', 'доктор', 'председатель', 'представление', 'солдат', 'художник', 'оружие',
             'соответствие', 'парень', 'зрение', 'генерал', 'понятие', 'строительство', 'услуга', 'содержание',
             'радость', 'безопасность', 'продукт', 'комплекс', 'бизнес', 'сотрудник', 'предложение', 'технология',
             'реформа', 'отсутствие', 'собака', 'камень', 'будущее', 'рассказ', 'контроль', 'продукция', 'техника',
             'здание', 'необходимость', 'подготовка', 'республика', 'хозяйство', 'бюджет', 'деревня', 'элемент',
             'обстоятельство', 'победа', 'источник', 'звезда', 'сестра', 'практика', 'проведение', 'карман',
             'определение', 'функция', 'войско', 'комиссия', 'применение', 'капитан', 'работник', 'обеспечение',
             'офицер', 'фамилия', 'предел', 'выборы', 'ученый', 'бутылка', 'теория', 'разработка', 'личность',
             'праздник', 'влияние', 'читатель', 'удовольствие', 'ответственность', 'учитель', 'множество',
             'особенность', 'показатель', 'корабль', 'впечатление', 'частность', 'детство', 'профессор', 'прошлое',
             'командир', 'коридор', 'поддержка', 'собрание', 'болезнь', 'клетка', 'заявление', 'попытка', 'сравнение',
             'расчет', 'депутат', 'комитет', 'выражение', 'здоровье', 'десяток', 'глубина', 'студент', 'секунда',
             'скорость', 'ошибка', 'режиссер', 'поверхность', 'ощущение', 'станция', 'революция', 'колено',
             'министерство', 'стекло', 'высота', 'бабушка', 'трубка', 'мастер', 'поведение', 'столица', 'механизм',
             'передача', 'способность', 'подход', 'энергия', 'существование', 'исполнение', 'сожаление', 'заместитель',
             'ресурс', 'рождение', 'администрация', 'стоимость', 'улыбка', 'артист', 'фигура', 'субъект', 'реакция',
             'список', 'фотография', 'журналист', 'нарушение', 'заседание', 'больница', 'существо', 'свойство',
             'поколение', 'животное', 'усилие', 'отличие', 'остров', 'противник', 'реализация', 'страница',
             'формирование', 'житель', 'красота', 'растение', 'явление', 'наличие', 'одежда', 'кресло', 'больной',
             'университет', 'традиция', 'декабрь', 'ладонь', 'сведение', 'цветок', 'октябрь', 'занятие', 'сентябрь',
             'помещение', 'январь', 'зритель', 'редакция', 'фактор', 'август', 'известие', 'зависимость', 'охрана',
             'оборудование', 'концерт', 'отделение', 'расход', 'выставка', 'милиция', 'переход', 'произведение',
             'родина', 'собственность', 'лагерь', 'имущество', 'кровать', 'аппарат', 'середина', 'клиент', 'отрасль',
             'беседа', 'законодательство', 'продажа', 'повышение', 'полковник', 'сомнение', 'понимание', 'апрель',
             'кодекс', 'настроение', 'должность', 'преступление', 'лестница', 'установка', 'появление', 'получение',
             'образец', 'главное', 'костюм', 'ценность', 'обязанность', 'таблица', 'воспоминание', 'лошадь', 'коллега',
             'организм', 'ученик', 'учреждение', 'открытие', 'характеристика', 'выполнение', 'оборона', 'выступление',
             'температура', 'перспектива', 'подруга', 'приказ', 'жертва', 'ресторан', 'километр', 'признак',
             'промышленность', 'американец', 'заключение', 'восток', 'исключение', 'постановление', 'перевод',
             'секретарь', 'польза', 'звонок', 'обстановка', 'чиновник', 'соглашение', 'деталь', 'русский', 'тишина',
             'зарплата', 'подарок', 'тюрьма', 'конкурс', 'книжка', 'изучение', 'просьба', 'публика', 'сообщение',
             'угроза', 'достижение', 'назначение', 'реклама', 'портрет', 'стакан', 'творчество', 'телевизор',
             'инструмент', 'концепция', 'лейтенант', 'реальность', 'знакомый', 'конфликт', 'переговоры', 'запись',
             'площадка', 'последствие', 'сотрудничество', 'зеркало', 'академия', 'палата', 'потребность', 'ноябрь',
             'увеличение', 'поездка', 'потеря', 'февраль', 'мероприятие', 'принятие', 'устройство', 'вещество',
             'категория', 'гостиница', 'издание', 'объединение', 'темнота', 'человечество', 'колесо', 'опасность',
             'разрешение', 'воздействие', 'коллектив', 'камера', 'следствие', 'кандидат', 'родственник', 'давление',
             'присутствие', 'взаимодействие', 'партнер', 'двигатель', 'достоинство', 'страсть', 'испытание', 'оплата',
             'разница', 'водитель', 'снижение', 'формула', 'капитал', 'новость', 'эффект', 'губернатор', 'доклад',
             'убийство', 'эксперт', 'автобус', 'платье', 'общение', 'психология', 'проверка', 'процедура', 'рабочий',
             'ремонт', 'обращение', 'обучение', 'ожидание', 'памятник', 'корень', 'наблюдение', 'доказательство',
             'признание', 'постель', 'владелец', 'компьютер', 'инженер', 'старуха', 'ракета', 'вершина', 'выпуск',
             'торговля', 'молодежь', 'корпус', 'недостаток', 'сущность', 'талант', 'эффективность', 'полоса',
             'основное', 'рассмотрение', 'следователь', 'описание', 'редактор', 'дворец', 'забота', 'столик',
             'эксперимент', 'печать', 'кольцо', 'пистолет', 'воспитание', 'начальство', 'профессия', 'ворота', 'дружба',
             'окончание', 'величина', 'записка', 'инициатива', 'совесть', 'активность', 'кредит', 'господь',
             'конференция', 'потолок', 'библиотека', 'помощник', 'конструкция', 'металл', 'молоко', 'прокурор',
             'транспорт', 'поэзия', 'соединение', 'краска', 'расстояние', 'подразделение', 'сигнал', 'атмосфера',
             'контакт', 'сигарета', 'восторг', 'золото', 'премия', 'король', 'подъезд', 'автомат', 'мальчишка',
             'чтение', 'поселок', 'свидетель', 'ставка', 'удивление', 'поворот', 'возвращение', 'мгновение', 'статус',
             'параметр', 'сказка', 'тенденция', 'дыхание', 'версия', 'масштаб', 'монастырь', 'хозяйка', 'эксплуатация',
             'коммунист', 'пенсия', 'приятель', 'объяснение', 'производитель', 'философия', 'мощность', 'обязательство',
             'кризис', 'указание', 'яблоко', 'препарат', 'действительность', 'москвич', 'остаток', 'изображение',
             'сделка', 'сочинение', 'покупатель', 'затрата', 'строка', 'единица', 'обработка', 'чемпионат']

def get_word():
    return rnd.choice(word_list).upper()

# функция получения текущего состояния
def display_hangman(tries):
    # значение tries = 6 соответствует начальному положению, пустая виселица;
    # значение tries = 0 соответствует конечному положению, то есть проигрышу и полностью нарисованному телу повешенного.    
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток

    print('Давайте играть в угадайку слов!')

    # print(word)

    print(display_hangman(tries))
    print(word_completion)

    while tries > 0:
        user_input = input('Введите букву или слово целиком : ').upper()

        if len(user_input) == 1 and not user_input.isalpha():
            print('Неправильный ввод! Будьте внимательнее')
            continue

        if user_input in guessed_letters or user_input in guessed_words:
            print('Вы уже это вводили, будте внимательнее')
            continue

        if user_input == word:
            print('Поздравляем, вы угадали слово! Вы победили!')
            break

        if user_input in word:
            wc_list = list(word_completion)
            for i in range(len(wc_list)):
                if user_input == word[i]:
                    wc_list[i] = user_input[0]

            word_completion = ''.join(wc_list)

            print(word_completion)
            continue

        tries -= 1
        print(word_completion)
        print(display_hangman(tries))

        guessed_letters.append(user_input)
    else:
        print('К сожалению вы проиграли. Загаданое слово :', word)

while True:
    play(get_word())

    if input('Для продолжения введите "да" : ') != 'да':
        break

print('До свидания! Приходите еще')
"""

#print("{:,d}".format(int(input())))   

# print(max(len(part) for part in input().split('О')))

'''
numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
res = 0
for num in numbers:
    res += (num % 2 == 1) and (num > 1) 
    print(num, (num % 2 == 1) and (num > 1) )
print(res)
'''

#print(*[list(range(1, i + 1)) for i in range(1, int(input()) + 1)], sep='\n')

'''
# put your python code here
import math

def pascal_row(n):
    row = []
    for k in range(n + 1):
        c = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
        row.append(c)
    return row

n = 4 # int(input())
for i in range(n):
    print(*pascal_row(i), sep=' ')
'''

'''
n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])
    
max_elem = matrix[0][0]
mid = n // 2

for i in range(n):
    for j in range(n):
        if (
                (i >= j) and (i <= n - 1 - j)
            ) or
            (
                (i <= j) and (i >= n - 1 - j)
            ) and matrix[i][j] > largest:
            print(i, j, matrix[i][j])
            largest = matrix[i][j]
print(max_elem)
'''

'''
# put your python code here
n, m = int(input()), int(input())

matrix = []

for i in range(n):
    matrix.append([i * j for j in range(m)])
    
for row in matrix:
    print(*[str(x).ljust(3) for x in row])
'''

'''
# put your python code here
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

flag = True

for i in range(1, n**2 + 1):
    for j in range(n):
        if i not in matrix[j]:
            print(i)
            flag = False
            break
            
if not flag:
    print('NO')
else:
    print('YES')
'''

'''
Filling with a spiral 🌀🌶️🌶️
Two natural numbers n and m are fed into the program. Write a program that creates an n × m matrix, filling it with a ‘spiral’ according to the pattern.

Input format
The program takes two natural numbers n and m as input on a single line – the number of rows and columns in the matrix.
'''
n, m = [int(i) for i in input().split()]

matrix = [[0] * m for _ in range(n)]

count = 1

top, bottom = 0, n - 1
left, right = 0, m - 1

while count <= n * m:
    for x in range(left, right + 1):
        matrix[top][x] = count
        count += 1
    top += 1
    if top > bottom:
        break
        
    for y in range(top, bottom + 1):
        matrix[y][right] = count
        count += 1
    right -= 1
    if left > right:
        break
        
    for x in range(right, left - 1, -1):
        matrix[bottom][x] = count
        count += 1
    bottom -= 1
    if top > bottom:
        break
        
    for y in range(bottom, top - 1, -1):
        matrix[y][left] = count
        count += 1
    left += 1
    
for row in matrix:
    print(*row)