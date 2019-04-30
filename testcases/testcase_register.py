# -*- coding:utf-8 -*-
# @Time  : 2019/4/18 11:08
# @Author: lisa.liu
# @Email : 2423844@qq.com
# @File  : testcase_register.py

from common import DoExcel
import unittest
import json
from ddt import ddt, data, unpack
from common.HttpRequest import HttpRequest
from common import contents
from common import do_mysql
from random import randint
import re


@ddt
class TestRegister(unittest.TestCase):
    myexcel = DoExcel.DoExcel(contents.case_file, 'register')
    cases = myexcel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest()
        cls.mysql = do_mysql.DoMySQL()

    @data(*cases)
    def test_register(self, case):

        if case.data.find('register_mobile'):
            print(case.data.find('register_mobile'))
            sql = 'select MAX(mobilephone) from future.member'
            max_phone = self.mysql.fetch_one(sql)['MAX(mobilephone)']
            max_phone = int(max_phone) - randint(1000,9999)  #利用随机数生成随机注册号
            print(max_phone)
            case.data = case.data.replace('register_mobile', str(max_phone))  # 替换手机号码
            print(case.data, '这里可以查看一下')

        expected = case.expected
        res = self.http_request.http_request(case.method, case.url, eval(case.data))
        print(case.title)
        print(case.data)

        try:
            self.assertEqual(res.text, expected)
        except AssertionError as e:
            self.myexcel.write_result(case.case_id + 1, res.text, 'FAIL')
            raise e
        else:
            self.myexcel.write_result(case.case_id + 1, res.text, 'PASS')
            if res.json()['msg']=='注册成功':
                print('程序走到了这里')
                sql = "SELECT * FROM future.member where mobilephone=#xxx#"
                print(sql)
                p="#(.*?)#"
                sql=re.sub(p,str(max_phone),sql)
                print('替换后',sql)
                if self.mysql.fetch_one(sql):
                    pass
                else:
                    print("数据库中无注册成功的会员数据")




    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()
