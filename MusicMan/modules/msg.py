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

import os
from MusicMan.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL, OWNER
class Messages():
      START_MSG = "**👋🏻 Hai [{}](tg://user?id={})**\n\n🤖 Saya Adalah Bot Canggih Yang Dibuat Untuk Memutar Musik Di Obrolan Suara Grup & Saluran Telegram.‌‌\n\n🧑🏻‍💻 Dikelolah oleh: [ɢᴏᴏᴅ ʙᴏʏs](https://t.me/GB_03101999) \n\n"
      HELP_MSG = [
        ".",
f"""
**👋🏻 Hai Selamat Datang Kembali Di {PROJECT_NAME}

⚪️ {PROJECT_NAME} Dapat Memutar Musik Di Obrolan Suara Grup Anda Serta Obrolan Suara Saluran

⚪️ Assistant Name >> @{ASSISTANT_NAME}\n\nKlik next Untuk Info Lebih Lanjut**
""",

f"""
**🛠️ Pengaturan**

1) Jadikan Bot Sebagai Admin
2) Mulai Obrolan Suara / Vcg
3) Kirim Perintah /userbotjoin
• Jika Assistant Bot Bergabung Selamat Menikmati Musik, 
• Jika Assistant Bot Tidak Bergabung Silahkan Tambahkan @{ASSISTANT_NAME} Ke Grup Anda Dan Coba Lagi

**Untuk Saluran Music Play**
1) Jadikan Bot Sebagai Admin Saluran
2) Kirim /userbotjoinchannel Di Grup Tertaut
3) Sekarang Kirim Perintah Di Grup Tertaut

**🔰 Perintah 🔰**

**=>> Memutar Lagu 🎧**

• /play (nama lagu) - Untuk Memutar lagu yang Anda minta melalui youtube
• /dplay (nama lagu) - Untuk Memutar lagu yang Anda minta melalui deezer
• /splay (nama lagu) - Untuk Memutar lagu yang Anda minta melalui jio saavn
• /ytplay (nama lagu) - Untuk Memutar lagu yang Anda minta melalui youtube dengan lebih detail

**=>> Pemutaran ⏯**

• /player: Buka menu Pengaturan pemain
• /skip: Melewati trek saat ini
• /pause: Jeda trek
• /resume: Melanjutkan trek yang dijeda
• /end: ​​Menghentikan pemutaran media
• /current: Menampilkan trek yang sedang diputar
• /playlist: Menampilkan daftar putar

Semua Perintah Bisa Digunakan Kecuali Perintah /player /skip /pause /resume  /end Hanya Untuk Admin Grup
""",
        
f"""
**=>> Saluran Music Play 🛠**

⚪️ Hanya untuk admin grup tertaut:

• /cplay (nama lagu) - putar lagu yang Anda minta
• /cdplay (nama lagu) - putar lagu yang Anda minta melalui deezer
• /csplay (nama lagu) - putar lagu yang Anda minta melalui jio saavn
• /cplaylist - Tampilkan daftar yang sedang diputar
• /cccurrent - Tampilkan sedang diputar
• /cplayer - buka panel pengaturan pemutar musik
• /cpause - jeda pemutaran lagu
• /cresume - melanjutkan pemutaran lagu
• /cskip - putar lagu berikutnya
• /cend - hentikan pemutaran musik
• /userbotjoinchannel - undang asisten ke obrolan Anda

⚪️ Jika Anda Tidak Suka Bermain Di Grup Tertaut:

1) Dapatkan ID Saluran Anda.
2) Buat Grup Dengan Judul: Channel Music: ID_SALURAN_ANDA
3) Tambahkan Bot Sebagai Admin Saluran Dengan Izin Penuh
4) Tambahkan @{ASSISTANT_NAME} Ke Saluran Sebagai admin.
5) Cukup Kirim Perintah Di Grup Anda
""",

f"""
**=>> Lebih Banyak Alat 🧑‍🔧**

- /musicplayer [on/off]: Aktifkan/Nonaktifkan Pemutar Musik
- /admincache: Memperbarui Info Admin Grup Anda. Coba Jika Bot Tidak Mengenali Admin
- /userbotjoin: Undang @{ASSISTANT_NAME} Userbot Ke Grup Anda

**=>> Perintah untuk Pengguna Sudo ️ ⚔️**

 • /userbotleaveall - Hapus Asisten Dari Semua Obrolan
 • /gcast - Pesan Balasan Brodcast Global Ke Semua Obrolan
Pengguna Sudo Dapat Menjalankan Perintah Apa Pun Di Grup Mana Pun‌‌

"""
      ]
