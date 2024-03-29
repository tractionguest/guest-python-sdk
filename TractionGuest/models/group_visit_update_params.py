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


class GroupVisitUpdateParams(object):
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
        'name': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'location_id': 'int',
        'registration_limit': 'int',
        'manual_registration_approval': 'bool',
        'public_registration_enabled': 'bool',
        'host_ids': 'list[int]',
        'invite_ids': 'list[int]',
        'refresh_registration_url': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'location_id': 'location_id',
        'registration_limit': 'registration_limit',
        'manual_registration_approval': 'manual_registration_approval',
        'public_registration_enabled': 'public_registration_enabled',
        'host_ids': 'host_ids',
        'invite_ids': 'invite_ids',
        'refresh_registration_url': 'refresh_registration_url'
    }

    def __init__(self, name=None, start_time=None, end_time=None, location_id=None, registration_limit=None, manual_registration_approval=None, public_registration_enabled=None, host_ids=None, invite_ids=None, refresh_registration_url=None, local_vars_configuration=None):  # noqa: E501
        """GroupVisitUpdateParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._start_time = None
        self._end_time = None
        self._location_id = None
        self._registration_limit = None
        self._manual_registration_approval = None
        self._public_registration_enabled = None
        self._host_ids = None
        self._invite_ids = None
        self._refresh_registration_url = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if location_id is not None:
            self.location_id = location_id
        self.registration_limit = registration_limit
        self.manual_registration_approval = manual_registration_approval
        self.public_registration_enabled = public_registration_enabled
        if host_ids is not None:
            self.host_ids = host_ids
        if invite_ids is not None:
            self.invite_ids = invite_ids
        if refresh_registration_url is not None:
            self.refresh_registration_url = refresh_registration_url

    @property
    def name(self):
        """Gets the name of this GroupVisitUpdateParams.  # noqa: E501


        :return: The name of this GroupVisitUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupVisitUpdateParams.


        :param name: The name of this GroupVisitUpdateParams.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def start_time(self):
        """Gets the start_time of this GroupVisitUpdateParams.  # noqa: E501


        :return: The start_time of this GroupVisitUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this GroupVisitUpdateParams.


        :param start_time: The start_time of this GroupVisitUpdateParams.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this GroupVisitUpdateParams.  # noqa: E501


        :return: The end_time of this GroupVisitUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this GroupVisitUpdateParams.


        :param end_time: The end_time of this GroupVisitUpdateParams.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def location_id(self):
        """Gets the location_id of this GroupVisitUpdateParams.  # noqa: E501


        :return: The location_id of this GroupVisitUpdateParams.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this GroupVisitUpdateParams.


        :param location_id: The location_id of this GroupVisitUpdateParams.  # noqa: E501
        :type: int
        """

        self._location_id = location_id

    @property
    def registration_limit(self):
        """Gets the registration_limit of this GroupVisitUpdateParams.  # noqa: E501


        :return: The registration_limit of this GroupVisitUpdateParams.  # noqa: E501
        :rtype: int
        """
        return self._registration_limit

    @registration_limit.setter
    def registration_limit(self, registration_limit):
        """Sets the registration_limit of this GroupVisitUpdateParams.


        :param registration_limit: The registration_limit of this GroupVisitUpdateParams.  # noqa: E501
        :type: int
        """

        self._registration_limit = registration_limit

    @property
    def manual_registration_approval(self):
        """Gets the manual_registration_approval of this GroupVisitUpdateParams.  # noqa: E501


        :return: The manual_registration_approval of this GroupVisitUpdateParams.  # noqa: E501
        :rtype: bool
        """
        return self._manual_registration_approval

    @manual_registration_approval.setter
    def manual_registration_approval(self, manual_registration_approval):
        """Sets the manual_registration_approval of this GroupVisitUpdateParams.


        :param manual_registration_approval: The manual_registration_approval of this GroupVisitUpdateParams.  # noqa: E501
        :type: bool
        """

        self._manual_registration_approval = manual_registration_approval

    @property
    def public_registration_enabled(self):
        """Gets the public_registration_enabled of this GroupVisitUpdateParams.  # noqa: E501


        :return: The public_registration_enabled of this GroupVisitUpdateParams.  # noqa: E501
        :rtype: bool
        """
        return self._public_registration_enabled

    @public_registration_enabled.setter
    def public_registration_enabled(self, public_registration_enabled):
        """Sets the public_registration_enabled of this GroupVisitUpdateParams.


        :param public_registration_enabled: The public_registration_enabled of this GroupVisitUpdateParams.  # noqa: E501
        :type: bool
        """

        self._public_registration_enabled = public_registration_enabled

    @property
    def host_ids(self):
        """Gets the host_ids of this GroupVisitUpdateParams.  # noqa: E501


        :return: The host_ids of this GroupVisitUpdateParams.  # noqa: E501
        :rtype: list[int]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        """Sets the host_ids of this GroupVisitUpdateParams.


        :param host_ids: The host_ids of this GroupVisitUpdateParams.  # noqa: E501
        :type: list[int]
        """

        self._host_ids = host_ids

    @property
    def invite_ids(self):
        """Gets the invite_ids of this GroupVisitUpdateParams.  # noqa: E501


        :return: The invite_ids of this GroupVisitUpdateParams.  # noqa: E501
        :rtype: list[int]
        """
        return self._invite_ids

    @invite_ids.setter
    def invite_ids(self, invite_ids):
        """Sets the invite_ids of this GroupVisitUpdateParams.


        :param invite_ids: The invite_ids of this GroupVisitUpdateParams.  # noqa: E501
        :type: list[int]
        """

        self._invite_ids = invite_ids

    @property
    def refresh_registration_url(self):
        """Gets the refresh_registration_url of this GroupVisitUpdateParams.  # noqa: E501


        :return: The refresh_registration_url of this GroupVisitUpdateParams.  # noqa: E501
        :rtype: bool
        """
        return self._refresh_registration_url

    @refresh_registration_url.setter
    def refresh_registration_url(self, refresh_registration_url):
        """Sets the refresh_registration_url of this GroupVisitUpdateParams.


        :param refresh_registration_url: The refresh_registration_url of this GroupVisitUpdateParams.  # noqa: E501
        :type: bool
        """

        self._refresh_registration_url = refresh_registration_url

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
        if not isinstance(other, GroupVisitUpdateParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupVisitUpdateParams):
            return True

        return self.to_dict() != other.to_dict()
