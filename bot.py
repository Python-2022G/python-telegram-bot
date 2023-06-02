from telegram import Bot
import os
import requests

# get TOKEN from environment variable
TOKEN = os.environ['TOKEN']

# create bot object
bot = Bot(TOKEN)

# get updates
last_update = bot.get_updates()[-1]

# get chat_id
chat_id = last_update.message.chat.chat_id
text    = last_update.message.text

# send message
bot.send_message(chat_id, text)


# reply message
message = last_update.message
message.reply_text("I'm a bot, please talk to me!", bot)
