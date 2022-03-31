# Ported By @VckyouuBitch From Geez-Projects
# Fixes bugs kemaren ngestuck kaya hidup piki


import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import quote_plus
from asyncio import sleep
from userbot import CHROME_DRIVER, CMD_HELP, GOOGLE_CHROME_BIN
from userbot.events import register


CARBONLANG = "auto"
TTS_LANG = "en"
TRT_LANG = "en"
TEMP_DOWNLOAD_DIRECTORY = "/root/userbot/.bin"

all_col = [
    "Black",
    "Navy",
    "DarkBlue",
    "MediumBlue",
    "Blue",
    "DarkGreen",
    "Green",
    "Teal",
    "DarkCyan",
    "DeepSkyBlue",
    "DarkTurquoise",
    "MediumSpringGreen",
    "Lime",
    "SpringGreen",
    "Aqua",
    "Cyan",
    "MidnightBlue",
    "DodgerBlue",
    "LightSeaGreen",
    "ForestGreen",
    "SeaGreen",
    "DarkSlateGray",
    "DarkSlateGrey",
    "LimeGreen",
    "MediumSeaGreen",
    "Turquoise",
    "RoyalBlue",
    "SteelBlue",
    "DarkSlateBlue",
    "MediumTurquoise",
    "Indigo  ",
    "DarkOliveGreen",
    "CadetBlue",
    "CornflowerBlue",
    "RebeccaPurple",
    "MediumAquaMarine",
    "DimGray",
    "DimGrey",
    "SlateBlue",
    "OliveDrab",
    "SlateGray",
    "SlateGrey",
    "LightSlateGray",
    "LightSlateGrey",
    "MediumSlateBlue",
    "LawnGreen",
    "Chartreuse",
    "Aquamarine",
    "Maroon",
    "Purple",
    "Olive",
    "Gray",
    "Grey",
    "SkyBlue",
    "LightSkyBlue",
    "BlueViolet",
    "DarkRed",
    "DarkMagenta",
    "SaddleBrown",
    "DarkSeaGreen",
    "LightGreen",
    "MediumPurple",
    "DarkViolet",
    "PaleGreen",
    "DarkOrchid",
    "YellowGreen",
    "Sienna",
    "Brown",
    "DarkGray",
    "DarkGrey",
    "LightBlue",
    "GreenYellow",
    "PaleTurquoise",
    "LightSteelBlue",
    "PowderBlue",
    "FireBrick",
    "DarkGoldenRod",
    "MediumOrchid",
    "RosyBrown",
    "DarkKhaki",
    "Silver",
    "MediumVioletRed",
    "IndianRed ",
    "Peru",
    "Chocolate",
    "Tan",
    "LightGray",
    "LightGrey",
    "Thistle",
    "Orchid",
    "GoldenRod",
    "PaleVioletRed",
    "Crimson",
    "Gainsboro",
    "Plum",
    "BurlyWood",
    "LightCyan",
    "Lavender",
    "DarkSalmon",
    "Violet",
    "PaleGoldenRod",
    "LightCoral",
    "Khaki",
    "AliceBlue",
    "HoneyDew",
    "Azure",
    "SandyBrown",
    "Wheat",
    "Beige",
    "WhiteSmoke",
    "MintCream",
    "GhostWhite",
    "Salmon",
    "AntiqueWhite",
    "Linen",
    "LightGoldenRodYellow",
    "OldLace",
    "Red",
    "Fuchsia",
    "Magenta",
    "DeepPink",
    "OrangeRed",
    "Tomato",
    "HotPink",
    "Coral",
    "DarkOrange",
    "LightSalmon",
    "Orange",
    "LightPink",
    "Pink",
    "Gold",
    "PeachPuff",
    "NavajoWhite",
    "Moccasin",
    "Bisque",
    "MistyRose",
    "BlanchedAlmond",
    "PapayaWhip",
    "LavenderBlush",
    "SeaShell",
    "Cornsilk",
    "LemonChiffon",
    "FloralWhite",
    "Snow",
    "Yellow",
    "LightYellow",
    "Ivory",
    "White",
]



@register(outgoing=True, pattern="^.crblang (.*)")
async def setlang(prog):
    global CARBONLANG
    CARBONLANG = prog.pattern_match.group(1)
    await prog.edit(f"Language for carbon.now.sh set to {CARBONLANG}")


@register(outgoing=True, pattern="^.carbon1")
async def carbon_api(e):
    """ A Wrapper for carbon.now.sh """
    await e.edit("`Memulai Proses..`")
    CARBON = 'https://carbon.now.sh/?bg=rgba(249%2C237%2C212%2C0)&t=synthwave-84&wt=none&l=application%2Fjson&ds=true&dsyoff=20px&dsblur=0px&wc=true&wa=true&pv=56px&ph=0px&ln=false&fl=1&fm=IBM%20Plex%20Mono&fs=14.5px&lh=153%25&si=false&es=4x&wm=false&code={code}'
    global CARBONLANG
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    code = quote_plus(pcode)  # Converting to urlencoded
    await e.edit("`Proses di..\n25%`")
    if os.path.isfile("/root/userbot/.bin/carbon.png"):
        os.remove("/root/userbot/.bin/carbon.png")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {'download.default_directory': '/root/userbot/.bin'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=chrome_options)
    driver.get(url)
    await e.edit("`Proses di..\n50%`")
    download_path = '/root/userbot/.bin'
    driver.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command')
    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {
            'behavior': 'allow',
            'downloadPath': download_path
        }
    }
    driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await e.edit("`Processing..\n75%`")
    # Waiting for downloading
    while not os.path.isfile("/root/userbot/.bin/carbon.png"):
        await sleep(0.5)
    await e.edit("`sudah sampai..\n100%`")
    file = '/root/userbot/.bin/carbon.png'
    await e.edit("`Mengirim..`")
    await e.client.send_file(
        e.chat_id,
        file,
        caption="Created by [LANDAK 🦔](https://t.me/maafgausahsokap/)\
        \nGroup [SPAM BOT](https://t.me/ootspambot/)",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )

    os.remove('/root/userbot/.bin/carbon.png')
    driver.quit()
    # Removing carbon.png after uploading
    await e.delete()  # Deleting msg


@register(outgoing=True, pattern="^.carbon2")
async def carbon_api(e):
    """ A Wrapper for carbon.now.sh """
    await e.edit("`Memulai Proses..`")
    CARBON = 'https://carbon.now.sh/?bg=rgba(239%2C40%2C44%2C1)&t=one-light&wt=none&l=application%2Ftypescript&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=143%25&si=false&es=2x&wm=false&code={code}'
    global CARBONLANG
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    code = quote_plus(pcode)  # Converting to urlencoded
    await e.edit("`Proses di..\n25%`")
    if os.path.isfile("/root/userbot/.bin/carbon.png"):
        os.remove("/root/userbot/.bin/carbon.png")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {'download.default_directory': '/root/userbot/.bin'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=chrome_options)
    driver.get(url)
    await e.edit("`Proses di..\n50%`")
    download_path = '/root/userbot/.bin'
    driver.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command')
    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {
            'behavior': 'allow',
            'downloadPath': download_path
        }
    }
    driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await e.edit("`Proses di..\n75%`")
    # Waiting for downloading
    while not os.path.isfile("/root/userbot/.bin/carbon.png"):
        await sleep(0.5)
    await e.edit("`Sudah sampai..\n100%`")
    file = '/root/userbot/.bin/carbon.png'
    await e.edit("`Mengirim..`")
    await e.client.send_file(
        e.chat_id,
        file,
        caption="created by [LANDAK 🦔](https://t.me/maafgausahsokap/)\
        \nGroup Support [Dawn Labs](https://t.me/ootspambot/)",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )

    os.remove('/root/userbot/.bin/carbon.png')
    driver.quit()
    # Removing carbon.png after uploading
    await e.delete()  # Deleting msg


@register(outgoing=True, pattern="^.carbon3")
async def carbon_api(e):
    """ A Wrapper for carbon.now.sh """
    await e.edit("`Memulai Proses..`")
    CARBON = 'https://carbon.now.sh/?bg=rgba(74%2C144%2C226%2C1)&t=material&wt=none&l=auto&ds=false&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Fira%20Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code={code}'
    global CARBONLANG
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    code = quote_plus(pcode)  # Converting to urlencoded
    await e.edit("`Proses di..\n25%`")
    if os.path.isfile("/root/userbot/.bin/carbon.png"):
        os.remove("/root/userbot/.bin/carbon.png")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {'download.default_directory': '/root/userbot/.bin'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=chrome_options)
    driver.get(url)
    await e.edit("`Proses di..\n50%`")
    download_path = '/root/userbot/.bin'
    driver.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command')
    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {
            'behavior': 'allow',
            'downloadPath': download_path
        }
    }
    driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await e.edit("`Processing..\n75%`")
    # Waiting for downloading
    while not os.path.isfile("/root/userbot/.bin/carbon.png"):
        await sleep(0.5)
    await e.edit("`Sudah Sampai..\n100%`")
    file = '/root/userbot/.bin/carbon.png'
    await e.edit("`Mengirim..`")
    await e.client.send_file(
        e.chat_id,
        file,
        caption="Created By [LANDAK 🦔](https://t.me/maafgausahsokap/)\
        \nGroup Support [Spam](https://t.me/ootspambot/)",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )

    os.remove('/root/userbot/.bin/carbon.png')
    driver.quit()
    # Removing carbon.png after uploading
    await e.delete()  # Deleting msg


@register(outgoing=True, pattern="^.carbon4")
async def carbon_api(e):
    """ A Wrapper for carbon.now.sh """
    await e.edit("`Memulai Proses..`")
    CARBON = 'https://carbon.now.sh/?bg=rgba(29%2C40%2C104%2C1)&t=one-light&wt=none&l=application%2Ftypescript&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=143%25&si=false&es=2x&wm=false&code={code}'
    global CARBONLANG
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    code = quote_plus(pcode)  # Converting to urlencoded
    await e.edit("`Proses di..\n25%`")
    if os.path.isfile("/root/userbot/.bin/carbon.png"):
        os.remove("/root/userbot/.bin/carbon.png")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {'download.default_directory': '/root/userbot/.bin'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=chrome_options)
    driver.get(url)
    await e.edit("`Proses di..\n50%`")
    download_path = '/root/userbot/.bin'
    driver.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command')
    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {
            'behavior': 'allow',
            'downloadPath': download_path
        }
    }
    driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await e.edit("`Proses di..\n75%`")
    # Waiting for downloading
    while not os.path.isfile("/root/userbot/.bin/carbon.png"):
        await sleep(0.5)
    await e.edit("`Sudah Sampai..\n100%`")
    file = '/root/userbot/.bin/carbon.png'
    await e.edit("`Mengirim..`")
    await e.client.send_file(
        e.chat_id,
        file,
        caption="Created by [LANDAK 🦔](https://t.me/maafgausahsokap/),\
        \nGroup Support [Group Spam](https://t.me/ootspambot)",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )

    os.remove('/root/userbot/.bin/carbon.png')
    driver.quit()
    # Removing carbon.png after uploading
    await e.delete()  # Deleting msg


@register(outgoing=True, pattern="^.carbon")
async def carbon_api(e):
    """ A Wrapper for carbon.now.sh """
    await e.edit("`memulai proses..`")
    CARBON = 'https://carbon.now.sh/?bg=rgba(76%2C144%2C140%2C1)&t=night-owl&wt=none&l=coffeescript&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Fira%20Code&fs=14px&lh=133%25&si=false&es=2x&wm=false&code={code}'
    global CARBONLANG
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    code = quote_plus(pcode)  # Converting to urlencoded
    await e.edit("`Proses di..\n25%`")
    if os.path.isfile("/root/userbot/.bin/carbon.png"):
        os.remove("/root/userbot/.bin/carbon.png")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {'download.default_directory': '/root/userbot/.bin'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=chrome_options)
    driver.get(url)
    await e.edit("`Proses di..\n50%`")
    download_path = '/root/userbot/.bin'
    driver.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command')
    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {
            'behavior': 'allow',
            'downloadPath': download_path
        }
    }
    driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await e.edit("`Proses di..\n75%`")
    # Waiting for downloading
    while not os.path.isfile("/root/userbot/.bin/carbon.png"):
        await sleep(0.5)
    await e.edit("`Sudah Sampai..\n100%`")
    file = '/root/userbot/.bin/carbon.png'
    await e.edit("`Mengirim..`")
    await e.client.send_file(
        e.chat_id,
        file,
        caption="Created by [LANDAK 🦔](https://t.me/maafgausahsokap/),\
        \nGroup Support [Spam BOT](https://t.me/ootspambot/)",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )

    os.remove('/root/userbot/.bin/carbon.png')
    driver.quit()
    # Removing carbon.png after uploading
    await e.delete()  # Deleting msg


CMD_HELP.update({
    "carbon":
    "`.carbon`value <values=1,2,3,4>\
        \nUsage:reply or type .carbon1 or 2,3,4 value and beautify your text."
})
