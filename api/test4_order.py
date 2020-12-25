import requests
from utile import app


class OrderApi:
    def __init__(self):
        # 创建订单
        self.create_url = app.host_url + "/order"
        # 查看订单
        self.query_url = app.host_url + "/order/{}"
        # 用户订单列表
        self.user_url = app.host_url + "/order/by_user"

    def create_order(self, product_id=8, count=1):
        data = {"products":[{"product_id":product_id,"count":count}]}
        return requests.post(self.create_url, headers=app.header, json=data)

    def query_order(self, order_id=50):
        return requests.get(self.query_url.format(order_id), headers=app.header)

    def user_order(self, page=1):
        data = {"page": page}
        return requests.get(self.user_url, params=data, headers=app.header)
