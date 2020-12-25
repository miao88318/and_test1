import requests
from utile import app


class CategoryApi:
    def __init__(self):
        self.category_url = app.host_url + "/category/all"
        self.classify_url = app.host_url + "/product/by_category"
        self.commodity_url = app.host_url + "/product/{}"

    def category(self):
        return requests.get(self.category_url)

    def classify(self, id_data="2"):
        data = {"id": id_data}
        return requests.get(self.classify_url, params=data)

    def commodity(self, commodity_id):
        return requests.get(self.commodity_url.format(commodity_id))
