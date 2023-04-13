#!/usr/bin/env python
# encoding: utf-8
from urllib import request
import json


class Webhook:
    def __init__(self, url, author_name, author_icon, author_link):
        self._url = url
        self._author_name = author_name
        self._author_icon = author_icon
        self._author_link = author_link
        pass

    def send_card(self, title, message, fields):
        test_data = {
            "attachments": [
                {
                    "type": "Card",
                    "fallback": "Something bad happened",
                    "color": "#00ff2a",
                    "title": title,
                    "text": message,
                    "author_name": self._author_name,
                    "author_icon": self._author_icon,
                    "author_link": self._author_link,
                    "fields": fields
                }
            ]
        }

        json_data = json.dumps(test_data)
        # print('Json data')
        print(json_data)

        req = request.Request(self._url, data=json_data.encode())
        req.add_header('Content-Type', 'application/json')

        res_data = request.urlopen(req)
        res = res_data.read()
        print("Result:")
        print(res)
        pass
