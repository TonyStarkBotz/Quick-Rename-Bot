import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # TonyStarkBotz client config
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

    # premium account string session required 😢 
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    
    # database config
    DB_NAME = os.environ.get("DB_NAME","Quick_Rename_Bot")     
    DB_URL = os.environ.get("DB_URL","")
 
    # other configs
    PIC = os.environ.get("PIC", "https://graph.org/file/31c39410431e41677f742.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-100"))

    #force subs
    try:
        FORCE_SUB = int(os.environ.get("FORCE_SUB", "")) 
    except:
        FORCE_SUB = os.environ.get("FORCE_SUB", "xmenmt01")
        
    # wes response configuration     
    PORT = int(os.environ.get("PORT", "8080"))
    BOT_UPTIME = time.time()

class tony(object):
    # part of text configuration
    START_TXT = """<b>Ｈ𝙰𝙸, {}👋

𝚃ʜɪs 𝙸s 𝙰ɴ 𝙰ᴅᴠᴀᴄᴇᴅ 𝙰ɴᴅ 𝚈ᴇᴛ 𝙿ᴏᴡᴇʀғᴜʟ 𝚁ᴇɴᴀᴍᴇ 𝙱ᴏᴛ
𝚄sɪɴɢ 𝚃ʜɪs 𝙱ᴏᴛ 𝚈ᴏᴜ 𝙲ᴀɴ 𝚁ᴇɴᴀᴍᴇ & 𝙲ʜᴀɴɢᴇ 𝚃ʜᴜᴍʙɴᴀɪʟ 𝙾ғ 𝚈ᴏᴜʀ 𝙵ɪʟᴇ 
𝚈ᴏᴜ 𝙲ᴀɴ 𝙰ʟsᴏ 𝙲ᴏɴᴠᴇʀᴛ 𝚅ɪᴅᴇᴏ 𝚃ᴏ 𝙵ɪʟᴇ & 𝙵ɪʟᴇ 𝚃ᴏ 𝚅ɪᴅᴇᴏ
𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 𝙰𝙻𝚂𝙾 𝚂𝚄𝙿𝙿𝙾𝚁𝚃𝚂 𝙲𝚄𝚂𝚃𝙾𝙼 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻 𝙰𝙽𝙳 𝙲𝚄𝚂𝚃𝙾𝙼 𝙲𝙰𝙿𝚃𝙸𝙾𝙽

Tʜɪs Bᴏᴛ Wᴀs Cʀᴇᴀᴛᴇᴅ Bʏ : @TonyStark_Botz 💞</b>"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 ᴍy ɴᴀᴍᴇ : {}
├🖥️ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : <a href=https://t.me/TonyStark_Botz>TonyStark Botz</a> 
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://github.com/TonyStarkBotz>TonyStark Botz</a>
├📕 Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
├✏️ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
├📊 ᴠᴇʀsɪᴏɴ: <a href=https://github.com/TonyStarkBotz/Quick-Rename-Bot>3.𝟶.𝟶</a></b>     
╰───────────────⍟ """

    HELP_TXT = """
<b>•></b> /start Tʜᴇ Bᴏᴛ.

✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nɴᴀᴍᴇ \nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           
ℹ️ 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/TonyStarkBotzXSupport>𝑺𝑼𝑷𝑷𝑶𝑹𝑻 𝑮𝑹𝑶𝑼𝑷</a>
"""

    UPGRADE= """
•⪼ ★𝘗𝘭𝘢𝘯𝘴     -    ⏳𝘋𝘢𝘵𝘦 -  💸𝘗𝘳𝘪𝘤𝘦 
•⪼ 🥉𝘉𝘳𝘰𝘯𝘻𝘦   -     3𝘥𝘢𝘺𝘴 -    29
•⪼ 🥈𝘚𝘪𝘭𝘷𝘦𝘳    -     7𝘥𝘢𝘺𝘴 -    39
•⪼ 🥇𝘎𝘰𝘭𝘥     -    15𝘥𝘢𝘺𝘴 -   59
•⪼ 🏆𝘗𝘭𝘢𝘵𝘪𝘯𝘶𝘮  -    1𝘮𝘰𝘯𝘵𝘩 -   99
•⪼ 💎𝘋𝘪𝘢𝘮𝘰𝘯𝘥  -    2𝘮𝘰𝘯𝘵𝘩 -   199

- 𝘋𝘢𝘪𝘭𝘺 𝘜𝘱𝘭𝘰𝘢𝘥 𝘓𝘪𝘮𝘪𝘵 𝘜𝘯𝘭𝘪𝘮𝘪𝘵𝘦𝘥
- 𝘋𝘪𝘴𝘤𝘰𝘶𝘯𝘵 𝘈𝘭𝘭 𝘗𝘭𝘢𝘯 𝘙𝘴.9
    """
    THUMBNAIL = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴᴀɪʟ</u></b>

<b>•></b> Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴᴀɪʟ.
<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴᴀɪʟ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ.
"""
    CAPTION= """
📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ

Exᴀᴍᴩʟᴇ:- `/set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}`
"""
    BOT_STATUS = """
⚡️ ʙᴏᴛ sᴛᴀᴛᴜs ⚡️

⌚️ ʙᴏᴛ ᴜᴩᴛɪᴍᴇ: `{}`
👭 ᴛᴏᴛᴀʟ ᴜsᴇʀꜱ: `{}`
💸 ᴛᴏᴛᴀʟ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs: `{}`
֍ ᴜᴘʟᴏᴀᴅ: `{}`
⊙ ᴅᴏᴡɴʟᴏᴀᴅ: `{}`
"""
    LIVE_STATUS = """
⚡ ʟɪᴠᴇ sᴇʀᴠᴇʀ sᴛᴀᴛᴜs ⚡

ᴜᴘᴛɪᴍᴇ: `{}`
ᴄᴘᴜ: `{}%`
ʀᴀᴍ: `{}%` 
ᴛᴏᴛᴀʟ ᴅɪsᴋ: `{}`
ᴜsᴇᴅ sᴘᴀᴄᴇ: `{} {}%`
ғʀᴇᴇ sᴘᴀᴄᴇ: `{}`
ᴜᴘʟᴏᴀᴅ: `{}`
ᴅᴏᴡɴʟᴏᴀᴅ: `{}`
V𝟹.𝟶.𝟶 [STABLE]
"""
    DIGITAL_METADATA = """
❪ SET CUSTOM METADATA ❫

- /metadata - Tᴏ Sᴇᴛ & Cʜᴀɴɢᴇ ʏᴏᴜʀ ᴍᴇᴛᴀᴅᴀᴛᴀ ᴄᴏᴅᴇ

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @TonyStark_Botz" -metadata author="@TonyStark_Botz" -metadata:s:s title="Subtitled By :- @TonyStark_Botz" -metadata:s:a title="By :- @TonyStark_Botz" -metadata:s:v title="By:- @TonyStark_Botz" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @TonyContactBot
"""
    
    CUSTOM_FILE_NAME = """
<u>🖋️ Custom File Name</u>

you can pre-add a prefix and suffix along with your new filename

➢ /set_prefix - To add a prefix along with your _filename.
➢ /see_prefix - Tᴏ Sᴇᴇ Yᴏᴜʀ Pʀᴇғɪx !!
➢ /del_prefix - Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Pʀᴇғɪx !!
➢ /set_suffix - To add a suffix along with your filename_.
➢ /see_suffix - Tᴏ Sᴇᴇ Yᴏᴜʀ Sᴜғғɪx !!
➢ /del_suffix - Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Sᴜғғɪx !!

Exᴀᴍᴩʟᴇ:- `/set_suffix @MovieTimesTV`
Exᴀᴍᴩʟᴇ:- `/set_prefix @MovieTimesTV`
"""
    
    #⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @TonyStark_Botz🙏🥲
    # ᴡʜᴏᴇᴠᴇʀ ɪs ᴅᴇᴘʟᴏʏɪɴɢ ᴛʜɪs ʀᴇᴘᴏ ɪs ᴡᴀʀɴᴇᴅ ⚠️ ᴅᴏ ɴᴏᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛs ɢɪᴠᴇɴ ɪɴ ᴛʜɪs ʀᴇᴘᴏ #ғɪʀsᴛ ᴀɴᴅ ʟᴀsᴛ ᴡᴀʀɴɪɴɢ ⚠️
    DEV_TXT = """<b><u>Sᴩᴇᴄɪᴀʟ Tʜᴀɴᴋꜱ & Dᴇᴠᴇʟᴏᴩᴇʀꜱ</b></u>
    
» 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : <a href=https://github.com/TonyStarkBotz/Quick-Rename-Bot>Quick-Rename-Bot</a>

• ❣️ <a href=https://github.com/TonyStarkBotz>TonyStarkBotz</a> """
    # ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @TonyStark_Botz" -metadata author="@TonyStark_Botz" -metadata:s:s title="Subtitled By :- @TonyStark_Botz" -metadata:s:a title="By :- @TonyStark_Botz" -metadata:s:v title="By:- @TonyStark_Botz" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @TonyContactBot
"""
    
    PROGRESS = """<b>\n
╭━━━━❰ PROCESSING...❱━➣
┣⪼ 🗃️ ꜱɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ ᴅᴏɴᴇ : {0}%
┣⪼ 🚀 ꜱᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ ᴇᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""

# Don't Remove Credit 😔
# Telegram Channel @TonyStark_Botz & @MovieTimesTV
# Developer @Tony_Stark_75
# Update Channel @TonyStark_Botz & @TonyStarkBotzXSupport
