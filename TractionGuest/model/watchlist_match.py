"""
    Traction Guest API

    The Traction Guest API is currently under limited release to select customers as we gather and iterate on feedback.  # Getting Started If you are interested in getting early access to the API, please send us an email to [support@tractionguest.com](mailto:support@tractionguest.com).  We will also add you to our Slack channel where you can ask questions and get further help.  # Terms and Conditions Please visit: [https://tractionguest.com/tos/api/](https://tractionguest.com/tos/api/)  # Versioning This API follows [semantic versioning](https://semver.org/), which follows the `Major`.`Minor`.`Patch` format.  * The `Major` number increments when potentially incompatible changes are made. * The `Minor` number increments when backwards-compatible additions are made. * The `Patch` number increments when backwards-compatible bug-fixes are made.   # noqa: E501

    The version of the OpenAPI document: 0.15.0
    Contact: support@tractionguest.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from TractionGuest.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


class WatchlistMatch(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'name': (str,),  # noqa: E501
            'list': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'alt_names': ([str],),  # noqa: E501
            'federal_register_notice': (str,),  # noqa: E501
            'source_information_url': (str,),  # noqa: E501
            'source_list_url': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'category': (str,),  # noqa: E501
            'street1': (str,),  # noqa: E501
            'street2': (str,),  # noqa: E501
            'city': (str,),  # noqa: E501
            'state': (str,),  # noqa: E501
            'country': (str,),  # noqa: E501
            'notes': (str,),  # noqa: E501
            'frc': (str,),  # noqa: E501
            'start': (str,),  # noqa: E501
            'end': (str,),  # noqa: E501
            'frserve': (str,),  # noqa: E501
            'optional_id': (str,),  # noqa: E501
            'alert_type': (str,),  # noqa: E501
            'pair_status': (str,),  # noqa: E501
            'pair_reason': (str,),  # noqa: E501
            'pair_comments': (str,),  # noqa: E501
            'application_display_name': (str,),  # noqa: E501
            'application_id': (str,),  # noqa: E501
            'client_id': (str,),  # noqa: E501
            'client_key': (str,),  # noqa: E501
            'client_full_name': (str,),  # noqa: E501
            'list_key': (str,),  # noqa: E501
            'list_name': (str,),  # noqa: E501
            'list_id': (str,),  # noqa: E501
            'list_version': (str,),  # noqa: E501
            'list_modify_date': (str,),  # noqa: E501
            'list_profile_id': (str,),  # noqa: E501
            'list_profile_key': (str,),  # noqa: E501
            'link_single_string_name': (str,),  # noqa: E501
            'list_parent_single_string_name': (str,),  # noqa: E501
            'list_category': (str,),  # noqa: E501
            'list_pep_category': (str,),  # noqa: E501
            'list_do_bs': (str,),  # noqa: E501
            'list_countries': (str,),  # noqa: E501
            'rank_string': (str,),  # noqa: E501
            'ranktype': (str,),  # noqa: E501
            'rankweight': (str,),  # noqa: E501
            'pair_load_date': (str,),  # noqa: E501
            'e_address_to': (str,),  # noqa: E501
            'e_address_cc': (str,),  # noqa: E501
            'origin': (str,),  # noqa: E501
            'secondsviewed': (str,),  # noqa: E501
            'initial_user': (str,),  # noqa: E501
            'is_pair_parent_flag': (str,),  # noqa: E501
            'pair_met_search_criteria_flag': (str,),  # noqa: E501
            'editable_due_to_assignment_flag': (str,),  # noqa: E501
            'modify_date': (str,),  # noqa: E501
            'modified_by_user': (str,),  # noqa: E501
            'pair_report_type': (str,),  # noqa: E501
            'finscan_category': (str,),  # noqa: E501
            'wrapper_status': (str,),  # noqa: E501
            'source_lists': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name': 'name',  # noqa: E501
        'list': 'list',  # noqa: E501
        'id': 'id',  # noqa: E501
        'alt_names': 'alt_names',  # noqa: E501
        'federal_register_notice': 'federal_register_notice',  # noqa: E501
        'source_information_url': 'source_information_url',  # noqa: E501
        'source_list_url': 'source_list_url',  # noqa: E501
        'type': 'type',  # noqa: E501
        'category': 'category',  # noqa: E501
        'street1': 'street1',  # noqa: E501
        'street2': 'street2',  # noqa: E501
        'city': 'city',  # noqa: E501
        'state': 'state',  # noqa: E501
        'country': 'country',  # noqa: E501
        'notes': 'notes',  # noqa: E501
        'frc': 'frc',  # noqa: E501
        'start': 'start',  # noqa: E501
        'end': 'end',  # noqa: E501
        'frserve': 'frserve',  # noqa: E501
        'optional_id': 'optional_ID',  # noqa: E501
        'alert_type': 'alert_type',  # noqa: E501
        'pair_status': 'pair_status',  # noqa: E501
        'pair_reason': 'pair_reason',  # noqa: E501
        'pair_comments': 'pair_comments',  # noqa: E501
        'application_display_name': 'application_display_name',  # noqa: E501
        'application_id': 'application_id',  # noqa: E501
        'client_id': 'client_id',  # noqa: E501
        'client_key': 'client_key',  # noqa: E501
        'client_full_name': 'client_full_name',  # noqa: E501
        'list_key': 'list_key',  # noqa: E501
        'list_name': 'list_name',  # noqa: E501
        'list_id': 'list_id',  # noqa: E501
        'list_version': 'list_version',  # noqa: E501
        'list_modify_date': 'list_modify_date',  # noqa: E501
        'list_profile_id': 'list_profile_id',  # noqa: E501
        'list_profile_key': 'list_profile_key',  # noqa: E501
        'link_single_string_name': 'link_single_string_name',  # noqa: E501
        'list_parent_single_string_name': 'list_parent_single_string_name',  # noqa: E501
        'list_category': 'list_category',  # noqa: E501
        'list_pep_category': 'list_pep_category',  # noqa: E501
        'list_do_bs': 'list_do_bs',  # noqa: E501
        'list_countries': 'list_countries',  # noqa: E501
        'rank_string': 'rank_string',  # noqa: E501
        'ranktype': 'ranktype',  # noqa: E501
        'rankweight': 'rankweight',  # noqa: E501
        'pair_load_date': 'pair_load_date',  # noqa: E501
        'e_address_to': 'e_address_to',  # noqa: E501
        'e_address_cc': 'e_address_cc',  # noqa: E501
        'origin': 'origin',  # noqa: E501
        'secondsviewed': 'secondsviewed',  # noqa: E501
        'initial_user': 'initial_user',  # noqa: E501
        'is_pair_parent_flag': 'is_pair_parent_flag',  # noqa: E501
        'pair_met_search_criteria_flag': 'pair_met_search_criteria_flag',  # noqa: E501
        'editable_due_to_assignment_flag': 'editable_due_to_assignment_flag',  # noqa: E501
        'modify_date': 'modify_date',  # noqa: E501
        'modified_by_user': 'modified_by_user',  # noqa: E501
        'pair_report_type': 'pair_report_type',  # noqa: E501
        'finscan_category': 'finscan_category',  # noqa: E501
        'wrapper_status': 'wrapper_status',  # noqa: E501
        'source_lists': 'source_lists',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, name, list, *args, **kwargs):  # noqa: E501
        """WatchlistMatch - a model defined in OpenAPI

        Args:
            name (str):
            list (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): [optional]  # noqa: E501
            alt_names ([str]): [optional]  # noqa: E501
            federal_register_notice (str): [optional]  # noqa: E501
            source_information_url (str): [optional]  # noqa: E501
            source_list_url (str): [optional]  # noqa: E501
            type (str): . [optional]  # noqa: E501
            category (str): . [optional]  # noqa: E501
            street1 (str): . [optional]  # noqa: E501
            street2 (str): . [optional]  # noqa: E501
            city (str): . [optional]  # noqa: E501
            state (str): . [optional]  # noqa: E501
            country (str): . [optional]  # noqa: E501
            notes (str): . [optional]  # noqa: E501
            frc (str): . [optional]  # noqa: E501
            start (str): . [optional]  # noqa: E501
            end (str): . [optional]  # noqa: E501
            frserve (str): . [optional]  # noqa: E501
            optional_id (str): . [optional]  # noqa: E501
            alert_type (str): . [optional]  # noqa: E501
            pair_status (str): . [optional]  # noqa: E501
            pair_reason (str): . [optional]  # noqa: E501
            pair_comments (str): . [optional]  # noqa: E501
            application_display_name (str): . [optional]  # noqa: E501
            application_id (str): . [optional]  # noqa: E501
            client_id (str): . [optional]  # noqa: E501
            client_key (str): . [optional]  # noqa: E501
            client_full_name (str): . [optional]  # noqa: E501
            list_key (str): . [optional]  # noqa: E501
            list_name (str): . [optional]  # noqa: E501
            list_id (str): . [optional]  # noqa: E501
            list_version (str): . [optional]  # noqa: E501
            list_modify_date (str): . [optional]  # noqa: E501
            list_profile_id (str): . [optional]  # noqa: E501
            list_profile_key (str): . [optional]  # noqa: E501
            link_single_string_name (str): . [optional]  # noqa: E501
            list_parent_single_string_name (str): . [optional]  # noqa: E501
            list_category (str): . [optional]  # noqa: E501
            list_pep_category (str): . [optional]  # noqa: E501
            list_do_bs (str): . [optional]  # noqa: E501
            list_countries (str): . [optional]  # noqa: E501
            rank_string (str): . [optional]  # noqa: E501
            ranktype (str): . [optional]  # noqa: E501
            rankweight (str): . [optional]  # noqa: E501
            pair_load_date (str): . [optional]  # noqa: E501
            e_address_to (str): . [optional]  # noqa: E501
            e_address_cc (str): . [optional]  # noqa: E501
            origin (str): . [optional]  # noqa: E501
            secondsviewed (str): . [optional]  # noqa: E501
            initial_user (str): . [optional]  # noqa: E501
            is_pair_parent_flag (str): . [optional]  # noqa: E501
            pair_met_search_criteria_flag (str): . [optional]  # noqa: E501
            editable_due_to_assignment_flag (str): . [optional]  # noqa: E501
            modify_date (str): . [optional]  # noqa: E501
            modified_by_user (str): . [optional]  # noqa: E501
            pair_report_type (str): . [optional]  # noqa: E501
            finscan_category (str): . [optional]  # noqa: E501
            wrapper_status (str): . [optional]  # noqa: E501
            source_lists (str): . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.name = name
        self.list = list
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
