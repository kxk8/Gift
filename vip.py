from db import get_user_data, set_user_data

VIP_COST_STARS = 40
VIP_COST_TON_USD = 0.8

def is_vip(user_id):
    data = get_user_data(user_id)
    return data.get("vip", False)

def activate_vip(user_id):
    data = get_user_data(user_id)
    data["vip"] = True
    data["vip_sweeps_left"] = 5  # عدد السحوبات التي يشملها الاشتراك
    set_user_data(user_id, data)

def use_vip_sweep(user_id):
    data = get_user_data(user_id)
    if data.get("vip_sweeps_left", 0) > 0:
        data["vip_sweeps_left"] -= 1
        set_user_data(user_id, data)
        return True
    return False
