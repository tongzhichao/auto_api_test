#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: http_requests.py
@time: 17-4-28 下午2:16
"""
import requests
import json


class HttpRequests(object):
    @staticmethod
    def do_post(url, params, **kwargs):

        if kwargs is not None:
            params.update(kwargs)
            response = requests.post(url, data=json.dumps(params))
            if response.status_code == 200:
                return True, response
            else:
                return False, response.status_code
        else:
            response = requests.post(url, data=json.dumps(params))
            if response.status_code == 200:
                return True, response
            else:
                return False, response.status_code
