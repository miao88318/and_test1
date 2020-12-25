import unittest
from api.test5_apiFactory import ApiFactory
from utile.auto_assert import auto
from utile.analysis_data import AnalysisData
from parameterized import parameterized


# def category_data():
#     category_list = []
#     classify_list = []
#     commodity_list = []
#     json_data = AnalysisData.get_json_data("category.json")
#     for i in json_data.get("category"):
#         category_list.append((i.get("category_code"), i.get("category_length"),
#                              i.get("category_name")))
#     for a in json_data.get("classify"):
#         classify_list.append((a.get("classify_code"), a.get("classify_id"),
#                               a.get("classify_length_url"), a.get("classify_name")))
#     for s in json_data.get("commodity"):
#         commodity_list.append((s.get("commodity_id"), s.get("commodity_code"),
#                                s.get("commodity_name"), s.get("commodity_price"),
#                                s.get("commodity_length_url")))
#
#     return {"category":category_list, "classify": classify_list, "commodity": commodity_list}


class TestCategory(unittest.TestCase):
    @parameterized.expand(AnalysisData.get_json_data("category.json", "category", ["category_code","category_length", "category_name"]))
    def test01_category(self, category_code, category_length, category_name):
        print("category_code:{}, category_length:{}, category_name:{}".format(category_code, category_length, category_name))
        # # 状态码
        # category_code = 200
        # # 长度-url
        # category_length = 0
        # # name
        # category_name = "炒货"
        # 请求
        response = ApiFactory.category_api().category()
        # 断言-状态码
        auto(self, response.status_code, category_code)
        # 断言-长度
        auto(self, len(response.json()), category_length, "more")
        # 断言-name
        auto(self, category_name, response.text, "in")

    @parameterized.expand(AnalysisData.get_json_data("category.json", "classify", ["classify_code", "classify_id", "classify_length_url", "classify_name"]))
    def test02_classify(self, classify_code, classify_id, classify_length_url, classify_name):
        print("classify_code:{}, classify_id:{}, classify_length_url:{}, classify_name:{}".format(classify_code, classify_id, classify_length_url, classify_name))
        # 状态码
        # classify_code = 200
        # # id
        # classify_id = 4
        # # url
        # classify_length_url = 0
        # # name
        # classify_name = "油炸花生 300克"
        # 请求
        response = ApiFactory.category_api().classify(classify_id)
        # 断言状态码
        auto(self, response.status_code, classify_code)
        # 断言-长度
        auto(self, len(response.json()), classify_length_url, "more")
        # 断言-name
        auto(self, classify_name, response.text, "in")

    @parameterized.expand(AnalysisData.get_json_data("category.json", "commodity", ["commodity_id", "commodity_code", "commodity_name", "commodity_price", "commodity_length_url"]))
    def test03_commodity(self, commodity_id, commodity_code, commodity_name, commodity_price, commodity_length_url):
        print("commodity_id:{}, commodity_code:{}, commodity_name:{}, commodity_price:{}, commodity_length_url:{}".format(commodity_id, commodity_code, commodity_name, commodity_price, commodity_length_url))
        # # id
        # commodity_id = 17
        # # 状态码
        # commodity_code = 200
        # # name
        # commodity_name = "油炸花生 300克"
        # # 价格-price
        # commodity_price = "0.01"
        # # 长度url
        # commodity_length_url = 0
        # 请求
        response = ApiFactory.category_api().commodity(commodity_id)
        # 断言状态码
        auto(self, response.status_code, commodity_code)
        # 断言-id
        auto(self, response.json().get("id"), commodity_id)
        # 断言-name
        auto(self, response.json().get("name"), commodity_name)
        # 断言-price
        auto(self, response.json().get("price"), commodity_price)
        # 断言长度-url
        auto(self, len(response.json().get("main_img_url")), commodity_length_url, "more")




