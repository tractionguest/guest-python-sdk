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
from TractionGuest.capacities_api import CapacitiesApi  # noqa: E501
from TractionGuest.rest import ApiException


class TestCapacitiesApi(unittest.TestCase):
    """CapacitiesApi unit test stubs"""

    def setUp(self):
        self.api = TractionGuest.capacities_api.CapacitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_capacity(self):
        """Test case for get_capacity

        Get the current capacity details for a location  # noqa: E501
        """
        pass

    def test_get_capacity_forecast(self):
        """Test case for get_capacity_forecast

        Get the capacity details for a location  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
