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


class SigninDetail(object):
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
        'documents': 'list[SignableDocument]',
        'signin_watchlist': 'SigninWatchlist',
        'hosts': 'list[Host]',
        'signin_data': 'list[SigninData]',
        'signin_acknowledgement': 'SigninAcknowledgement',
        'note': 'str',
        'is_signed_out': 'bool',
        'signin_timestamp': 'datetime',
        'signin_photo_url': 'str',
        'signed_out_timestamp': 'datetime',
        'mobile_number': 'str',
        'location_name': 'str',
        'last_name': 'str',
        'is_acknowledged': 'bool',
        'is_accounted_for': 'bool',
        'first_name': 'str',
        'email': 'str',
        'company': 'str',
        'registration': 'Registration'
    }

    attribute_map = {
        'id': 'id',
        'documents': 'documents',
        'signin_watchlist': 'signin_watchlist',
        'hosts': 'hosts',
        'signin_data': 'signin_data',
        'signin_acknowledgement': 'signin_acknowledgement',
        'note': 'note',
        'is_signed_out': 'is_signed_out',
        'signin_timestamp': 'signin_timestamp',
        'signin_photo_url': 'signin_photo_url',
        'signed_out_timestamp': 'signed_out_timestamp',
        'mobile_number': 'mobile_number',
        'location_name': 'location_name',
        'last_name': 'last_name',
        'is_acknowledged': 'is_acknowledged',
        'is_accounted_for': 'is_accounted_for',
        'first_name': 'first_name',
        'email': 'email',
        'company': 'company',
        'registration': 'registration'
    }

    def __init__(self, id=None, documents=None, signin_watchlist=None, hosts=None, signin_data=None, signin_acknowledgement=None, note=None, is_signed_out=None, signin_timestamp=None, signin_photo_url=None, signed_out_timestamp=None, mobile_number=None, location_name=None, last_name=None, is_acknowledged=None, is_accounted_for=None, first_name=None, email=None, company=None, registration=None, local_vars_configuration=None):  # noqa: E501
        """SigninDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._documents = None
        self._signin_watchlist = None
        self._hosts = None
        self._signin_data = None
        self._signin_acknowledgement = None
        self._note = None
        self._is_signed_out = None
        self._signin_timestamp = None
        self._signin_photo_url = None
        self._signed_out_timestamp = None
        self._mobile_number = None
        self._location_name = None
        self._last_name = None
        self._is_acknowledged = None
        self._is_accounted_for = None
        self._first_name = None
        self._email = None
        self._company = None
        self._registration = None
        self.discriminator = None

        self.id = id
        if documents is not None:
            self.documents = documents
        if signin_watchlist is not None:
            self.signin_watchlist = signin_watchlist
        if hosts is not None:
            self.hosts = hosts
        if signin_data is not None:
            self.signin_data = signin_data
        if signin_acknowledgement is not None:
            self.signin_acknowledgement = signin_acknowledgement
        if note is not None:
            self.note = note
        if is_signed_out is not None:
            self.is_signed_out = is_signed_out
        if signin_timestamp is not None:
            self.signin_timestamp = signin_timestamp
        if signin_photo_url is not None:
            self.signin_photo_url = signin_photo_url
        if signed_out_timestamp is not None:
            self.signed_out_timestamp = signed_out_timestamp
        if mobile_number is not None:
            self.mobile_number = mobile_number
        if location_name is not None:
            self.location_name = location_name
        if last_name is not None:
            self.last_name = last_name
        if is_acknowledged is not None:
            self.is_acknowledged = is_acknowledged
        if is_accounted_for is not None:
            self.is_accounted_for = is_accounted_for
        if first_name is not None:
            self.first_name = first_name
        if email is not None:
            self.email = email
        if company is not None:
            self.company = company
        if registration is not None:
            self.registration = registration

    @property
    def id(self):
        """Gets the id of this SigninDetail.  # noqa: E501


        :return: The id of this SigninDetail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SigninDetail.


        :param id: The id of this SigninDetail.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def documents(self):
        """Gets the documents of this SigninDetail.  # noqa: E501


        :return: The documents of this SigninDetail.  # noqa: E501
        :rtype: list[SignableDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this SigninDetail.


        :param documents: The documents of this SigninDetail.  # noqa: E501
        :type: list[SignableDocument]
        """

        self._documents = documents

    @property
    def signin_watchlist(self):
        """Gets the signin_watchlist of this SigninDetail.  # noqa: E501


        :return: The signin_watchlist of this SigninDetail.  # noqa: E501
        :rtype: SigninWatchlist
        """
        return self._signin_watchlist

    @signin_watchlist.setter
    def signin_watchlist(self, signin_watchlist):
        """Sets the signin_watchlist of this SigninDetail.


        :param signin_watchlist: The signin_watchlist of this SigninDetail.  # noqa: E501
        :type: SigninWatchlist
        """

        self._signin_watchlist = signin_watchlist

    @property
    def hosts(self):
        """Gets the hosts of this SigninDetail.  # noqa: E501


        :return: The hosts of this SigninDetail.  # noqa: E501
        :rtype: list[Host]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this SigninDetail.


        :param hosts: The hosts of this SigninDetail.  # noqa: E501
        :type: list[Host]
        """

        self._hosts = hosts

    @property
    def signin_data(self):
        """Gets the signin_data of this SigninDetail.  # noqa: E501


        :return: The signin_data of this SigninDetail.  # noqa: E501
        :rtype: list[SigninData]
        """
        return self._signin_data

    @signin_data.setter
    def signin_data(self, signin_data):
        """Sets the signin_data of this SigninDetail.


        :param signin_data: The signin_data of this SigninDetail.  # noqa: E501
        :type: list[SigninData]
        """

        self._signin_data = signin_data

    @property
    def signin_acknowledgement(self):
        """Gets the signin_acknowledgement of this SigninDetail.  # noqa: E501


        :return: The signin_acknowledgement of this SigninDetail.  # noqa: E501
        :rtype: SigninAcknowledgement
        """
        return self._signin_acknowledgement

    @signin_acknowledgement.setter
    def signin_acknowledgement(self, signin_acknowledgement):
        """Sets the signin_acknowledgement of this SigninDetail.


        :param signin_acknowledgement: The signin_acknowledgement of this SigninDetail.  # noqa: E501
        :type: SigninAcknowledgement
        """

        self._signin_acknowledgement = signin_acknowledgement

    @property
    def note(self):
        """Gets the note of this SigninDetail.  # noqa: E501


        :return: The note of this SigninDetail.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this SigninDetail.


        :param note: The note of this SigninDetail.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def is_signed_out(self):
        """Gets the is_signed_out of this SigninDetail.  # noqa: E501

        A one-way method of Signing out a Signin  # noqa: E501

        :return: The is_signed_out of this SigninDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_signed_out

    @is_signed_out.setter
    def is_signed_out(self, is_signed_out):
        """Sets the is_signed_out of this SigninDetail.

        A one-way method of Signing out a Signin  # noqa: E501

        :param is_signed_out: The is_signed_out of this SigninDetail.  # noqa: E501
        :type: bool
        """

        self._is_signed_out = is_signed_out

    @property
    def signin_timestamp(self):
        """Gets the signin_timestamp of this SigninDetail.  # noqa: E501


        :return: The signin_timestamp of this SigninDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._signin_timestamp

    @signin_timestamp.setter
    def signin_timestamp(self, signin_timestamp):
        """Sets the signin_timestamp of this SigninDetail.


        :param signin_timestamp: The signin_timestamp of this SigninDetail.  # noqa: E501
        :type: datetime
        """

        self._signin_timestamp = signin_timestamp

    @property
    def signin_photo_url(self):
        """Gets the signin_photo_url of this SigninDetail.  # noqa: E501


        :return: The signin_photo_url of this SigninDetail.  # noqa: E501
        :rtype: str
        """
        return self._signin_photo_url

    @signin_photo_url.setter
    def signin_photo_url(self, signin_photo_url):
        """Sets the signin_photo_url of this SigninDetail.


        :param signin_photo_url: The signin_photo_url of this SigninDetail.  # noqa: E501
        :type: str
        """

        self._signin_photo_url = signin_photo_url

    @property
    def signed_out_timestamp(self):
        """Gets the signed_out_timestamp of this SigninDetail.  # noqa: E501


        :return: The signed_out_timestamp of this SigninDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._signed_out_timestamp

    @signed_out_timestamp.setter
    def signed_out_timestamp(self, signed_out_timestamp):
        """Sets the signed_out_timestamp of this SigninDetail.


        :param signed_out_timestamp: The signed_out_timestamp of this SigninDetail.  # noqa: E501
        :type: datetime
        """

        self._signed_out_timestamp = signed_out_timestamp

    @property
    def mobile_number(self):
        """Gets the mobile_number of this SigninDetail.  # noqa: E501


        :return: The mobile_number of this SigninDetail.  # noqa: E501
        :rtype: str
        """
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, mobile_number):
        """Sets the mobile_number of this SigninDetail.


        :param mobile_number: The mobile_number of this SigninDetail.  # noqa: E501
        :type: str
        """

        self._mobile_number = mobile_number

    @property
    def location_name(self):
        """Gets the location_name of this SigninDetail.  # noqa: E501


        :return: The location_name of this SigninDetail.  # noqa: E501
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """Sets the location_name of this SigninDetail.


        :param location_name: The location_name of this SigninDetail.  # noqa: E501
        :type: str
        """

        self._location_name = location_name

    @property
    def last_name(self):
        """Gets the last_name of this SigninDetail.  # noqa: E501


        :return: The last_name of this SigninDetail.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this SigninDetail.


        :param last_name: The last_name of this SigninDetail.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def is_acknowledged(self):
        """Gets the is_acknowledged of this SigninDetail.  # noqa: E501

        Whether this Signin has been acknowledged yet. Can also be used as a one-way method of setting the Signin as acknowledged.  # noqa: E501

        :return: The is_acknowledged of this SigninDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_acknowledged

    @is_acknowledged.setter
    def is_acknowledged(self, is_acknowledged):
        """Sets the is_acknowledged of this SigninDetail.

        Whether this Signin has been acknowledged yet. Can also be used as a one-way method of setting the Signin as acknowledged.  # noqa: E501

        :param is_acknowledged: The is_acknowledged of this SigninDetail.  # noqa: E501
        :type: bool
        """

        self._is_acknowledged = is_acknowledged

    @property
    def is_accounted_for(self):
        """Gets the is_accounted_for of this SigninDetail.  # noqa: E501


        :return: The is_accounted_for of this SigninDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_accounted_for

    @is_accounted_for.setter
    def is_accounted_for(self, is_accounted_for):
        """Sets the is_accounted_for of this SigninDetail.


        :param is_accounted_for: The is_accounted_for of this SigninDetail.  # noqa: E501
        :type: bool
        """

        self._is_accounted_for = is_accounted_for

    @property
    def first_name(self):
        """Gets the first_name of this SigninDetail.  # noqa: E501


        :return: The first_name of this SigninDetail.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this SigninDetail.


        :param first_name: The first_name of this SigninDetail.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def email(self):
        """Gets the email of this SigninDetail.  # noqa: E501


        :return: The email of this SigninDetail.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SigninDetail.


        :param email: The email of this SigninDetail.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def company(self):
        """Gets the company of this SigninDetail.  # noqa: E501


        :return: The company of this SigninDetail.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this SigninDetail.


        :param company: The company of this SigninDetail.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def registration(self):
        """Gets the registration of this SigninDetail.  # noqa: E501


        :return: The registration of this SigninDetail.  # noqa: E501
        :rtype: Registration
        """
        return self._registration

    @registration.setter
    def registration(self, registration):
        """Sets the registration of this SigninDetail.


        :param registration: The registration of this SigninDetail.  # noqa: E501
        :type: Registration
        """

        self._registration = registration

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
        if not isinstance(other, SigninDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SigninDetail):
            return True

        return self.to_dict() != other.to_dict()
