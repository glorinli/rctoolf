#!/usr/bin/env python
# encoding: utf-8

from webhook import Webhook

if __name__ == '__main__':
    hook = Webhook("https://hooks.ringcentral.com/webhook/v2/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
                   ".eyJvdCI6InUiLCJvaSI6IjEzOTAxNjQxODkxODciLCJpZCI6IjEyMDE4MDczODcifQ"
                   ".goXReAz6Udxmi72q3_rFotX2nyx2mYSrdFxcpHnqcLM", "Test", "Test", "Test")
    hook.send_card("Test title", "Test message", None)
