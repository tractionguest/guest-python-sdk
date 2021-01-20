# coding: utf-8

"""
    Traction Guest API

    The Traction Guest API is currently under limited release to select customers as we gather and iterate on feedback.  # Getting Started If you are interested in getting early access to the API, please send us an email to [support@tractionguest.com](mailto:support@tractionguest.com).  We will also add you to our Slack channel where you can ask questions and get further help.  # Terms and Conditions Please visit: [https://tractionguest.com/tos/api/](https://tractionguest.com/tos/api/)  # Versioning This API follows [semantic versioning](https://semver.org/), which follows the `Major`.`Minor`.`Patch` format.  * The `Major` number increments when potentially incompatible changes are made. * The `Minor` number increments when backwards-compatible additions are made. * The `Patch` number increments when backwards-compatible bug-fixes are made.   # noqa: E501

    The version of the OpenAPI document: 0.14.2
    Contact: support@tractionguest.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from TractionGuest.configuration import Configuration


class PackageUpdateParams(object):
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
        'picked_up': 'bool',
        'carrier_name': 'str',
        'recipient_id': 'int'
    }

    attribute_map = {
        'picked_up': 'picked_up',
        'carrier_name': 'carrier_name',
        'recipient_id': 'recipient_id'
    }

    def __init__(self, picked_up=None, carrier_name=None, recipient_id=None, local_vars_configuration=None):  # noqa: E501
        """PackageUpdateParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._picked_up = None
        self._carrier_name = None
        self._recipient_id = None
        self.discriminator = None

        if picked_up is not None:
            self.picked_up = picked_up
        if carrier_name is not None:
            self.carrier_name = carrier_name
        if recipient_id is not None:
            self.recipient_id = recipient_id

    @property
    def picked_up(self):
        """Gets the picked_up of this PackageUpdateParams.  # noqa: E501

        changes the package_state to picked up and assigns non null value to picked_up_at  # noqa: E501

        :return: The picked_up of this PackageUpdateParams.  # noqa: E501
        :rtype: bool
        """
        return self._picked_up

    @picked_up.setter
    def picked_up(self, picked_up):
        """Sets the picked_up of this PackageUpdateParams.

        changes the package_state to picked up and assigns non null value to picked_up_at  # noqa: E501

        :param picked_up: The picked_up of this PackageUpdateParams.  # noqa: E501
        :type: bool
        """

        self._picked_up = picked_up

    @property
    def carrier_name(self):
        """Gets the carrier_name of this PackageUpdateParams.  # noqa: E501

        change/update the package's carrier/courier information  # noqa: E501

        :return: The carrier_name of this PackageUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._carrier_name

    @carrier_name.setter
    def carrier_name(self, carrier_name):
        """Sets the carrier_name of this PackageUpdateParams.

        change/update the package's carrier/courier information  # noqa: E501

        :param carrier_name: The carrier_name of this PackageUpdateParams.  # noqa: E501
        :type: str
        """

        self._carrier_name = carrier_name

    @property
    def recipient_id(self):
        """Gets the recipient_id of this PackageUpdateParams.  # noqa: E501

        id of the Host for which you want to send notifications to regarding their package  # noqa: E501

        :return: The recipient_id of this PackageUpdateParams.  # noqa: E501
        :rtype: int
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this PackageUpdateParams.

        id of the Host for which you want to send notifications to regarding their package  # noqa: E501

        :param recipient_id: The recipient_id of this PackageUpdateParams.  # noqa: E501
        :type: int
        """

        self._recipient_id = recipient_id

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
        if not isinstance(other, PackageUpdateParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PackageUpdateParams):
            return True

        return self.to_dict() != other.to_dict()
