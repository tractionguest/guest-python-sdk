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


class ExternalWatchlistResult(object):
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
        'matches': 'list[WatchlistMatch]',
        'colour': 'str',
        'integration': 'str',
        'search_terms': 'WatchlistSearch'
    }

    attribute_map = {
        'matches': 'matches',
        'colour': 'colour',
        'integration': 'integration',
        'search_terms': 'search_terms'
    }

    def __init__(self, matches=None, colour=None, integration=None, search_terms=None, local_vars_configuration=None):  # noqa: E501
        """ExternalWatchlistResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._matches = None
        self._colour = None
        self._integration = None
        self._search_terms = None
        self.discriminator = None

        if matches is not None:
            self.matches = matches
        if colour is not None:
            self.colour = colour
        if integration is not None:
            self.integration = integration
        if search_terms is not None:
            self.search_terms = search_terms

    @property
    def matches(self):
        """Gets the matches of this ExternalWatchlistResult.  # noqa: E501


        :return: The matches of this ExternalWatchlistResult.  # noqa: E501
        :rtype: list[WatchlistMatch]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ExternalWatchlistResult.


        :param matches: The matches of this ExternalWatchlistResult.  # noqa: E501
        :type: list[WatchlistMatch]
        """

        self._matches = matches

    @property
    def colour(self):
        """Gets the colour of this ExternalWatchlistResult.  # noqa: E501

          # noqa: E501

        :return: The colour of this ExternalWatchlistResult.  # noqa: E501
        :rtype: str
        """
        return self._colour

    @colour.setter
    def colour(self, colour):
        """Sets the colour of this ExternalWatchlistResult.

          # noqa: E501

        :param colour: The colour of this ExternalWatchlistResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["RED", "GREEN", "YELLOW", "ORANGE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and colour not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `colour` ({0}), must be one of {1}"  # noqa: E501
                .format(colour, allowed_values)
            )

        self._colour = colour

    @property
    def integration(self):
        """Gets the integration of this ExternalWatchlistResult.  # noqa: E501

          # noqa: E501

        :return: The integration of this ExternalWatchlistResult.  # noqa: E501
        :rtype: str
        """
        return self._integration

    @integration.setter
    def integration(self, integration):
        """Sets the integration of this ExternalWatchlistResult.

          # noqa: E501

        :param integration: The integration of this ExternalWatchlistResult.  # noqa: E501
        :type: str
        """

        self._integration = integration

    @property
    def search_terms(self):
        """Gets the search_terms of this ExternalWatchlistResult.  # noqa: E501


        :return: The search_terms of this ExternalWatchlistResult.  # noqa: E501
        :rtype: WatchlistSearch
        """
        return self._search_terms

    @search_terms.setter
    def search_terms(self, search_terms):
        """Sets the search_terms of this ExternalWatchlistResult.


        :param search_terms: The search_terms of this ExternalWatchlistResult.  # noqa: E501
        :type: WatchlistSearch
        """

        self._search_terms = search_terms

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
        if not isinstance(other, ExternalWatchlistResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExternalWatchlistResult):
            return True

        return self.to_dict() != other.to_dict()
