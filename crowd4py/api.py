# -*- coding: utf-8 -*-
import requests
from . import helpers
from .task import Task
import lxml.etree as et


class API:
    """crowd4u API"""

    def __init__(self, api_info={}, project_info={}):
        """API instance Constructor
        :param api_info:
        :param project_info:
        """
        user_id = api_info.get('USERID', '')
        password = api_info.get('PASSWORD', '')
        api_root = api_info.get('API_ROOT', 'http://crowd4u.org')
        user_info = {
            "requester": api_info.get('REQUESTER', '-1'),
            "from_app": 1,
            "_machine_language": "ja_JP",
            "group_id": api_info.get('GROUP_ID', '83'),
            "_user_token": api_info.get('USER_TOKEN', '')
        }

        self.user_id = user_id
        self.password = password
        self.api_root = api_root
        self.user_info = user_info

        project_name = project_info.get('PROJECT_NAME', '')
        relation_name = project_info.get('RELATION_NAME', '')

        self.cookies = ""
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

        r = requests.get(url=self.api_root + endpoint, params=params)
        return r.json() if r.status_code == 200 else None

    def get_task(self, debug=False) -> Task:
        task_url = self.get_task_url()
        task_url = task_url.replace('https://', 'http://') if debug else task_url
        r = requests.get(task_url, auth=(self.user_id, self.password))
        self.cookies = r.cookies
        task = Task(xml_text=r.content)
        return task

    def request_answer(self, tid, increment_count=1):
        endpoint = "/api/request_task"
        params = {"project_name": self.project_name,
                  "relation_name": "_Priority_Current",
                  "tid": tid,
                  "increment_count": increment_count}
        r = requests.put(url=self.api_root + endpoint, auth=(self.user_id, self.password), params=params)
        return True if r.status_code == 200 else False

    def post_answer(self, post_url: str, ans_data: dict):
        values = ans_data.values()
        keys = ans_data.keys()
        attached_keys = [helpers.attach_prefix(k) for k in keys]
        post_data = dict(zip(attached_keys, values))
        r = requests.post(post_url, data=post_data, auth=(self.user_id, self.password), cookies=self.cookies)
        return r.status_code

    def get_task_url(self) -> str:
        endpoint = '/task_assignment'
        r = requests.get(self.api_root + endpoint, data=self.user_info, auth=(self.user_id, self.password))
        json = r.json()
        task_url = json["task_url"]
        assert isinstance(task_url, str)
        return task_url
