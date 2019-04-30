#-*- coding:utf-8 -*-
# @Time  : 2019/4/19 16:24
# @Author: lisa.liu
# @Email : 2423844@qq.com
# @File  : testcase_login.py

from common import DoExcel
import unittest
import json
from ddt import ddt,data,unpack
from common.HttpRequest import HttpRequest
from common import contents
from common import logger

logger = logger.get_logger(__name__)


@ddt
class TestLogin(unittest.TestCase):
    myexcel = DoExcel.DoExcel(contents.case_file, 'login')
    cases = myexcel.get_cases()

    def setUp(self):
        self.http_request=HttpRequest()
        logger.info('准备测试前置')


    @data(*cases)
    def test_login(self,case):
        logger.info('开始测试:{}'.format(case.title))
        #
        expected=case.expected
        res=self.http_request.http_request(case.method,case.url,eval(case.data)).text
        print(case.title)
        try:
            self.assertEqual(res, expected)  #assertEqual是对象方法，继承来的
        except AssertionError as e:
            self.myexcel.write_result(case.case_id + 1, res, 'FAIL')
            logger.error('报错了{}'.format(e))
            raise e
        else:
            self.myexcel.write_result(case.case_id + 1, res, 'PASS')

        logger.info('结束测试{}'.format(case.title))


    def tearDown(self):
        logger.info('测试后置处理')
        pass