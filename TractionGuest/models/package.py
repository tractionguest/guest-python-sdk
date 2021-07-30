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


class Package(object):
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
        'recipient': 'Host',
        'location': 'Location',
        'package_state': 'str',
        'carrier_name': 'str',
        'picked_up_at': 'datetime',
        'created_at': 'datetime',
        'image': 'Image'
    }

    attribute_map = {
        'id': 'id',
        'recipient': 'recipient',
        'location': 'location',
        'package_state': 'package_state',
        'carrier_name': 'carrier_name',
        'picked_up_at': 'picked_up_at',
        'created_at': 'created_at',
        'image': 'image'
    }

    def __init__(self, id=None, recipient=None, location=None, package_state=None, carrier_name=None, picked_up_at=None, created_at=None, image=None, local_vars_configuration=None):  # noqa: E501
        """Package - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._recipient = None
        self._location = None
        self._package_state = None
        self._carrier_name = None
        self._picked_up_at = None
        self._created_at = None
        self._image = None
        self.discriminator = None

        self.id = id
        if recipient is not None:
            self.recipient = recipient
        self.location = location
        self.package_state = package_state
        if carrier_name is not None:
            self.carrier_name = carrier_name
        self.picked_up_at = picked_up_at
        self.created_at = created_at
        if image is not None:
            self.image = image

    @property
    def id(self):
        """Gets the id of this Package.  # noqa: E501


        :return: The id of this Package.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Package.


        :param id: The id of this Package.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def recipient(self):
        """Gets the recipient of this Package.  # noqa: E501


        :return: The recipient of this Package.  # noqa: E501
        :rtype: Host
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this Package.


        :param recipient: The recipient of this Package.  # noqa: E501
        :type: Host
        """

        self._recipient = recipient

    @property
    def location(self):
        """Gets the location of this Package.  # noqa: E501


        :return: The location of this Package.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Package.


        :param location: The location of this Package.  # noqa: E501
        :type: Location
        """
        if self.local_vars_configuration.client_side_validation and location is None:  # noqa: E501
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def package_state(self):
        """Gets the package_state of this Package.  # noqa: E501

        this can be one of the following states: 'processing', 'recipient_matched', 'needs_attention' or 'picked_up'  # noqa: E501

        :return: The package_state of this Package.  # noqa: E501
        :rtype: str
        """
        return self._package_state

    @package_state.setter
    def package_state(self, package_state):
        """Sets the package_state of this Package.

        this can be one of the following states: 'processing', 'recipient_matched', 'needs_attention' or 'picked_up'  # noqa: E501

        :param package_state: The package_state of this Package.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and package_state is None:  # noqa: E501
            raise ValueError("Invalid value for `package_state`, must not be `None`")  # noqa: E501
        allowed_values = ["processing", "recipient_matched", "needs_attention", "picked_up"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and package_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `package_state` ({0}), must be one of {1}"  # noqa: E501
                .format(package_state, allowed_values)
            )

        self._package_state = package_state

    @property
    def carrier_name(self):
        """Gets the carrier_name of this Package.  # noqa: E501

        A carrier name that gets detected on the shipping label. i.e. USPS, Purolator, DHL, Canada Post, Royal Mail, etc...   # noqa: E501

        :return: The carrier_name of this Package.  # noqa: E501
        :rtype: str
        """
        return self._carrier_name

    @carrier_name.setter
    def carrier_name(self, carrier_name):
        """Sets the carrier_name of this Package.

        A carrier name that gets detected on the shipping label. i.e. USPS, Purolator, DHL, Canada Post, Royal Mail, etc...   # noqa: E501

        :param carrier_name: The carrier_name of this Package.  # noqa: E501
        :type: str
        """

        self._carrier_name = carrier_name

    @property
    def picked_up_at(self):
        """Gets the picked_up_at of this Package.  # noqa: E501


        :return: The picked_up_at of this Package.  # noqa: E501
        :rtype: datetime
        """
        return self._picked_up_at

    @picked_up_at.setter
    def picked_up_at(self, picked_up_at):
        """Sets the picked_up_at of this Package.


        :param picked_up_at: The picked_up_at of this Package.  # noqa: E501
        :type: datetime
        """

        self._picked_up_at = picked_up_at

    @property
    def created_at(self):
        """Gets the created_at of this Package.  # noqa: E501


        :return: The created_at of this Package.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Package.


        :param created_at: The created_at of this Package.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def image(self):
        """Gets the image of this Package.  # noqa: E501


        :return: The image of this Package.  # noqa: E501
        :rtype: Image
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Package.


        :param image: The image of this Package.  # noqa: E501
        :type: Image
        """

        self._image = image

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
        if not isinstance(other, Package):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Package):
            return True

        return self.to_dict() != other.to_dict()
