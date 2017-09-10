# -*- coding: utf-8 -*-
import unittest
import lxml.etree as et
import sys
import os
from crowd4py import Task


class Crowd4pyTaskTests(unittest.TestCase):
    """Crowd4py task.py tests"""

    def test_get_value_from_xml(self):
        xml = open("tests/task.xml", encoding='utf-8')
        xml_text = xml.read()
        etroot = et.fromstring(xml_text.encode())
        data_from_xml = Task.get_value_from_xml(etroot=etroot)
        data = dict(tid='999', _FACT1_relation_name='Test')
        self.assertEqual(data_from_xml['tid'], data['tid'])
        xml.close()

    def test_get_post_url(self):
        xml = open("tests/task.xml", encoding='utf-8')
        xml_text = xml.read()
        etroot = et.fromstring(xml_text.encode())
        task_post_url = Task.get_post_url(etroot=etroot)
        post_url = "http://oahu.slis.tsukuba.ac.jp/event/CompTest?_task_id=5146153"
        self.assertEqual(first=task_post_url, second=post_url)
        xml.close()

    def test_get_post_url_from_html(self):
        html = open("tests/request_priority.html", encoding='utf-8')
        html_text = html.read()
        etroot = et.fromstring(html_text.encode())
        url = Task.get_post_url_from_html(etroot=etroot)
        self.assertEqual(first=url, second='//crowd4u.org/event/comp_product?_task_id=2838815')
        html.close()

    def test_get_priority_params_from_html(self):
        html = open("tests/request_priority.html", encoding='utf-8')
        html_text = html.read()
        etroot = et.fromstring(html_text.encode())
        d = Task.get_priority_params_from_html(etroot=etroot)
        self.assertEqual(first=d['_FACT1___tid'], second="tid")
        self.assertEqual(first=d['tid'], second="")
        html.close()

if __name__ == '__main__':
    unittest.main()
