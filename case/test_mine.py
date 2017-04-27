#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: test_mine.py
@time: 17-4-13 下午2:57
"""


import requests
import json
import unittest
from lib.file_opreate import ConfigOperate
from config.get_base_parms import *
import random
from lib import printlog

class TestMine(unittest.TestCase):
    '''测试我的相关接口'''

    def setUp(self):
        self.url = ConfigOperate('/home/liuyu/project/autoapitest/config/global.ini').get_config('httpconf', 'baseurl')
        self.base_parms = get_base_parms()
        self.headers = {' content-type': 'application/json'}

    def test_my_post_topic(self):
        '''我发布的帖子'''
        response = requests.post(self.url + '/forum_app/my_post_topics', data=json.dumps(self.base_parms))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)
    def test_my_replay_topic(self):
        '''我回复的帖子'''
        response = requests.post(self.url + '/forum_app/my_reply_topics', data=json.dumps(self.base_parms))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)

    def test_my_collection(self):
        '''我的收藏'''
        response = requests.post(self.url + '/forum_app/my_collection', data=json.dumps(self.base_parms))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)

    def test_share_qq_wechat_add_score(self):
        '''分享QQ\微信加积分(随机)'''
        subtype = random.choice(['qq', 'wechat'])
        self.base_parms.update({'type': 'share_one', 'sub_type': subtype})
        response = requests.post(self.url + '/user/add_score', data=json.dumps(self.base_parms))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)

    def test_share_qzone_add_score(self):
        '''分享空间\朋友圈加积分(随机)'''
        subtype = random.choice(['qq', 'wechat'])
        self.base_parms.update({'type': 'share_group', 'sub_type': subtype})
        response = requests.post(self.url + '/user/add_score', data=json.dumps(self.base_parms))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)

    def test_edit_profile(self):
        '''修改用户资料'''
        self.base_parms.update({'key': ['nickname', 'location', 'gender'], 'value': ['jiekoutest', '上海', 0]})
        response = requests.post(self.url + '/user/edit_profile', data=json.dumps(self.base_parms))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)

    def test_my_home_page_paly_games(self):
        '''测试个人主页-玩过的游戏'''
        self.base_parms.update({'user_id': get_random_uid(), 'home_type': 'play_games'})
        response = requests.post(self.url + '/user/home_page', data=json.dumps(self.base_parms))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)

    def test_my_home_page_paly_games(self):
        '''测试个人主页-评论过的游戏'''
        self.base_parms.update({'user_id': get_random_uid(), 'home_type': 'game_posts'})
        response = requests.post(self.url + '/user/home_page', data=json.dumps(self.base_parms))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)

    def test_my_home_page_paly_games(self):
        '''测试个人主页-发布的帖子'''
        self.base_parms.update({'user_id': get_random_uid(), 'home_type': 'topics'})
        response = requests.post(self.url + '/user/home_page', data=json.dumps(self.base_parms))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)

    def test_my_played_game(self):
        '''我的游戏,我玩过的游戏'''
        self.base_parms.update({'my_type': 'play_games'})
        response = requests.post(self.url + '/user/my_game', data=json.dumps(self.base_parms))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)

    def test_my_comment_game(self):
        '''我的游戏,我评论过的游戏'''
        self.base_parms.update({'my_type': 'game_posts'})
        response = requests.post(self.url + '/user/my_game', data=json.dumps(self.base_parms))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)
        PrintLog.print_log_info("ceshi")


    def tearDown(self):
        print(self.result)

if __name__ == '__main__':
    unittest.main()

