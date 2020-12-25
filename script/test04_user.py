import unittest
from api.test5_apiFactory import ApiFactory
from utile import app
from utile.auto_assert import auto
from utile.analysis_data import AnalysisData
from parameterized import parameterized


class TestUser(unittest.TestCase):
    @parameterized.expand(AnalysisData.get_json_data("user.json", "token", ["token_code", "token_length"]))
    def test1_token(self, token_code, token_length):
        print("token_code:{}, token_length:{}".format(token_code, token_length))
        # token_code = 200
        # token_length = 0
        response = ApiFactory.user_api().create_token()
        auto(self, response.status_code, token_code)
        auto(self, len(response.json()), token_length, "more")
        app.header["token"] = response.json().get("token")
        print("app:{}".format(app.header))

    @parameterized.expand(AnalysisData.get_json_data("user.json", "verify", ["verify_code", "verify_isValid"]))
    def test2_verify(self, verify_code, verify_isValid):
        print("verify_code:{}, verify_isValid:{}".format(verify_code, verify_isValid))
        # verify_code = 200
        # verify_isValid = True
        response = ApiFactory.user_api().verify_token()
        auto(self, response.status_code, verify_code)
        auto(self, response.json().get("isValid"), verify_isValid)

    @parameterized.expand(AnalysisData.get_json_data("user.json", "address", ["address_code", "address_name", "address_mobile"]))
    def test3_address(self, address_code, address_name, address_mobile):
        print("address_code:{}, address_name:{}, address_mobile:{}".format(address_code, address_name, address_mobile))
        # address_code = 200
        # address_name = "李白"
        # address_mobile = "13012345678"
        response = ApiFactory.user_api().address_user()
        auto(self, response.status_code, address_code)
        auto(self, response.json().get("name"), address_name)
        auto(self, response.json().get("mobile"), address_mobile)