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


class SigninUpdateParams(object):
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
        'is_signed_out': 'bool',
        'is_acknowledged': 'bool',
        'is_accounted_for': 'bool'
    }

    attribute_map = {
        'is_signed_out': 'is_signed_out',
        'is_acknowledged': 'is_acknowledged',
        'is_accounted_for': 'is_accounted_for'
    }

    def __init__(self, is_signed_out=None, is_acknowledged=None, is_accounted_for=None, local_vars_configuration=None):  # noqa: E501
        """SigninUpdateParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_signed_out = None
        self._is_acknowledged = None
        self._is_accounted_for = None
        self.discriminator = None

        if is_signed_out is not None:
            self.is_signed_out = is_signed_out
        if is_acknowledged is not None:
            self.is_acknowledged = is_acknowledged
        if is_accounted_for is not None:
            self.is_accounted_for = is_accounted_for

    @property
    def is_signed_out(self):
        """Gets the is_signed_out of this SigninUpdateParams.  # noqa: E501

        Used to sign out the `Signin`, can only be set to `true`.  # noqa: E501

        :return: The is_signed_out of this SigninUpdateParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_signed_out

    @is_signed_out.setter
    def is_signed_out(self, is_signed_out):
        """Sets the is_signed_out of this SigninUpdateParams.

        Used to sign out the `Signin`, can only be set to `true`.  # noqa: E501

        :param is_signed_out: The is_signed_out of this SigninUpdateParams.  # noqa: E501
        :type: bool
        """

        self._is_signed_out = is_signed_out

    @property
    def is_acknowledged(self):
        """Gets the is_acknowledged of this SigninUpdateParams.  # noqa: E501

        Used to acknowledge the `Signin`, can only be set to `true`.  # noqa: E501

        :return: The is_acknowledged of this SigninUpdateParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_acknowledged

    @is_acknowledged.setter
    def is_acknowledged(self, is_acknowledged):
        """Sets the is_acknowledged of this SigninUpdateParams.

        Used to acknowledge the `Signin`, can only be set to `true`.  # noqa: E501

        :param is_acknowledged: The is_acknowledged of this SigninUpdateParams.  # noqa: E501
        :type: bool
        """

        self._is_acknowledged = is_acknowledged

    @property
    def is_accounted_for(self):
        """Gets the is_accounted_for of this SigninUpdateParams.  # noqa: E501

        Used when keeping track of people in emergency situations  # noqa: E501

        :return: The is_accounted_for of this SigninUpdateParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_accounted_for

    @is_accounted_for.setter
    def is_accounted_for(self, is_accounted_for):
        """Sets the is_accounted_for of this SigninUpdateParams.

        Used when keeping track of people in emergency situations  # noqa: E501

        :param is_accounted_for: The is_accounted_for of this SigninUpdateParams.  # noqa: E501
        :type: bool
        """

        self._is_accounted_for = is_accounted_for

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
        if not isinstance(other, SigninUpdateParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SigninUpdateParams):
            return True

        return self.to_dict() != other.to_dict()
