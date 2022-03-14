# ©tofik_dn
# Minta tipis tipis

import random

from userbot import CMD_HELP
from userbot.events import register
from userbot import DEFAULTUSER
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos


@register(outgoing=True, pattern=r"^\.vidkep$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@asupanbanget", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"𝙔𝘼𝙃𝘼𝙃𝘼 𝙎𝘼𝙉𝙂𝙀𝘼𝙉, 𝙉𝙄𝙃 𝘼𝙎𝙐𝙋𝘼𝙉𝙉𝙔𝘼 𝙏𝙊𝘿 [{DEFAULTUSER}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("𝘒𝘶𝘳𝘢𝘯𝘨 𝘣𝘦𝘳𝘶𝘯𝘵𝘶𝘯𝘨 𝘺𝘢, 𝘗𝘢𝘥𝘢𝘩𝘢𝘭 𝘮𝘢𝘶 𝘤𝘰𝘭𝘪.")

@register(outgoing=True, pattern=r"^\.deswe$")
async def _(event):
    try:
        desahnya = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancewesangesange", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahnya),
            caption=f"𝘾𝙍𝙊𝙏𝙏𝙏𝙏!!! 𝙉𝙄𝙃 𝙑𝙉 𝘿𝙀𝙎𝘼𝙃 𝘾𝙀𝙒𝙀 [{DEFAULTUSER}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("`𝘠𝘢𝘩 𝘒𝘶𝘳𝘢𝘯𝘨 𝘣𝘦𝘳𝘶𝘯𝘵𝘶𝘯𝘨 𝘭𝘶 𝘣𝘢𝘯𝘨...`")


@register(outgoing=True, pattern=r"^\.deswo$")
async def _(event):
    try:
        desahnya = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancowo", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahnya),
            caption=f"𝘾𝙍𝙊𝙏𝙏𝙏𝙏!!! 𝙉𝙄𝙃 𝙑𝙉 𝘿𝙀𝙎𝘼𝙃 𝘾𝙊𝙒𝙊[{DEFAULTUSER}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("`𝘠𝘢𝘩 𝘒𝘶𝘳𝘢𝘯𝘨 𝘉𝘦𝘳𝘶𝘯𝘵𝘶𝘯𝘨 𝘭𝘶 𝘯𝘦𝘯𝘨...`")

        
@register(outgoing=True, pattern=r"^\.syg$")
async def _(event):
    try:
        ayangnya = [
            ayang
            async for ayang in event.client.iter_messages(
                "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ayangnya),
            caption=f"Nih Ayang Aku 😘 [{DEFAULTUSER}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("𝘎𝘢𝘥𝘢 𝘠𝘢𝘯𝘨 𝘔𝘢𝘶 𝘚𝘢𝘮𝘢 𝘓𝘰 𝘒𝘢𝘳𝘦𝘯𝘢 𝘓𝘰 𝘋𝘦𝘬𝘪𝘭 𝘬𝘢𝘺𝘢 𝘣𝘢𝘫𝘶 𝘱𝘢𝘳𝘵𝘢𝘪 𝘣𝘦𝘬𝘢𝘴𝘢𝘯🤭.")


CMD_HELP.update(
    {
        "asupan": "**Plugin : **`asupan`\
        \n\n  •  **Syntax :** `.vidkep`\
        \n  •  **Function : **Untuk Mengirim video asupan secara random.\
        \n\n  •  **Syntax :** `.deswo` `.deswe`\
        \n  •  **Function : **Untuk Mengirim suara desah buat lu yang sange.\
        \n\n  •  **Syntax :** `.syg`\
        \n  •  **Function : **Untuk Mencari ayang buat cowok yang jomblo.\
    "
    }
)
