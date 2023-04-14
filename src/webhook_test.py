#!/usr/bin/env python
# encoding: utf-8

import unittest
from webhook import Webhook
import os
from dotenv import load_dotenv

load_dotenv()


class WebhookTest(unittest.TestCase):
    hook = Webhook(os.getenv("TEST_WEBHOOK"), "Test", "Test", "Test")

    def test_send_card(self):
        fields = [
            {
                "title": "Test field",
                "value": "Test value",
                "short": True
            }
        ]

        self.hook.send_card("Test title", "Test message", fields)

    def test_send(self):
        self.hook.send("Test message")


if __name__ == '__main__':
    unittest.main()
