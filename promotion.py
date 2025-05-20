from config import PROMO_CHANNEL_USERNAME
from db import get_user_data

PROMO_POST_COST = 25  # نجوم

def get_promo_post_text(gift_text, giveaway_id):
    return f"""
🎉 تم إطلاق سحب جديد!

{gift_text}

🆔 رقم السحب: {giveaway_id}

📥 شارك الآن عبر الزر بالأسفل!

روليت G.T
    """
