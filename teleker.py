from telethon import TelegramClient, events, utils
from telethon.tl import types
import time
import requests
from datetime import datetime
from mtranslate import translate
import os
import pyttsx3
import time
import json
import psutil
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

#  Remember to use your own values from my.telegram.org!
api_id = "2421227"
api_hash = "5cfbdb99e4477b828bf06a9cd1efeead"

client = TelegramClient('new_session_name', api_id, api_hash)

# #####################################
# #####################################
# me =  client.get_me()
# frist_name = me.first_name
# edit_list_for_prof = [f"😀{frist_name}😀",f"{frist_name}",f"😀{frist_name}😀",f"{frist_name}",f"😀{frist_name}😀",f"{frist_name}"]

# @client.on(events.NewMessage(pattern=r'(?i).*/hi_telekr'))
# async def hi_hadndeler(event):
#         for text in edit_list_for_prof:
#             result = client(functions.account.UpdateProfileRequest(
#                 first_name=f'{text}',
#         ))
# #######################################
# #######################################
# hi telehr and info


@client.on(events.NewMessage(outgoing=True, pattern=r'(?i).*/hi_telekr'))
async def hi_hadndeler(event):
    info_bot = '''سلام 😀🖖
من تیلکر هستم 😝
یک سلف اسکریپت فان برای تلگرام 😏🖖
درسته اسکریپت 🙃
برعکس سورس سلف ها دیگه که با php نوشته شده من با زبان قدرتمند پایتون نوشته شدم😗🖖
بعله پایتون 🐍
میتونید منو رو یک هاست بزارید تا همیشه فعال باشم 🤓
فعلا لینک دانلودم در دسترس نیست بدا میزاریم 🤗
راستی من میتونم به عنوان یک ربات هم تو گروه باشم🥳✌️
برای دیدن دستورا من میتونین  info/  رو ارسال کنین تا لیست دستورات ببینید😉'''
    await event.reply(str(f"{info_bot}"))


@client.on(events.NewMessage(pattern=r'(?i).*/bot'))
async def info(event):
    info_command = ' 😉بله جابرخان انلاینم'

    await event.reply(str(f"{info_command}"))


# return commands bot
@client.on(events.NewMessage(pattern=r'(?i).*/info'))
async def info(event):
    info_command = ''' آمبولاس میترکه 😐🖖
/bomb
———————————————————-
همه میمون ها با هم 😐🖖
/monkey
———————————————————-
رقص رنگ ها 😬🖖
/colors
———————————————————-
فاک یو 😑🖖
/fuck_you
———————————————————-
شت 😐💔
/shet
———————————————————-
همه خنده ها 😀🖖
/smail
———————————————————-
هک ناسا 😀🖖 
/hack_nasa
———————————————————-
حرکت ماه 😀🖖
/mah
———————————————————-
ساعت چنده؟ 🕔
/time_now
———————————————————-
دوست دارم ❤️
/love 
———————————————————-
دوست دارم ❤️
/mylove 
———————————————————-
🕔 ساعت
/go_time
———————————————————-
فاک 🤦‍♂️
/fuck
———————————————————-
عکس 📸
/get_photo
———————————————————-
دیوانه 😜
/carzy
———————————————————-
خواب
/sleep
———————————————————-
💜
/pink_heart
———————————————————-
💜
/pink_love
———————————————————-
/angosht
———————————————————-
/pashm
———————————————————-
/lashi
———————————————————-
/eshgh
———————————————————-
اب و هوا
/weather
———————————————————-
سرچ گوگل
/google_search
———————————————————-
متن به ویس
/say
———————————————————-
ترجمه
/translator
———————————————————-
سیستم 
/sys_info
———————————————————-
سیو
/save
———————————————————-
سیو پروفایل
/save_profile
'''

    await event.reply(str(f"{info_command}"))


@client.on(events.NewMessage(pattern=r'(?i).*/lashi'))
async def bomb(event):
    edit_list = ['کـــ', 'کــص ', ' ن کــص', 'کـــص نـــنـ',
                 'کـــص نـنـتـ', '💝کص نـنـت', '☘کـــص نـنـت دیگه☘']
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1)


@client.on(events.NewMessage(pattern=r'(?i).*/eshgh'))
async def bomb(event):
    edit_list = ['💛💛💛💛💛', '🧡🧡🧡🧡🧡', '💛💛💛💛💛', '💖💖💖💖💖',
                 '💞💞💞💞💞', '💝💝💝💝💝', '💕💕💕💕💕', '💗💗💗💗💗', 'I love🙂🧡']
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1)


@client.on(events.NewMessage(pattern=r'(?i).*/angosht'))
async def bomb(event):
    edit_list = ["👌________________👈", "👌_______________👈", "👌______________👈",
                 "👌__________👈", "👌_________👈", "👌________👈", '👌____👈', '👌_👈', '✌انگشت شد✌']
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1)


@client.on(events.NewMessage(pattern=r'(?i).*/pashm'))
async def bomb(event):
    edit_list = ['🍂🍂🍂🍂🍂🍂🍂🍂🍂🍂🍂🍂🍂🍂🍂', '🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁', '🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃', '🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱', '☘️☘️☘️☘️☘️☘️☘️☘️☘️☘️☘️☘️☘️☘️☘️',
                 'پشم دیگه ندارم ولی برگام ریخت بمولا', '🍃🍂🍁🌱🌿☘️🍀🍃🍁🍂🌿🌱☘️🍀🍃', '🍂🍁🌱🌿🍂🍁🌱🌿🍂🍁🌱🌿🍂🍁🌱🌿', 'دیگه برگی برام نمونده ']
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1)


# return anbo bomb :)
@client.on(events.NewMessage(pattern=r'(?i).*/bomb'))
async def bomb(event):
    edit_list = ["💣————————————————————————————🚑", "💣————————————————————————🚑",
                 "💣————————————————————🚑", "💣————————————🚑", "💣———🚑", "💥BOOOM💥"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1)


# return monkey
@client.on(events.NewMessage(pattern=r'(?i).*/monkey'))
async def mankes(event):
    edit_list = ["🐒", "🙊", "🙉", "🙈", "🐵"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1.5)
# return colors


@client.on(events.NewMessage(pattern=r'(?i).*/colors'))
async def colors(event):
    edit_list = ["🟧🟨🟩🟦🟪", "🟫🟨🟩🟦🟪", "🟦🟫🟥🟦🟩", "🟧🟪🟩⬜️⬛️", "🟧🟨🟩🟦🟪🔳", "🟧🟨🟩🟦🔳🟪",
                 "🟧🟨🟩🔳🟦🟪", "🟧🟨🔳🟩🟦🟪", "🟧🔳🟨🟩🟦🟪", "🔳🟧🟨🟩🟦🟪", "🔳🔳🟨🟩🟦🟪", "🔳🔳🔳🟩🟦🟪",
                 "🔳🔳🔳🔳🔳🔳", "🔲🔲🔲🔲🔲🔲", "🔳🔳🔳🔳🔳🔳", "FINISH 🟡🟠🔴🟢🔵🟣⚫️⚪️🟤", "FINISH 🟡⚫️⚪️🟤🟢🔵🟣🟠🔴"]

    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(0.9)


# return fuck you
@client.on(events.NewMessage(pattern=r'(?i).*/fuck_you'))
async def fuck(event):
    edit_list = ["*fuck you*🖕🏿🖕🏾🖕🏽🖕🏼🖕🏻🖕", "🖕🏿", "*Fuck you*🖕🖕🏻🖕🏼🖕🏽🖕🏾🖕🏿""🖕", "*FUck you*🖕🏿🖕🖕🏾🖕🏻🖕🏽🖕🏼", "🖕🏻",
                 "*FUCk you*🖕🏼🖕🖕🏻🖕🏽🖕🏾🖕🏿", "🖕🏾", "*FUCK You*🖕🏼🦶🏻👊👺", "🖕", "🖕🏻", "🖕🏾", "🖕🖕🏻", "🖕🏿🖕🏿🖕🏿", "🖕🏼🖕🏼🖕🏼", "🖕🏼"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1)


# return sheet
@client.on(events.NewMessage(pattern=r'(?i).*/shet'))
async def sheet(event):
    edit_list = ["shet😐🤦‍♂️", "sheet😐🤦‍♂️", "sheeeet😐🤦‍♂️",
                 "sheeeeet😐🤦‍♂️", "sheeeeeeeet😐🤦‍♂️", "sheeeeeeeeeeeeet😐🤦‍♂️", "😐💔"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1.51)


# return all smail
@client.on(events.NewMessage(pattern=r'(?i).*/smail'))
async def smale(event):
    edit_list = ["😀", "😃", "😄", "😁", "😆", "😂", "🤣"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1.81)


# return nasa hacking
@client.on(events.NewMessage(pattern=r'(?i).*/hack_nasa'))
async def smale(event):
    edit_list = ["HACKING 🕸NASA🕸...\n<[##        ]> 20%", "HACKING 🕸NASA🕸..\n<[###       ]> 30%",
                 "HACKING 🕸NASA🕸...\n<[####      ]> 40%", "HACKING 🕸NASA🕸..\n<[#####     ]> 50%", "HACKING 🕸NASA🕸...\n<[######    ]> 60%",
                 "HACKING 🕸NASA🕸..\n<[#######   ]> 70%", "HACKING 🕸NASA🕸...\n<[########  ]> 80%", "HACKING 🕸NASA🕸..\n<[######### ]> 90%",
                 "HACKING 🕸NASA🕸...\n<[##########]> 100%", "nasa hacked 😐🕷", "*fuck you*🖕🏿🖕🏾🖕🏽🖕🏼🖕🏻🖕"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1)


# return all mah
@client.on(events.NewMessage(pattern=r'(?i).*/mah'))
async def mah(event):
    edit_list = ["🌑🌑", "🌘🌘", "🌗🌗", "🌖🌖", "🌕🌕", "🌔🌔", "🌓🌓",
                 "🌒🌒", "🌑🌑", "🌑🌑🌑", "🌘🌘🌘", "🌗🌗🌗", "🌖🌖🌖", "🌕🌕🌕", "🌔🌔🌔", "🌓🌓🌓",
                 "🌒🌒🌒", "🌑🌑🌑", "🌑🌑🌑🌑", "🌘🌘🌘🌘", "🌗🌗🌗🌗", "🌖🌖🌖🌖", "🌕🌕🌕🌕", "🌔🌔🌔🌔", "🌓🌓🌓🌓",
                 "🌒🌒🌒🌒", "🌑🌑🌑🌑", "🌑"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1)


# get time system and return
@client.on(events.NewMessage(pattern=r'(?i).*/time_now'))
async def time_now(event):
    list_emogy = ["🕐", "🕑", "🕒", "🕓", "🕔",
                  "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛", "🕛"]
    list_mah = ["🌑🌑", "🌘🌘", "🌗🌗", "🌖🌖", "🌕🌕", "🌔🌔", "🌓🌓", "🌒🌒", "🌑🌑"]
    for i in range(0, 100):
        for mah in list_mah:
            for char in list_emogy:
                timer = time.localtime()
                time_info = tuple(timer)
                year = time_info[0]
                mon = time_info[1]
                day = time_info[2]
                now = datetime.now()
                timing = now.strftime("%H : %M : %S")
                result = f'''{mah}YEAR : {year}
{mah}MON : {mon}
{mah}DAY : {day}
    {char} {timing} {char}
                '''
                await event.edit((str(result)))
                time.sleep(0.1)


@client.on(events.NewMessage(pattern=r'(?i).*/love'))
async def love(event):
    edit_list = ["❤️", "💛", "🧡", "💚", "💙", "💜", "🖤", "💜", "💙", "💚", "💛", "🧡", "❤️", "🧡", "💛",
                 "💚", "💙", "💜", "🖤", "❤️🖤", "🖤❤️", "🖤❤️❤️🖤", "🖤❤️❤️🖤🖤❤️❤️🖤", "❤️🖤🖤❤️❤️🖤🖤❤️",
                 "🖤❤️❤️🖤🖤❤️❤️🖤", "❤️🖤🖤❤️❤️🖤🖤❤️", "🖤❤️❤️🖤🖤❤️❤️🖤", "❤️🖤🖤❤️❤️🖤🖤❤️"
                 "❤️I LOVE YOU ❤️", "I LOVE YOU", "❤️I LOVE YOU❤️", "I LOVE YOU", "❤️I LOVE YOU❤️"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1)


@client.on(events.NewMessage(pattern=r'(?i).*/lov'))
async def love(event):
    edit_list = ["❤️", "💛", "🧡", "💚", "💙", "💜", "🖤", "💜", "💙", "💚", "💛", "🧡", "❤️", "🧡", "💛",
                 "💚", "💙", "💜", "🖤", "❤️🖤", "🖤❤️", "🖤❤️❤️🖤", "🖤❤️❤️🖤🖤❤️❤️🖤", "❤️🖤🖤❤️❤️🖤🖤❤️",
                 "🖤❤️❤️🖤🖤❤️❤️🖤", "❤️🖤🖤❤️❤️🖤🖤❤️", "🖤❤️❤️🖤🖤❤️❤️🖤", "❤️🖤🖤❤️❤️🖤🖤❤️",
                 "💙"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1)


@client.on(events.NewMessage(pattern=r'(?i).*/go_time'))
async def go_time(event):
    edit_list = ["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛", "🕛",
                 "🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛", "🕛",
                 "🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛", "🕛"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1.1)


@client.on(events.NewMessage(pattern=r'(?i).*/fuck'))
async def khak(event):
    edit_list = ["🙍‍♂️", "🤦‍♂️", "🙍‍♂️", "🤦‍♂️",
                 "🙍‍♂️", "🤦‍♂️", "🙍‍♂️", "🤦‍♂️", "🚶‍♂️🚬"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1.4)


@client.on(events.NewMessage(pattern=r'(?i).*/get_photo'))
async def get_photo(event):
    edit_list = ["واستا میخام ازت عکس بگیرم 😆📷",
                 "آها گرفتم 📸", "بیا اینم عکست | 🐒|     😁🖖"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1.6)


@client.on(events.NewMessage(pattern=r'(?i).*/dast_ha'))
async def dast_ha(event):
    edit_list = ["✋", "☝️", "✌️", "🤘", "🤟", "🖐",
                 "🖖", "✋", "☝️", "✌️", "🤘", "🤟", "🖐", "🖖"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1.4)


@client.on(events.NewMessage(pattern=r'(?i).*/carzy'))
async def devane(event):
    edit_list = ["😝", "😛", "😜", "🤪", "😝", "😛", "😜"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1.6)


@client.on(events.NewMessage(pattern=r'(?i).*/sleep'))
async def devane(event):
    edit_list = ["😯", "😲", "🥱", "😴"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1.6)


@client.on(events.NewMessage(pattern=r'(?i).*/pink_heart'))
async def pink_heart(event):
    edit_list = ["💜", "🤍", "💟"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1.6)


@client.on(events.NewMessage(pattern=r'(?i).*/pink_love'))
async def pink_love(event):
    edit_list = ["💖", "💗", "💓", "💕", "💞", "💝", "💘"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1.6)


@client.on(events.NewMessage(pattern=r'(?i).*/life'))
async def life(event):
    edit_list = ["👶", "👦", "🧒", "👨", "👫",
                 "👨‍👩‍👦", "👨‍👩‍👧‍👦", "🧔", "👴", "⚰️", "🖤🚬"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1.7)


@client.on(events.NewMessage(pattern=r'(?i).*/smalle_ice'))
async def smalle_ice(event):
    edit_list = ["😁", "😬", "😁", "😬", "😁", "😬",
                 "😁", "😬", "😁", "😬", "😁", "😬", "🥶"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1.5)


@client.on(events.NewMessage(pattern=r'(?i).*/flags'))
async def flags(event):
    edit_list = ["🏴", "🏳️", "🏁"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1)


@client.on(events.NewMessage(pattern=r'(?i).*/mylove'))
async def flags(event):
    edit_list = ["د", "دو", "دوس", "دوست", "دوست د", "دوست دا", "دوست دار", "دوست دارم", "دوست دارم چ", "دوست دارم چو",
                 "دوست دارم چون",
                 "😂 دو ست دارم چون باشگاهم ست دوم هم تموم شد ست اخر تموم بشه میگم بهت "]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1.5)


@client.on(events.NewMessage(pattern=r'(?i).*/mylov2'))
async def flags(event):
    edit_list = ["د", "دو", "دوس", "دوست", "دوست د", "ادوست د", "دوست دار",
                 "دوست دارم", "دوست دارم م", "دوست دارم ما", "دوست دارم ماد", "دوست دارم مادر"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1.5)


@client.on(events.NewMessage(pattern=r'(?i).*/goal'))
async def flags(event):
    edit_list = ["راستش", " راستش میخوام", "راستش میخوام ب", "راستش میخوام بک", "راستش میخوام بکن", "راستش میخوام بکنم", "راستش میخوام بکنمت",
                 "راستش میخوام بکنمت ولی", " راستش میخوام بکنمت ولی گل", "راستش میخوام بکنمت ولی گل کندن", "راستش میخوام بکنمت ولی گل کندن نداره"]
    for text in edit_list:
        await event.edit(str(f"{text}"))
        time.sleep(1.5)
####################################################
####################################################


@client.on(events.NewMessage(outgoing=True, pattern=r'(?i).*/translator'))
async def main(event):
    cammand = event.raw_text
    await event.edit(str("درحال ترجمه ..."))
    # print(cammand[11:])
    to_translate = str(cammand[11:])
    en = translate(to_translate, 'en')
    ar = translate(to_translate, 'ar')
    fa = translate(to_translate, 'fa')
    it = translate(to_translate, 'it')
    ru = translate(to_translate, 'ru')
    resault = f'''⚡️ترجمه کلمه 📄 {to_translate}
به زبان های 🌎🌏🌍
انگلیسی 👨‍🏫 فارسی👨‍🏫روسی🧑‍🏫ایتالیای🧑‍🏫عربی👨‍🏫
〰️〰️〰️〰️〰️〰️
〽️انگلیسی : {en}
〽️فارسی: {fa}
〽️روسی: {ru}
〽️ایتالیای: {it}
〽️عربی: {ar}
    '''

    await event.edit(str(resault))

    if __name__ == '__main__':
        main()

###################################################
###################################################


@client.on(events.NewMessage(outgoing=True, pattern=r'(?i).*/save'))
async def save_file(event):
    await event.edit("در حال ذخیره سازی...")
    if event.is_reply:
        replied = await event.get_reply_message()
        print(replied.media)
        path = os.getcwd()
        await client.download_media(replied, str(path))

        await event.edit(str(f"ذخیره شد در {path}"))


@client.on(events.NewMessage(outgoing=True, pattern=r'(?i).*/save_profile'))
async def save_profile(event):
    await event.edit("در حال ذخیره سازی...")
    if event.is_reply:
        replied = await event.get_reply_message()
        sender = replied.sender
        path = os.getcwd()
        await client.download_profile_photo(sender, path)

        await event.edit('پروفایل @{} ذخیره شد'.format(sender.username))


@client.on(events.NewMessage(outgoing=True, pattern=r'(?i).*/sys_info'))
async def sys_info(event):
    for i in range(0, 50):
        cpu_info = psutil.cpu_times_percent()
        cpu_usage = cpu_info[0]
        # print(cpu_usage)
        MEMORY = psutil.virtual_memory()
        result = f"""**CPU** `SYSTEM` : {cpu_usage} %
**MEMORY** `SESTEM` : {MEMORY[2]} %"""
        await event.edit(str(result))
        time.sleep(1)


###############################################################
#####  Spamers #####
###############################################################
@client.on(events.NewMessage(outgoing=True, pattern=r'(?i).*/spm'))
async def spm(event):
    command = str(event.raw_text)
    command = command.split(":")
    text = command[1]
    number = command[2]
    for i in range(0, int(number)):
        await event.respond(str(text))


@client.on(events.NewMessage(outgoing=True, pattern=r'(?i).*/edit_spamer'))
async def spm(event):
    command = str(event.raw_text)
    command = command.split(":")
    text = command[1]
    number = command[2]
    text = text + '\n'
    out_put = str(text) * int(number)
    await event.edit(str(out_put))


@client.on(events.NewMessage(outgoing=True, pattern=r'(?i).*/say'))
async def say_word(event):
    command = str(event.raw_text)
    command = command.split(':')
    text = command[1]
    engine = pyttsx3.init()  # object creation

    """Saving Voice to a file"""
    # On linux make sure that 'espeak' and 'ffmpeg' are installed
    engine.save_to_file(f'{text}', f'{text}.mp3')
    engine.runAndWait()

    await client.send_file('me', f'{text}.mp3', attributes=[types.DocumentAttributeAudio(
        duration=7,
        voice=True,
        waveform=utils.encode_waveform(bytes(range(2 ** 5))  # 2**5 because 5-bit
                                       ))])


def proccess_data(data):
    return {"city": data['name'], "datetime": time.ctime(int(data['dt'])), "temp": data['main']['temp'], "humidity": data['main']['humidity']}


def get_weather_data(city, appid='85893261f011147fe8dd2c2a26740412'):
    URL = "https://api.openweathermap.org/data/2.5/weather"
    PARAMS = {'q': city, 'appid': appid}
    r = requests.get(url=URL, params=PARAMS)
    return proccess_data(r.json())


@client.on(events.NewMessage(outgoing=True, pattern=r'(?i).*/weather'))
async def weather(event):
    command = str(event.raw_text)
    command = command.split(':')
    city = command[1]
    out_put = get_weather_data(city=city)
    print(out_put)
    out_put = json.loads
    out_put = out_put['temp']
    event.edit(f'{out_put}')


##################################
####### google search #######
#################################
@client.on(events.NewMessage(outgoing=True, pattern=r'(?i).*/google_search'))
async def google_search(event):
    command = str(event.raw_text)
    command = command.split(":")
    print(command)
    query = command[1]
    print(query)
    result = ''
    for i in search(query):
        result += '>> ' + i + '\n\n'
    # for results in result:
    await event.edit(result)


client.start()
client.run_until_disconnected()
