from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Kanalimiz", url="https://t.me/hayotiy_damlar")],
        [InlineKeyboardButton(
            "ADMIN🖥️", url="https://t.me/SAIDJON_OKENN")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help Qo'shimcha malumot uchun bosing..."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
