#-*- coding:utf-8 -*-
# @Time  : 2019/4/22 10:54
# @Author: lisa.liu
# @Email : 2423844@qq.com
# @File  : testcase_login_relation.py

#-*- coding:utf-8 -*-
# @Time  : 2019/4/19 16:24
# @Author: lisa.liu
# @Email : 2423844@qq.com
# @File  : testcase_login.py


#该用例用于理解setup和setupclass的执行顺序和执行次数

from common import DoExcel
import unittest
import json
from ddt import ddt,data,unpack
from common.HttpRequest import HttpRequest
from common import contents
from common import config


@ddt
class TestLogin(unittest.TestCase):
    myexcel = DoExcel.DoExcel(contents.case_file, 'login')
    cases = myexcel.get_cases()


    @classmethod
    def setUpClass(cls):
        print("I'm setupClass")

    def setUp(self):
        print("I'm setUp")


    @data(*cases)
    def test_login(self,case):

        print(case.title)
        print(case.url)


    def tearDown(self):
        print("I'm tearDown")

    @classmethod
    def tearDownClass(cls):
        print("I'm tearDownClass")

