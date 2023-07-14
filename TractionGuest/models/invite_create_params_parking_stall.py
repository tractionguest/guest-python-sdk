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


class InviteCreateParamsParkingStall(object):
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
        'stall_number': 'int',
        'parking_lot_id': 'int',
        'parking_stall_id': 'int'
    }

    attribute_map = {
        'stall_number': 'stall_number',
        'parking_lot_id': 'parking_lot_id',
        'parking_stall_id': 'parking_stall_id'
    }

    def __init__(self, stall_number=None, parking_lot_id=None, parking_stall_id=None, local_vars_configuration=None):  # noqa: E501
        """InviteCreateParamsParkingStall - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._stall_number = None
        self._parking_lot_id = None
        self._parking_stall_id = None
        self.discriminator = None

        if stall_number is not None:
            self.stall_number = stall_number
        if parking_lot_id is not None:
            self.parking_lot_id = parking_lot_id
        if parking_stall_id is not None:
            self.parking_stall_id = parking_stall_id

    @property
    def stall_number(self):
        """Gets the stall_number of this InviteCreateParamsParkingStall.  # noqa: E501


        :return: The stall_number of this InviteCreateParamsParkingStall.  # noqa: E501
        :rtype: int
        """
        return self._stall_number

    @stall_number.setter
    def stall_number(self, stall_number):
        """Sets the stall_number of this InviteCreateParamsParkingStall.


        :param stall_number: The stall_number of this InviteCreateParamsParkingStall.  # noqa: E501
        :type: int
        """

        self._stall_number = stall_number

    @property
    def parking_lot_id(self):
        """Gets the parking_lot_id of this InviteCreateParamsParkingStall.  # noqa: E501


        :return: The parking_lot_id of this InviteCreateParamsParkingStall.  # noqa: E501
        :rtype: int
        """
        return self._parking_lot_id

    @parking_lot_id.setter
    def parking_lot_id(self, parking_lot_id):
        """Sets the parking_lot_id of this InviteCreateParamsParkingStall.


        :param parking_lot_id: The parking_lot_id of this InviteCreateParamsParkingStall.  # noqa: E501
        :type: int
        """

        self._parking_lot_id = parking_lot_id

    @property
    def parking_stall_id(self):
        """Gets the parking_stall_id of this InviteCreateParamsParkingStall.  # noqa: E501


        :return: The parking_stall_id of this InviteCreateParamsParkingStall.  # noqa: E501
        :rtype: int
        """
        return self._parking_stall_id

    @parking_stall_id.setter
    def parking_stall_id(self, parking_stall_id):
        """Sets the parking_stall_id of this InviteCreateParamsParkingStall.


        :param parking_stall_id: The parking_stall_id of this InviteCreateParamsParkingStall.  # noqa: E501
        :type: int
        """

        self._parking_stall_id = parking_stall_id

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
        if not isinstance(other, InviteCreateParamsParkingStall):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InviteCreateParamsParkingStall):
            return True

        return self.to_dict() != other.to_dict()
