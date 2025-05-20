import random
from db import get_user_data

def pick_winners(participants: list[int], count: int) -> list[int]:
    if len(participants) <= count:
        return participants
    return random.sample(participants, count)
