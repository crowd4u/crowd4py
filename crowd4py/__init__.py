# -*- coding: utf-8 -*-
import configparser
config = configparser.ConfigParser()
config.read('../config.ini')
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

from .api import API
from .task import Task
from . import helpers

