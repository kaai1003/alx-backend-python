#!/usr/bin/env python3
"""TestGithubOrgClient class Module"""
from client import GithubOrgClient
import unittest
from unittest.mock import patch
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class definition"""

    @parameterized.expand([('google'), ('abc')])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """test org func"""

        test = GithubOrgClient(org_name)
        test.org()
        mock.called_with_once(test.ORG_URL.format(org=org_name))
