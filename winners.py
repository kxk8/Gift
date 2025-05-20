def format_winners_announcement(winners: list[str]):
    text = "🏆 *نتائج السحب:*\n\n"
    for i, username in enumerate(winners, 1):
        text += f"{i}️⃣ {username}\n"
    text += "\n🎉 مبروك للفائزين!"
    return text
