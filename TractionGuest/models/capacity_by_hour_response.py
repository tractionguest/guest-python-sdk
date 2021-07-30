# coding: utf-8

"""
    Traction Guest API

    The Traction Guest API is currently under limited release to select customers as we gather and iterate on feedback.  # Getting Started If you are interested in getting early access to the API, please send us an email to [support@tractionguest.com](mailto:support@tractionguest.com).  We will also add you to our Slack channel where you can ask questions and get further help.  # Terms and Conditions Please visit: [https://tractionguest.com/tos/api/](https://tractionguest.com/tos/api/)  # Versioning This API follows [semantic versioning](https://semver.org/), which follows the `Major`.`Minor`.`Patch` format.  * The `Major` number increments when potentially incompatible changes are made. * The `Minor` number increments when backwards-compatible additions are made. * The `Patch` number increments when backwards-compatible bug-fixes are made.   # noqa: E501

    The version of the OpenAPI document: 0.16.0
    Contact: support@tractionguest.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from TractionGuest.configuration import Configuration


class CapacityByHourResponse(object):
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
        'range_start': 'datetime',
        'range_end': 'datetime',
        'expected_visitors': 'int'
    }

    attribute_map = {
        'range_start': 'range_start',
        'range_end': 'range_end',
        'expected_visitors': 'expected_visitors'
    }

    def __init__(self, range_start=None, range_end=None, expected_visitors=None, local_vars_configuration=None):  # noqa: E501
        """CapacityByHourResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._range_start = None
        self._range_end = None
        self._expected_visitors = None
        self.discriminator = None

        if range_start is not None:
            self.range_start = range_start
        if range_end is not None:
            self.range_end = range_end
        if expected_visitors is not None:
            self.expected_visitors = expected_visitors

    @property
    def range_start(self):
        """Gets the range_start of this CapacityByHourResponse.  # noqa: E501


        :return: The range_start of this CapacityByHourResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._range_start

    @range_start.setter
    def range_start(self, range_start):
        """Sets the range_start of this CapacityByHourResponse.


        :param range_start: The range_start of this CapacityByHourResponse.  # noqa: E501
        :type: datetime
        """

        self._range_start = range_start

    @property
    def range_end(self):
        """Gets the range_end of this CapacityByHourResponse.  # noqa: E501


        :return: The range_end of this CapacityByHourResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._range_end

    @range_end.setter
    def range_end(self, range_end):
        """Sets the range_end of this CapacityByHourResponse.


        :param range_end: The range_end of this CapacityByHourResponse.  # noqa: E501
        :type: datetime
        """

        self._range_end = range_end

    @property
    def expected_visitors(self):
        """Gets the expected_visitors of this CapacityByHourResponse.  # noqa: E501


        :return: The expected_visitors of this CapacityByHourResponse.  # noqa: E501
        :rtype: int
        """
        return self._expected_visitors

    @expected_visitors.setter
    def expected_visitors(self, expected_visitors):
        """Sets the expected_visitors of this CapacityByHourResponse.


        :param expected_visitors: The expected_visitors of this CapacityByHourResponse.  # noqa: E501
        :type: int
        """

        self._expected_visitors = expected_visitors

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
        if not isinstance(other, CapacityByHourResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CapacityByHourResponse):
            return True

        return self.to_dict() != other.to_dict()
