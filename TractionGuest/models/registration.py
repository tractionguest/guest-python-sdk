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


class Registration(object):
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
        'id': 'str',
        'visitor': 'Visitor',
        'invite': 'Invite',
        'photo_url': 'str',
        'company': 'str',
        'email': 'str',
        'name': 'str',
        'created_at': 'datetime',
        'signin': 'Signin'
    }

    attribute_map = {
        'id': 'id',
        'visitor': 'visitor',
        'invite': 'invite',
        'photo_url': 'photo_url',
        'company': 'company',
        'email': 'email',
        'name': 'name',
        'created_at': 'created_at',
        'signin': 'signin'
    }

    def __init__(self, id=None, visitor=None, invite=None, photo_url=None, company=None, email=None, name=None, created_at=None, signin=None, local_vars_configuration=None):  # noqa: E501
        """Registration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._visitor = None
        self._invite = None
        self._photo_url = None
        self._company = None
        self._email = None
        self._name = None
        self._created_at = None
        self._signin = None
        self.discriminator = None

        self.id = id
        if visitor is not None:
            self.visitor = visitor
        if invite is not None:
            self.invite = invite
        self.photo_url = photo_url
        self.company = company
        self.email = email
        self.name = name
        self.created_at = created_at
        if signin is not None:
            self.signin = signin

    @property
    def id(self):
        """Gets the id of this Registration.  # noqa: E501

        Registration unique identifier  # noqa: E501

        :return: The id of this Registration.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Registration.

        Registration unique identifier  # noqa: E501

        :param id: The id of this Registration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def visitor(self):
        """Gets the visitor of this Registration.  # noqa: E501


        :return: The visitor of this Registration.  # noqa: E501
        :rtype: Visitor
        """
        return self._visitor

    @visitor.setter
    def visitor(self, visitor):
        """Sets the visitor of this Registration.


        :param visitor: The visitor of this Registration.  # noqa: E501
        :type: Visitor
        """

        self._visitor = visitor

    @property
    def invite(self):
        """Gets the invite of this Registration.  # noqa: E501


        :return: The invite of this Registration.  # noqa: E501
        :rtype: Invite
        """
        return self._invite

    @invite.setter
    def invite(self, invite):
        """Sets the invite of this Registration.


        :param invite: The invite of this Registration.  # noqa: E501
        :type: Invite
        """

        self._invite = invite

    @property
    def photo_url(self):
        """Gets the photo_url of this Registration.  # noqa: E501

        URL of the uploaded photo  # noqa: E501

        :return: The photo_url of this Registration.  # noqa: E501
        :rtype: str
        """
        return self._photo_url

    @photo_url.setter
    def photo_url(self, photo_url):
        """Sets the photo_url of this Registration.

        URL of the uploaded photo  # noqa: E501

        :param photo_url: The photo_url of this Registration.  # noqa: E501
        :type: str
        """

        self._photo_url = photo_url

    @property
    def company(self):
        """Gets the company of this Registration.  # noqa: E501

        Company's name  # noqa: E501

        :return: The company of this Registration.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this Registration.

        Company's name  # noqa: E501

        :param company: The company of this Registration.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def email(self):
        """Gets the email of this Registration.  # noqa: E501

        E-mail  # noqa: E501

        :return: The email of this Registration.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Registration.

        E-mail  # noqa: E501

        :param email: The email of this Registration.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def name(self):
        """Gets the name of this Registration.  # noqa: E501

        Guest's name  # noqa: E501

        :return: The name of this Registration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Registration.

        Guest's name  # noqa: E501

        :param name: The name of this Registration.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this Registration.  # noqa: E501

        Datetime when registration was created  # noqa: E501

        :return: The created_at of this Registration.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Registration.

        Datetime when registration was created  # noqa: E501

        :param created_at: The created_at of this Registration.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def signin(self):
        """Gets the signin of this Registration.  # noqa: E501


        :return: The signin of this Registration.  # noqa: E501
        :rtype: Signin
        """
        return self._signin

    @signin.setter
    def signin(self, signin):
        """Sets the signin of this Registration.


        :param signin: The signin of this Registration.  # noqa: E501
        :type: Signin
        """

        self._signin = signin

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
        if not isinstance(other, Registration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Registration):
            return True

        return self.to_dict() != other.to_dict()
