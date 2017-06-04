# -*- coding: utf-8 -*-

import unittest
from crowd4py import helpers


class Crowd4uHelpersTests(unittest.TestCase):
    """Crowd4py helpers.py tests"""

    def test_attach_prefix(self):
        test_normal = "tid"
        test_not_attach_01 = "_FACT1_relation_name"

        normal = helpers.attach_prefix(test_normal)
        self.assertEqual(normal, "_FACT1___tid")
        not_attach_01 = helpers.attach_prefix(test_not_attach_01)
        self.assertEqual(not_attach_01, "_FACT1_relation_name")

    def test_detach_prefix(self):
        test_normal = "_FACT1___tid"
        test_not_detach_01 = "_FACT1_relation_name"

        normal = helpers.detach_prefix(test_normal)
        self.assertEqual(normal, "tid")
        not_detach_01 = helpers.detach_prefix(test_not_detach_01)
        self.assertEqual(not_detach_01, "_FACT1_relation_name")


if __name__ == '__main__':
    unittest.main()
