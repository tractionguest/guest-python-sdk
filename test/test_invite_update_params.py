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
from TractionGuest.models.invite_update_params import InviteUpdateParams  # noqa: E501
from TractionGuest.rest import ApiException

class TestInviteUpdateParams(unittest.TestCase):
    """InviteUpdateParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InviteUpdateParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = TractionGuest.models.invite_update_params.InviteUpdateParams()  # noqa: E501
        if include_optional :
            return InviteUpdateParams(
                mobile_number = '0', 
                user_id = 56, 
                on_premise = True, 
                notification_triggers = [
                    TractionGuest.models.notification_trigger.NotificationTrigger(
                        offset_unit = 'days', 
                        notification_groups = [
                            '0'
                            ], 
                        email_template_id = 56, 
                        offset_origin = 'START', 
                        offset_amount = 56, 
                        offset_direction = 'BEFORE', )
                    ], 
                first_name = '0', 
                email_template_id = 56, 
                custom_fields = [
                    TractionGuest.models.custom_field.CustomField(
                        format = 'string', 
                        field_name = '0', 
                        field_value = '0', 
                        id = 56, )
                    ], 
                host_ids = [
                    56
                    ], 
                title = '0', 
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                last_name = '0', 
                end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                email = '0', 
                company = '0'
            )
        else :
            return InviteUpdateParams(
        )

    def testInviteUpdateParams(self):
        """Test InviteUpdateParams"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
