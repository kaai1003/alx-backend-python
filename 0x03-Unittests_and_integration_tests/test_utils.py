#!/usr/bin/env python3
"""TestAccessNestedMap class Module"""
from parameterized import parameterized
import unittest

access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class definition"""
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {'b': 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access_nested_map func"""
        test = access_nested_map(nested_map, path)
        self.assertEqual(test, expected)

    @parameterized.expand([({}, ("a",), KeyError),
                           ({"a": 1}, ("a", "b")), KeyError])
    def test_access_nested_map_exception(self,
                                         nested_map,
                                         path, exception):
        """raise exception test for nested map"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
