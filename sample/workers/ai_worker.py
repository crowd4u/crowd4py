# -*- coding: utf-8 -*-
from workers.worker_base import WorkerBase
from sklearn.svm import LinearSVC
from sklearn.externals import joblib

class AIWorker(WorkerBase):
    """This is the simple AI worker
    """
    def setup(self, path='estimator.pkl.cmp'):
        """Setup estimator for train
        """
        self.training_data = []
        self.training_target = []
        self.save_path = path
        self.estimator = LinearSVC(C=1.0)

    def load(self, path='estimator.pkl.cmp'):
        """Load estimator's training model on detected file for predict
        """
        self.estimator = joblib.load(path)

    def train(self, book1, book2, result):
        """AI worker create training data in train terms.

        Parameters
        ----------
        book1  : object
        book2  : object
        result : object
        """
        print(book1, book2, result)

        if result["is_skipped"] == None:
            return
        if result["is_same"] == None:
            return

        self.training_data.append(self.__create_data(book1, book2))
        self.training_target.append(self.__create_target(result))

    def predict(self, book1, book2):
        """AI worker answers result of book1 is same of book2 or not by created models

        Parameters
        ----------
        book1  : object
        book2  : object

        Returns
        -------
        answer : bool
        """
        print(book1, book2)

        predict = self.estimator.predict([self.__create_data(book1, book2)])
        return bool(predict[0])

    def fit(self):
        """Call this method after create train method expressly
        """
        self.estimator.fit(self.training_data, self.training_target)

    def dump(self):
        """Save the dump file on detected file path by setup detection
        """
        joblib.dump(self.estimator, self.save_path, compress=True)

    def __create_data(self, book1, book2):
        """Create array of training data by books object
        """
        return list(map(lambda key: int(book1[key] == book2[key]), book1.keys()))

    def __create_target(self, result):
        """Create boolean target data by result object
        """

        return int(result["is_same"] == "True")
