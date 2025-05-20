from aiogram import types
from loader import dp
from keyboards import main_menu

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer(
        "🎉 أهلاً بك في بوت الروليت!\n\nاختر من القائمة:",
        reply_markup=main_menu()
    )
