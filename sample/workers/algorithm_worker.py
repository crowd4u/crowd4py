# -*- coding: utf-8 -*-
from workers.worker_base import WorkerBase

class AlgorithmWorker(WorkerBase):
    def train(self, book1, book2, result):
        print(book1, book2, result)

    def output(self, book1, book2):
        print(book1, book2)
        answer = False
        if book1["title"] == book2["title"]:
            answer = True
        return answer
