# -*- coding: utf-8 -*-
from __init__ import API_CONF, PROJECT_CONF
from utils.api import BibAPI
from workers.ai_worker import AIWorker

LIMIT = 10

if __name__ == "__main__":
    aiWorker = AIWorker()
    api = BibAPI(api_info=API_CONF, project_info=PROJECT_CONF)

    aiWorker.setup()
    for i in range(LIMIT):
        book1, book2, result = api.fetchTrainingData(debug=True)
        aiWorker.train(book1, book2, result)

    # Create training model and save model on file
    aiWorker.fit()
    aiWorker.dump()
