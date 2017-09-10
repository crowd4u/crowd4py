# -*- coding: utf-8 -*-
from workers.worker_base import WorkerBase
from sklearn.svm import LinearSVC
from sklearn.externals import joblib

class AIWorker(WorkerBase):
    """This is the simple AI worker
    """
    def __init__(self, training=True, save_path='estimator.pkl.cmp', load_path='estimator.pkl.cmp'):
        self.training_data = []
        self.training_target = []
        if training and save_path:
            self.save_path = save_path
            self.estimator = LinearSVC(C=1.0)
        elif not training and load_path:
            self.load_path = load_path
            self.estimator = joblib.load(load_path)
        else:
            raise Exception("no detect path error")

    def train(self, book1, book2, result):
        """AI worker create training data in train terms.

        Parameters
        ----------
        book1  : object
        book2  : object
        result : object
        """
        if result["is_skipped"] == None:
            return
        if result["is_same"] == None:
            return

        self.training_data.append(self.__create_data(book1, book2))
        self.training_target.append(self.__create_target(result))

    def output(self, book1, book2):
        """AI worker answers result of book1 is same of book2 or not by created models

        Parameters
        ----------
        book1  : object
        book2  : object

        Returns
        -------
        answer : bool
        """
        predict = self.estimator.predict([self.__create_data(book1, book2)])
        return bool(predict[0])

    def fit(self):
        """ Call this method after create train method expressly
        """
        self.estimator.fit(self.training_data, self.training_target)

    def dump(self):
        joblib.dump(self.estimator, self.save_path, compress=True)

    def __create_data(self, book1, book2):
        return list(map(lambda key: int(book1[key] == book2[key]), book1.keys()))

    def __create_target(self, result):
        return int(result["is_same"])
