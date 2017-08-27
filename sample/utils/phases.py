# -*- coding: utf-8 -*-
from __init__ import API_CONF, PROJECT_CONF
from utils.api import API
from utils.conductor import *

def phase1(workerInstance=None, limit=1):
    api = API(api_info=API_CONF, project_info=PROJECT_CONF)
    TrainingConductor(api, workerInstance, limit).carryOut()

def phase2(workerInstance=None, limit=1):
    api = API(api_info=API_CONF, project_info=PROJECT_CONF)
    OutputConductor(api, workerInstance, limit).carryOut()
