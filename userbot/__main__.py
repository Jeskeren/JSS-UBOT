# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

import sys
from importlib import import_module

from userbot import ALIVE_NAME, BOT_VER, BOTLOG_CHATID, LOGS, UPSTREAM_REPO_BRANCH, call_py, bot
from userbot.modules import ALL_MODULES
from pytgcalls import idle
from userbot.utils.tools import hadeh_ajg
from userbot.utils.utils import autobot
try:
    for module_name in ALL_MODULES:
        imported_module = import_module("userbot.modules." + module_name)
    bot.start()
    call_py.start()
    LOGS.info(f"🤙🏻𝙆𝙔-𝙐𝘽𝙊𝙏🤙🏻 🦖 V{BOT_VER} [ TELAH DIAKTIFKAN TOD! ]")
except BaseException as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)


async def kyy_ubot_on():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(
                BOTLOG_CHATID,
                f"🤙🏻Userbot berhasil di aktifkan Mekihh\n━━━━━━━━━━━━━━━\n❃ Bot Of : {ALIVE_NAME}\n❃ BotVer : {BOT_VER}@{UPSTREAM_REPO_BRANCH}\n━━━━━━━━━━━━━━━",
            )
    except Exception as e:
        LOGS.info(str(e))

bot.loop.run_until_complete(autobot())
bot.loop.run_until_complete(kyy_ubot_on())
idle()
bot.loop.run_until_complete(hadeh_ajg())
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
