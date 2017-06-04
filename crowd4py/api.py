# -*- coding: utf-8 -*-
from crowd4py import API_ROOT, USERID, PASSWORD

import requests
from . import helpers
from .task import Task
import lxml.etree as et


class API:
    """crowd4u API"""

    def __init__(self, user_info='', project_name='', relation_name=''):
        """API instance Constructor
        :param user_info:
        :param project_name:
        :param relation_name:
        """

        self.cookies = ""
        self.user_info = user_info
        self.project_name = project_name
        self.relation_name = relation_name

    def relation_data(self):
        """Sends a GET request.
        :return: :r.json:`Json` object
        :rtype: json Object or None
        """
        endpoint = "/api/relation_data"
        params = {"project_name": self.project_name,
                  "relation_name": self.relation_name}

        r = requests.get(url=API_ROOT + endpoint, params=params)
        return r.json() if r.status_code == 200 else None

    def get_task(self, debug=False) -> Task:
        task_url = self.get_task_url()
        task_url = task_url.replace('https://', 'http://') if debug else task_url
        r = requests.get(task_url, auth=(USERID, PASSWORD))
        self.cookies = r.cookies
        task = Task(xml_text=r.content)
        return task

    def request_answer(self, tid, increment_count=1):
        endpoint = "/api/request_task"
        params = {"project_name": self.project_name,
                  "relation_name": self.relation_name,
                  "tid": tid,
                  "increment_count": increment_count}
        r = requests.get(url=API_ROOT + endpoint, auth=(USERID, PASSWORD), params=params)
        return True if r.status_code == 200 else False

    def post_answer(self, post_url: str, ans_data: dict):
        values = ans_data.values()
        keys = ans_data.keys()
        attached_keys = [helpers.attach_prefix(k) for k in keys]
        post_data = dict(zip(attached_keys, values))
        r = requests.post(post_url, data=post_data, auth=(USERID, PASSWORD), cookies=self.cookies)
        return r.status_code

    def get_task_url(self) -> str:
        endpoint = '/task_assignment'
        r = requests.get(API_ROOT + endpoint, data=self.user_info, auth=(USERID, PASSWORD))
        json = r.json()
        task_url = json["task_url"]
        assert isinstance(task_url, str)
        return task_url
