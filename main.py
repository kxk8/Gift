from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# نقطة انطلاق البوت
@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("🎉 أهلاً بك في بوت الروليت!")

if __name__ == "__main__":
    from handlers import start, giveaway
    from services import ton_payment, telegram_stars
    executor.start_polling(dp, skip_updates=True)
