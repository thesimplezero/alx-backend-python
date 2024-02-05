#!/usr/bin/env python3
"""
Unit tests for client.py
"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for GithubOrgClient class
    """

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test the has_license method of GithubOrgClient class
        """
        # Instantiate GithubOrgClient
        client = GithubOrgClient("testorg")

        result = client.has_license(repo, license_key)

        self.assertEqual(result, expected_result)
