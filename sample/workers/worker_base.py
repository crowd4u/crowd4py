# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class WorkerBase(metaclass=ABCMeta):
    """WorkerBase is the abstract class of worker
    we needs to implement following abstract methods
    """

    @abstractmethod
    def train(self, **args):
        """train is the abstractmethod so need implementing
        describe training process of the worker
        """
        pass

    @abstractmethod
    def predict(self, **args):
        """output is the abstractmethod so need implementing
        describe answering process of the worker
        """
        pass
