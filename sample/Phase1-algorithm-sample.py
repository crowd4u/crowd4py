# -*- coding: utf-8 -*-
from __init__ import API_CONF, PROJECT_CONF
from utils.api import API
from utils.conductor import TrainingConductor
from workers.algorithm_worker import AlgorithmWorker

LIMIT = 1

if __name__ == "__main__":
    api = API(api_info=API_CONF, project_info=PROJECT_CONF)
    worker = AlgorithmWorker()

    conductor = TrainingConductor(api=api, workerInstance=worker, limit=LIMIT)
    conductor.carryOut()
