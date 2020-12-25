import unittest
from api.test5_apiFactory import ApiFactory
from utile.auto_assert import auto
from utile.analysis_data import AnalysisData
from parameterized import parameterized


# def home_data():
#     banner_list = []
#     theme_list = []
#     product_list = []
#     # 读取json文件数据
#     json_data = AnalysisData.get_json_data("home.json")
#     # 解析 组装成[()]
#     for i in json_data.get("banner"):
#         banner_list.append((i.get("banner_code"), i.get("banner_id"),
#                             i.get("banner_name"), i.get("banner_length")))
#
#     for a in json_data.get("theme"):
#         theme_list.append((a.get("theme_code"), a.get("theme_ids"),
#                            a.get("theme_length_url"), a.get("theme_name")))
#
#     for s in json_data.get("product"):
#         product_list.append((s.get("product_code"), s.get("product_length"),
#                              s.get("product_keys")))
#
#     return {"banner": banner_list, "theme": theme_list, "product": product_list}


class TestHome(unittest.TestCase):
    @parameterized.expand(AnalysisData.get_json_data("home.json", "banner", ["banner_code", "banner_id", "banner_name", "banner_length"]))
    def test01_banner(self, banner_code, banner_id, banner_name, banner_length):
        # # 状态码
        # banner_code = 200
        # # id
        # banner_id = 1
        # # name
        # banner_name = "首页置顶"
        # # items长度大于0
        # banner_length = 0
        # 请求
        print("banner_code:{}, banner_id:{}, banner_name:{}, banner_length:{}".format(banner_code, banner_id, banner_name, banner_length))
        response = ApiFactory.home_api().banner()
        # 断言-状态码
        auto(self, response.status_code, banner_code)
        # 断言-id
        auto(self, response.json().get("id"), banner_id)
        # 断言-name
        auto(self, response.json().get("name"), banner_name)
        # 断言items长度大于0
        auto(self, len(response.json().get("items")), banner_length, tag="more")
        # 断言图片url不为空
        auto(self, len(response.json().get("items")[0].get("img").get("url")), banner_length, tag="more")

    @parameterized.expand(AnalysisData.get_json_data("home.json", "theme", ["theme_code", "theme_ids", "theme_length_url", "theme_name"]))
    def test02_theme(self, theme_code, theme_ids, theme_length_url, theme_name):
        # 状态码
        # theme_code = 200
        # # id=1, id=2, id=3
        # theme_ids = ['id":1', 'id":2', 'id":3']
        # # 长度-url
        # theme_length_url = 0
        # # name
        # theme_name = "专题栏位一"
        # 请求
        print("theme_code:{}, theme_ids:{}, theme_length_url:{}, theme_name:{}".format(theme_code, theme_ids, theme_length_url, theme_name))
        response = ApiFactory.home_api().theme()
        # 断言-状态码
        auto(self, response.status_code, theme_code)
        # 断言- id=1, id=2, id=3
        for i in theme_ids:
            auto(self, i, response.text, tag="in")
        # 断言-长度
        auto(self, len(response.json()), theme_length_url, tag="more")
        # 断言-name
        auto(self, response.json()[0].get("name"), theme_name)
        # 断言-url
        auto(self, len(response.json()[0].get("topic_img").get("url")), theme_length_url, tag="more")

    @parameterized.expand(AnalysisData.get_json_data("home.json", "product", ["product_code", "product_length", "product_keys"]))
    def test03_product(self, product_code, product_length, product_keys):
        # # 状态码
        # product_code = 200
        # # 长度
        # product_length = 0
        # # 关键字段
        # product_keys = ["id", "name", "price", "main_img_url"]
        print("product_code:{}, product_length:{}, product_keys:{}".format(product_code, product_length, product_keys))
        response = ApiFactory.home_api().product()
        # 断言-状态码
        auto(self, response.status_code, product_code)
        # 断言-长度
        auto(self, len(response.json()), product_length, tag="more")
        # 断言-关键字段
        for i in product_keys:
            auto(self, i, response.text, tag="in")

