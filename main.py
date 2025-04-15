from keep_alive import keep_alive
import telebot
from telebot import types

keep_alive()

BOT_TOKEN = "1234567890:AAEvCFjiF5FbJBf7ekXsjRtzC5oUEh8O9kI"
bot = telebot.TeleBot(BOT_TOKEN)

users_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("إنشاء صفقة", callback_data="create_deal")
    markup.add(btn1)
    bot.send_message(chat_id, "مرحبًا بك في بوت GiftsFlow!\nاختر من الأزرار:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "create_deal":
        chat_id = call.message.chat.id
        users_data[chat_id] = {"step": "waiting_for_buyer"}
        bot.send_message(chat_id, "أرسل الآن معرف المشتري (مثل: @username):")

@bot.message_handler(func=lambda m: True)
def handle_messages(message):
    chat_id = message.chat.id
    if chat_id in users_data:
        step = users_data[chat_id].get("step")
        
        if step == "waiting_for_buyer":
            users_data[chat_id]["buyer"] = message.text
            users_data[chat_id]["step"] = "waiting_for_amount"
            bot.send_message(chat_id, "أرسل الآن المبلغ الذي سيدفعه المشتري (بعملة TON):")
        
        elif step == "waiting_for_amount":
            users_data[chat_id]["amount"] = message.text
            users_data[chat_id]["step"] = "done"
            
            buyer = users_data[chat_id]["buyer"]
            amount = users_data[chat_id]["amount"]
            bot.send_message(chat_id, f"تم إنشاء الصفقة:\nالمشتري: {buyer}\nالمبلغ: {amount} TON")
            del users_data[chat_id]

bot.polling()
