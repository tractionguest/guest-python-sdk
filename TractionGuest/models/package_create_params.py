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


class PackageCreateParams(object):
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
        'base64_image': 'str',
        'location_id': 'int'
    }

    attribute_map = {
        'base64_image': 'base64_image',
        'location_id': 'location_id'
    }

    def __init__(self, base64_image=None, location_id=None, local_vars_configuration=None):  # noqa: E501
        """PackageCreateParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._base64_image = None
        self._location_id = None
        self.discriminator = None

        self.base64_image = base64_image
        self.location_id = location_id

    @property
    def base64_image(self):
        """Gets the base64_image of this PackageCreateParams.  # noqa: E501

        Base64 encoded image on which to perform processing  # noqa: E501

        :return: The base64_image of this PackageCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._base64_image

    @base64_image.setter
    def base64_image(self, base64_image):
        """Sets the base64_image of this PackageCreateParams.

        Base64 encoded image on which to perform processing  # noqa: E501

        :param base64_image: The base64_image of this PackageCreateParams.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and base64_image is None:  # noqa: E501
            raise ValueError("Invalid value for `base64_image`, must not be `None`")  # noqa: E501

        self._base64_image = base64_image

    @property
    def location_id(self):
        """Gets the location_id of this PackageCreateParams.  # noqa: E501

        Location id for where the package was delivered  # noqa: E501

        :return: The location_id of this PackageCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this PackageCreateParams.

        Location id for where the package was delivered  # noqa: E501

        :param location_id: The location_id of this PackageCreateParams.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and location_id is None:  # noqa: E501
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

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
        if not isinstance(other, PackageCreateParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PackageCreateParams):
            return True

        return self.to_dict() != other.to_dict()
