#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: test_forum.py
@time: 17-4-19 上午10:41
"""

import requests
import json
import unittest
from lib.file_opreate import ConfigOperate
from config.get_base_parms import *
import random

class TestForum(unittest.TestCase):
    '''社区相关接口测试'''

    def setUp(self):
        self.url = ConfigOperate('/home/liuyu/project/autoapitest/config/global.ini').get_config('httpconf', 'baseurl')
        self.base_parms = get_base_parms()
        self.headers = {' content-type': 'application/json'}

    def test_forum_index(self):
        '''测试社区首页'''
        page = random.choice(range(5, 20))
        offset = random.choice(range(5, 30))
        self.base_parms.update({'group_id': get_random_group_id(), 'page': page, 'offset': offset})
        response = requests.post(self.url + '/forum_app/index4', data=json.dumps(self.base_parms))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)

    def test_forum_group_new(self):
        '''测试话题详情页最新页面'''
        self.base_parms.update({'group_id': get_random_group_id(), 'sort_rule': 0})
        response = requests.post(self.url + '/forum_app/group4', data=json.dumps(self.base_parms))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)

    def test_forum_group_hot(self):
        '''测试话题详情页精选页面'''
        self.base_parms.update({'group_id': get_random_group_id(), 'sort_rule': 1})
        response = requests.post(self.url + '/forum_app/group4', data=json.dumps(self.base_parms))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)

    def test_forum_topic(self):
        '''测试帖子详情页'''
        self.base_parms.update({'group_id': get_random_group_id(), 'sort_rule': 1})
        response = requests.post(self.url + '/forum_app/topic', data=json.dumps(self.base_parms))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)


    def tearDown(self):
        print(self.result)

if __name__ == '__main__':
    unittest.main()