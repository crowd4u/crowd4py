# -*- coding: utf-8 -*-
import configparser
import os

cfg_file = os.path.join(os.path.dirname(__file__), 'config.ini')
config = configparser.ConfigParser()

config.read(cfg_file)

API_CONF = config['oahu']
# If you use crowd4u api, you should set crowd4u infomations in config file
# API_CONF = config['crowd4u']

PROJECT_CONF = config['project']
