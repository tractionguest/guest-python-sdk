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


class AuditLog(object):
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
        'created_at': 'str',
        'request_uuid': 'str',
        'remote_address': 'str',
        'comment': 'str',
        'version': 'int',
        'audited_changes': 'list[AuditLogChange]',
        'action': 'str',
        'username': 'str',
        'user_id': 'int',
        'auditable_type': 'str',
        'auditable_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'request_uuid': 'request_uuid',
        'remote_address': 'remote_address',
        'comment': 'comment',
        'version': 'version',
        'audited_changes': 'audited_changes',
        'action': 'action',
        'username': 'username',
        'user_id': 'user_id',
        'auditable_type': 'auditable_type',
        'auditable_id': 'auditable_id'
    }

    def __init__(self, id=None, created_at=None, request_uuid=None, remote_address=None, comment=None, version=None, audited_changes=None, action=None, username=None, user_id=None, auditable_type=None, auditable_id=None, local_vars_configuration=None):  # noqa: E501
        """AuditLog - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_at = None
        self._request_uuid = None
        self._remote_address = None
        self._comment = None
        self._version = None
        self._audited_changes = None
        self._action = None
        self._username = None
        self._user_id = None
        self._auditable_type = None
        self._auditable_id = None
        self.discriminator = None

        self.id = id
        if created_at is not None:
            self.created_at = created_at
        if request_uuid is not None:
            self.request_uuid = request_uuid
        if remote_address is not None:
            self.remote_address = remote_address
        if comment is not None:
            self.comment = comment
        if version is not None:
            self.version = version
        if audited_changes is not None:
            self.audited_changes = audited_changes
        if action is not None:
            self.action = action
        if username is not None:
            self.username = username
        if user_id is not None:
            self.user_id = user_id
        if auditable_type is not None:
            self.auditable_type = auditable_type
        if auditable_id is not None:
            self.auditable_id = auditable_id

    @property
    def id(self):
        """Gets the id of this AuditLog.  # noqa: E501

          # noqa: E501

        :return: The id of this AuditLog.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuditLog.

          # noqa: E501

        :param id: The id of this AuditLog.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this AuditLog.  # noqa: E501

          # noqa: E501

        :return: The created_at of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AuditLog.

          # noqa: E501

        :param created_at: The created_at of this AuditLog.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def request_uuid(self):
        """Gets the request_uuid of this AuditLog.  # noqa: E501

          # noqa: E501

        :return: The request_uuid of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._request_uuid

    @request_uuid.setter
    def request_uuid(self, request_uuid):
        """Sets the request_uuid of this AuditLog.

          # noqa: E501

        :param request_uuid: The request_uuid of this AuditLog.  # noqa: E501
        :type: str
        """

        self._request_uuid = request_uuid

    @property
    def remote_address(self):
        """Gets the remote_address of this AuditLog.  # noqa: E501

          # noqa: E501

        :return: The remote_address of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._remote_address

    @remote_address.setter
    def remote_address(self, remote_address):
        """Sets the remote_address of this AuditLog.

          # noqa: E501

        :param remote_address: The remote_address of this AuditLog.  # noqa: E501
        :type: str
        """

        self._remote_address = remote_address

    @property
    def comment(self):
        """Gets the comment of this AuditLog.  # noqa: E501

          # noqa: E501

        :return: The comment of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AuditLog.

          # noqa: E501

        :param comment: The comment of this AuditLog.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def version(self):
        """Gets the version of this AuditLog.  # noqa: E501

          # noqa: E501

        :return: The version of this AuditLog.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AuditLog.

          # noqa: E501

        :param version: The version of this AuditLog.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def audited_changes(self):
        """Gets the audited_changes of this AuditLog.  # noqa: E501


        :return: The audited_changes of this AuditLog.  # noqa: E501
        :rtype: list[AuditLogChange]
        """
        return self._audited_changes

    @audited_changes.setter
    def audited_changes(self, audited_changes):
        """Sets the audited_changes of this AuditLog.


        :param audited_changes: The audited_changes of this AuditLog.  # noqa: E501
        :type: list[AuditLogChange]
        """

        self._audited_changes = audited_changes

    @property
    def action(self):
        """Gets the action of this AuditLog.  # noqa: E501

          # noqa: E501

        :return: The action of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this AuditLog.

          # noqa: E501

        :param action: The action of this AuditLog.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def username(self):
        """Gets the username of this AuditLog.  # noqa: E501

          # noqa: E501

        :return: The username of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AuditLog.

          # noqa: E501

        :param username: The username of this AuditLog.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def user_id(self):
        """Gets the user_id of this AuditLog.  # noqa: E501

          # noqa: E501

        :return: The user_id of this AuditLog.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AuditLog.

          # noqa: E501

        :param user_id: The user_id of this AuditLog.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def auditable_type(self):
        """Gets the auditable_type of this AuditLog.  # noqa: E501

          # noqa: E501

        :return: The auditable_type of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._auditable_type

    @auditable_type.setter
    def auditable_type(self, auditable_type):
        """Sets the auditable_type of this AuditLog.

          # noqa: E501

        :param auditable_type: The auditable_type of this AuditLog.  # noqa: E501
        :type: str
        """

        self._auditable_type = auditable_type

    @property
    def auditable_id(self):
        """Gets the auditable_id of this AuditLog.  # noqa: E501

          # noqa: E501

        :return: The auditable_id of this AuditLog.  # noqa: E501
        :rtype: int
        """
        return self._auditable_id

    @auditable_id.setter
    def auditable_id(self, auditable_id):
        """Sets the auditable_id of this AuditLog.

          # noqa: E501

        :param auditable_id: The auditable_id of this AuditLog.  # noqa: E501
        :type: int
        """

        self._auditable_id = auditable_id

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
        if not isinstance(other, AuditLog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuditLog):
            return True

        return self.to_dict() != other.to_dict()
