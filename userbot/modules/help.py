# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from userbot.events import register
from telethon import events
import asyncio


@register(outgoing=True, pattern="^.help$")
async def helpx(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("\nAvailable Modules:"
"\n\n• 𝗔𝗱𝗺𝗶𝗻: `admin`, `chat`"
"\n• 𝗨𝗽𝗱𝗮𝘁𝗲𝗿: `update`, `update now`"
"\n• 𝗠𝗲𝗺𝗲𝘀: `memes`, `deepfry`, `dfry`, `dice`, `basketball`, `dart`, `waifu`, `random`, `carbon`,"
"\n• 𝗔𝗻𝗱𝗿𝗼𝗶𝗱: `android`, `magisk`"
"\n• 𝗔𝗳𝗸: `afk`"
"\n• 𝗧𝗼𝗼𝗹𝘀: `all`, `antivirus`, `dictionary`,`dogbin`, `listmyusernames`, `ocr`,`qr`, `sangmata`, `currency`, `wiki`, `ud`, `tts`, `trt`, `yt`, `imdb`, `ss`, `telegraph`, `compress`, `rbg`, `barcode`, `quotly`"  
"\n• 𝗡𝗼𝘁𝗲𝘀: `notes`, `filter`, `snips`"
"\n• 𝗧𝗲𝘅𝘁-𝗧𝗿𝗮𝗻𝘀𝗳𝗼𝗿𝗺:`figlet`, `sticklet_un`, `base64`, `hash`, `textx`"
"\n• 𝗣𝗠: `logpms`, `nopm`, `pmpermit`"
"\n• 𝗖𝗵𝗮𝘁: `chatinfo`, `create`, `invite`, `profile`, `welcome`, `stats` `raw`, `purge`, `purgeme`, `del`, `edit`, `sd`, `whois`"  
"\n• 𝗥𝗲𝘁𝗮𝗿𝗱𝗲𝗱: `lydia`, `repeat`,  `spam`, `sed`"
"\n• 𝗘𝘃𝗮𝗹𝗮𝘁𝗼𝗿𝘀: `eval`, `exec`, `term`, `pip`"
"\n• 𝗚𝗶𝘁𝗵𝘂𝗯: `git`, `gcommit`, `heroku`, `repo`, `myrepo`"
"\n• 𝗪𝗲𝗯: `google` `reverse`, `img`, `w3m`, `weather`, `speed`, `dc`, `ping`"
"\n• 𝗨𝗽𝗹𝗼𝗮𝗱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱: `direct`, `aria`, `aria2`, `gdrive`, `mega`, `rip`, `download`, `webupload`"
"\n• 𝗖𝗼𝘃𝗶𝗱: `cod19`"
"\n• 𝗨𝘀𝗲𝗿𝗯𝗼𝘁: `useitoub`, `sleep`, `shutdown`, `restart`, `anti_spambot`, `sysd`, `botver`, `alive`, `dbs`, `creator`, `readme`, `time`, `date`" 
"\n• 𝗦𝘁𝗶𝗰𝗸𝗲𝗿𝘀: `stickers`"  
"\n• 𝗠𝘂𝘀𝗶𝗰: `song`, `lyrics`")
        
            await e.edit("Please specify which module do you want help for !!\
            \nUsage: .help <module name> to know how it works")
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\n"
        await event.reply(string)
