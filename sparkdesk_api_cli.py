# -*- coding: UTF-8 -*-
"""
@Project : sparkdesk-api
@File    : sparkdesk_api_cli.py

"""
from sparkdesk_api.core import SparkAPI

if __name__ == '__main__':

    # 默认api接口版本为1.5，2.0需要自行申请。开启v2.0版本只需指定 version=2.1 即可
    sparkAPI = SparkAPI(
        app_id='b41be88d',
        api_secret='NzQ3NzVjZTFhZDQ4NGQyNWE5NjhmNjM2',
        api_key='e16a0aea7a85b600f56e065f703ae6be',
    )

    # single chat
    # print(sparkAPI.chat("repeat: hello world"))

    # continue chat
    sparkAPI.chat_stream()