import asyncio
from telethon import TelegramClient, events
from telethon.tl.types import InputPeerUser
from telethon.tl.functions.messages import SendMessageRequest, SendMediaRequest
from telethon.tl.types import InputMediaPhoto
import os

# ==== API & Session setup ====
api_id = 26683504          # my.telegram.org থেকে নিন
api_hash = 'a0cd79990f643825df8d436137399d2e'  # my.telegram.org থেকে নিন
phone = '+8801832823749'  # আপনার personal account phone number
session_name = 'session'  # session file

# ==== Forward Settings ====
forward_to_id = 2654127042     # আপনার Telegram ID
source_channel_id = 2596756201 # যেই চ্যানেল থেকে মেসেজ নেবেন

# ==== Client setup ====
client = TelegramClient(session_name, api_id, api_hash)

# 🔹 Prediction/Result মেসেজ ফিল্টার ও ফরওয়ার্ড
@client.on(events.NewMessage(chats=source_channel_id))
async def forward_prediction(event):
    text = event.raw_text.lower() if event.raw_text else ''
    if 'prediction' in text or 'result' in text:
        await client.send_message(forward_to_id, event.message)

# 🔹 প্রতি ১ ঘন্টা পর অটো পোস্ট
async def scheduled_post():
    while True:
        text = "📢 নতুন আপডেট! আমাদের অফিসিয়াল চ্যানেলে যুক্ত হন।। \n\n👉 এই বটটি তৈরি করেছেন 𝐌ᴀsᴛᴇʀ 𝐌ɪɴᴅ 𝐓ᴇᴀᴍ"
        photo_url = "https://i.postimg.cc/nhLMWF76/1759125564374.png"

        # বোতাম সহ মেসেজ
        buttons = [
            [("Registration Link", "https://www.tigroclub.pro/#/register?invitationCode=44128102423"),
             ("𝐌ᴀsᴛᴇʀ 𝐌ɪɴᴅ 𝐓ᴇᴀᴍ", "https://t.me/MASTER_MIND_TEAM")],
            [("Gift Code", "https://t.me/TOMS_HISTORY"),
             ("YOUTUBE", "https://youtube.com/@technical-tom")]
        ]

        keyboard = [[Button.url(text, url) for text, url in row] for row in buttons]

        await client.send_file(
            forward_to_id,
            file=photo_url,
            caption=text,
            buttons=keyboard
        )

        await asyncio.sleep(3600)  # প্রতি ১ ঘন্টা

async def main():
    await client.start(phone)
    print("✅ Personal account bot running 24/7...")
    asyncio.create_task(scheduled_post())
    await client.run_until_disconnected()

if name == "main":
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())
