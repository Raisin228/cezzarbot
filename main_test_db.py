from telebot import *
from time import *
from random import *
from list_stickers_id import *
import TOKEN

bot = telebot.TeleBot(TOKEN.condig)

# создание кнопок для начала работы
markup_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
but_start = types.KeyboardButton('Начать работу')
markup_start.add(but_start)

# создание кнопок для выбора действия
markup_action = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button1 = types.KeyboardButton('🔒 Шифpoвание')
button2 = types.KeyboardButton('🔑 Дешифpoвание')
markup_action.add(button1, button2)

# язык
markup_language = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttn1 = types.KeyboardButton('🇷🇺 Русский (без буквы ё)')
buttn2 = types.KeyboardButton('🇬🇧 Английский')
markup_language.add(buttn1, buttn2)

# continue
markup_continue = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
bt1 = types.KeyboardButton('Да 😀')
bt2 = types.KeyboardButton('Нет 😑')
markup_continue.add(bt1, bt2)

eng_lower = 'abcdefghijklmnopqrstuvwxyz'
eng_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
error_rus = [' ', '.', ',', ';', ':', '!', '?', 'ё', 'Ё', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '=', '+',
         '*', '/', '@', '#', '$', '%', '^', '&', '(', ')', '~', '–', '—', '«', '»', '’', '”', '"', '{', '}', '[', ']']
for i in eng_upper:
    error_rus.append(i)
for j in eng_lower:
    error_rus.append(j)

error_eng = [' ', '.', ',', ';', ':', '!', '?', 'ё', 'Ё', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '=', '+',
         '*', '/', '@', '#', '$', '%', '^', '&', '(', ')', '~', '–', '—', '«', '»', '’', '”', '"', '{', '}', '[', ']']
for i in rus_upper:
    error_eng.append(i)
for j in rus_lower:
    error_eng.append(j)

# функция для шифрования текста на основе входных данных использзуя шифр Цезаря
def encryption(st, step_shift, lang):
    tab = [chr(i) + chr(i) for i in range(ord('А'), ord('Я') + 1)]
    tab_eng = [chr(i) + chr(i) for i in range(ord('A'), ord('Z') + 1)]
    tab.extend(tab_eng)
    ans = ''
    for i in range(len(st)):
        if lang == 'русский':
            if st[i] not in error_rus:
                if lang == 'русский':
                    len_alph = 32
                    letters_upper = rus_upper
                    letters_small = rus_lower
                elif lang == 'английский':
                    len_alph = 26
                    letters_upper = eng_upper
                    letters_small = eng_lower

                if st[i] == st[i].upper():
                    ind = letters_upper.find(st[i])
                    new_ind = (ind + step_shift) % len_alph
                    new_letter = letters_upper[new_ind]
                else:
                    ind = letters_small.find(st[i])
                    new_ind = (ind + step_shift) % len_alph
                    new_letter = letters_small[new_ind]
                ans += new_letter
            else:
                ans += st[i]
        else:
            if st[i] not in error_eng:
                if lang == 'русский':
                    len_alph = 32
                    letters_upper = rus_upper
                    letters_small = rus_lower
                elif lang == 'английский':
                    len_alph = 26
                    letters_upper = eng_upper
                    letters_small = eng_lower

                if st[i] == st[i].upper():
                    ind = letters_upper.find(st[i])
                    new_ind = (ind + step_shift) % len_alph
                    new_letter = letters_upper[new_ind]
                else:
                    ind = letters_small.find(st[i])
                    new_ind = (ind + step_shift) % len_alph
                    new_letter = letters_small[new_ind]
                ans += new_letter
            else:
                ans += st[i]
    for q in tab:
        ans = ans.replace(q, '\n\n')

    return ans

def decode(st, step_shift, lang):
    tab = [chr(i) + chr(i) for i in range(ord('А'), ord('Я') + 1)]
    tab_eng = [chr(i) + chr(i) for i in range(ord('A'), ord('Z') + 1)]
    tab.extend(tab_eng)
    ans = ''
    for j in range(len(st)):
        if lang == 'русский':
            if st[j] not in error_rus:
                if lang == 'русский':
                    len_alph = 32
                    letters_upper = rus_upper
                    letters_small = rus_lower
                else:
                    len_alph = 26
                    letters_upper = eng_upper
                    letters_small = eng_lower

                if st[j] == st[j].upper():
                    ind = letters_upper.find(st[j])
                    old_ind = (ind - step_shift) % len_alph
                    old_letter = letters_upper[old_ind]
                else:
                    ind = letters_small.find(st[j])
                    old_ind = (ind - step_shift) % len_alph
                    old_letter = letters_small[old_ind]
                ans += old_letter
            else:
                ans += st[j]
        else:
            if st[j] not in error_eng:
                if lang == 'русский':
                    len_alph = 32
                    letters_upper = rus_upper
                    letters_small = rus_lower
                else:
                    len_alph = 26
                    letters_upper = eng_upper
                    letters_small = eng_lower

                if st[j] == st[j].upper():
                    ind = letters_upper.find(st[j])
                    old_ind = (ind - step_shift) % len_alph
                    old_letter = letters_upper[old_ind]
                else:
                    ind = letters_small.find(st[j])
                    old_ind = (ind - step_shift) % len_alph
                    old_letter = letters_small[old_ind]
                ans += old_letter
            else:
                ans += st[j]
    for q in tab:
        ans = ans.replace(q, '\n\n')
    return ans

global database
database = {}

# код для реагирования на команду /start
@bot.message_handler(commands=['start'])
def welcome(message):
    database[message.from_user.id] = ['', '', 0, '', 0]
    #print(database)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFhOFi849cOCPSM7fda6clEeHhqkml7gACUCoAAnG2WEj3hSO3VXNO-CkE')
    bot.send_message(message.chat.id,
                     'Добро пожаловать, {0.first_name}!\nЯ - <b>Билл Шифр</b>, бот созданный для того, чтобы \n'
                     '[шифровать/дешифровать] сообщения посредством шифра Цезаря.'.format(message.from_user,
                                                                                          bot.get_me()),
                     parse_mode='html')
    msg = bot.send_message(message.chat.id, 'Нажмите команду ', reply_markup=markup_start)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Рекомендации к написанию сообщения для [кодирования/декодирования]: \n'
                                      '1. Постарайтесь НЕ писать римские цифры в своём сообщении, потому что они будут восприняты ботом как английские буквы!!! Их вы можете заменить на арабские \n'
                                      '2. Избегайте использования спец символов, потому что они могут повлиять на зашифрованный текст! \n'
                                      '3. Не отправляйте боту смайлики, потому что он не сможет их закодировать (это не текст) \n'
                                      '4. Если чат-боту отправить стикер взамен вы получите рандомный стикер \n'
                                      '5. Если язык вашего сообщения не будет соответствовать тому, который вы выбрали, бот оставит сообщение не зашифровав его! \n'
                                      '6. Если остались какие-то вопросы вы можете обратиться к автору проекта (@Bogdanatrosenko)😀', reply_markup=markup_start)

# функция реагирования на стикеры
@bot.message_handler(content_types=['sticker'])
def duck(message):
    stick = choice(List)
    bot.send_sticker(message.chat.id, stick)

# обработчик сообщений
@bot.message_handler(content_types=['text'])
def main_programm(message):
    fl = False
    msg = message.text
    try:
        if isinstance(msg, str):
            if message.text == 'Начать работу':
                database[message.from_user.id] = ['', '', 0, '', 0]
                #print(database)
                bot.send_message(message.chat.id, 'Что вы хотите сделать?', reply_markup=markup_action)

            elif message.text.lower() == '🔒 шифpoвание':
                database[message.from_user.id][0] = 'ш'
                database[message.from_user.id][4] = 0
                #print(database)
                bot.send_message(message.chat.id, 'Пожалуйста выберите язык шифруемого сообщения',
                                 reply_markup=markup_language)

            elif message.text.lower() == '🔑 дешифpoвание':
                database[message.from_user.id][0] = 'д'
                database[message.from_user.id][4] = 0
                #print(database)
                bot.send_message(message.chat.id, 'Пожалуйста выберите язык шифруемого сообщения',
                                 reply_markup=markup_language)

            elif message.text == '🇬🇧 Английский' and database[message.from_user.id][0] in ['ш', 'д']:

                database[message.from_user.id][1] = 'английский'
                #print(database)
                bot.send_message(message.chat.id, 'Введите ключ шифрования ROT', reply_markup=types.ReplyKeyboardRemove())

            elif message.text == '🇷🇺 Русский (без буквы ё)' and database[message.from_user.id][0] in ['ш', 'д']:
                database[message.from_user.id][1] = 'русский'
                #print(database)
                bot.send_message(message.chat.id, 'Введите ключ шифрования ROT', reply_markup=types.ReplyKeyboardRemove())


            elif database[message.from_user.id][1] == 'русский' and database[message.from_user.id][0] in ['ш', 'д'] and database[message.from_user.id][4] == 0:
                try:
                    step_shift = int(message.text)
                    if 1 <= step_shift <= 32 and step_shift > 0:
                        database[message.from_user.id][2] = step_shift
                        database[message.from_user.id][4] = 1
                        #print(database)
                    else:
                        bot.send_message(message.chat.id, 'Вы должны ввести число в диапазоне от 1 до 32')
                except:
                    bot.send_message(message.chat.id, 'Вы должны ввести число в диапазоне от 1 до 32')

            elif database[message.from_user.id][1] == 'английский' and database[message.from_user.id][0] in ['ш', 'д'] and database[message.from_user.id][4] == 0:
                try:
                    step_shift = int(message.text)
                    if 1 <= step_shift <= 26 and step_shift > 0:
                        database[message.from_user.id][2] = step_shift
                        database[message.from_user.id][4] = 1
                        #print(database)
                    else:
                        bot.send_message(message.chat.id, 'Вы должны ввести число в диапазоне от 1 до 26')
                except:
                    bot.send_message(message.chat.id, 'Вы должны ввести число в диапазоне от 1 до 26')
            else:
                bot.send_message(message.chat.id, 'Я вас не понимаю 😑', reply_markup=markup_start)
                fl = True

            if database[message.from_user.id][1] in ['русский', 'английский'] and database[message.from_user.id][0] in ['ш', 'д'] and database[message.from_user.id][2] != 0 and database[message.from_user.id][4] == 1 and fl != True:
                msg = bot.send_message(message.chat.id, 'Введите строку которую нужно [шифровать/дешифровать]')
                bot.register_next_step_handler(msg, String)
        else:
             bot.send_sticker(message.chat.id, '')
    except:
        bot.send_message(message.chat.id, 'Извените я не понял вашего вопроса 😐', reply_markup=markup_start)

def String(message):
    st = message.text
    if isinstance(st, str):
        database[message.from_user.id][3] = st
        #print(database)

        if database[message.from_user.id][0] == 'ш':
            bot.send_message(message.chat.id, 'Закодированное сообщение:')
            bot.send_message(message.chat.id, encryption(database[message.from_user.id][3], database[message.from_user.id][2], database[message.from_user.id][1]))
            sleep(2)
            msg = bot.send_message(message.chat.id, 'Нажмите команду ', reply_markup=markup_start)
            bot.register_next_step_handler(msg, main_programm)
        elif database[message.from_user.id][0] == 'д':
            bot.send_message(message.chat.id, 'Раскодированное сообщение:')
            bot.send_message(message.chat.id, decode(database[message.from_user.id][3], database[message.from_user.id][2], database[message.from_user.id][1]))
            sleep(2)
            msg = bot.send_message(message.chat.id, 'Нажмите команду ', reply_markup=markup_start)
            bot.register_next_step_handler(msg, main_programm)
    else:
        msg = bot.send_message(message.chat.id, 'Я не могу работать с данными, которые НЕ являются строками!')
        bot.send_message(message.chat.id, 'Попробуйте снова ☺')
        bot.register_next_step_handler(msg, String)

bot.polling(none_stop=True, interval=0)