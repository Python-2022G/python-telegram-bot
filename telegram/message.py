from telegram.chat import Chat

class Message:
    def __init__(self, message_id, chat: Chat, text=None, photo=None, audio=None, document=None):
        self.message_id = message_id
        self.chat = chat
        self.text = text
        self.photo = photo
        self.audio = audio
        self.document = document
    
    def reply_text(self, text, bot):
        return bot.send_message(self.chat.chat_id, text)
    
    def reply_photo(self, photo, bot):
        return bot.send_photo(self.chat.chat_id, photo)
    
    def reply_audio(self, audio, bot):
        return bot.send_audio(self.chat.chat_id, audio)
    
    def reply_document(self, document, bot):
        return bot.send_document(self.chat.chat_id, document)
    
    def to_dict(self):
        return {
            'message_id': self.message_id, 
            'chat': self.chat.to_dict(), 
            'text': self.text, 
            'photo': self.photo, 
            'audio': self.audio, 
            'document': self.document
        }
