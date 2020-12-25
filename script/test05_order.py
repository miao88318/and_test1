import unittest
from api.test5_apiFactory import ApiFactory
from utile.auto_assert import auto
from utile.analysis_data import AnalysisData
from parameterized import parameterized


class TestOrder(unittest.TestCase):

    @parameterized.expand(AnalysisData.get_json_data("order.json", "create", ["produtc_id", "count", "create_code", "create_length", "create_pass"]))
    def test1_create(self, produtc_id, count, create_code, create_length, create_pass):
        print("produtc_id:{}, count:{}, create_code:{}, create_length:{}, create_pass:{}".format(produtc_id, count, create_code, create_length, create_pass))
        # produtc_id = 2
        # count = 1
        # # 状态码
        # create_code = 200
        # # 长度不为空
        # create_length = 0
        # # pass等于ture
        # create_pass = True
        # 请求
        response = ApiFactory.order_api().create_order(produtc_id, count)
        # 断言-状态码
        auto(self, response.status_code, create_code)
        # 断言-order_id长度
        auto(self, len(response.json().get("order_id")), create_length, "more")
        # 断言 - order_no长度
        auto(self, len(response.json().get("order_no")), create_length, "more")
        # 断言-pass等于ture
        auto(self, response.json().get("pass"), create_pass)

    @parameterized.expand(AnalysisData.get_json_data("order.json", "query", ["query_id", "query_code", "query_order_no", "query_total_price"]))
    def test2_query(self, query_id, query_code, query_order_no, query_total_price):
        print("query_id:{}, query_code:{}, query_order_no:{}, query_total_price:{}".format(query_id, query_code, query_order_no, query_total_price))
        # 订单id
        # query_id = 103
        # # 状态码
        # query_code = 200
        # # 订单no
        # query_order_no = "DC20665823292544"
        # # 订单price
        # query_total_price = "0.01"
        # 请求
        response = ApiFactory.order_api().query_order(query_id)
        # 断言-状态码
        auto(self, response.status_code, query_code)
        # 断言-id
        auto(self, response.json().get("id"), query_id)
        # 断言-order_no
        auto(self, response.json().get("order_no"), query_order_no)
        # 断言-total_price
        auto(self, response.json().get("total_price"), query_total_price)

    @parameterized.expand(AnalysisData.get_json_data("order.json", "user", ["user_code", "user_page", "user_list", "user_keys"]))
    def test3_user(self, user_code, user_page, user_list, user_keys):
        print("user_code:{}, user_page:{}, user_list:{}, user_keys:{}".format(user_code, user_page, user_list, user_keys))
        # # 状态码
        # user_code = 200
        # # 当前页码
        # user_page = 1
        # # 订单列表长度
        # user_list = 0
        # # 关键字段
        # user_keys = ["id", "order_no", "total_price"]
        # 请求
        response = ApiFactory.order_api().user_order(user_page)
        # 断言-状态码
        auto(self, response.status_code, user_code)
        # 断言-当前页数
        auto(self, response.json().get("current_page"), user_page)
        # 断言-订单列表长度
        auto(self, len(response.json().get("data")), user_list, "more")
        # 断言关键字段
        for i in user_keys:
            auto(self, i, response.text, "in")
