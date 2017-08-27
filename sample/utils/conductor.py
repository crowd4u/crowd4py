# -*- coding: utf-8 -*-
class Conductor:
    """Conductor class describe processes of training and output
    """

    def __init__(self, api, workerInstance, limit=1):
        """Initialize conductor class and set api and worker instance

        Parameters
        ----------
        api : object
            Api wrapper object of specific bibliographic task
        workerInstance : object(WorkerBase)
            Worker instance that inherite WorkerBaseClass
        limit : int
            The limit of get tasks
        """
        self.limit = limit
        self.api = api
        self.worker = workerInstance

    def carryOut(self):
        """Describing a flow
        """
        pass

    def carryOutStepwise(self):
        """Describing a flow with one by one
        """
        pass

class TrainingConductor(Conductor):
    def carryOutStepwise(self, dev=True):
        """Describing a flow of get task data and training worker by one time

        Parameters
        ----------
        dev : bool
            If dev is true, api use develop api, otherwise use production api

        Returns
        -------
        None
            Fetch the api data and train worker one time
        """
        return self.worker.train(*(self.api.fetchTrainingData(debug=dev)))

    def carryOut(self, dev=True):
        """Describin a flow of get task data and training worker until detected limits

        Parameters
        ----------
        dev : bool
            If dev is true, api use develop api, otherwise use production api

        Returns
        -------
        None
            Fetch the api data and train worker one time
        """
        for i in range(self.limit):
            self.carryOutStepwise(dev)

class OutputConductor(Conductor):
    def carryOutStepwise(self, dev=True):
        """Describing a flow of get task data and answering worker by one time

        Parameters
        ----------
        dev : bool
            If dev is true, api use develop api, otherwise use production api

        Returns
        -------
        None
            Fetch the api data and train worker one time
        """
        output = self.worker.output(*(self.api.fetchData(debug=dev)))
        return self.api.send(output)

    def carryOut(self, dev=True):
        """Describin a flow of get task data and answering worker until detected limits

        Parameters
        ----------
        dev : bool
            If dev is true, api use develop api, otherwise use production api

        Returns
        -------
        None
            Fetch the api data and train worker one time
        """
        for i in range(self.limit):
            self.carryOutStepwise(dev)
