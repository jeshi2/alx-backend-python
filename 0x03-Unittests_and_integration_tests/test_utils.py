#!/usr/bin/env python3

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function in the utils module.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: dict,
            path: tuple,
            expected_result) -> None:
        """
        Test the access_nested_map function with various inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
            self,
            nested_map,
            path):
        """
        Test that accessing a non-existing key raises a KeyError with
        the expected message.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test case for the get_json function in the utils module.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that get_json returns the expected result using
        unittest.mock.patch.
        """
        class Mocked(Mock):
            """
            class that inherits from Mock
            """

            def json(self):
                """
                json returning a payload
                """
                return test_payload

        with patch("requests.get") as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(test_url), test_payload)


if __name__ == "__main__":
    unittest.main()
