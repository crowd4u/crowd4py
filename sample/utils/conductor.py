# -*- coding: utf-8 -*-
class Conductor:
    def __init__(self, api, workerInstance, limit=1):
        self.limit = limit
        self.api = api
        self.worker = workerInstance

    def carryOut(self):
        pass

    def carryOutStepwise(self):
        pass

class TrainingConductor(Conductor):
    def carryOutStepwise(self, dev=True):
        return self.worker.train(*(self.api.fetchTrainingData(debug=dev)))

    def carryOut(self, dev=True):
        for i in range(self.limit):
            self.carryOutStepwise(dev)

class OutputConductor(Conductor):
    def carryOutStepwise(self, dev=True):
        output = self.worker.output(*(self.api.fetchData(debug=dev)))
        return self.api.send(output)

    def carryOut(self, dev=True):
        for i in range(self.limit):
            self.carryOutStepwise(dev)
