# -*- coding: utf-8 -*-
from __init__ import API_CONF, PROJECT_CONF

import json
import pandas as pd
import math
import random
import time

import crowd4py

def get_all_answers():
    return pd.read_csv('answers/answered_facts_summary.csv')

def load_current_answers():
    try:
        print("loading pickle file...")
        return pd.read_pickle("answers/current_answers.pickle")
    except:
        print("generating answering data...")
        return pd.read_csv('answers/answered_facts_summary.csv')

def save_current_answers(current):
    current.to_pickle("answers/current_answers.pickle")

def pick_up(answers, master_bib_id, sub_bib_id):
    matched_answers = answers[(answers.master_bib_id == master_bib_id) & (answers.sub_bib_id == sub_bib_id)]
    return matched_answers

def choice_answers(current):
    print("---choice_answers---")
    print(len(current))
    print(current)

    choiced = current.sample(n=1)

    answer = choiced.iloc[0]['answer']
    index = choiced.index[0]
    return answer, index

def example_predict(answers, current, data):
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
    human_answers = pick_up(current, master_bib_id, sub_bib_id)

    # 3個以上回答がないデータの場合もしくは、
    # 回答が1個もない場合はスキップする
    if len(matched_answers) <= 3 or len(human_answers) < 1:
        worker_answer['is_skipped'] = True
        return worker_answer, current

    decision, idx = choice_answers(human_answers)
    if math.isnan(decision):
        worker_answer['is_skipped'] = True
    elif decision:
        worker_answer['is_same'] = True
    else:
        worker_answer['is_same'] = False

    current = current.drop(idx)
    return worker_answer, current

if __name__ == '__main__':
    answers = get_all_answers()
    current = load_current_answers()

    print(len(answers))
    print(len(current))

    try:
        api = crowd4py.API(api_info=API_CONF, project_info=PROJECT_CONF)
        for i in range(1000):
            task = api.get_task(debug=True)
            ans_data, current = example_predict(answers, current, task.data)
            print(api.post_answer(task.post_url, ans_data))
            print("posted answer: is_same={0}, is_skipped={1}".format(ans_data['is_same'], ans_data['is_skipped']))
    finally:
        save_current_answers(current)


