import unittest
from utile.HTMLTestRunner_PY3 import HTMLTestRunner

from script.test02_home import TestHome
from script.test03_category import TestCategory
from script.test04_user import TestUser
from script.test05_order import TestOrder

suite = unittest.TestSuite()
suite_list = [TestHome, TestCategory, TestUser, TestOrder]
# suite_list = [TestUser]
for i in suite_list:
    suite.addTest(unittest.makeSuite(i))
report = "./report.html"

with open(report, "wb")as f:
    runner = HTMLTestRunner(f, title="小程序")
    runner.run(suite)


