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
from MusicMan.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,DURATION_LIMIT, OWNER
class Messages():
      HELP_MSG = [
        ".",
f"""
**Hai Selamat datang kembali di {PROJECT_NAME}
✣️ {PROJECT_NAME} dapat Memutar Lagu di Voice Chat Group Dengan cara yang Mudah.
✣️ Assistant Music » @{ASSISTANT_NAME}\n\nKlik Next untuk instruksi**

""",

f"""
<b>👋🏻 Haii {message.from_user.mention} Nama Saya Adalah {PROJECT_NAME}

Saya adalah bot canggih yang dibuat untuk memutar musik di obrolan suara Grup Telegram.

Dikelolah Oleh: {OWNER}

Tekan Tombol Bantuan Untuk Mengetahui Fitur Lengkap Saya</b>
"""
      ]
