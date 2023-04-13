#!/usr/bin/env python
# encoding: utf-8

import unittest
from webhook import Webhook


class WebhookTest(unittest.TestCase):
    hook = Webhook("https://hooks.ringcentral.com/webhook/v2/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
                   ".eyJvdCI6InUiLCJvaSI6IjEzOTAxNjQxODkxODciLCJpZCI6IjEyMDE4MDczODcifQ"
                   ".goXReAz6Udxmi72q3_rFotX2nyx2mYSrdFxcpHnqcLM", "Test", "Test", "Test")

    def test_send_card(self):
        fields = [
            {
                "title": "Test field",
                "value": "Test value",
                "short": True
            }
        ]

        self.hook.send_card("Test title", "Test message", fields)
        pass


if __name__ == '__main__':
    unittest.main()
