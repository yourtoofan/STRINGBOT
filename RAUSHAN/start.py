from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo="https://files.catbox.moe/hkqkpv.jpg",
        caption=f"""✦ » ʜᴇʏ  {msg.from_user.mention}  ✤,
✦ » ɪ ᴀᴍ {me2},

✦ » Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

✦ » ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ.

✦ » ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ: [ᴍɪᴄᴋᴇʏ](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="▪ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ ▪️", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("🔸 sᴜᴘᴘᴏʀᴛ🔸", url="https://t.me/ZOYU_SUPPORT"),
                    InlineKeyboardButton("▫️ ᴜᴘᴅᴀᴛᴇs▫️", url="https://t.me/THE_INCRICIBLE")
                ],
                [
                    InlineKeyboardButton("🔸 sᴏᴜʀᴄᴇ 🔸", url="https://github.com/YOURTOOFAN/STRINGBOT"),
                    InlineKeyboardButton("▫️ᴍᴜsɪᴄ ʙᴏᴛ▫️", url="https://t.me/ZOYUMUSICBOT")
                ]                
            ]
        )
    )
