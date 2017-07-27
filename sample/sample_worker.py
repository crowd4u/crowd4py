# -*- coding: utf-8 -*-
from __init__ import API_CONF, PROJECT_CONF

import json
import pandas as pd
import math

import crowd4py

def get_all_answers():
    return pd.read_csv('answers/answered_facts_summary.csv')

def pick_up(answers, master_bib_id, sub_bib_id):
    matched_answers = answers[(answers.master_bib_id == master_bib_id) & (answers.sub_bib_id == sub_bib_id)]
    return matched_answers
    
def decide_by_majority_vote(matched_answers):
    group_by_ans = matched_answers.answer.value_counts(sort=True, dropna=False)
    print(group_by_ans)
    largest_index = group_by_ans.index[0]
    return largest_index

def example_predict(answers, data):
    """
    :param data:
    :return: worker_answer
    """
    print(data)
    
    worker_answer = data
    worker_answer['_input_value_names'] = ""
    
    master_bib_id = data['master_bib_id']
    sub_bib_id = data['sub_bib_id']
    
    matched_answers = pick_up(answers, master_bib_id, sub_bib_id)
    if len(matched_answers) == 0:
        worker_answer['is_skipped'] = True
        return worker_answer
    
    decision = decide_by_majority_vote(matched_answers)
        
    if math.isnan(decision):
        worker_answer['is_skipped'] = True
    elif decision:
        worker_answer['is_same'] = True
    else:
        worker_answer['is_same'] = False
    
    return worker_answer

if __name__ == '__main__':
    answers = get_all_answers()
    
    api = crowd4py.API(api_info=API_CONF, project_info=PROJECT_CONF)
    for i in range(1000):
        task = api.get_task(debug=True)
        ans_data = example_predict(answers, task.data)
        print(api.post_answer(task.post_url, ans_data))
        print("posted answer: is_same={0}, is_skipped={1}".format(ans_data['is_same'], ans_data['is_skipped']))
