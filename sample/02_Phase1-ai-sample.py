# -*- coding: utf-8 -*-
from __init__ import API_CONF, PROJECT_CONF
from utils.api import BibAPI
from workers.ai_worker import AIWorker


if __name__ == "__main__":
    aiWorker = AIWorker()
    api = BibAPI(api_info=API_CONF, project_info=PROJECT_CONF)

    aiWorker.setup()
    trainingData = api.fetchTrainingData(debug=True)
    for data in trainingData:
        aiWorker.train(data['book1'], data['book2'], data['result'])

    # Create training model and save model on file
    aiWorker.fit()
    aiWorker.dump()
