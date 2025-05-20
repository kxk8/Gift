from db import get_user_data, set_user_data

PREMIUM_FEATURES_COST = 10
TON_PRICE_USD = 0.2

def unlock_features_for_one_draw(user_id):
    data = get_user_data(user_id)
    data["unlocked_once"] = True
    set_user_data(user_id, data)

def is_features_unlocked(user_id):
    data = get_user_data(user_id)
    return data.get("vip", False) or data.get("unlocked_once", False)

def clear_one_time_unlock(user_id):
    data = get_user_data(user_id)
    if "unlocked_once" in data:
        del data["unlocked_once"]
        set_user_data(user_id, data)
