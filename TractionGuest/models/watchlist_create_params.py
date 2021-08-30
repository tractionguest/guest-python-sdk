# coding: utf-8

"""
    Traction Guest API

    The Traction Guest API is currently under limited release to select customers as we gather and iterate on feedback.  # Getting Started If you are interested in getting early access to the API, please send us an email to [support@tractionguest.com](mailto:support@tractionguest.com).  We will also add you to our Slack channel where you can ask questions and get further help.  # Terms and Conditions Please visit: [https://tractionguest.com/tos/api/](https://tractionguest.com/tos/api/)  # Versioning This API follows [semantic versioning](https://semver.org/), which follows the `Major`.`Minor`.`Patch` format.  * The `Major` number increments when potentially incompatible changes are made. * The `Minor` number increments when backwards-compatible additions are made. * The `Patch` number increments when backwards-compatible bug-fixes are made.   # noqa: E501

    The version of the OpenAPI document: 0.17.0
    Contact: support@tractionguest.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from TractionGuest.configuration import Configuration


class WatchlistCreateParams(object):
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
        'aliases': 'list[str]',
        'notes': 'str',
        'last_name': 'str',
        'first_name': 'str',
        'email': 'str',
        'colour': 'str',
        'base64_image': 'str',
        'driver_license': 'str'
    }

    attribute_map = {
        'aliases': 'aliases',
        'notes': 'notes',
        'last_name': 'last_name',
        'first_name': 'first_name',
        'email': 'email',
        'colour': 'colour',
        'base64_image': 'base64_image',
        'driver_license': 'driver_license'
    }

    def __init__(self, aliases=None, notes=None, last_name=None, first_name=None, email=None, colour=None, base64_image=None, driver_license=None, local_vars_configuration=None):  # noqa: E501
        """WatchlistCreateParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._aliases = None
        self._notes = None
        self._last_name = None
        self._first_name = None
        self._email = None
        self._colour = None
        self._base64_image = None
        self._driver_license = None
        self.discriminator = None

        if aliases is not None:
            self.aliases = aliases
        if notes is not None:
            self.notes = notes
        if last_name is not None:
            self.last_name = last_name
        if first_name is not None:
            self.first_name = first_name
        if email is not None:
            self.email = email
        if colour is not None:
            self.colour = colour
        if base64_image is not None:
            self.base64_image = base64_image
        if driver_license is not None:
            self.driver_license = driver_license

    @property
    def aliases(self):
        """Gets the aliases of this WatchlistCreateParams.  # noqa: E501


        :return: The aliases of this WatchlistCreateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this WatchlistCreateParams.


        :param aliases: The aliases of this WatchlistCreateParams.  # noqa: E501
        :type: list[str]
        """

        self._aliases = aliases

    @property
    def notes(self):
        """Gets the notes of this WatchlistCreateParams.  # noqa: E501


        :return: The notes of this WatchlistCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this WatchlistCreateParams.


        :param notes: The notes of this WatchlistCreateParams.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def last_name(self):
        """Gets the last_name of this WatchlistCreateParams.  # noqa: E501


        :return: The last_name of this WatchlistCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this WatchlistCreateParams.


        :param last_name: The last_name of this WatchlistCreateParams.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def first_name(self):
        """Gets the first_name of this WatchlistCreateParams.  # noqa: E501


        :return: The first_name of this WatchlistCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this WatchlistCreateParams.


        :param first_name: The first_name of this WatchlistCreateParams.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def email(self):
        """Gets the email of this WatchlistCreateParams.  # noqa: E501


        :return: The email of this WatchlistCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this WatchlistCreateParams.


        :param email: The email of this WatchlistCreateParams.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def colour(self):
        """Gets the colour of this WatchlistCreateParams.  # noqa: E501


        :return: The colour of this WatchlistCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._colour

    @colour.setter
    def colour(self, colour):
        """Sets the colour of this WatchlistCreateParams.


        :param colour: The colour of this WatchlistCreateParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["RED", "YELLOW", "GREEN", "ORANGE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and colour not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `colour` ({0}), must be one of {1}"  # noqa: E501
                .format(colour, allowed_values)
            )

        self._colour = colour

    @property
    def base64_image(self):
        """Gets the base64_image of this WatchlistCreateParams.  # noqa: E501

        A base64 encoded image. base64_image should be strict encoded   # noqa: E501

        :return: The base64_image of this WatchlistCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._base64_image

    @base64_image.setter
    def base64_image(self, base64_image):
        """Sets the base64_image of this WatchlistCreateParams.

        A base64 encoded image. base64_image should be strict encoded   # noqa: E501

        :param base64_image: The base64_image of this WatchlistCreateParams.  # noqa: E501
        :type: str
        """

        self._base64_image = base64_image

    @property
    def driver_license(self):
        """Gets the driver_license of this WatchlistCreateParams.  # noqa: E501


        :return: The driver_license of this WatchlistCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._driver_license

    @driver_license.setter
    def driver_license(self, driver_license):
        """Sets the driver_license of this WatchlistCreateParams.


        :param driver_license: The driver_license of this WatchlistCreateParams.  # noqa: E501
        :type: str
        """

        self._driver_license = driver_license

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
        if not isinstance(other, WatchlistCreateParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WatchlistCreateParams):
            return True

        return self.to_dict() != other.to_dict()
