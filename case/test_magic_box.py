#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: test_magic_box.py
@time: 17-4-13 下午2:57
"""

import requests
import json
import unittest
from lib.file_opreate import ConfigOperate
from config.get_base_parms import *


class TestMagicBox(unittest.TestCase):
    '''魔盒游戏测试'''

    def setUp(self):

        self.url = ConfigOperate('/home/liuyu/project/autoapitest/config/global.ini').get_config('httpconf', 'baseurl')
        self.base_parms = get_base_parms()
        self.headers = {'content-type': 'application/json'}

    def test_update_info(self):
        '''获取升级信息'''

        response = requests.post(self.url+'/api/get/latest-version-info', data=json.dumps(self.base_parms))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)

    def test_plugin_version_info(self):
        ''' 获取视频插件升级信息 '''

        response = requests.post(self.url+'/api/get/plugin-version-info', data=json.dumps(self.base_parms), headers=self.headers)
        self.result = response.json()
        self.assertEqual(response.status_code, 200)

    def test_recommond_game(self):
        '''获取下载页面推荐的游戏'''

        response = requests.post(self.url+'/api/get/recommend-games', data=json.dumps(self.base_parms))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['msg'], '成功')
        self.assertEqual(self.result['data']['showCount'], 6)

    def test_get_box_game(self):
        '''获取魔盒游戏详细信息'''

        apks = [
                    {
                        "pkgName": "com.invictus.impossiball",
                        "verCode": "1511300729",
                        "signatureSf": "cb82a5010dd28529ffa1e58116643335",
                        "signatureMf": "0f140a2381575ff2222e47e817a09b53",
                    }
            ]
        base_parms = get_base_parms()
        base_parms.update({'apks': apks})
        response = requests.post(self.url + '/api/get/box-games', data=json.dumps(base_parms))
        if response.status_code == 200:
            self.result = response.json()
        else:
            self.result = '无返回数据,HTTP状态码为%d' % response.status_code
        # msg = json.loads(response.text.encode('utf-8'))['msg']
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(msg, 'ok')

    # def test_get_upgrade_game(self):

        # pass

    def test_get_default_keyword(self):
        '''获取搜索框默认关键词'''
        response = requests.post(self.url + '/api/get/default-keywords', data=json.dumps(get_base_parms()))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)

    def test_hot_games(self):
        '''获取搜索页推荐的游戏列表'''
        response = requests.post(self.url + '/api/get/hot-games', data=json.dumps(get_base_parms()))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)

    def test_get_ad_config(self):
        '''测试获取广告位信息'''
        response = requests.post(self.url + '/api/get/ad-config', data=json.dumps(get_base_parms()))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)

    def test_game_view_page(self):
        '''游戏详情页测试'''
        base_params = get_base_parms()
        base_params.update({'id': 2000, 'pa': str(get_random_gameid()[0])})
        response = requests.post(self.url + '/view/page', data=json.dumps(base_params))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)

    def test_duplicate_game(self):
        '''获取开小号游戏列表'''
        base_params = get_base_parms()
        ext_params = [{"pkgName": "com.dreamsky.DiabloLOL", "verCode": 310}, {"pkgName": "com.sqage.Ogre.OgreInstance.uc", "verCode": 24}, {"pkgName": "com.windplay.mobius.dnv.uc", "verCode": 7}]
        base_params.update({'apks': ext_params})
        response = requests.post(self.url + '/api/get/duplicate-game-list', data=json.dumps(base_params))
        if response.status_code == 200:
            self.result = response.json()
            self.assertEqual(self.result['rc'], 0)
        else:
            self.result = '接口请求发生错误,HTTP状态码为%d' % response.status_code
        self.assertEqual(response.status_code, 200, '请求成功')

    def test_get_game_list(self):
        '''获取魔盒游戏最热列表'''
        base_parms = get_base_parms()
        base_parms.update({'gameType': 'boxGame', 'orderType': 'hottest'})
        response = requests.post(self.url + '/api/get/game-list', data=json.dumps(base_parms))
        self.result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.result['rc'], 0)

    # def test_get_page

    def tearDown(self):
        print(self.result)

if __name__ == '__main__':
    unittest.main()

