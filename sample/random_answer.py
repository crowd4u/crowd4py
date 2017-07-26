# -*- coding: utf-8 -*-
from __init__ import API_CONF, PROJECT_CONF

import crowd4py
import threading

training_data = []

def example_predict(data):
    """
    :param data:
    :return: ans_data
    """
    data['_input_value_names'] = ""
    print(data['title_1'], data['title_2'])
    if data['title_1'] == data['title_2']:
        data['is_same'] = True
        print('same bib_id')
    else:
        data['is_skipped'] = True
        print('different bib_id')
    # if training_data is None:
    #     return None
    # print(data['tid'])
    # for i, d in enumerate(training_data):
    #     if data['tid'] == d['tid']:
    #         data['is_same'] = d['is_same']
    #         break
    # if any(data['tid'] == d['tid'] for d in training_data):
    #     data['is_same'] =
    return data


def poring_training_data(api):
    json = api.relation_data()
    global training_data
    training_data = json['data']


if __name__ == '__main__':
    api = crowd4py.API(api_info=API_CONF, project_info=PROJECT_CONF)

    # マルチスレッドでポーリング
    # t = threading.Thread(target=poring_training_data(api))
    # t.daemon = True
    # t.start()

    for i in range(1000):
        task = api.get_task(debug=True)
        ans_data = example_predict(task.data)
        if ans_data is None:
            api.request_answer(task.data['tid'])
            print("requested task answer ")
        else:
            print(api.post_answer(task.post_url, ans_data))
            print("post answer ")
