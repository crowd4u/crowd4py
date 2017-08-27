# -*- coding: utf-8 -*-
from __init__ import API_CONF, PROJECT_CONF
from utils.api import API
from utils.conductor import *

"""
This program is divided into a learning phase and an answering phase.
The learning phase is done in phase 1 and the answering phase is done in phase 2
"""

def phase1(workerInstance=None, limit=1):
    api = API(api_info=API_CONF, project_info=PROJECT_CONF)
    TrainingConductor(api, workerInstance, limit).carryOut()

def phase2(workerInstance=None, limit=1):
    api = API(api_info=API_CONF, project_info=PROJECT_CONF)
    OutputConductor(api, workerInstance, limit).carryOut()
