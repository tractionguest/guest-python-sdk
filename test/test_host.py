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
import datetime

import TractionGuest
from TractionGuest.models.host import Host  # noqa: E501
from TractionGuest.rest import ApiException

class TestHost(unittest.TestCase):
    """Host unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Host
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = TractionGuest.models.host.Host()  # noqa: E501
        if include_optional :
            return Host(
                id = 56, 
                email = '0', 
                first_name = '0', 
                last_name = '0', 
                profile_pic_url = '0', 
                department = '0', 
                mobile_number = '0'
            )
        else :
            return Host(
                id = 56,
        )

    def testHost(self):
        """Test Host"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
