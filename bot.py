import telebot
import random

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

# Словарь для хранения выданных email для каждого пользователя
user_emails = {}

# Функция для выдачи случайного email пользователю
@bot.message_handler(commands=['getmail'])
def get_random_email(message):
    global email_list, user_emails
    user_id = message.from_user.id
    
    # Проверяем, есть ли еще доступные email
    if len(email_list) > 0:
        # Выбираем случайный email из доступных
        email = random.choice(email_list)
        email_list.remove(email)  # Убираем email из общего списка
        user_emails[user_id] = email  # Сохраняем выданный email для этого пользователя
        
        # Отправляем пользователю выданный email
        bot.send_message(message.chat.id, f'Email для вас: `{email}`', parse_mode='MarkDown')
    else:
        # Если все email-адреса уже выданы
        bot.send_message(message.chat.id, 'Извините, все email-адреса уже выданы.', parse_mode='html')

# Пример команды для сброса выданных email для всех пользователей и восстановления списка
@bot.message_handler(commands=['reset_all'])
def reset_all_emails(message):
    global email_list, user_emails

    # Восстанавливаем все email-адреса
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
    user_emails.clear()  # Очищаем список выданных email

    bot.send_message(message.chat.id, 'Все email-адреса сброшены и готовы к новой выдаче.', parse_mode='html')

bot.polling(none_stop=True)