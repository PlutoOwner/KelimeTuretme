import asyncio
import time
from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from main import oyun, USERNAME
from Kelime_bot.helpers.kelimeler import *
from Kelime_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message



# Oyunu başlat. 
@Client.on_message(filters.command(["game",f"game@{USERNAME}"]) & ~filters.private & ~filters.channel & ~filters.edited)
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**❗ Oyun Zaten Grubunuzda Devam Ediyor ✍🏻 \n Oyunu durdurmak için yazıp /cancel durdurabilirsiniz")
    else:
        await m.reply(f"**{m.from_user.mention}** [`{m.from_user.id}`] Tarafından! \nKelime Bulma Oyunu Başladı .\n\nİyi Şanslar !", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["pass"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/60 
📝 Söz :   <code>{kelime_list}</code>
💰 Kazandığınız Puan: 1
🔎 İpucu: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluk : {int(len(kelime_list)/2)} 

✏️ Karışık harflerden doğru kelimeyi bulun
        """
        await c.send_message(m.chat.id, text)

        await asyncio.sleep(600)

        if oyun[m.chat.id]['aktif']:
            await c.send_message(m.chat.id, f"❗️ Oyun Durduruldu\n\nSebep: `Uzun süredir kimse cevap vermedi.`\nDoğru Kelime : `{oyun[m.chat.id]['kelime']}` idi")
            oyun[m.chat.id] = {}






            
