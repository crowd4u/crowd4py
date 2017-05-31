# -*- coding: utf-8 -*-
import crowd4py

user_info = {
    "requester": 00,
    "from_app": 1,
    "_machine_language": "ja_JP",
    "group_id": 00,
    "_user_token": ""}

project_name = ''
relation_name = ''


def example_predict(data):
    """

    :param data:
    :return: ans_data
    """
    ans_data = data
    return ans_data

if __name__ == "__main__":
    api = crowd4py.API(user_info=user_info, project_name=project_name, relation_name=relation_name)
    data = api.get_task()

    ans_data = example_predict(data)

    if ans_data is None:
        api.request_answer(data['tid'])
    else:
        api.post_answer(data['tid'], ans_data)

