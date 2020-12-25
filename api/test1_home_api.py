# 导包
import requests
from utile import app


class HomeApi:
    def __init__(self):
        # 轮播图
        self.banner_url = app.host_url + "/banner/{}"
        # 专题栏
        self.theme_url = app.host_url + "/theme"
        # 最近新品
        self.product_url = app.host_url + "/product/recent"

    def banner(self, banner_id=1):
        # banner_id:轮播图id
        return requests.get(self.banner_url.format(banner_id))

    def theme(self, ids="1, 2, 3"):
        # ids:专题id值,单个或者多个
        data = {"ids": ids}
        return requests.get(self.theme_url, params=data)

    def product(self):
        return requests.get(self.product_url)
