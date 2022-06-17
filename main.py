from datetime import datetime
from multiprocessing.connection import Client

import pandas as pd
from telethon import TelegramClient, events, sync
from telethon.sync import TelegramClient
from telethon.tl.types import (ContactStatus, UserStatusOffline,
                               UserStatusOnline)

api_id = '17493881'
api_hash = '1bb6d6baa364cc0fdad29ac8239a4029'
phone = '+13017037129'

with open('/home/alan/Desktop/groups.txt','r') as groupsList:
    groups = groupsList.readlines()

client = TelegramClient('@milanjan', api_id, api_hash)
client.connect()
if not client.is_user_authorized():
  client.send_code_request(phone)
  client.sign_in(phone, input('Enter the code: '))

async def main():
    await client.start()
    user_details = await client.get_entity(groups)
    channelss = await client.get
    print(user_details.username, user_details.status)
    for i in range(len(user_details)):
        print(user_details[i].username, user_details[i].status)



with client:
    client.loop.run_until_complete(main())
