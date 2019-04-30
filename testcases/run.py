#-*- coding:utf-8 -*-
# @Time  : 2019/4/29 18:32
# @Author: lisa.liu
# @Email : 2423844@qq.com
# @File  : run.py

import unittest
from testcases import testcase_login,testcase_register,testcase_invest,testcase_recharge
from common import HTMLTestRunnerNew
from common import contents

suite = unittest.TestSuite()
loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(testcase_register))
# suite.addTest(loader.loadTestsFromModule(testcase_login))
# suite.addTest(loader.loadTestsFromModule(testcase_recharge))
# suite.addTest(loader.loadTestsFromModule(testcase_invest))

discover = unittest.defaultTestLoader.discover(contents.case_dir,"testcase_*.py")

with open(contents.report_dir+'/report.html','wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,title='Lisa.HTTPTEST',description='qianchengdai',tester='Lisa.Liu')
    runner.run(discover)