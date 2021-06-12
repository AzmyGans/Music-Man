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
      HELP_MSG = [
        ".",
f"""
**👋🏻 Hai Selamat Datang Kembali Di {PROJECT_NAME}

✣️ {PROJECT_NAME} dapat Memutar Lagu di Voice Chat Group Dengan cara yang Mudah.

✣️ Assistant Music » @{ASSISTANT_NAME}\n\nKlik Next untuk instruksi**

""",

f"""
**🛠️ BAGAIMANA CARA MENGGUNAKANNYA?

1. Jadikan Bot Sebagai Admin
2. Mulai Obrolan Suara / VCG
3. Ketik /ubotjoin Dan Coba /play 
× Jika Assistant Bot Bergabung Selamat Menikmati Musik, 
× Jika Assistant Bot Tidak Bergabung Silahkan Tambahkan @{ASSISTANT_NAME} Ke Grup Anda Dan Coba Lagi

🎛 PERINTAH MUSIC PLAYER UNTUK MEMUTAR LAGU

× /play : link youtube atau reply ke audio file untuk memutar lagu
× /play [judul lagu] : Untuk Memutar lagu yang Anda minta melalui youtube
× /dplay [judul lagu] : Untuk Memutar lagu yang Anda minta melalui deezer
× /splay [judul lagu] : Untuk Memutar lagu yang Anda minta melalui jio saavn

🎛 PERINTAH MUSIC PLAYER HANYA ADMIN GRUP

× /skip : Untuk Menskip pemutaran lagu ke Lagu berikutnya
× /pause : Untuk Menjeda pemutaran Lagu
× /resume : Untuk Melanjutkan pemutaran Lagu yang di pause
× /end : Untuk Memberhentikan pemutaran Lagu
× /ubotjoin - Untuk Mengundang asisten ke obrolan Anda

🎛 PERINTAH UNTUK DOWNLOAD LAGU ATAU VIDEO

× /song [judul lagu] : Untuk Mendownload lagu di YouTube 
× /video [judul lagu] : Untuk Mendownload Video di YouTube dengan detail
× /deezer [judul lagu] : Untuk Mendownload lagu dari deezer 
× /saavn [judul lagu] : Untuk Mendownload lagu dari website saavn

📝 CATATAN HARAP DIBACA AGAR TIDAK TERJADI KENDALA

• Untuk Menghindari Bot Error Jangan Melakukan Spam Musik Ke Dalam Antrian Sekaligus
• Lagu Yang Melebihi Waktu 2 Jam Tidak Dapat Diputar
• Jika Assistant Tidak Mau Naik Ke Obrolan Suara, Matiin Obrolan Suara Dan Mulai Lagi
• Jika Assistent Tidak Bisa Di Invite, Ketik /unban @{ASSISTANT_NAME} Terus Ketik /ubotjoin Di Grup Anda 
• Itu Saja Pesan Dari Saya Terimakasih, Selamat Bermusik**"""
      ]
