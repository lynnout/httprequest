#-*- coding:utf-8 -*-
# @Time  : 2019/4/17 18:14
# @Author: lisa.liu
# @Email : 2423844@qq.com
# @File  : HttpRequest.py

import  requests
import json
from common import logger

logger = logger.get_logger(__name__)

#session调用的方法
class HttpRequest:
    def __init__(self):
        self.session = requests.sessions.session()

    def http_request(self,method,url,data,json=None):
        logger.debug('请求的url:{}'.format(url))
        logger.debug('请求的data:{}'.format(data))

        method = method.lower()
        if method == 'get':
            res=self.session.request(method=method,url=url,params=data)
        elif method=='post':
            if json:
                res=self.session.request(method=method,url=url, json=json)
            else:
                res=self.session.request(method=method,url=url, data=data)

        else:
            res=None
            logger.error('Unsupported method')
        return res

    def close(self):
        self.session.close()



if __name__=='__main__':
    url = 'http://test.lemonban.com/futureloan/mvc/api/'
    login = 'member/login'
    register = 'member/register'
    recharge = 'member/recharge'
    data = {'mobilephone': '18616728419', 'pwd': '123456', 'regname': 'lynnout', 'amount': '1000'}
    my_request=HttpRequest()
    my_request_login = my_request.http_request('post',url + login, data)
    print(my_request_login.url)
    print(my_request_login.text)
    my_request_recharge = my_request.http_request('post',url + recharge, data)
    print(my_request_recharge.url)
    print(my_request_recharge.text)
    my_request.close()