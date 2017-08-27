# -*- coding: utf-8 -*-
class Conductor:
    def __init__(self, api, workerInstance, limit=1):
        self.limit = limit
        self.api = api
        self.worker = workerInstance

    def carryOut(self):
        pass

class TrainingConductor(Conductor):
    def carryOut(self, dev=True):
        for i in range(self.limit):
            book1, book2, result = self.api.fetchTrainingData(debug=dev)
            self.worker.train(book1, book2, result)

class OutputConductor(Conductor):
    def carryOut(self, dev=True):
        for i in range(self.limit):
            book1, book2 = self.api.fetchData(debug=dev)
            output = self.worker.output(book1, book2)
            posted_data = self.api.send(output)
            print(posted_data)
