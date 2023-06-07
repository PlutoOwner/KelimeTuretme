from pyrogram import Client
from pyrogram import filters
from random import shuffle

from pyrogram.types import Message
from Kelime_bot.helpers.keyboards import *
from Kelime_bot.helpers.kelimeler import kelime_sec
from Kelime_bot import *
from main import *



@Client.on_message(filters.command(["cancel",f"cancel@{USERNAME}"]) & ~filters.private & ~filters.channel & ~filters.edited)
async def stop(c:Client, m:Message):
    global oyun
    
    siralama = []
    for i in oyun[m.chat.id]["oyuncular"]:
        siralama.append(f"{i}   :   {oyun[m.chat.id]['oyuncular'][i]} Bal")
    siralama.sort(reverse=True)
    siralama_text = ""
    for i in siralama:
        siralama_text += i + "\n"     
    
    await c.send_message(m.chat.id, f"**{m.from_user.mention}** Tarafından Oyun Bitirildi\n\nYeni Oyuna Başlamak İçin /game Yaza Bilirsiniz\n\n 📝 Puan Listesi  :\n\n{siralama_text}")
    oyun[m.chat.id] = {}
    
