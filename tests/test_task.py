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
        xml_text = Task.text_cleaning(xml_text.encode())
        etroot = et.fromstring(xml_text)
        data_from_xml = Task.get_value_from_xml(etroot=etroot)
        data = dict(tid='999', _FACT1_relation_name='Test')
        self.assertEqual(data_from_xml['tid'], data['tid'])
        xml.close()

    def test_get_post_url(self):
        xml = open("tests/task.xml", encoding='utf-8')
        xml_text = xml.read()
        xml_text = Task.text_cleaning(xml_text.encode())
        etroot = et.fromstring(xml_text)
        task_post_url = Task.get_post_url(etroot=etroot)
        post_url = "http://oahu.slis.tsukuba.ac.jp/event/CompTest?_task_id=5146153"
        self.assertEqual(first=task_post_url, second=post_url)
        xml.close()


if __name__ == '__main__':
    unittest.main()
