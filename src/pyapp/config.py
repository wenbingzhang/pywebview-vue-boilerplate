#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import platform


class Config:
    '''配置文件'''
    appName = 'vue-pywebview-pyinstaller'  # 应用名称
    appVersion = "1.0.0"  # 应用版本号
    cryptoKey = "cd132edd-4721-4b8f-b4be-c88223abfa01"

    appSystem = platform.system()    # 本机系统类型
