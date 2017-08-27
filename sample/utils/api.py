# -*- coding: utf-8 -*-
import crowd4py

class API():
    def __init__(self, api_info, project_info):
        self.api = crowd4py.API(api_info=api_info, project_info=project_info)

    def fetchTrainingData(self, debug=True):
        data = self.__fetch(debug=debug)
        book1, book2 = self.__createBooksData(data)
        result = self.__createResult(data)
        return book1, book2, result

    def fetchData(self, debug=True):
        data = self.__fetch(debug=debug)
        book1, book2 = self.__createBooksData(data)
        return book1, book2

    def send(self, answer):
        task_data = self.current_task.data.copy()
        answer_data = self.__create_answering_data(answer)
        task_data.update(answer_data)
        return self.api.post_answer(self.current_task.post_url, task_data)

    def __fetch(self, debug=True):
        self.current_task = self.api.get_task(debug=debug)
        return self.current_task.data

    def __createBooksData(self, data):
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
        result = {
            "is_same": data["is_same"],
            "is_skipped": data["is_skipped"]
        }
        return result

    def __create_answering_data(self, answer):
        return {"is_same": answer, "is_skipped": False, "_input_value_names": ""}
