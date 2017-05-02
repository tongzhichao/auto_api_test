#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: main.py.py
@time: 17-3-31 下午9:34
"""

# 基础包：接口测试的封装
import unittest, time
from lib.HTMLTestRunner import HTMLTestRunner
from lib.sendmail import SendEmail


test_dir = './case/'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_file_name = './report/' + now + 'result.html'
    fp = open(report_file_name, 'wb')
    runner = HTMLTestRunner(stream=fp, title='接口自动化测试报告', description='用例执行情况如下')
    runner.run(discover)
    fp.close()
    to_list = ['liuyu@yyhudong.com']
    cc_list = ['testing@yyhudong.com']
    file_path_tuple = (report_file_name,)
    send_conf = SendEmail('smtp.163.com', '18724353405@163.com', 'qq123123')
    # send_conf = SendEmail('mail.yyhudong.com', 'liuyu@yyhhudong.com', 'qq123..')
    if send_conf.send_email(to_list, cc_list, sub='接口测试报告' + now, content=open(report_file_name, 'rb').read(), file_path=file_path_tuple):
        print('发送成功')
    else:
        print('发送失败')

