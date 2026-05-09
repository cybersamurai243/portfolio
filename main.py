import telebot
from telebot import types
import time
import re

TOKEN = ""
ADMIN_ID = 123456789
bot = telebot.TeleBot(TOKEN)

users_db = {}

CATALOG = {
    "JACKETS": {
        "ACRONYM J1A-GT": {"price": 42000, "stock": 2, "desc": "Gore-Tex Pro Generation 2.2."},
        "STONE ISLAND GHOST": {"price": 28500, "stock": 5, "desc": "Mono-colour stretch wool canvas."}
    },
    "HOODIES": {
        "OFF-WHITE LOGO": {"price": 12500, "stock": 10, "desc": "Slim fit, diagonal spray stripes."},
        "ESSENTIALS FOG": {"price": 4800, "stock": 25, "desc": "Oversized fit, heavy fleece."}
    },
    "PANTS": {
        "NIKE ACG CARGO": {"price": 6200, "stock": 12, "desc": "Water-repellent fabric."}
    },
    "FOOTWEAR": {
        "JORDAN 1 RETRO": {"price": 18500, "stock": 5, "desc": "High OG Chicago Reimagined."}
    },
    "ACCESSORIES": {
        "SUPREME BACKPACK": {"price": 5400, "stock": 10, "desc": "Cordura fabric."}
    }
}

def get_user_data(uid):
    if uid not in users_db:
        users_db[uid] = {
            'cart': {},
            'balance': 500,
            'orders': [],
            'promo_used': False,
            'name': '',
            'phone': '',
            'address': ''
        }
    return users_db[uid]

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("BROWSE CATALOG", "VIEW CART")
    markup.add("MY PROFILE", "ORDER HISTORY")
    markup.add("SUPPORT & INFO", "APPLY PROMO CODE")
    return markup

@bot.message_handler(commands=['start'])
def welcome(message):
    uid = message.from_user.id
    get_user_data(uid)
    bot.send_message(message.chat.id, "AETHER STORE // TERMINAL ONLINE", reply_markup=main_menu())

@bot.message_handler(func=lambda m: m.text == "BROWSE CATALOG")
def show_categories(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for cat in CATALOG.keys():
        markup.add(types.InlineKeyboardButton(cat, callback_data=f"cat_{cat}"))
    bot.send_message(message.chat.id, "SELECT SECTOR:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("cat_"))
def show_items(call):
    cat_name = call.data.split("_")[1]
    items = CATALOG[cat_name]
    for name, data in items.items():
        text = f"ITEM: {name}\nPRICE: {data['price']} UAH\nSPEC: {data['desc']}"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("ADD TO CARGO", callback_data=f"buy_{name}"))
        bot.send_message(call.message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("buy_"))
def handle_buy(call):
    uid = call.from_user.id
    item_name = call.data.split("_")[1]
    user = get_user_data(uid)
    user['cart'][item_name] = user['cart'].get(item_name, 0) + 1
    bot.answer_callback_query(call.id, text="LOGGED")

@bot.message_handler(func=lambda m: m.text == "VIEW CART")
def cart_view(message):
    uid = message.from_user.id
    user = get_user_data(uid)
    if not user['cart']:
        bot.send_message(message.chat.id, "CART IS EMPTY.")
        return
    total = 0
    res = "CARGO STATUS:\n\n"
    for item, qty in user['cart'].items():
        price = 0
        for cat in CATALOG.values():
            if item in cat: price = cat[item]['price']
        total += price * qty
        res += f"- {item} x{qty}\n"
    res += f"\nTOTAL: {total} UAH"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("CONFIRM TRANSACTION", callback_data="checkout_start"))
    bot.send_message(message.chat.id, res, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "checkout_start")
def start_checkout(call):
    bot.answer_callback_query(call.id)
    msg = bot.send_message(call.message.chat.id, "INPUT RECIPIENT NAME (LETTERS ONLY):")
    bot.register_next_step_handler(msg, process_name)

def process_name(message):
    uid = message.from_user.id
    name = message.text
    if not re.match(r"^[A-Za-zА-Яа-яіієєґґ' ]+$", name) or len(name) < 2:
        msg = bot.send_message(message.chat.id, "❌ INVALID NAME. USE LETTERS ONLY (MIN 2):")
        bot.register_next_step_handler(msg, process_name)
        return
    users_db[uid]['name'] = name
    msg = bot.send_message(message.chat.id, "INPUT CONTACT PHONE (DIGITS ONLY):")
    bot.register_next_step_handler(msg, process_phone)

def process_phone(message):
    uid = message.from_user.id
    phone = message.text
    if not phone.isdigit() or not (10 <= len(phone) <= 13):
        msg = bot.send_message(message.chat.id, "❌ INVALID PHONE. USE DIGITS ONLY (10-12 SYMBOLS):")
        bot.register_next_step_handler(msg, process_phone)
        return
    users_db[uid]['phone'] = phone
    msg = bot.send_message(message.chat.id, "INPUT DELIVERY COORDS (CITY, BRANCH #):")
    bot.register_next_step_handler(msg, process_final)

def process_final(message):
    uid = message.from_user.id
    user = users_db[uid]
    user['address'] = message.text
    order_id = int(time.time() % 100000)
    items_str = "\n".join([f"- {k} (x{v})" for k, v in user['cart'].items()])
    summary = (f"ORDER #{order_id}\nCLIENT: {user['name']}\n"
               f"TEL: {user['phone']}\nADDR: {user['address']}\nITEMS:\n{items_str}")
    bot.send_message(ADMIN_ID, f"⚠️ NEW INCOMING:\n\n{summary}")
    thanks = (
        f"✅ TRANSACTION COMPLETED, {user['name'].upper()}!\n\n"
        f"ORDER ID: #{order_id}\n"
        "--------------------------\n"
        "THANK YOU FOR CHOOSING AETHER STORE.\n"
        "OUR OPERATOR WILL VERIFY YOUR DATA AND SEND A TRACKING CODE SHORTLY.\n"
        "--------------------------\n"
        "SYSTEM STATUS: ORDER_ARCHIVED"
    )
    bot.send_message(message.chat.id, thanks, reply_markup=main_menu())
    user['cart'] = {}

if __name__ == "__main__":
    bot.infinity_polling()
