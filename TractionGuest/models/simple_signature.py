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


class SimpleSignature(object):
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
        'status': 'str',
        'template_name': 'str',
        'id': 'str',
        'title': 'str'
    }

    attribute_map = {
        'status': 'status',
        'template_name': 'template_name',
        'id': 'id',
        'title': 'title'
    }

    def __init__(self, status=None, template_name=None, id=None, title=None, local_vars_configuration=None):  # noqa: E501
        """SimpleSignature - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._template_name = None
        self._id = None
        self._title = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if template_name is not None:
            self.template_name = template_name
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title

    @property
    def status(self):
        """Gets the status of this SimpleSignature.  # noqa: E501

          # noqa: E501

        :return: The status of this SimpleSignature.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SimpleSignature.

          # noqa: E501

        :param status: The status of this SimpleSignature.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def template_name(self):
        """Gets the template_name of this SimpleSignature.  # noqa: E501

          # noqa: E501

        :return: The template_name of this SimpleSignature.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this SimpleSignature.

          # noqa: E501

        :param template_name: The template_name of this SimpleSignature.  # noqa: E501
        :type: str
        """

        self._template_name = template_name

    @property
    def id(self):
        """Gets the id of this SimpleSignature.  # noqa: E501

          # noqa: E501

        :return: The id of this SimpleSignature.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimpleSignature.

          # noqa: E501

        :param id: The id of this SimpleSignature.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this SimpleSignature.  # noqa: E501

          # noqa: E501

        :return: The title of this SimpleSignature.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SimpleSignature.

          # noqa: E501

        :param title: The title of this SimpleSignature.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if not isinstance(other, SimpleSignature):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimpleSignature):
            return True

        return self.to_dict() != other.to_dict()
