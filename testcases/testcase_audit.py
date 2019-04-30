#-*- coding:utf-8 -*-
# @Time  : 2019/4/24 15:54
# @Author: lisa.liu
# @Email : 2423844@qq.com
# @File  : testcase_audit.py

from common import DoExcel
import unittest
import json
from ddt import ddt, data, unpack
from common.HttpRequest import HttpRequest
from common import contents
from common import do_mysql
from common import config
from common.context import replace


@ddt
class TestAudit(unittest.TestCase):
    myexcel = DoExcel.DoExcel(contents.case_file, 'audit')
    cases = myexcel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest()
        cls.config = config.ReadConfig()

    @data(*cases)
    def test_audit(self, case):

        case.data = eval(replace(case.data))
        expected = str(case.expected)
        res = self.http_request.http_request(case.method, case.url, case.data).json()['code']
        print(case.title)
        print(case.data)

        try:
            self.assertEqual(res, expected)
        except AssertionError as e:
            self.myexcel.write_result(case.case_id + 1, res, 'FAIL')
            raise e
        else:
            self.myexcel.write_result(case.case_id + 1, res, 'PASS')

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()