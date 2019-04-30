# -*- coding:utf-8 -*-
# @Time  : 2019/4/19 17:12
# @Author: lisa.liu
# @Email : 2423844@qq.com
# @File  : testcase_recharge.py


from common import DoExcel
import unittest
import json
from ddt import ddt, data, unpack
from common.HttpRequest import HttpRequest
from common import contents
from common.do_mysql import DoMySQL


@ddt
class TestRecharge(unittest.TestCase):
    myexcel = DoExcel.DoExcel(contents.case_file, 'recharge')
    cases = myexcel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest()
        cls.mysql=DoMySQL()

    @data(*cases)
    def test_recharge(self, case):

        expected = str(case.expected)
        if case.sql:
            sql=case.sql
            sql_re = self.mysql.fetch_one(sql)
            print(sql_re['leaveamount'])
            before = sql_re['leaveamount']


        res = self.http_request.http_request(case.method, case.url, eval(case.data))
        print(res.text)
        res_code = res.json()['code']
        print(case.title)
        try:
            self.assertEqual(res_code, expected)
        except AssertionError as e:
            self.myexcel.write_result(case.case_id + 1, res_code, 'FAIL')
            raise e
        else:
            self.myexcel.write_result(case.case_id + 1, res_code, 'PASS')
            if case.sql:
                sql = case.sql
                sql_re = self.mysql.fetch_one(sql)
                print(sql_re['leaveamount'])
                after = sql_re['leaveamount']
                add=int(eval(case.data)['amount'])
                self.assertEqual(before+add,after)


    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
