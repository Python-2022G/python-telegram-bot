from telegram import Bot
import requests

TOKEN = '6203711973:AAGQ0KgDqOiko9KnQZOF1i8hIluAuCuBWDk'

# create bot object
bot = Bot(TOKEN)

# get updates
last_update = bot.get_updates()[-1]

print(last_update.message.message_id)



# get chat_id
# chat_id = last_update.message.chat.chat_id
# text    = last_update.message.text

# print(chat_id, text)

# # send message
# bot.send_message(chat_id, text)


# # reply message
# message = last_update.message
# message.reply_text("I'm a bot, please talk to me!", bot)
