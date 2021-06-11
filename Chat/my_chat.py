class My_Chat:
    """
    Хранение сообщений
    Функция отправкаи
    Функция вывода списака
    """
    message_list: list

    def send_message(self, text):
        self.message_list.append(text)

    def get_massage_list(self):
        return self.message_list
