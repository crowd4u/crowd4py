# -*- coding: utf-8 -*-
from __init__ import API_CONF, PROJECT_CONF
from utils.api import BibAPI
from workers.algorithm_worker import AlgorithmWorker

LIMIT = 10

if __name__ == "__main__":
    algorithmWorker = AlgorithmWorker()
    api = BibAPI(api_info=API_CONF, project_info=PROJECT_CONF)

    for i in range(LIMIT):
        book1, book2, result = api.fetchTrainingData(debug=True)
        algorithmWorker.train(book1, book2, result)
