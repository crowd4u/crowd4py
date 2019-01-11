# -*- coding: utf-8 -*-
from workers.worker_base import WorkerBase

class AlgorithmWorker(WorkerBase):
    """This is the human rule based algorithm worker
    The worker's algorithm is very simple
    That check the title of books and same title return true, otherwise false.
    """
    def train(self, book1, book2, result):
        """algorithm worker no uses training models
        So train show the data of bibliographics and result

        Parameters
        ----------
        book1  : object
        book2  : object
        result : object
        """
        print(book1, book2, result)

    def predict(self, book1, book2):
        """Checking the title of books and same title return true, otherwise false.

        Parameters
        ----------
        book1  : object
        book2  : object

        Returns
        -------
        answer : bool
        """
        print(book1, book2)

        answer = False
        if book1["title"] == book2["title"]:
            answer = True
        return answer
