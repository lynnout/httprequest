#-*- coding:utf-8 -*-
# @Time  : 2019/4/24 14:13
# @Author: lisa.liu
# @Email : 2423844@qq.com
# @File  : context.py

import re
from common import config
from common import do_mysql
import configparser

class Context:

    loan_id = None


def replace(data):
    #print('替换前',data)
    p="#(.*?)#" #正则表达式
    while re.search(p,data):
        g = re.search(p,data).group(1)
        #print(g)
        try:
            conf = config.ReadConfig().get('data',g)
        except configparser.NoOptionError as e:
            conf = str(Context.loan_id)
            print(conf)
#            raise e
        #print(conf)
        data = re.sub(p,conf,data,count=1)
        #print('替换后',data)
    return data

# def replace_sql(data,sql_result):
#     p = "#(.*?)#"  # 正则表达式
#     while re.search(p, data):
#         g = re.search(p, data).group(1)
#         # print(sql_result)
#         data = re.sub(p, sql_result, data, count=1)
#
#         # print('替换后',data)
#     return data


if __name__=='__main__':
    print(Context.loan_id)
    x=replace("{'mobilephone':'#loan_id#','pwd':'#normal_pwd#'}")
    print(x)

