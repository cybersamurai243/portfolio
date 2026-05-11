import telebot
from telebot import types

TOKEN = "8613542111:AAGP1x5-VldTPuWkKp6RktmKmT9F1WKkxxg"
bot = telebot.TeleBot(TOKEN)

# --- ГОЛОВНЕ МЕНЮ ---
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Турніри")
    btn2 = types.KeyboardButton("Девайси")
    btn3 = types.KeyboardButton("Бронювання")
    btn4 = types.KeyboardButton("Вільні місця")
    btn5 = types.KeyboardButton("Закуски")
    btn6 = types.KeyboardButton("Акції")
    btn7 = types.KeyboardButton("Розіграші")
    btn8 = types.KeyboardButton("Відгуки")
    btn9 = types.KeyboardButton("Локації")

    markup.add(btn1, btn2, btn3)
    markup.add(btn4, btn5)
    markup.add(btn6, btn7)
    markup.add(btn8, btn9)

    return markup


# --- КНОПКА НАЗАД ---
def back_button():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Назад")
    markup.add(btn)
    return markup


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Головне меню:",
        reply_markup=main_menu()
    )


@bot.message_handler(func=lambda message: True)
def handle(message):

    # --- ТУРНІРИ ---
    if message.text == "Турніри":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("CS2")
        btn2 = types.KeyboardButton("Dota 2")
        btn3 = types.KeyboardButton("Valorant")
        btn_back = types.KeyboardButton("Назад")

        markup.add(btn1, btn2, btn3, btn_back)

        bot.send_message(message.chat.id, "Оберіть гру:", reply_markup=markup)

    elif message.text =="CS2":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("CS2 Турнір 2x2")
        btn2 = types.KeyboardButton("CS2 Турнір 5x5")
        btn_back = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn_back)
        bot.send_message(
        message.chat.id,
        "Доступні турніри CS2:",
        reply_markup=markup
    )
    elif message.text =="Dota 2":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Dota 2 Турнір 1x1")
        btn2 = types.KeyboardButton("Dota 2 Турнір 5x5")
        btn_back = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn_back)
        bot.send_message(
        message.chat.id,
        "Доступні турніри Dota 2:",
        reply_markup=markup
    )
    elif message.text =="Valorant":
        bot.send_message(
        message.chat.id,
        "Тут будуть доступні турніри по Valorant : ",
    )
    elif message.text =="CS2 Турнір 2x2":
        bot.send_message(
        message.chat.id,
        "CS2 Турнір 2x2\n\n"
        "Формат : 2x2  \n"
        "Вартість : 200грн\n"
        "Ранг : Беркут\n"
        "Контакти : @admin\n"
    )
    elif message.text =="CS2 Турнір 5x5":
        bot.send_message(
        message.chat.id,
        "CS2 Турнір 5x5\n\n"
        "Формат : 5x5  \n"
        "Вартість : 500грн\n"
        "Ранг : Супрім\n"
        "Контакти : @admin\n"
    )
    elif message.text =="Dota 2 Турнір 1x1":
        bot.send_message(
        message.chat.id,
        "Dota 2 Турнір 1x1\n\n"
        "Формат : 1x1  \n"
        "Вартість : 100грн\n"
        "Ранг : Лицар\n"
        "Контакти : @admin\n"
    )
    elif message.text =="Dota 2 Турнір 5x5":
        bot.send_message(
        message.chat.id,
        "Dota 2 Турнір 5x5\n\n"
        "Формат : 5x5  \n"
        "Вартість : 1000грн\n"
        "Ранг : ~5000mmr\n"
        "Контакти : @admin\n"
    )  
    # --- ДЕВАЙСИ ---
    elif message.text == "Девайси":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Classic ПК")
        btn2 = types.KeyboardButton("VIP ПК")
        btn3 = types.KeyboardButton("VIP+ ПК")
        btn_back = types.KeyboardButton("Назад")

        markup.add(btn1, btn2, btn3, btn_back)

        bot.send_message(message.chat.id, "Оберіть клас пристрою:", reply_markup=markup)

    elif message.text =="Classic ПК":
        bot.send_message(message.chat.id, "Classic зона:\n"
        "ПК: i5, GTX 1660\n"
        "Монітор: 144Hz\n"
        "Мишка: g102\n"
        "Клавіатура: мембранна")
    elif message.text =="VIP ПК":
        bot.send_message(message.chat.id, "VIP зона:\n"
        "ПК: i7, GTX 3060\n"
        "Монітор: 240Hz\n"
        "Мишка: g502\n"
        "Клавіатура: механічна")
    elif message.text =="VIP+ ПК":
        bot.send_message(message.chat.id, "VIP+ зона:\n"
        "ПК: i9, GTX 5090\n"
        "Монітор: 360Hz\n"
        "Мишка: G pro x superlight\n"
        "Клавіатура: магнітна")
    # --- ІНШІ КНОПКИ (поки заглушки) ---
    elif message.text == "Бронювання":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Classic зона")
        btn2 = types.KeyboardButton("VIP зона")
        btn3 = types.KeyboardButton("VIP+ зона")
        btn_back = types.KeyboardButton("Назад")

        markup.add(btn1, btn2, btn3, btn_back)
        bot.send_message(message.chat.id, "Оберіть зону",reply_markup=markup)

    elif message.text in ["Classic зона", "VIP зона", "VIP+ зона"]:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("13:00")
        btn2 = types.KeyboardButton("14:30")
        btn3 = types.KeyboardButton("16:00")
        btn_back = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, btn_back)
        bot.send_message(message.chat.id, f"Ви обрали{message.text}.Оберіть час:",reply_markup=markup)        
    elif message.text in ["13:00", "14:30", "16:00"]:
        bot.send_message(message.chat.id, f"Бронювання на {message.text}.Підтвердженно:",reply_markup=main_menu())
    elif message.text == "Вільні місця":
        bot.send_message(message.chat.id, "Тут буде інформація про вільні місця")

    elif message.text == "Закуски":
        bot.send_message(message.chat.id, "Тут буде меню їжі")

    elif message.text == "Акції":
        bot.send_message(message.chat.id, "Тут будуть акції")

    elif message.text == "Розіграші":
        bot.send_message(message.chat.id, "Тут будуть розіграші")

    elif message.text == "Відгуки":
        bot.send_message(message.chat.id, "Тут буде перехід на Google Maps")

    elif message.text == "Локації":
        bot.send_message(message.chat.id, "Тут буде карта")

    # --- НАЗАД ---
    elif message.text == "Назад":
        bot.send_message(
            message.chat.id,
            "Головне меню",
            reply_markup=main_menu()
        )
def get_time(message):
    bot.send_message(
        message.chat.id,
        f"Бронювання на {message.text} підтверджено",
        reply_markup=main_menu()
    )

bot.infinity_polling()
