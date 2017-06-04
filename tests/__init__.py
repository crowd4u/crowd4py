# -*- coding: utf-8 -*-
import sys
import os
import configparser
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

config = configparser.ConfigParser()
config.read('config.ini')
oahu = config['oahu']
USERID = oahu.get('USERID', '')
PASSWORD = oahu.get('PASSWOR', '')
API_ROOT = oahu.get('API_ROOT', 'http://crowd4u.org')
USERINFO = {
    "requester": oahu.get('requester', '-1'),
    "from_app": 1,
    "_machine_language": "ja_JP",
    "group_id": oahu.get('group_id', '83'),
    "_user_token": oahu.get('_user_token', '')}
