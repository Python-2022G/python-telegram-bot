class Chat:
    def __init__(self, chat_id, first_name, last_name=None, username=None):
        self.chat_id = chat_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
    
    def to_dict(self):
        return {
            'chat_id': self.chat_id, 
            'first_name': self.first_name, 
            'last_name': self.last_name, 
            'username': self.username
        }
    