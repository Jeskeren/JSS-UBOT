from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi Kakak Rizky boleh Nimbrung ehehe..**")


@register(outgoing=True, pattern='^.geez(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Max Kek Kontol☑️**")
    await typew.edit("**Max Kek Kontol✅**")
    sleep(1)
    await typew.edit("**Abeng kek Monyet☑️**")
    await typew.edit("**Abeng Kek Monyet✅**")
    sleep(2)
    await typew.edit("**Mox Kek Babi Laut☑️**")
    await typew.edit("**Mox Kek Babi Laut✅**")
    sleep(2)
    await typew.edit("**Santos Botak Biadap☑️**")
    await typew.edit("**Santos Botak Biadap✅**")
    sleep(2)
    await typew.edit("**Exsa Jelek Bet Jelek☑️**")
    await typew.edit("**Exsa Jelek Bet Jelek✅**")
    sleep(2)
    await typew.edit("**Hans Sagapung☑️**")
    await typew.edit("**Hans Sagapung✅**")
    sleep(2)
    await typew.edit("**Exy GACOR☑️**")
    await typew.edit("**Exy GACOR✅**")
    sleep(2)
    await typew.edit("**Rony,Suka Nyepong☑️**")
    await typew.edit("**Rony,Suka Nyepong✅**")
    sleep(3)
    await typew.edit("**CUMA RIZKY YANG BENER!**")


@register(outgoing=True, pattern='^.lahk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Lahk, Lo tolol?`")
    sleep(1)
    await typew.edit("`Apa dongok?`")
    sleep(1)
    await typew.edit("`Gausah sok keras`")
    sleep(1)
    await typew.edit("`Gua ga ketrigger sama bocah baru nyemplung!`")


@register(outgoing=True, pattern='^.wah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wahh, War nya keren bang`")
    sleep(2)
    await typew.edit("`Tapi, Yang gua liat, kok Kaya lawakan`")
    sleep(2)
    await typew.edit("`Oh iya, Kan lo badut 🤡`")
    sleep(2)
    await typew.edit("`Kosa kata pas ngelawak, Jangan di pake war bang`")
    sleep(2)
    await typew.edit("`Kesannya lo ngasih kita hiburan.`")
    sleep(2)
    await typew.edit("`Kasian badut🤡, Ga di hargain pengunjung, Eh lampiaskan nya ke Tele, Wkwkwk`")
    sleep(3)
    await typew.edit("`Dah sana cabut, Makasih hiburannya, Udah bikin Gua tawa ngakak`")

CMD_HELP.update({
    "rambot":
    "`.rambot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.geez`\
    \nUsage: misi."
})
