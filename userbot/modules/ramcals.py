# Thanks Full To Team Ultroid
# Ported By Vcky @VckyouuBitch + @MaafGausahSokap
# Copyright (c) 2021 Geez - Projects
# Geez - Projects https://github.com/Vckyou/Geez-UserBot
# RAM - UBOT https://github.com/ramadhani892/RAM-UBOT
# Ini Belum Ke Fix Ya Bg :')
# Ambil aja gapapa tp Gaguna kaya hidup lu Woakkakaka


from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from telethon.tl.types import ChatAdminRights
from userbot import CMD_HELP
from userbot.events import register

NO_ADMIN = "`WOY HINA LU BUKAN ADMIN NGENTOT!!`"

def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"


async def get_call(event):
    kybot = await event.client(getchat(event.chat_id))
    rizky = await event.client(getvc(kybot.full_chat.call, limit=1))
    return rizky.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@register(outgoing=True, pattern=r"^\.startvc$")
async def start_voice(kybot):
    chat = await kybot.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await kybot.edit(f"**Maaf {ALIVE_NAME} Bukan Admin 👮**")
        return
    try:
        await kybot.client(startvc(kybot.chat_id))
        await kybot.edit("`OS UDAH DIBUKA NGENTOT, KALO UDAH DI BUKA JANGAN ON CAM PAMERIN MUKA LU YANG MIRIP BABI HUTAN YAH BANGSAT!`")
    except Exception as ex:
        await kybot.edit(f"**ERROR:** `{ex}`")


@register(outgoing=True, pattern=r"^\.stopvc$")
async def stop_voice(rizky):
    chat = await rizky.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await rizky.edit(f"**Maaf {ALIVE_NAME} Bukan Admin 👮**")
        return
    try:
        await rizky.client(stopvc(await get_call(rizky)))
        await rizky.edit("`OS NYA DIMATIIN NORAK, TYPING AJA TYPING SABAN HARI OS MULU GA CAPE TU MULUT YA NGENTOT!`")
    except Exception as ex:
        await rizky.edit(f"**ERROR:** `{ex}`")

@register(outgoing=True, pattern=r"^\.vcinvite", groups_only=True)
async def _(rambot):
    await rambot.edit("`Memulai Invite member group...`")
    users = []
    z = 0
    async for x in rambot.client.iter_participants(rambot.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await rambot.client(invitetovc(call=await get_call(rambot), users=p))
            z += 6
        except BaseException:
            pass
    await rambot.edit(f"`Menginvite {z} Member`")


CMD_HELP.update(
    {
        "ramcalls": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.startvc`\
         \n↳ : Memulai Obrolan Suara dalam Group.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.stopvc`\
         \n↳ : `Menghentikan Obrolan Suara Pada Group.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vcinvite`\
         \n↳ : Invite semua member yang berada di group. (Kadang bisa kadang kaga).\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.joinvc` & `.leavevc`\
         \n↳ : Membuat Obrolan Suara Secara Fake."
    }
)
