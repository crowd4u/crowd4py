# -*- coding: utf-8 -*-
import crowd4py
import threading

user_info = {
    'requester': 818,
    'from_app': 1,
    '_machine_language': 'ja_JP',
    'group_id': 83,
    '_user_token': ''}

project_name = 'CompTestV2'
relation_name = '_Task_Bibrecord_IdentificationTask'
training_data = []


def example_predict(data):
    """
    :param data:
    :return: ans_data
    """
    ans_data = data
    return ans_data


def poring_training_data(api):
    pass


if __name__ == '__main__':
    api = crowd4py.API(user_info=user_info, project_name=project_name, relation_name=relation_name)
    task = api.get_task()

    # マルチスレッドでポーリング
    # t = threading.Thread(target=poring_training_data(api))
    # t.daemon = True
    # t.start()

    ans_data = example_predict(task.data)

    if ans_data is None:
        api.request_answer(task.data['tid'])
    else:
        api.post_answer(task.post_url, ans_data)
