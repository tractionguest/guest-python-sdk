# coding: utf-8

"""
    Traction Guest API

    The Traction Guest API is currently under limited release to select customers as we gather and iterate on feedback.  # Getting Started If you are interested in getting early access to the API, please send us an email to [support@tractionguest.com](mailto:support@tractionguest.com).  We will also add you to our Slack channel where you can ask questions and get further help.  # Terms and Conditions Please visit: [https://tractionguest.com/tos/api/](https://tractionguest.com/tos/api/)  # Versioning This API follows [semantic versioning](https://semver.org/), which follows the `Major`.`Minor`.`Patch` format.  * The `Major` number increments when potentially incompatible changes are made. * The `Minor` number increments when backwards-compatible additions are made. * The `Patch` number increments when backwards-compatible bug-fixes are made.   # noqa: E501

    The version of the OpenAPI document: 0.14.1
    Contact: support@tractionguest.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import TractionGuest
from TractionGuest.packages_api import PackagesApi  # noqa: E501
from TractionGuest.rest import ApiException


class TestPackagesApi(unittest.TestCase):
    """PackagesApi unit test stubs"""

    def setUp(self):
        self.api = TractionGuest.packages_api.PackagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_package(self):
        """Test case for create_package

        Create package  # noqa: E501
        """
        pass

    def test_delete_package(self):
        """Test case for delete_package

        """
        pass

    def test_get_package(self):
        """Test case for get_package

        Get Package  # noqa: E501
        """
        pass

    def test_get_packages(self):
        """Test case for get_packages

        Get packages  # noqa: E501
        """
        pass

    def test_update_package(self):
        """Test case for update_package

        Update Package  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
