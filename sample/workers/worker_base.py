# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class WorkerBase(metaclass=ABCMeta):
    def __init__(self):
        return

    @abstractmethod
    def train(self, book1, book2, result):
        pass

    @abstractmethod
    def output(self, book1, book2):
        pass
