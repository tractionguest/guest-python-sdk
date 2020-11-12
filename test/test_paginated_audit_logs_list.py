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
from TractionGuest.models.paginated_audit_logs_list import PaginatedAuditLogsList  # noqa: E501
from TractionGuest.rest import ApiException

class TestPaginatedAuditLogsList(unittest.TestCase):
    """PaginatedAuditLogsList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedAuditLogsList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = TractionGuest.models.paginated_audit_logs_list.PaginatedAuditLogsList()  # noqa: E501
        if include_optional :
            return PaginatedAuditLogsList(
                pagination = TractionGuest.models.pagination.Pagination(
                    total_records = 56, 
                    current_offset = 56, 
                    next_offset = 56, 
                    last_id = 56, 
                    limit = 56, ), 
                audit_logs = [
                    TractionGuest.models.audit_log.AuditLog(
                        id = 56, 
                        created_at = '0', 
                        request_uuid = '0', 
                        remote_address = '0', 
                        comment = '0', 
                        version = 56, 
                        audited_changes = [
                            TractionGuest.models.audit_log_change.AuditLogChange(
                                field_name = '0', 
                                field_value_before = '0', 
                                field_value_after = '0', 
                                format = 'string', )
                            ], 
                        action = '0', 
                        username = '0', 
                        user_id = 56, 
                        auditable_type = '0', 
                        auditable_id = 56, )
                    ]
            )
        else :
            return PaginatedAuditLogsList(
                pagination = TractionGuest.models.pagination.Pagination(
                    total_records = 56, 
                    current_offset = 56, 
                    next_offset = 56, 
                    last_id = 56, 
                    limit = 56, ),
                audit_logs = [
                    TractionGuest.models.audit_log.AuditLog(
                        id = 56, 
                        created_at = '0', 
                        request_uuid = '0', 
                        remote_address = '0', 
                        comment = '0', 
                        version = 56, 
                        audited_changes = [
                            TractionGuest.models.audit_log_change.AuditLogChange(
                                field_name = '0', 
                                field_value_before = '0', 
                                field_value_after = '0', 
                                format = 'string', )
                            ], 
                        action = '0', 
                        username = '0', 
                        user_id = 56, 
                        auditable_type = '0', 
                        auditable_id = 56, )
                    ],
        )

    def testPaginatedAuditLogsList(self):
        """Test PaginatedAuditLogsList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
