import requests
import json

def logger(f):




class User:
    nickname: str
    url: str = ""
    massege: str

    def __init__(self, nickname, url):
        self.nickname = nickname
        self.url = url
        self.session = requests.session()

    def post_login(self):
        response = self.session.post(self.url + '/login', json={"u_name": self.nickname})
        return f"{response.status_code} - {response.text}"

    def get_massege(self):
        response = self.session.get(self.url + '/get_messages')

        for value in json.loads(response.text).values():
            for val in value:
                #print(val)
                if val:
                    for key, value in val.items():
                        print(f"{key}: {value}")
                else:
                    continue

    def send_massege(self, massage):
        response = self.session.post(self.url + '/send_message', json={self.nickname: massage})
        # print(response.status_code)
        return f"{response.status_code} - {response.text}"

    def post_logout(self):
        response = self.session.post(self.url + '/logout', json={"u_name": self.nickname})
        return f"{response.status_code} - {response.text}"
