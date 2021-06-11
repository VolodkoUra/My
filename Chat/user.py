from my_chat import My_Chat

class User(My_Chat):
    """
    Хранение имини пользователя
    отправить сообщение
    получить список сообщений
    """
    user_name: str


    def __init__(self, user_name):
        self.user_name = user_name
        self.message_list = []



