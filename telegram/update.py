from telegram.message import Message

class Update:
    def __init__(self, update_id, message: Message):
        self.update_id = update_id
        self.message = message
    
    def to_dict(self):
        return {
            'update_id': self.update_id, 
            'message': self.message.to_dict()
        }
