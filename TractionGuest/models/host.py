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


class Host(object):
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
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'profile_pic_url': 'str',
        'department': 'str',
        'mobile_number': 'str'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'profile_pic_url': 'profile_pic_url',
        'department': 'department',
        'mobile_number': 'mobile_number'
    }

    def __init__(self, id=None, email=None, first_name=None, last_name=None, profile_pic_url=None, department=None, mobile_number=None, local_vars_configuration=None):  # noqa: E501
        """Host - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._profile_pic_url = None
        self._department = None
        self._mobile_number = None
        self.discriminator = None

        self.id = id
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if profile_pic_url is not None:
            self.profile_pic_url = profile_pic_url
        if department is not None:
            self.department = department
        if mobile_number is not None:
            self.mobile_number = mobile_number

    @property
    def id(self):
        """Gets the id of this Host.  # noqa: E501


        :return: The id of this Host.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Host.


        :param id: The id of this Host.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def email(self):
        """Gets the email of this Host.  # noqa: E501


        :return: The email of this Host.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Host.


        :param email: The email of this Host.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this Host.  # noqa: E501


        :return: The first_name of this Host.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Host.


        :param first_name: The first_name of this Host.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Host.  # noqa: E501


        :return: The last_name of this Host.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Host.


        :param last_name: The last_name of this Host.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def profile_pic_url(self):
        """Gets the profile_pic_url of this Host.  # noqa: E501


        :return: The profile_pic_url of this Host.  # noqa: E501
        :rtype: str
        """
        return self._profile_pic_url

    @profile_pic_url.setter
    def profile_pic_url(self, profile_pic_url):
        """Sets the profile_pic_url of this Host.


        :param profile_pic_url: The profile_pic_url of this Host.  # noqa: E501
        :type: str
        """

        self._profile_pic_url = profile_pic_url

    @property
    def department(self):
        """Gets the department of this Host.  # noqa: E501

          # noqa: E501

        :return: The department of this Host.  # noqa: E501
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this Host.

          # noqa: E501

        :param department: The department of this Host.  # noqa: E501
        :type: str
        """

        self._department = department

    @property
    def mobile_number(self):
        """Gets the mobile_number of this Host.  # noqa: E501


        :return: The mobile_number of this Host.  # noqa: E501
        :rtype: str
        """
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, mobile_number):
        """Sets the mobile_number of this Host.


        :param mobile_number: The mobile_number of this Host.  # noqa: E501
        :type: str
        """

        self._mobile_number = mobile_number

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
        if not isinstance(other, Host):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Host):
            return True

        return self.to_dict() != other.to_dict()
