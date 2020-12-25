# from api.test1_home_api import HomeApi
# # 轮播图
# print("轮播图:{}".format(HomeApi().banner().json()))
# # 专题栏
# print("专题栏:{}".format(HomeApi().theme().json()))
# # 最近新品
# print("最近新品:{}".format(HomeApi().product().json()))


from api.test2_category import CategoryApi

# print("分类:{}".format(CategoryApi().category().json()))
# print("商品分类:{}".format(CategoryApi().classify().json()))
# print("商品信息:{}".format(CategoryApi().commodity().json()))


# from utile import app
# from api.test3_user import UserApi
#
# # 创建token
# response = UserApi().create_token().json()
# print("创建token返回值:{}".format(response))
# # 保存token
# app.header["token"] = response.get("token")
# # 验证token
# print("验证token:{}".format(UserApi().verify_token().json()))
# # 获取地址
# print("地址信息:{}".format(UserApi().address_user().json()))

from utile import app
from api.test3_user import UserApi
from api.test4_order import OrderApi
# 创建token
response = UserApi().create_token().json()
print("创建token返回值:{}".format(response))
# 保存token
app.header["token"] = response.get("token")
# 创建订单
print("创建:{}".format(OrderApi().create_order(2, 1).json()))
# 查询订单
print("查看:{}".format(OrderApi().query_order(103).json()))
# 用户订单列表
print("列表:{}".format(OrderApi().user_order(1).json()))