# -*- coding: utf-8 -*-
from __init__ import API_CONF, PROJECT_CONF

import crowd4py
import threading

answer_data = []

def get_all_answers:

def matched_answers(master_bib_id, sub_bib_id):
    
def decide_by_majority_vote(answers):

def example_predict(data):
    """
    :param data:
    :return: worker_answer
    """
    print(data)
    
    worker_answer['_input_value_names'] = ""
    
    master_bib_id = data['master_bib_id']
    sub_bib_id = data['sub_bib_id']
    
    matched_answers = pick_up_answers(master_bib_id, sub_bib_id)
    if len(matched_answers) == 0:
        worker_answer['is_skipped'] = True
        return worker_answer
    
    decision = decide_by_majority_vote(matched_answers)
    if decision == 'is_same':
        worker_answer['is_same'] = True
    else if decision == 'is_not_same':
        worker_answer['is_same'] = False
    else:
        worker_answer['is_skipped'] = True
    
    return worker_answer

if __name__ == '__main__':
    get_all_answers
    
    api = crowd4py.API(api_info=API_CONF, project_info=PROJECT_CONF)
    for i in range(1000):
        task = api.get_task(debug=True)
        ans_data = example_predict(task.data)
        if ans_data is None:
            api.request_answer(task.data['tid'])
            print("requested task answer ")
        else:
            print(api.post_answer(task.post_url, ans_data))
            print("posted answer")
