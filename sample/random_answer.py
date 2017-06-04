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
    data['is_same'] = "True"
    data['_input_value_names'] = ""
    ans_data = data
    return ans_data


def poring_training_data(api):
    pass


def input_empty_at_none(ans_data):
    data = []
    for d in ans_data.items():
        if d[1] is None:
            d = (d[0], '')
        data.append(d)
    return dict(data)


if __name__ == '__main__':
    api = crowd4py.API(user_info=user_info, project_name=project_name, relation_name=relation_name)
    task = api.get_task(debug=True)

    # マルチスレッドでポーリング
    # t = threading.Thread(target=poring_training_data(api))
    # t.daemon = True
    # t.start()

    ans_data = example_predict(task.data)
    if ans_data is None:
        api.request_answer(task.data['tid'])
        print("requested task answer ")
    else:
        print(task.post_url)
        print(api.post_answer(task.post_url, ans_data))
        print("post answer ")
