from aiogram.types import User
from aiogram import Bot
from config import ADMIN_ID

async def is_user_subscribed(bot: Bot, user_id: int, channel_username: str) -> bool:
    try:
        member = await bot.get_chat_member(chat_id=channel_username, user_id=user_id)
        return member.status in ["member", "creator", "administrator"]
    except Exception as e:
        await bot.send_message(ADMIN_ID, f"خطأ أثناء التحقق من الاشتراك:\n{str(e)}")
        return False
