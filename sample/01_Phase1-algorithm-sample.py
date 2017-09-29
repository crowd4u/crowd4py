# -*- coding: utf-8 -*-
from __init__ import API_CONF, PROJECT_CONF
from utils.api import BibAPI
from workers.algorithm_worker import AlgorithmWorker


if __name__ == "__main__":
    algorithmWorker = AlgorithmWorker()
    api = BibAPI(api_info=API_CONF, project_info=PROJECT_CONF)

    trainingData = api.fetchTrainingData(debug=True)
    for data in trainingData:
        algorithmWorker.train(data['book1'], data['book2'], data['result'])