#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: test_login.py.py
@time: 17-4-6 上午1:42
"""
import unittest
from lib.file_opreate import ConfigOperate
from lib.http_requests import HttpRequests
from lib.printlog import PrintLog

class TestLogin(unittest.TestCase):
    '''登录模块测试'''

    def setUp(self):

        self.url = ConfigOperate('/home/liuyu/auto_api_test/config/global.ini').get_config('httpconf', 'forum_baseurl')
        self.data = {
            "username": "yyhdggtest000",
            "password": "9628FFAECF05013841852CB572D50D45",
            "type": "username",
            "device": {
                "mac": "unknown",
                "fingerprint": "Xiaomi/kenzo/kenzo:6.0.1/MMB29M/V8.2.1.0.MHOCNDL:user/release-keys",
                "model": "Redmi Note 3",
                "product": "kenzo",
                "vendor": "Xiaomi",
                "sdk": 23,
                "widthPixels": 1080,
                "heightPixels": 1920,
                "density": 480,
                "currentAndroidId": "1b8d2c5ea5c93c11",
                "firstAndroidId": "unknown",
                "firstBoot": 1491357039345,
                "firstImei": "unknown",
                "hasWeChat": "true",
                "hasqq": "true",
                "language": "zh",
                "country": "CN",
                "cpu": {
                    "cpuimplementer": "0x41",
                    "cpuarchitecture": "8",
                    "cpurevision": "4",
                    "revision": "4",
                    "processorcnt": "5",
                    "hardware": "Qualcomm Technologies, Inc MSM8956",
                    "cpuvariant": "0x0",
                    "features": "fp asimd evtstrm aes pmull sha1 sha2 crc32 wp half thumb fastmult vfp edsp neon vfpv3 tlsi vfpv4 idiva idivt",
                    "cpupart": "0xd03"
                },
                "prop": {
                    "ro.product.brand": "Xiaomi",
                    "ro.product.name": "kenzo",
                    "ro.product.model": "Redmi Note 3",
                    "ro.build.fingerprint": "Xiaomi/kenzo/kenzo:6.0.1/MMB29M/V8.2.1.0.MHOCNDL:user/release-keys",
                    "ro.build.version.sdk": "23",
                    "ro.build.version.release": "6.0.1",
                    "ro.build.date": "Tue Feb 14 20:19:12 CST 2017",
                    "ro.build.date.utc": "1487074752",
                    "ro.boot.cpuid": "",
                    "ro.btconfig.vendor": "",
                    "persist.sys.timezone": "Asia/Shanghai",
                    "persist.sys.country": "",
                    "persist.sys.language": "",
                    "persist.sys.dalvik.vm.lib": "",
                    "ro.build.description": "kenzo-user 6.0.1 MMB29M V8.2.1.0.MHOCNDL release-keys",
                    "ro.runtime.firstboot": "1491357039345",
                    "ro.serialno": "acccbe9c",
                    "ro.product.device": "kenzo",
                    "ro.kernel.qemu": "",
                    "ro.hardware": "qcom",
                    "ro.product.cpu.abi": "arm64-v8a"
                },
                "gpuVendor": "Adreno (TM) 510",
                "imei": "861735031851214",
                "connectionType": "WiFi",
                "carrier": "Unknown"
            },
            "caller": {
                "id": "ggclient",
                "sf": "A052F5F784A80A2A9B3AE97339C2C9C5",
                "rsa": "F08C552DA28E99672ACACFA7039F3560",
                "mf": "08D2F61DAD464B916FBFA11ADCC550A0",
                "regId": "D/sj08XtOhp/xqO61JeJ6rgt2bNqMfk47FJ2rNwdee8=",
                "pkgName": "com.iplay.assistant",
                "channel": "B1",
                "verCode": 417,
                "token": ""
            },
            "token": "",
            "reqTime": 1491470331215
        }

    def test_login(self):
        ''' 测试登录 '''
        rp = HttpRequests.do_post(self.url+'/login', self.data)
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            PrintLog.print_log_info('登录接口测试通过' + '\n' + str(result))
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()


