from telethon import TelegramClient, sync

api_id = 25316255
api_hash = 'caacc56333e6d2445732ea75eddd56e5'


client = TelegramClient('session_name1', api_id, api_hash,system_version='4.16.30-vxCUSTOM')
client.start()

group = -1002299003223

messages = client.get_entity(group)
client.send_message(group, 'проверка бота')

