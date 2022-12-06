# coding: utf-8

"""
    Traction Guest API

    The Traction Guest API is currently under limited release to select customers as we gather and iterate on feedback.  # Getting Started If you are interested in getting early access to the API, please send us an email to [support@tractionguest.com](mailto:support@tractionguest.com).  We will also add you to our Slack channel where you can ask questions and get further help.  # Terms and Conditions Please visit: [https://tractionguest.com/tos/api/](https://tractionguest.com/tos/api/)  # Versioning This API follows [semantic versioning](https://semver.org/), which follows the `Major`.`Minor`.`Patch` format.  * The `Major` number increments when potentially incompatible changes are made. * The `Minor` number increments when backwards-compatible additions are made. * The `Patch` number increments when backwards-compatible bug-fixes are made.   # noqa: E501

    The version of the OpenAPI document: 0.18.0
    Contact: support@tractionguest.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from TractionGuest.configuration import Configuration


class AuditLogChange(object):
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
        'field_name': 'str',
        'field_value_before': 'str',
        'field_value_after': 'str',
        'format': 'str'
    }

    attribute_map = {
        'field_name': 'field_name',
        'field_value_before': 'field_value_before',
        'field_value_after': 'field_value_after',
        'format': 'format'
    }

    def __init__(self, field_name=None, field_value_before=None, field_value_after=None, format=None, local_vars_configuration=None):  # noqa: E501
        """AuditLogChange - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._field_name = None
        self._field_value_before = None
        self._field_value_after = None
        self._format = None
        self.discriminator = None

        if field_name is not None:
            self.field_name = field_name
        if field_value_before is not None:
            self.field_value_before = field_value_before
        if field_value_after is not None:
            self.field_value_after = field_value_after
        if format is not None:
            self.format = format

    @property
    def field_name(self):
        """Gets the field_name of this AuditLogChange.  # noqa: E501

        What the field should be displayed/labeled as  # noqa: E501

        :return: The field_name of this AuditLogChange.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this AuditLogChange.

        What the field should be displayed/labeled as  # noqa: E501

        :param field_name: The field_name of this AuditLogChange.  # noqa: E501
        :type: str
        """

        self._field_name = field_name

    @property
    def field_value_before(self):
        """Gets the field_value_before of this AuditLogChange.  # noqa: E501

        The value to be displayed for the field before changes  # noqa: E501

        :return: The field_value_before of this AuditLogChange.  # noqa: E501
        :rtype: str
        """
        return self._field_value_before

    @field_value_before.setter
    def field_value_before(self, field_value_before):
        """Sets the field_value_before of this AuditLogChange.

        The value to be displayed for the field before changes  # noqa: E501

        :param field_value_before: The field_value_before of this AuditLogChange.  # noqa: E501
        :type: str
        """

        self._field_value_before = field_value_before

    @property
    def field_value_after(self):
        """Gets the field_value_after of this AuditLogChange.  # noqa: E501

        The value to be displayed for the field after changes  # noqa: E501

        :return: The field_value_after of this AuditLogChange.  # noqa: E501
        :rtype: str
        """
        return self._field_value_after

    @field_value_after.setter
    def field_value_after(self, field_value_after):
        """Sets the field_value_after of this AuditLogChange.

        The value to be displayed for the field after changes  # noqa: E501

        :param field_value_after: The field_value_after of this AuditLogChange.  # noqa: E501
        :type: str
        """

        self._field_value_after = field_value_after

    @property
    def format(self):
        """Gets the format of this AuditLogChange.  # noqa: E501

        The format type of the field  # noqa: E501

        :return: The format of this AuditLogChange.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this AuditLogChange.

        The format type of the field  # noqa: E501

        :param format: The format of this AuditLogChange.  # noqa: E501
        :type: str
        """
        allowed_values = ["string", "boolean", "integer", "json", "no_value"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and format not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

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
        if not isinstance(other, AuditLogChange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuditLogChange):
            return True

        return self.to_dict() != other.to_dict()
