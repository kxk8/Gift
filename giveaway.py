from aiogram import types
from loader import dp
from keyboards import main_menu

@dp.message_handler(lambda msg: msg.text == "🎲 إنشاء سحب جديد")
async def create_giveaway(message: types.Message):
    await message.answer("📝 أرسل الآن نص الرسالة التي تريد نشرها في السحب:")

    # نحفظ أن المستخدم داخل مرحلة "إنشاء"
    dp.current_state(user=message.from_user.id).set_state("waiting_for_giveaway_text")

@dp.message_handler(state="waiting_for_giveaway_text")
async def receive_giveaway_text(message: types.Message):
    text = message.text

    # تحقق بسيط إذا بي روابط
    if any(link in text for link in ["http", "https", "t.me"]):
        await message.answer("❌ لا يُسمح بوضع روابط داخل رسالة السحب.")
        return

    # نحفظ النص ونكمل الخطوات (مثال فقط)
    await message.answer("⏰ حدد وقت انتهاء السحب (بالساعات):")
    dp.current_state(user=message.from_user.id).set_state("waiting_for_duration")

@dp.message_handler(state="waiting_for_duration")
async def receive_duration(message: types.Message):
    try:
        hours = int(message.text)
        seconds = hours * 3600
        # نكمل إنشاء السحب - حفظ، توليد ID، نشر لاحقاً...
        await message.answer(f"✅ تم تحديد المدة: {hours} ساعة.\n🎉 جاري حفظ السحب.")
    except ValueError:
        await message.answer("❌ الرجاء كتابة رقم صحيح لعدد الساعات.")
