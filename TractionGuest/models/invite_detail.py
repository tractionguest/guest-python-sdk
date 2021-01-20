# coding: utf-8

"""
    Traction Guest API

    The Traction Guest API is currently under limited release to select customers as we gather and iterate on feedback.  # Getting Started If you are interested in getting early access to the API, please send us an email to [support@tractionguest.com](mailto:support@tractionguest.com).  We will also add you to our Slack channel where you can ask questions and get further help.  # Terms and Conditions Please visit: [https://tractionguest.com/tos/api/](https://tractionguest.com/tos/api/)  # Versioning This API follows [semantic versioning](https://semver.org/), which follows the `Major`.`Minor`.`Patch` format.  * The `Major` number increments when potentially incompatible changes are made. * The `Minor` number increments when backwards-compatible additions are made. * The `Patch` number increments when backwards-compatible bug-fixes are made.   # noqa: E501

    The version of the OpenAPI document: 0.14.2
    Contact: support@tractionguest.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from TractionGuest.configuration import Configuration


class InviteDetail(object):
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
        'registration': 'Registration',
        'mobile_number': 'str',
        'email_template': 'EmailTemplate',
        'invite_watchlist': 'InviteWatchlist',
        'notification_triggers': 'list[NotificationTrigger]',
        'custom_fields': 'list[CustomField]',
        'watchlist_colour': 'str',
        'location': 'Location',
        'hosts': 'list[Host]',
        'start_date': 'datetime',
        'last_name': 'str',
        'first_name': 'str',
        'end_date': 'datetime',
        'email': 'str',
        'created_at': 'datetime',
        'company': 'str',
        'checked_in': 'bool',
        'group_visit': 'GroupVisit'
    }

    attribute_map = {
        'id': 'id',
        'registration': 'registration',
        'mobile_number': 'mobile_number',
        'email_template': 'email_template',
        'invite_watchlist': 'invite_watchlist',
        'notification_triggers': 'notification_triggers',
        'custom_fields': 'custom_fields',
        'watchlist_colour': 'watchlist_colour',
        'location': 'location',
        'hosts': 'hosts',
        'start_date': 'start_date',
        'last_name': 'last_name',
        'first_name': 'first_name',
        'end_date': 'end_date',
        'email': 'email',
        'created_at': 'created_at',
        'company': 'company',
        'checked_in': 'checked_in',
        'group_visit': 'group_visit'
    }

    def __init__(self, id=None, registration=None, mobile_number=None, email_template=None, invite_watchlist=None, notification_triggers=None, custom_fields=None, watchlist_colour=None, location=None, hosts=None, start_date=None, last_name=None, first_name=None, end_date=None, email=None, created_at=None, company=None, checked_in=None, group_visit=None, local_vars_configuration=None):  # noqa: E501
        """InviteDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._registration = None
        self._mobile_number = None
        self._email_template = None
        self._invite_watchlist = None
        self._notification_triggers = None
        self._custom_fields = None
        self._watchlist_colour = None
        self._location = None
        self._hosts = None
        self._start_date = None
        self._last_name = None
        self._first_name = None
        self._end_date = None
        self._email = None
        self._created_at = None
        self._company = None
        self._checked_in = None
        self._group_visit = None
        self.discriminator = None

        self.id = id
        if registration is not None:
            self.registration = registration
        if mobile_number is not None:
            self.mobile_number = mobile_number
        if email_template is not None:
            self.email_template = email_template
        if invite_watchlist is not None:
            self.invite_watchlist = invite_watchlist
        if notification_triggers is not None:
            self.notification_triggers = notification_triggers
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if watchlist_colour is not None:
            self.watchlist_colour = watchlist_colour
        if location is not None:
            self.location = location
        if hosts is not None:
            self.hosts = hosts
        if start_date is not None:
            self.start_date = start_date
        self.last_name = last_name
        self.first_name = first_name
        if end_date is not None:
            self.end_date = end_date
        self.email = email
        if created_at is not None:
            self.created_at = created_at
        if company is not None:
            self.company = company
        if checked_in is not None:
            self.checked_in = checked_in
        if group_visit is not None:
            self.group_visit = group_visit

    @property
    def id(self):
        """Gets the id of this InviteDetail.  # noqa: E501


        :return: The id of this InviteDetail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InviteDetail.


        :param id: The id of this InviteDetail.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def registration(self):
        """Gets the registration of this InviteDetail.  # noqa: E501


        :return: The registration of this InviteDetail.  # noqa: E501
        :rtype: Registration
        """
        return self._registration

    @registration.setter
    def registration(self, registration):
        """Sets the registration of this InviteDetail.


        :param registration: The registration of this InviteDetail.  # noqa: E501
        :type: Registration
        """

        self._registration = registration

    @property
    def mobile_number(self):
        """Gets the mobile_number of this InviteDetail.  # noqa: E501

        Phone number  # noqa: E501

        :return: The mobile_number of this InviteDetail.  # noqa: E501
        :rtype: str
        """
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, mobile_number):
        """Sets the mobile_number of this InviteDetail.

        Phone number  # noqa: E501

        :param mobile_number: The mobile_number of this InviteDetail.  # noqa: E501
        :type: str
        """

        self._mobile_number = mobile_number

    @property
    def email_template(self):
        """Gets the email_template of this InviteDetail.  # noqa: E501


        :return: The email_template of this InviteDetail.  # noqa: E501
        :rtype: EmailTemplate
        """
        return self._email_template

    @email_template.setter
    def email_template(self, email_template):
        """Sets the email_template of this InviteDetail.


        :param email_template: The email_template of this InviteDetail.  # noqa: E501
        :type: EmailTemplate
        """

        self._email_template = email_template

    @property
    def invite_watchlist(self):
        """Gets the invite_watchlist of this InviteDetail.  # noqa: E501


        :return: The invite_watchlist of this InviteDetail.  # noqa: E501
        :rtype: InviteWatchlist
        """
        return self._invite_watchlist

    @invite_watchlist.setter
    def invite_watchlist(self, invite_watchlist):
        """Sets the invite_watchlist of this InviteDetail.


        :param invite_watchlist: The invite_watchlist of this InviteDetail.  # noqa: E501
        :type: InviteWatchlist
        """

        self._invite_watchlist = invite_watchlist

    @property
    def notification_triggers(self):
        """Gets the notification_triggers of this InviteDetail.  # noqa: E501

        List of scheduled notifications for an invite  # noqa: E501

        :return: The notification_triggers of this InviteDetail.  # noqa: E501
        :rtype: list[NotificationTrigger]
        """
        return self._notification_triggers

    @notification_triggers.setter
    def notification_triggers(self, notification_triggers):
        """Sets the notification_triggers of this InviteDetail.

        List of scheduled notifications for an invite  # noqa: E501

        :param notification_triggers: The notification_triggers of this InviteDetail.  # noqa: E501
        :type: list[NotificationTrigger]
        """

        self._notification_triggers = notification_triggers

    @property
    def custom_fields(self):
        """Gets the custom_fields of this InviteDetail.  # noqa: E501


        :return: The custom_fields of this InviteDetail.  # noqa: E501
        :rtype: list[CustomField]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this InviteDetail.


        :param custom_fields: The custom_fields of this InviteDetail.  # noqa: E501
        :type: list[CustomField]
        """

        self._custom_fields = custom_fields

    @property
    def watchlist_colour(self):
        """Gets the watchlist_colour of this InviteDetail.  # noqa: E501


        :return: The watchlist_colour of this InviteDetail.  # noqa: E501
        :rtype: str
        """
        return self._watchlist_colour

    @watchlist_colour.setter
    def watchlist_colour(self, watchlist_colour):
        """Sets the watchlist_colour of this InviteDetail.


        :param watchlist_colour: The watchlist_colour of this InviteDetail.  # noqa: E501
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
    def location(self):
        """Gets the location of this InviteDetail.  # noqa: E501


        :return: The location of this InviteDetail.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this InviteDetail.


        :param location: The location of this InviteDetail.  # noqa: E501
        :type: Location
        """

        self._location = location

    @property
    def hosts(self):
        """Gets the hosts of this InviteDetail.  # noqa: E501


        :return: The hosts of this InviteDetail.  # noqa: E501
        :rtype: list[Host]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this InviteDetail.


        :param hosts: The hosts of this InviteDetail.  # noqa: E501
        :type: list[Host]
        """

        self._hosts = hosts

    @property
    def start_date(self):
        """Gets the start_date of this InviteDetail.  # noqa: E501


        :return: The start_date of this InviteDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this InviteDetail.


        :param start_date: The start_date of this InviteDetail.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def last_name(self):
        """Gets the last_name of this InviteDetail.  # noqa: E501


        :return: The last_name of this InviteDetail.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this InviteDetail.


        :param last_name: The last_name of this InviteDetail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and last_name is None:  # noqa: E501
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def first_name(self):
        """Gets the first_name of this InviteDetail.  # noqa: E501


        :return: The first_name of this InviteDetail.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this InviteDetail.


        :param first_name: The first_name of this InviteDetail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and first_name is None:  # noqa: E501
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def end_date(self):
        """Gets the end_date of this InviteDetail.  # noqa: E501


        :return: The end_date of this InviteDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this InviteDetail.


        :param end_date: The end_date of this InviteDetail.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def email(self):
        """Gets the email of this InviteDetail.  # noqa: E501


        :return: The email of this InviteDetail.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InviteDetail.


        :param email: The email of this InviteDetail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def created_at(self):
        """Gets the created_at of this InviteDetail.  # noqa: E501


        :return: The created_at of this InviteDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InviteDetail.


        :param created_at: The created_at of this InviteDetail.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def company(self):
        """Gets the company of this InviteDetail.  # noqa: E501


        :return: The company of this InviteDetail.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this InviteDetail.


        :param company: The company of this InviteDetail.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def checked_in(self):
        """Gets the checked_in of this InviteDetail.  # noqa: E501


        :return: The checked_in of this InviteDetail.  # noqa: E501
        :rtype: bool
        """
        return self._checked_in

    @checked_in.setter
    def checked_in(self, checked_in):
        """Sets the checked_in of this InviteDetail.


        :param checked_in: The checked_in of this InviteDetail.  # noqa: E501
        :type: bool
        """

        self._checked_in = checked_in

    @property
    def group_visit(self):
        """Gets the group_visit of this InviteDetail.  # noqa: E501


        :return: The group_visit of this InviteDetail.  # noqa: E501
        :rtype: GroupVisit
        """
        return self._group_visit

    @group_visit.setter
    def group_visit(self, group_visit):
        """Sets the group_visit of this InviteDetail.


        :param group_visit: The group_visit of this InviteDetail.  # noqa: E501
        :type: GroupVisit
        """

        self._group_visit = group_visit

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
        if not isinstance(other, InviteDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InviteDetail):
            return True

        return self.to_dict() != other.to_dict()
