from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    buttons = [
        [KeyboardButton("🎲 إنشاء سحب جديد")],
        [KeyboardButton("📊 حسابي")],
        [KeyboardButton("📚 كيفية استخدام البوت")],
        [KeyboardButton("💬 تواصل مع الدعم")],
        [KeyboardButton("📨 رابط الإحالة")],
        [KeyboardButton("💎 الاشتراك VIP")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
