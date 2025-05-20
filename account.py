from aiogram import types
from loader import dp
from db import get_user_data

@dp.message_handler(lambda msg: msg.text == "📊 حسابي")
async def my_account(message: types.Message):
    data = get_user_data(message.from_user.id)
    stars = data.get("stars", 0)
    ref_earned = data.get("ref_earned", 0)
    ref_count = data.get("ref_count", 0)
    vip = "✅ مفعل" if data.get("vip") else "❌ غير مفعل"
    sweeps = data.get("vip_sweeps_left", 0) if data.get("vip") else "-"

    await message.answer(
        f"""📊 *كشف حسابك:*
        
⭐️ النجوم: {stars}
💎 اشتراك VIP: {vip}
🎲 سحوبات VIP المتبقية: {sweeps}

📨 عدد الإحالات: {ref_count}
💰 ربحك من الإحالات: {ref_earned} نجمة
""", parse_mode="Markdown"
    )
