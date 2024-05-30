# -*- coding: UTF-8 -*-
"""
@Project : sparkdesk-api
@File    : sparkdesk_web_cli.py
@Author  : Baitianlang

@Description : 
"""
from sparkdesk_web.core import SparkWeb
from pyhandytools.file import FileUtils

if __name__ == '__main__':
    conf_data = FileUtils.load_json('./conf/keys.json')

    sparkWeb = SparkWeb(
        cookie=conf_data['Cookie'],
        fd=conf_data['fd'],
        GtToken=conf_data['GtToken']
    )

    # single chat
    # print(sparkWeb.chat("repeat: hello world"))

    # stream input chat
    # sparkWeb.chat_stream(history=True)

    # continue chat
    chat = sparkWeb.create_continuous_chat()
    while True:
        chat.chat(input("Ask: "))
    # chat.chat("肇庆是一个什么样的城市")
    # chat.chat("刚才你说的是哪个城市？")
