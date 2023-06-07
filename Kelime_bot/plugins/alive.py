from pyrogram import Client, filters
from main import OWNER_ID
from pyrogram.types import Message
from random import choice

stck = [
     "CAACAgIAAxkBAAJQI2RWQFyf_F1EZM-N_INCBl10Ad_KAAIKEQACdkdISeyQ96xemmtLLwQ", 
     "CAACAgQAAxkBAAJQH2RWQDr1_bYk_kMHteerS5rCBgeQAALWEAAC1UVxUQTxCxN01re6LwQ", 
     "CAACAgQAAxkBAAJQG2RWQDb3UqFmsVGvILKYpanFfHkWAAK3DQAComhxUV4gG205pRv8LwQ", 
     "CAACAgQAAxkBAAJQF2RWQCvwQWRdMKMDGguMjmnTENl8AAJBDQACqLJ5UbKdAAFNH4osKS8E", 
     "CAACAgQAAxkBAAJQE2RWP-9LUfo32dSoBU1CNcNIZKZmAAIMDAACOD34UBpuMYPsOQtLLwQ", 
     "CAACAgQAAxkBAAJQD2RWP-ki2Agy3ftHTTDE-4L_GrYiAALWCQACLvGpUDjfUroYxKuKLwQ", 
     "CAACAgQAAxkBAAJQC2RWP7-cu8IryBOjKEsYgzF6XBnRAAI0EAACv15wUftkEcaXM_pbLwQ", 
     "CAACAgQAAxkBAAJQB2RWP7WNxfuaCW1HL2HOjzV-kyO_AAL9EAACjN3wU22yWO7J3-zxLwQ", 
     "CAACAgQAAxkBAAJQAmRWP6X2fhzqIzEdhfmN9QJTqRlgAAJaDQACIoxYUPhiOcvN16F4LwQ", 
     "CAACAgQAAxkBAAJQlWRhPn9z5p6XBz95CPtFM3vGsTRNAALoCwACqExxUamwq9-AMmU3LwQ", 
     "CAACAgQAAxkBAAJQmWRhPo8-mNzdqkP60JKYHNDLghesAALoDwACDWlwUYKPa7mY2ZFwLwQ", 
     "CAACAgQAAxkBAAJQnWRhPp1x1yHn4yVnVK2SRciEgp8IAAL5DwACkjd4Uevo4Xj73rBtLwQ"
]


@Client.on_message(filters.command(["botcum", "alive"], [".", "/"]) & filters.user(OWNER_ID))
async def sahip(c: Client, m: Message):
    pluto = choice(stck)
    await m.reply_sticker(pluto)
