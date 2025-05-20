from config import TON_WALLET_ADDRESS
import math

def get_ton_payment_link(amount_ton: float, comment: str = "payment"):
    # توليد رابط Tonkeeper للدفع
    return f"https://tonkeeper.com/transfer/{TON_WALLET_ADDRESS}?amount={amount_ton}&text={comment}"

def calculate_ton_amount(usd_price: float, ton_usd_rate: float) -> float:
    # حساب السعر بوحدة TON مع تقريب لأعلى رقم عشري
    raw = usd_price / ton_usd_rate
    return round(raw + 0.00001, 6)
