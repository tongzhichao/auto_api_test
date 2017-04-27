#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: file_opreate.py
@time: 17-3-31 上午1:11
"""

import os
import sys
from configparser import ConfigParser


class ConfigOperate(object):

    """
    配置文件相关操作
    """

    def __init__(self, file_path):

        self.file_path = file_path
        self.config = ConfigParser()

    def get_config(self, section, option):

        if self.config.read(self.file_path):

            return self.config.get(section, option)

        else:

            return False

    def set_config(self, section, option, value):

        self.config.set(section, option, value)
        self._write_config()

    def add_section(self, section):

        self.config.add_section(section)
        self._write_config()

    def remove_section(self, section):

        self.config.remove_section(section)
        self._write_config()

    def remove_option(self, section, option):

        self.config.remove_option(section, option)
        self._write_config()

    def _write_config(self):

        self.config.write(open(self.file_path, 'w'))
        self.config.write(sys.stdout)


class FileOperate(object):

    def create_file(self):

        pass



