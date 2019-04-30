#-*- coding:utf-8 -*-
# @Time  : 2019/4/25 17:50
# @Author: lisa.liu
# @Email : 2423844@qq.com
# @File  : testcase_invest.py

#-*- coding:utf-8 -*-
# @Time  : 2019/4/23 18:12
# @Author: lisa.liu
# @Email : 2423844@qq.com
# @File  : testcase_add.py

from common import DoExcel
import unittest
import json
from ddt import ddt, data, unpack
from common.HttpRequest import HttpRequest
from common import contents
from common import do_mysql
from common import config
from common.context import replace
from common.context import Context


@ddt
class TestInvest(unittest.TestCase):
    myexcel = DoExcel.DoExcel(contents.case_file, 'invest')
    cases = myexcel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest()
        cls.mysql = do_mysql.DoMySQL()
        cls.config = config.ReadConfig()

    @data(*cases)
    def test_invest(self, case):

        case.data = eval(replace(case.data))
        expected = str(case.expected)
        if case.sql:
            sql=case.sql
            sql_re = self.mysql.fetch_one(sql)
            print('投资前余额',sql_re['leaveamount'])
            before = sql_re['leaveamount']

        res = self.http_request.http_request(case.method, case.url, case.data)
        print(case.title)
        print(case.data)
        print(res.text)

        try:
            self.assertEqual(res.json()['code'], expected)
        except AssertionError as e:
            self.myexcel.write_result(case.case_id + 1, res.json()['code'], 'FAIL')
            raise e
        else:
            self.myexcel.write_result(case.case_id + 1, res.json()['code'], 'PASS')
            if res.json()['msg'] == '加标成功':
                sql = "SELECT id FROM future.loan where memberid=1150 ORDER BY id desc"
                loan_id = self.mysql.fetch_one(sql)['id']
                print('loan_id',loan_id)
                setattr(Context,'loan_id',loan_id) #保存到类属性
                print('invest','loan_id',type(Context.loan_id),Context.loan_id)
            if case.sql:
                sql = case.sql
                sql_re = self.mysql.fetch_one(sql)
                print('投资后余额',sql_re['leaveamount'])
                after = sql_re['leaveamount']
                add = int(case.data['amount'])
                self.assertEqual(before-add, after)


    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        #cls.mysql.close()