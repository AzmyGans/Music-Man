# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
from MusicMan.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from MusicMan.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME, OWNER
logging.basicConfig(level=logging.INFO)

@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>┗┓ Haii {message.from_user.first_name} Nama Saya Adalah {PROJECT_NAME} ┏┛\n
Saya Bot Music Group, Yang Dapat Memutar Lagu Di Voice Chat Group Dengan Cara Yang Mudah
Saya Memiliki Banyak Fitur Praktis Seperti:
┏━━━━━━━━━━━━━━
┣• Memutar Lagu Yang Diminta
┣• Mendownload Lagu Yang Diminta
┣• Mendownload Video Yang Diminta
┗━━━━━━━━━━━━━━
❃ Managed With By: {OWNER}
━━━━━━━━━━━━━━━
Gunakan Perintah » /help « Untuk Mengetahui Fitur Lengkap Saya
</b>""",

# Edit Yang Perlu Lu ganti 
# Tapi Jangan di Hapus Thanks To nya Yaaa :D

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ᴛᴀᴍʙᴀʜᴋᴀɴ sᴀʏᴀ ᴋᴇ ɢʀᴏᴜᴘ ᴀɴᴅᴀ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "💭 sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}"), 
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ 📢", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "🛠 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🛠", url=f"https://{SOURCE_CODE}")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = 'ʙᴇʀɪᴋᴜᴛɴʏᴀ ➡️', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            
            [InlineKeyboardButton(text = '⬅️ ᴋᴇᴍʙᴀʟɪ', callback_data = f"help+{pos-1}"),]
                    InlineKeyboardButton(
                        "ᴘᴇɴᴄᴀʀɪᴀɴ🔎", switch_inline_query_current_chat=""
                    ),
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '⬅️ ᴋᴇᴍʙᴀʟɪ', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = 'ʙᴇʀɪᴋᴜᴛɴʏᴀ ➡️', callback_data = f"help+{pos+1}")
            ],
        ]
    return button


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ **Apakah Anda ingin mencari Link YouTube?**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [    
                    InlineKeyboardButton(
                        "✅ ʏᴀ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "ᴛɪᴅᴀᴋ ❌ ", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        """**Klik Tombol Dibawah Untuk Melihat Cara Menggunakan Bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📜 ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴏᴛ 📜", url="https://telegra.ph/Command-Telegram-Music-06-12"
                    )
                ]
            ]
        ),
    )  


@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
async def reload(client: Client, message: Message):
    await message.reply_text("""✅ Bot **Berhasil Dimulai Ulang!**\n\n• **Daftar Admin** Telah **Diperbarui**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
   )

