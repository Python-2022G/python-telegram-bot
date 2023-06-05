from telegram import Bot
import requests
import time

TOKEN = '6203711973:AAGQ0KgDqOiko9KnQZOF1i8hIluAuCuBWDk'

# create bot object
bot = Bot(TOKEN)

# get updates
last_update = bot.get_updates()[-1]

while True:
    curr_update = bot.get_updates()[-1]

    if last_update.update_id != curr_update.update_id:
        chat_id = curr_update.message.chat.chat_id

        if curr_update.message.text == '/start':
            bot.send_message(chat_id, 'Hello, I am a bot!')
        elif curr_update.message.text == '/stop':
            bot.send_message(chat_id, 'Bye!')
        elif curr_update.message.photo:
            bot.send_message(chat_id, 'Photo received!')
        else:
            bot.send_message(chat_id, 'I don\'t understand you!')

        last_update = curr_update

    time.sleep(1)

