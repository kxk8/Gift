from aiogram import Bot
from db import get_user_data, set_user_data

async def handle_user_left(bot: Bot, user_id: int, left_channel: str):
    data = get_user_data(user_id)
    joined_channels = data.get("joined_channels", [])

    if left_channel in joined_channels:
        joined_channels.remove(left_channel)
        data["joined_channels"] = joined_channels
        data["removed_from_draw"] = True
        set_user_data(user_id, data)

        await bot.send_message(
            user_id,
            f"🚫 تم إقصاؤك من السحب لأنك غادرت القناة: @{left_channel}\n📩 انضم من جديد لإعادة تسجيلك.",
            reply_markup=types.InlineKeyboardMarkup().add(
                types.InlineKeyboardButton("🔁 الانضمام مجددًا", url=f"https://t.me/{left_channel}")
            )
        )
