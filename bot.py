import telebot
import random
import os

bot = telebot.TeleBot('7934382999:AAF7tHgUfTaLHEhUxnSohqo_etpLSHso4S8')

# Массив с email-адресами
email_list = [
     'lida.savchenko.93@mail.ru:fq5VGS)q87VUB:Лидия:Савченко',
    'Shevchenkoenhx1982-oy@mail.ru:58QJVumaWY$H:Вера:Шевченко',
    'inna.sabirova.99@mail.ru:)0CfWMO$xgeLy:Инна:Сабирова',
    'ViktoriiaShakirovabafv@mail.ru:Oyq)4UBMb11p(:Виктория:Шакирова',
    'LiubovVlasovashah@mail.ru:BSYM5L_)v)p)j:Любовь:Власова',
    'Medvedevatflg.n.u@mail.ru:dos7MlUDi(B4z:Ольга:Медведева',
    'Tarasovagmns1992.ul@mail.ru:GMe!rJoiXc0tw:Тамара:Тарасова',
    'Mariiasgpdwi@mail.ru:Aq$A(1KZZ1g5:Мария:Карпенко',
    'Fadeevawojc.q-x@mail.ru:VDk0evUdaK)LJ:Ольга:Фадеева',
    'ViktoriiaRomanovaftix@mail.ru:VWi4_U45hrz1u:Виктория:Романова',
    'NinaZhuravlevaxarg@mail.ru:FXE_)ted_P0I:Нина:Журавлева',
    'Savchenko43.i@mail.ru:eRA699j)GzDBu:Валерия:Савченко',
    'Liudmiladdxjth@bk.ru:S4hO0Ac$cdf7:Людмила:Лаптева',
    'Marinaqacljz@list.ru:cVunbL)yc$2O:Марина:Лифанова',
]

# Функция для выдачи случайного email пользователю и отправки текстового файла
@bot.message_handler(commands=['getmail'])
def get_random_email(message):
    global email_list
    user_id = message.from_user.id

    if len(email_list) > 0:
        # Выбираем случайный email из списка
        email = random.choice(email_list)
        email_list.remove(email)

        # Создаем временный файл с email
        file_name = f'{user_id}_email.txt'
        with open(file_name, 'w') as file:
            file.write(f'Ваш email: {email}')

        # Отправляем файл пользователю
        with open(file_name, 'rb') as file:
            bot.send_document(message.chat.id, file)

        # Удаляем файл после отправки (по желанию)
        os.remove(file_name)
    else:
        bot.send_message(message.chat.id, 'Извините, все email-адреса уже выданы.', parse_mode='html')

# Обработчик команды /start и создание кнопок
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_main = telebot.types.KeyboardButton('Отримати e-mail')
    markup.row(btn_main)
    bot.send_message(message.chat.id, 'Привет! Нажми на кнопку, чтобы получить e-mail.', reply_markup=markup)

# Обработчик нажатий на кнопки
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == 'Отримати e-mail':
        get_random_email(message)

bot.polling(none_stop=True)
