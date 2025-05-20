from db import get_user_data, set_user_data

def register_referral(new_user_id, referrer_id):
    if new_user_id == referrer_id:
        return False
    data = get_user_data(new_user_id)
    if "ref_by" not in data:
        data["ref_by"] = referrer_id
        set_user_data(new_user_id, data)
        return True
    return False

def add_referral_earnings(user_id, amount):
    data = get_user_data(user_id)
    data["ref_earned"] = data.get("ref_earned", 0) + amount
    data["ref_count"] = data.get("ref_count", 0) + 1
    set_user_data(user_id, data)
