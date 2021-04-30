from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Hozirda bu bot faqat Youtubeni qo'llab-quvvatlaydi✅ Faqat Youtube Url-ni yuboring......"
    await message.reply_text(helptxt)
