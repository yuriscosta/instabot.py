# coding:utf-8

"""
    Arquivo principal para execução dos bots
"""

import time

from get_accounts import list_accounts
from bot import InitBot

for account in list_accounts():
    thread = InitBot(account['user'], account['password'])
    thread.start()
