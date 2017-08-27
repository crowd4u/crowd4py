# -*- coding: utf-8 -*-
import crowd4py

class API():
    """Wrapper of Crowd4py API
    Specific wrapper of detection bibliographic task
    """

    def __init__(self, api_info, project_info):
        """Initialize Crowd4py API object with api and project infomartion

        Parameters
        ----------
        api_info : object
            Information of api configuration specified by config.ini
        project_info : object
            Information of current project specified by config.ini
        """
        self.api = crowd4py.API(api_info=api_info, project_info=project_info)

    def fetchTrainingData(self, debug=True):
        """Fetch data from crowd4u api in training models

        Parameters
        ----------
        debug : bool
            If debug is true, api use develop api, otherwise use crowd4u api

        Returns
        -------
        book1  : object
        book2  : object
        result : object
            Fetch data and formating data for worker training.
            book1 and book2 is the bibliographic data that has title and isbn.
            result is the answer for the task.
        """
        data = self.__fetch(debug=debug)
        book1, book2 = self.__createBooksData(data)
        result = self.__createResult(data)
        return book1, book2, result

    def fetchData(self, debug=True):
        """Fetch data from crowd4u api in answering term

        Parameters
        ----------
        debug : bool
            If debug is true, api use develop api, otherwise use crowd4u api

        Returns
        -------
        book1  : object
        book2  : object
            Fetch data and formating data for worker training.
            book1 and book2 is the bibliographic data that has title and isbn.
            answering terms don't include result, so no return result in the function.
        """
        data = self.__fetch(debug=debug)
        book1, book2 = self.__createBooksData(data)
        return book1, book2

    def send(self, answer):
        """Send the answering data in workers.

        Parameters
        ----------
        answer : bool
            Worker answering

        Returns
        -------
        status : int
            Return http status code of server response
        """
        task_data = self.current_task.data.copy()
        answer_data = self.__create_answering_data(answer)
        task_data.update(answer_data)
        return self.api.post_answer(self.current_task.post_url, task_data)

    def __fetch(self, debug=True):
        """Common process of fetchTrainingData and fetchData methods
        """
        self.current_task = self.api.get_task(debug=debug)
        return self.current_task.data

    def __createBooksData(self, data):
        """Format data and create bibliographics data
        """
        book1 = {
            "bib_id": data["master_bib_id"],
            "title": data["title_1"],
            "volume": data["volume_1"],
            "responsibility": data["responsibility_1"],
            "publisher_name": data["publisher_name_1"],
            "issued": data["issued_1"],
            "isbn": data["isbn_1"],
            "origin_name": data["origin_name_1"],
            "origin_id": data["origin_id_1"],
            "origin_url": data["origin_url_1"]
        }
        book2 = {
            "bib_id": data["sub_bib_id"],
            "title": data["title_2"],
            "volume": data["volume_2"],
            "responsibility": data["responsibility_2"],
            "publisher_name": data["publisher_name_2"],
            "issued": data["issued_2"],
            "isbn": data["isbn_2"],
            "origin_name": data["origin_name_2"],
            "origin_id": data["origin_id_2"],
            "origin_url": data["origin_url_2"]
        }
        return book1, book2

    def __createResult(self, data):
        """Create result data in training terms
        """
        result = {
            "is_same": data["is_same"],
            "is_skipped": data["is_skipped"]
        }
        return result

    def __create_answering_data(self, answer):
        """Create answering data in answering terms
        """
        return {"is_same": answer, "is_skipped": False, "_input_value_names": ""}
