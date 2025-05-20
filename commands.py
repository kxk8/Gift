from aiogram import types
from loader import dp

@dp.message_handler(lambda msg: msg.text == "📨 رابط الإحالة")
async def referral_link(message: types.Message):
    bot_username = (await dp.bot.get_me()).username
    ref_link = f"https://t.me/{bot_username}?start=ref{message.from_user.id}"
    await message.answer(f"✅ هذا رابط الإحالة الخاص بك:\n{ref_link}\n\nكل شخص يسجل عبرك، تربح 20% من مشترياته لمدة 4 أشهر.")
