from main import oyun, rating, OWNER_ID
from pyrogram import Client, filters


@Client.on_message(filters.command("data") & filters.user("OWNER_ID")) 
async def data(c:Client, m):
    await m.reply(oyun)
    await m.reply(rating)
