import asyncio
from telethon import TelegramClient

# আপনার personal account এর তথ্য
api_id = 26683504               # my.telegram.org থেকে
api_hash = 'a0cd79990f643825df8d436137399d2e'    # my.telegram.org থেকে
phone = '+8801832823749'      # আপনার ফোন নম্বর
session_name = 'session'      # session ফাইলের নাম

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.start(phone)
    print("✅ Logged in successfully! Session file created.")
    await client.disconnect()

# Required for running in notebooks or async environments
import nest_asyncio
nest_asyncio.apply()

asyncio.run(main())
