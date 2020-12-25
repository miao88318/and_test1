import requests
from utile import app


class UserApi:
    def __init__(self):
        # 创建token
        self.token_url = app.host_url + "/token/user"
        # 验证token
        self.verify_url = app.host_url + "/token/verify"
        # 获取地址
        self.address_url = app.host_url + "/address"

    def create_token(self):
        data = {"code": app.code}
        return requests.post(self.token_url, headers=app.header, json=data)

    def verify_token(self):
        data = {"token": app.header.get("token")}
        return requests.post(self.verify_url, headers=app.header, json=data)

    def address_user(self):
        return requests.get(self.address_url, headers=app.header)