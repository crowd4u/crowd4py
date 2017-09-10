# -*- coding: utf-8 -*-
from __init__ import API_CONF, PROJECT_CONF
from utils.api import BibAPI
from workers.ai_worker import AIWorker

LIMIT = 10

if __name__ == "__main__":
    aiWorker = AIWorker()
    api = BibAPI(api_info=API_CONF, project_info=PROJECT_CONF)

    aiWorker.load()
    for i in range(LIMIT):
        book1, book2 = api.fetchData(debug=True)
        answer = aiWorker.predict(book1, book2)
        api.send(answer)
