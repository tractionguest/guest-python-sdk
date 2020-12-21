# coding: utf-8

"""
    Traction Guest API

    The Traction Guest API is currently under limited release to select customers as we gather and iterate on feedback.  # Getting Started If you are interested in getting early access to the API, please send us an email to [support@tractionguest.com](mailto:support@tractionguest.com).  We will also add you to our Slack channel where you can ask questions and get further help.  # Terms and Conditions Please visit: [https://tractionguest.com/tos/api/](https://tractionguest.com/tos/api/)  # Versioning This API follows [semantic versioning](https://semver.org/), which follows the `Major`.`Minor`.`Patch` format.  * The `Major` number increments when potentially incompatible changes are made. * The `Minor` number increments when backwards-compatible additions are made. * The `Patch` number increments when backwards-compatible bug-fixes are made.   # noqa: E501

    The version of the OpenAPI document: 0.14.1
    Contact: support@tractionguest.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from TractionGuest.configuration import Configuration


class PaginatedRegistrationsList(object):
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
        'registrations': 'list[object]',
        'pagination': 'object'
    }

    attribute_map = {
        'registrations': 'registrations',
        'pagination': 'pagination'
    }

    def __init__(self, registrations=None, pagination=None, local_vars_configuration=None):  # noqa: E501
        """PaginatedRegistrationsList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._registrations = None
        self._pagination = None
        self.discriminator = None

        if registrations is not None:
            self.registrations = registrations
        if pagination is not None:
            self.pagination = pagination

    @property
    def registrations(self):
        """Gets the registrations of this PaginatedRegistrationsList.  # noqa: E501


        :return: The registrations of this PaginatedRegistrationsList.  # noqa: E501
        :rtype: list[object]
        """
        return self._registrations

    @registrations.setter
    def registrations(self, registrations):
        """Sets the registrations of this PaginatedRegistrationsList.


        :param registrations: The registrations of this PaginatedRegistrationsList.  # noqa: E501
        :type: list[object]
        """

        self._registrations = registrations

    @property
    def pagination(self):
        """Gets the pagination of this PaginatedRegistrationsList.  # noqa: E501


        :return: The pagination of this PaginatedRegistrationsList.  # noqa: E501
        :rtype: object
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this PaginatedRegistrationsList.


        :param pagination: The pagination of this PaginatedRegistrationsList.  # noqa: E501
        :type: object
        """

        self._pagination = pagination

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
        if not isinstance(other, PaginatedRegistrationsList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaginatedRegistrationsList):
            return True

        return self.to_dict() != other.to_dict()
