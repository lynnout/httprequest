#-*- coding:utf-8 -*-
# @Time  : 2019/4/19 18:14
# @Author: lisa.liu
# @Email : 2423844@qq.com
# @File  : config.py

from configparser import ConfigParser
from common import contents


class ReadConfig:
    '''完成配置文件的读取'''
    def __init__(self):
        self.config=ConfigParser()
        self.config.read(contents.global_file)
        switch = self.config.getboolean('switch','on')
        if switch:
            self.config.read(contents.online_file,encoding='utf-8')
        else:
            self.config.read(contents.test_file,encoding='utf-8')

    def get(self,section,option):
        return self.config.get(section,option)


if __name__=='__main__':
    config=ReadConfig()
    print(config.get('api','pre_url'))