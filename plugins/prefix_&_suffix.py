# Don't Remove Credit 😔
# Telegram Channel @TonyStark_Botz & @MovieTimesTV
# Developer @Tony_Stark_75
# Update Channel @TonyStark_Botz & @TonyStarkBotzXSupport

from pyrogram import Client, filters, enums
from helper.database import db

# prefix commond ✨
@Client.on_message(filters.private & filters.command('set_prefix'))
async def add_prefix(client, message):
    if len(message.command) == 1:
        return await message.reply_text("**__Give The Prefix__\n\nExᴀᴍᴩʟᴇ:- `/set_prefix @MovieTimesTV`**")
    prefix = message.text.split(" ", 1)[1]
    tonyDev = await message.reply_text("Please Wait ...", reply_to_message_id=message.id)
    await db.set_prefix(message.from_user.id, prefix)
    await tonyDev.edit("__**✅ ᴘʀᴇꜰɪx ꜱᴀᴠᴇᴅ**__")

@Client.on_message(filters.private & filters.command('del_prefix'))
async def delete_prefix(client, message):
    tonyDev = await message.reply_text("Please Wait ...", reply_to_message_id=message.id)
    prefix = await db.get_prefix(message.from_user.id)
    if not prefix:
        return await tonyDev.edit("__**😔 ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ᴘʀᴇꜰɪx**__")
    await db.set_prefix(message.from_user.id, None)
    await tonyDev.edit("__**❌️ ᴘʀᴇꜰɪx ᴅᴇʟᴇᴛᴇᴅ**__")

@Client.on_message(filters.private & filters.command('see_prefix'))
async def see_prefix(client, message):
    tonyDev = await message.reply_text("Please Wait ...", reply_to_message_id=message.id)
    prefix = await db.get_prefix(message.from_user.id)
    if prefix:
        await tonyDev.edit(f"**ʏᴏᴜʀ ᴘʀᴇꜰɪx:-**\n\n`{prefix}`")
    else:
        await tonyDev.edit("__**😔 ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ᴘʀᴇꜰɪx**__")

# SUFFIX COMMOND ✨
@Client.on_message(filters.private & filters.command('set_suffix'))
async def add_suffix(client, message):
    if len(message.command) == 1:
        return await message.reply_text("**__Give The Suffix__\n\nExᴀᴍᴩʟᴇ:- `/set_suffix @MovieTimesTV`**")
    suffix = message.text.split(" ", 1)[1]
    tonyDev = await message.reply_text("Please Wait ...", reply_to_message_id=message.id)
    await db.set_suffix(message.from_user.id, suffix)
    await tonyDev.edit("__**✅ ꜱᴜꜰꜰɪx ꜱᴀᴠᴇᴅ**__")

@Client.on_message(filters.private & filters.command('del_suffix'))
async def delete_suffix(client, message):
    tonyDev = await message.reply_text("Please Wait ...", reply_to_message_id=message.id)
    suffix = await db.get_suffix(message.from_user.id)
    if not suffix:
        return await tonyDev.edit("__**😔 ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ꜱᴜꜰꜰɪx**__")
    await db.set_suffix(message.from_user.id, None)
    await tonyDev.edit("__**❌️ ꜱᴜꜰꜰɪx ᴅᴇʟᴇᴛᴇᴅ**__")

@Client.on_message(filters.private & filters.command('see_suffix'))
async def see_suffix(client, message):
    tonyDev = await message.reply_text("Please Wait ...", reply_to_message_id=message.id)
    suffix = await db.get_suffix(message.from_user.id)
    if suffix:
        await tonyDev.edit(f"**ʏᴏᴜʀ ꜱᴜꜰꜰɪx:-**\n\n`{suffix}`")
    else:
        await tonyDev.edit("__**😔 ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ꜱᴜꜰꜰɪx**__")

# Don't Remove Credit 😔
# Telegram Channel @TonyStark_Botz & @MovieTimesTV
# Developer @Tony_Stark_75
# Update Channel @TonyStark_Botz & @TonyStarkBotzXSupport
