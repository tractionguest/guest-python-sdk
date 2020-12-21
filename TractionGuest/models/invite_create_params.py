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


class InviteCreateParams(object):
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
        'mobile_number': 'str',
        'notification_triggers': 'list[object]',
        'first_name': 'str',
        'email_template_id': 'int',
        'custom_fields': 'list[object]',
        'host_ids': 'list[int]',
        'watchlist_colour': 'str',
        'title': 'str',
        'start_date': 'datetime',
        'last_name': 'str',
        'end_date': 'datetime',
        'email': 'str',
        'company': 'str',
        'group_visit_id': 'str'
    }

    attribute_map = {
        'mobile_number': 'mobile_number',
        'notification_triggers': 'notification_triggers',
        'first_name': 'first_name',
        'email_template_id': 'email_template_id',
        'custom_fields': 'custom_fields',
        'host_ids': 'host_ids',
        'watchlist_colour': 'watchlist_colour',
        'title': 'title',
        'start_date': 'start_date',
        'last_name': 'last_name',
        'end_date': 'end_date',
        'email': 'email',
        'company': 'company',
        'group_visit_id': 'group_visit_id'
    }

    def __init__(self, mobile_number=None, notification_triggers=None, first_name=None, email_template_id=None, custom_fields=None, host_ids=None, watchlist_colour=None, title=None, start_date=None, last_name=None, end_date=None, email=None, company=None, group_visit_id=None, local_vars_configuration=None):  # noqa: E501
        """InviteCreateParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mobile_number = None
        self._notification_triggers = None
        self._first_name = None
        self._email_template_id = None
        self._custom_fields = None
        self._host_ids = None
        self._watchlist_colour = None
        self._title = None
        self._start_date = None
        self._last_name = None
        self._end_date = None
        self._email = None
        self._company = None
        self._group_visit_id = None
        self.discriminator = None

        if mobile_number is not None:
            self.mobile_number = mobile_number
        if notification_triggers is not None:
            self.notification_triggers = notification_triggers
        self.first_name = first_name
        if email_template_id is not None:
            self.email_template_id = email_template_id
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if host_ids is not None:
            self.host_ids = host_ids
        if watchlist_colour is not None:
            self.watchlist_colour = watchlist_colour
        if title is not None:
            self.title = title
        if start_date is not None:
            self.start_date = start_date
        self.last_name = last_name
        if end_date is not None:
            self.end_date = end_date
        self.email = email
        if company is not None:
            self.company = company
        if group_visit_id is not None:
            self.group_visit_id = group_visit_id

    @property
    def mobile_number(self):
        """Gets the mobile_number of this InviteCreateParams.  # noqa: E501


        :return: The mobile_number of this InviteCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, mobile_number):
        """Sets the mobile_number of this InviteCreateParams.


        :param mobile_number: The mobile_number of this InviteCreateParams.  # noqa: E501
        :type: str
        """

        self._mobile_number = mobile_number

    @property
    def notification_triggers(self):
        """Gets the notification_triggers of this InviteCreateParams.  # noqa: E501


        :return: The notification_triggers of this InviteCreateParams.  # noqa: E501
        :rtype: list[object]
        """
        return self._notification_triggers

    @notification_triggers.setter
    def notification_triggers(self, notification_triggers):
        """Sets the notification_triggers of this InviteCreateParams.


        :param notification_triggers: The notification_triggers of this InviteCreateParams.  # noqa: E501
        :type: list[object]
        """

        self._notification_triggers = notification_triggers

    @property
    def first_name(self):
        """Gets the first_name of this InviteCreateParams.  # noqa: E501


        :return: The first_name of this InviteCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this InviteCreateParams.


        :param first_name: The first_name of this InviteCreateParams.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and first_name is None:  # noqa: E501
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def email_template_id(self):
        """Gets the email_template_id of this InviteCreateParams.  # noqa: E501


        :return: The email_template_id of this InviteCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._email_template_id

    @email_template_id.setter
    def email_template_id(self, email_template_id):
        """Sets the email_template_id of this InviteCreateParams.


        :param email_template_id: The email_template_id of this InviteCreateParams.  # noqa: E501
        :type: int
        """

        self._email_template_id = email_template_id

    @property
    def custom_fields(self):
        """Gets the custom_fields of this InviteCreateParams.  # noqa: E501


        :return: The custom_fields of this InviteCreateParams.  # noqa: E501
        :rtype: list[object]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this InviteCreateParams.


        :param custom_fields: The custom_fields of this InviteCreateParams.  # noqa: E501
        :type: list[object]
        """

        self._custom_fields = custom_fields

    @property
    def host_ids(self):
        """Gets the host_ids of this InviteCreateParams.  # noqa: E501


        :return: The host_ids of this InviteCreateParams.  # noqa: E501
        :rtype: list[int]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        """Sets the host_ids of this InviteCreateParams.


        :param host_ids: The host_ids of this InviteCreateParams.  # noqa: E501
        :type: list[int]
        """

        self._host_ids = host_ids

    @property
    def watchlist_colour(self):
        """Gets the watchlist_colour of this InviteCreateParams.  # noqa: E501


        :return: The watchlist_colour of this InviteCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._watchlist_colour

    @watchlist_colour.setter
    def watchlist_colour(self, watchlist_colour):
        """Sets the watchlist_colour of this InviteCreateParams.


        :param watchlist_colour: The watchlist_colour of this InviteCreateParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["RED", "GREEN", "YELLOW", "ORANGE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and watchlist_colour not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `watchlist_colour` ({0}), must be one of {1}"  # noqa: E501
                .format(watchlist_colour, allowed_values)
            )

        self._watchlist_colour = watchlist_colour

    @property
    def title(self):
        """Gets the title of this InviteCreateParams.  # noqa: E501


        :return: The title of this InviteCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InviteCreateParams.


        :param title: The title of this InviteCreateParams.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def start_date(self):
        """Gets the start_date of this InviteCreateParams.  # noqa: E501

        The `start_date` is required for invitations to lobbies  # noqa: E501

        :return: The start_date of this InviteCreateParams.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this InviteCreateParams.

        The `start_date` is required for invitations to lobbies  # noqa: E501

        :param start_date: The start_date of this InviteCreateParams.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def last_name(self):
        """Gets the last_name of this InviteCreateParams.  # noqa: E501


        :return: The last_name of this InviteCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this InviteCreateParams.


        :param last_name: The last_name of this InviteCreateParams.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and last_name is None:  # noqa: E501
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def end_date(self):
        """Gets the end_date of this InviteCreateParams.  # noqa: E501


        :return: The end_date of this InviteCreateParams.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this InviteCreateParams.


        :param end_date: The end_date of this InviteCreateParams.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def email(self):
        """Gets the email of this InviteCreateParams.  # noqa: E501


        :return: The email of this InviteCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InviteCreateParams.


        :param email: The email of this InviteCreateParams.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def company(self):
        """Gets the company of this InviteCreateParams.  # noqa: E501


        :return: The company of this InviteCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this InviteCreateParams.


        :param company: The company of this InviteCreateParams.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def group_visit_id(self):
        """Gets the group_visit_id of this InviteCreateParams.  # noqa: E501


        :return: The group_visit_id of this InviteCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._group_visit_id

    @group_visit_id.setter
    def group_visit_id(self, group_visit_id):
        """Sets the group_visit_id of this InviteCreateParams.


        :param group_visit_id: The group_visit_id of this InviteCreateParams.  # noqa: E501
        :type: str
        """

        self._group_visit_id = group_visit_id

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
        if not isinstance(other, InviteCreateParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InviteCreateParams):
            return True

        return self.to_dict() != other.to_dict()
