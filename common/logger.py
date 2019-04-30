#-*- coding:utf-8 -*-
# @Time  : 2019/4/29 16:20
# @Author: lisa.liu
# @Email : 2423844@qq.com
# @File  : logger.py

import logging
from common import contents

def get_logger(name):

    logger = logging.getLogger(name)
    logger.setLevel('DEBUG')

    fmt='%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s'
    formatter = logging.Formatter(fmt=fmt)

    console_handler = logging.StreamHandler()  #控制台
    console_handler.setLevel('DEBUG')  #日志的级别可以定义到配置文件中
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(contents.log_dir+'/case.log',encoding='utf-8')
    file_handler.setLevel('INFO')
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger



if __name__=="__main__":
    logger = get_logger('case')
    logger.info('info')
    logger.error('error')
    logger.debug('debug')
    logger.info('over')
