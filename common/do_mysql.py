#-*- coding:utf-8 -*-
# @Time  : 2019/4/22 15:33
# @Author: lisa.liu
# @Email : 2423844@qq.com
# @File  : do_mysql.py

import pymysql

class DoMySQL:
    #数据库初始化
    def __init__(self):
        host = "test.lemonban.com"
        user = "test"
        password = "test"
        port = 3306
        #创建连接
        self.mysql=pymysql.connect(host=host,user=user,password=password,port=port)
        self.cursor=self.mysql.cursor(pymysql.cursors.DictCursor)

    def fetch_one(self,sql):
        self.cursor.execute(sql)  # 执行sql语句
        self.mysql.commit()
        return self.cursor.fetchone() #获取sql语句的执行结果

    def fetch_all(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.mysql.close()


if __name__=='__main__':
    mysql=DoMySQL()

    result1 = mysql.fetch_one('select max(mobilephone) from future.member')
    result2 = mysql.fetch_all('select * from future.member where mobilephone="18616728419"')  #得到的结果为元组里面套元组
    result3 = mysql.fetch_one('select * from future.loan where id="2231"')
    # 得到的结果为元组里面套元组
    print(result1)
    print(result2)
    print(result3)
    mysql.close()