# -*- coding: utf-8 -*-
import lxml
from . import helpers
import lxml.etree as et


class Task:
    """task object"""

    def __init__(self, xml_text):
        etroot = et.fromstring(text=xml_text)
        self.data = self.get_value_from_xml(etroot=etroot)
        self.post_url = self.get_post_url(etroot=etroot)

    def __repr__(self):
        return self.data

    @staticmethod
    def get_value_from_xml(etroot: lxml.etree) -> dict:
        """
        get keys and values as array object from lxml.etree object
        :param etroot:lxml.etree object
        :return name, values: both are array object.
        """
        keys = []
        values = []
        for child in etroot.iter('parameter'):
            keys.append(child.find('name').text)
            values.append(child.find('value').text)

        detach_prefix_keys = [helpers.detach_prefix(k) for k in keys]
        data = dict(zip(detach_prefix_keys, values))
        return data

    @staticmethod
    def get_post_url(etroot: lxml.etree) -> str:
        """
        get post url from etree object
        :param etroot: lxml.etree object
        :return: url
        """
        post_url = "http:" + etroot.find('post_url').text
        return post_url

    @staticmethod
    def get_priority_from_html(etroot: lxml.etree) -> dict:
        keys = []
        values = []
        attr = etroot.xpath('//form')[0].attrib
        url = attr['action']

        keys.append('post_url')
        values.append(url)
        for child in etroot.iter('input'):
            try:
                keys.append(child.attrib['name'])
                values.append(child.attrib['value'])
            except:
                pass
        d = dict(zip(keys, values))
        return d
