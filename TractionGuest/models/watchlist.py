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


class Watchlist(object):
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
        'id': 'int',
        'aliases': 'list[str]',
        'photo': 'str',
        'notes': 'str',
        'last_name': 'str',
        'first_name': 'str',
        'email': 'str',
        'colour': 'str',
        'driver_license': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'aliases': 'aliases',
        'photo': 'photo',
        'notes': 'notes',
        'last_name': 'last_name',
        'first_name': 'first_name',
        'email': 'email',
        'colour': 'colour',
        'driver_license': 'driver_license',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, aliases=None, photo=None, notes=None, last_name=None, first_name=None, email=None, colour=None, driver_license=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """Watchlist - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._aliases = None
        self._photo = None
        self._notes = None
        self._last_name = None
        self._first_name = None
        self._email = None
        self._colour = None
        self._driver_license = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        if aliases is not None:
            self.aliases = aliases
        if photo is not None:
            self.photo = photo
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
        if driver_license is not None:
            self.driver_license = driver_license
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Watchlist.  # noqa: E501


        :return: The id of this Watchlist.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Watchlist.


        :param id: The id of this Watchlist.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def aliases(self):
        """Gets the aliases of this Watchlist.  # noqa: E501


        :return: The aliases of this Watchlist.  # noqa: E501
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this Watchlist.


        :param aliases: The aliases of this Watchlist.  # noqa: E501
        :type: list[str]
        """

        self._aliases = aliases

    @property
    def photo(self):
        """Gets the photo of this Watchlist.  # noqa: E501


        :return: The photo of this Watchlist.  # noqa: E501
        :rtype: str
        """
        return self._photo

    @photo.setter
    def photo(self, photo):
        """Sets the photo of this Watchlist.


        :param photo: The photo of this Watchlist.  # noqa: E501
        :type: str
        """

        self._photo = photo

    @property
    def notes(self):
        """Gets the notes of this Watchlist.  # noqa: E501


        :return: The notes of this Watchlist.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Watchlist.


        :param notes: The notes of this Watchlist.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def last_name(self):
        """Gets the last_name of this Watchlist.  # noqa: E501


        :return: The last_name of this Watchlist.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Watchlist.


        :param last_name: The last_name of this Watchlist.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def first_name(self):
        """Gets the first_name of this Watchlist.  # noqa: E501


        :return: The first_name of this Watchlist.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Watchlist.


        :param first_name: The first_name of this Watchlist.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def email(self):
        """Gets the email of this Watchlist.  # noqa: E501


        :return: The email of this Watchlist.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Watchlist.


        :param email: The email of this Watchlist.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def colour(self):
        """Gets the colour of this Watchlist.  # noqa: E501


        :return: The colour of this Watchlist.  # noqa: E501
        :rtype: str
        """
        return self._colour

    @colour.setter
    def colour(self, colour):
        """Sets the colour of this Watchlist.


        :param colour: The colour of this Watchlist.  # noqa: E501
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
    def driver_license(self):
        """Gets the driver_license of this Watchlist.  # noqa: E501


        :return: The driver_license of this Watchlist.  # noqa: E501
        :rtype: str
        """
        return self._driver_license

    @driver_license.setter
    def driver_license(self, driver_license):
        """Sets the driver_license of this Watchlist.


        :param driver_license: The driver_license of this Watchlist.  # noqa: E501
        :type: str
        """

        self._driver_license = driver_license

    @property
    def created_at(self):
        """Gets the created_at of this Watchlist.  # noqa: E501


        :return: The created_at of this Watchlist.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Watchlist.


        :param created_at: The created_at of this Watchlist.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Watchlist.  # noqa: E501


        :return: The updated_at of this Watchlist.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Watchlist.


        :param updated_at: The updated_at of this Watchlist.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, Watchlist):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Watchlist):
            return True

        return self.to_dict() != other.to_dict()
