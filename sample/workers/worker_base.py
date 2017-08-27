# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class WorkerBase(metaclass=ABCMeta):
    """WorkerBase is the abstract class of worker
    Conductor called train and output, so we needs to implement those methods
    """
    
    def __init__(self):
        return

    @abstractmethod
    def train(self, book1, book2, result):
        """train is the abstractmethod so need implementing
        describe training process of the worker

        Parameters
        ----------
        book1  : object
        book2  : object
        result : object
            book1 and book2 is the bibliographic data that has title and isbn.
            result is the answer for the task.
        """
        pass

    @abstractmethod
    def output(self, book1, book2):
        """output is the abstractmethod so need implementing
        describe answering process of the worker

        Parameters
        ----------
        book1  : object
        book2  : object
            book1 and book2 is the bibliographic data that has title and isbn

        Returns
        -------
        answering : bool
            If the book1 and book2 is the same, answering true
            Otherwise answering false
        """
        pass
