from pyrogram import Client, filters
from pyrogram.types import Message
from main import USERNAME, OWNER_ID
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton



keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕ Grubuna Ekle", url=f"http://t.me/{USERNAME}?startgroup=new")
    ],
    [
        InlineKeyboardButton(
            "👤 Owner", user_id=OWNER_ID
        )
    ]
])


help_keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("📚 Komutlar", url=f"http://t.me/{USERNAME}?start=help")
    ]

START = """
• **Merhaba** 📖\n\n• **Ben Bir Oyun Botuyum** 🎮 \n\n• **Çeşitli oyunlar oynamak ve eğlenceli vakit geçirmek için benimle oynayabilirsin** ✍🏻 \n\n• **Benimle oynamak için beni bir gruba ekle** . 💭
➤ Bilgi için 👉 /help Tıklayın. Komutlar kolay ve basittir. 
"""

HELP = """
**✌️ Komutlar Menüsüne Hoşgeldiniz.**
/game - Oyunu başlatmak için..
/pass - Üç adet hakkınız mevcut, oyunu geçmek için.. 
/skor - Oyuncular arasındaki rekabet bilgisi..
/cancel - Oyundan çıkmak için gerekli olan komuttur.. 
"""

   
    
# Komutlar. 
@Client.on_message(filters.command("start") & filters.private)
async def start(bot, message):
  await message.reply_photo("https://graph.org/file/446537c2190e1befc39a4.jpg",caption=START,reply_markup=keyboard)

@Client.on_message(filters.command("help") & filters.private)
async def help(bot, message):
  await message.reply_photo("https://graph.org/file/446537c2190e1befc39a4.jpg",caption=HELP) 

