# coding: utf-8

"""
    Traction Guest API

    The Traction Guest API is currently under limited release to select customers as we gather and iterate on feedback.  # Getting Started If you are interested in getting early access to the API, please send us an email to [support@tractionguest.com](mailto:support@tractionguest.com).  We will also add you to our Slack channel where you can ask questions and get further help.  # Terms and Conditions Please visit: [https://tractionguest.com/tos/api/](https://tractionguest.com/tos/api/)  # Versioning This API follows [semantic versioning](https://semver.org/), which follows the `Major`.`Minor`.`Patch` format.  * The `Major` number increments when potentially incompatible changes are made. * The `Minor` number increments when backwards-compatible additions are made. * The `Patch` number increments when backwards-compatible bug-fixes are made.   # noqa: E501

    The version of the OpenAPI document: 0.15.0
    Contact: support@tractionguest.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from TractionGuest.configuration import Configuration


class PaginatedAuditLogsList(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'pagination': 'Pagination',
        'audit_logs': 'list[AuditLog]'
    }

    attribute_map = {
        'pagination': 'pagination',
        'audit_logs': 'audit_logs'
    }

    def __init__(self, pagination=None, audit_logs=None, local_vars_configuration=None):  # noqa: E501
        """PaginatedAuditLogsList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pagination = None
        self._audit_logs = None
        self.discriminator = None

        self.pagination = pagination
        self.audit_logs = audit_logs

    @property
    def pagination(self):
        """Gets the pagination of this PaginatedAuditLogsList.  # noqa: E501


        :return: The pagination of this PaginatedAuditLogsList.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this PaginatedAuditLogsList.


        :param pagination: The pagination of this PaginatedAuditLogsList.  # noqa: E501
        :type: Pagination
        """
        if self.local_vars_configuration.client_side_validation and pagination is None:  # noqa: E501
            raise ValueError("Invalid value for `pagination`, must not be `None`")  # noqa: E501

        self._pagination = pagination

    @property
    def audit_logs(self):
        """Gets the audit_logs of this PaginatedAuditLogsList.  # noqa: E501


        :return: The audit_logs of this PaginatedAuditLogsList.  # noqa: E501
        :rtype: list[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this PaginatedAuditLogsList.


        :param audit_logs: The audit_logs of this PaginatedAuditLogsList.  # noqa: E501
        :type: list[AuditLog]
        """
        if self.local_vars_configuration.client_side_validation and audit_logs is None:  # noqa: E501
            raise ValueError("Invalid value for `audit_logs`, must not be `None`")  # noqa: E501

        self._audit_logs = audit_logs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PaginatedAuditLogsList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaginatedAuditLogsList):
            return True

        return self.to_dict() != other.to_dict()
