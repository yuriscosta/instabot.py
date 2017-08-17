#!/usr/bin/env python
# coding: utf-8

import os
import sys
import time

sys.path.append(os.path.join(sys.path[0], 'src'))

from check_status import check_status
from feed_scanner import feed_scanner
from follow_protocol import follow_protocol
from instabot import InstaBot
from unfollow_protocol import unfollow_protocol

from threading import Thread

class InitBot(Thread):
    def __init__(self, login, password):
        Thread.__init__(self)
        self.login = login
        self.password = password

    def run(self):
        try:
            bot = InstaBot(
                login=self.login,
                password=self.password,
                like_per_day=1000,
                comments_per_day=200,
                tag_list=['natal', 'riograndedonorte', 'praia', 'pontanegra', 'pirangi'],
                max_like_for_one_tag=200,
                follow_per_day=300,
                follow_time=5*60*60,
                unfollow_per_day=50,
                unfollow_break_min=15,
                unfollow_break_max=30,
                log_mod=0,
                proxy='',
                comment_list=[["Que"],
                              ["legal!", "maravilha!", "coisa bela!"],
                              ["Top!!!"]])
            while True:
                bot.new_auto_mod()
        except Exception as e:
            print(e)
