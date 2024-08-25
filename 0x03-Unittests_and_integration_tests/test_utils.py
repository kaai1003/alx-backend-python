#!/usr/bin/env python3
"""TestAccessNestedMap class Module"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock

access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class definition"""
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {'b': 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access_nested_map func"""
        test = access_nested_map(nested_map, path)
        self.assertEqual(test, expected)

    @parameterized.expand([({}, ("a",), 'a'),
                           ({"a": 1}, ("a", "b"), 'b')])
    def test_access_nested_map_exception(self,
                                         nested_map,
                                         path, exception):
        """raise exception test for nested map"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual("KeyError('{}')".format(exception),
                         repr(err.exception))


class TestGetJson(unittest.TestCase):
    """TestGetJson Class definition"""

    @parameterized.expand([('http://example.com', '{"payload": True}'),
                           ('http://holberton.io', '{"payload": False}')])
    def test_get_json(self, test_url, test_payload):
        """get json func test"""
        args = {'json.return_value': test_payload}
        with patch('requests.get', return_value=Mock(**args)) as req:
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            req.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """TestMemoize class definition"""

    def test_memoize(self):
        """test momeoize func"""

        class TestClass:
            """test class definition"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as m:
            test = TestClass()
            test.a_property()
            test.a_property()
            m.assert_called_once()
