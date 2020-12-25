from api.test1_home_api import HomeApi
from api.test2_category import CategoryApi
from api.test3_user import UserApi
from api.test4_order import OrderApi


class ApiFactory:
    # 前提:将来所有定义的接口类都需要在这里实例化返回所有接口实例化对象
    @classmethod
    def home_api(cls):
        # 返回首页接口类对象
        return HomeApi()

    @classmethod
    def category_api(cls):
        # 返回订单接口类对象
        return CategoryApi()

    @classmethod
    def user_api(cls):
        # 返回用户接口类对象
        return UserApi()

    @classmethod
    def order_api(cls):
        # 返回商品接口类对象
        return OrderApi()