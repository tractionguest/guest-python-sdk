"""
    Traction Guest API

    The Traction Guest API is currently under limited release to select customers as we gather and iterate on feedback.  # Getting Started If you are interested in getting early access to the API, please send us an email to [support@tractionguest.com](mailto:support@tractionguest.com).  We will also add you to our Slack channel where you can ask questions and get further help.  # Terms and Conditions Please visit: [https://tractionguest.com/tos/api/](https://tractionguest.com/tos/api/)  # Versioning This API follows [semantic versioning](https://semver.org/), which follows the `Major`.`Minor`.`Patch` format.  * The `Major` number increments when potentially incompatible changes are made. * The `Minor` number increments when backwards-compatible additions are made. * The `Patch` number increments when backwards-compatible bug-fixes are made.   # noqa: E501

    The version of the OpenAPI document: 0.15.0
    Contact: support@tractionguest.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from TractionGuest.api_client import ApiClient, Endpoint as _Endpoint
from TractionGuest.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.paginated_signins_list import PaginatedSigninsList
from TractionGuest.model.signin import Signin
from TractionGuest.model.signin_create_params import SigninCreateParams
from TractionGuest.model.signin_detail import SigninDetail
from TractionGuest.model.signin_update_params import SigninUpdateParams


class SigninsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_signin(
            self,
            **kwargs
        ):
            """Create Signin  # noqa: E501

            Creates a Signin  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_signin(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                signin_create_params (SigninCreateParams): Params for creating a Signin can omit certain fields if a `registration_id` is present.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Signin
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.create_signin = _Endpoint(
            settings={
                'response_type': (Signin,),
                'auth': [],
                'endpoint_path': '/signins',
                'operation_id': 'create_signin',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'signin_create_params',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'signin_create_params':
                        (SigninCreateParams,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'signin_create_params': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__create_signin
        )

        def __get_signin(
            self,
            signin_id,
            **kwargs
        ):
            """Get a Signin  # noqa: E501

            Gets the details of a single instance of a `Signin`.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_signin(signin_id, async_req=True)
            >>> result = thread.get()

            Args:
                signin_id (str):

            Keyword Args:
                include (str): A list of comma-separated related models to include. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                SigninDetail
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['signin_id'] = \
                signin_id
            return self.call_with_http_info(**kwargs)

        self.get_signin = _Endpoint(
            settings={
                'response_type': (SigninDetail,),
                'auth': [],
                'endpoint_path': '/signins/{signin_id}',
                'operation_id': 'get_signin',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'signin_id',
                    'include',
                ],
                'required': [
                    'signin_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'signin_id':
                        (str,),
                    'include':
                        (str,),
                },
                'attribute_map': {
                    'signin_id': 'signin_id',
                    'include': 'include',
                },
                'location_map': {
                    'signin_id': 'path',
                    'include': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_signin
        )

        def __get_signins(
            self,
            **kwargs
        ):
            """List all Signins  # noqa: E501

            Gets a list of all `Signin` entities.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_signins(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                location_ids (str): A comma separated list of Location IDs. [optional]
                with_colours (str): A comma separated list of case-insensitive colour values. i.e., `red`, `green`, `yellow`, and `orange`. [optional]
                query (str): Allows you to query by `company`, `email`, `first_name`, `last_name`, and `location_name`. [optional]
                with_acknowledged (bool): Filters to all those `Signin`s that have, or have not been acknowledged. [optional]
                with_signed_in (bool): Filters to all `Signin`s that are, or are not currently signed out.. [optional]
                signin_before (date): Filters results to all those *before* the provided datetime. [optional]
                signin_after (date): Filters results to all those *after* the provided datetime. [optional]
                limit (int): Limits the results to a specified number, defaults to 50. [optional]
                offset (int): Offsets the results to a specified number, defaults to 0. [optional]
                query_sort (str): Allows you to override ordering by most relevant results when querying. [optional]
                include (str): A list of comma-separated related models to include. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                PaginatedSigninsList
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_signins = _Endpoint(
            settings={
                'response_type': (PaginatedSigninsList,),
                'auth': [],
                'endpoint_path': '/signins',
                'operation_id': 'get_signins',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'location_ids',
                    'with_colours',
                    'query',
                    'with_acknowledged',
                    'with_signed_in',
                    'signin_before',
                    'signin_after',
                    'limit',
                    'offset',
                    'query_sort',
                    'include',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'query_sort',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('query_sort',): {

                        "DESC": "signin_timestamp_desc",
                        "ASC": "signin_timestamp_asc"
                    },
                },
                'openapi_types': {
                    'location_ids':
                        (str,),
                    'with_colours':
                        (str,),
                    'query':
                        (str,),
                    'with_acknowledged':
                        (bool,),
                    'with_signed_in':
                        (bool,),
                    'signin_before':
                        (date,),
                    'signin_after':
                        (date,),
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                    'query_sort':
                        (str,),
                    'include':
                        (str,),
                },
                'attribute_map': {
                    'location_ids': 'location_ids',
                    'with_colours': 'with_colours',
                    'query': 'query',
                    'with_acknowledged': 'with_acknowledged',
                    'with_signed_in': 'with_signed_in',
                    'signin_before': 'signin_before',
                    'signin_after': 'signin_after',
                    'limit': 'limit',
                    'offset': 'offset',
                    'query_sort': 'query_sort',
                    'include': 'include',
                },
                'location_map': {
                    'location_ids': 'query',
                    'with_colours': 'query',
                    'query': 'query',
                    'with_acknowledged': 'query',
                    'with_signed_in': 'query',
                    'signin_before': 'query',
                    'signin_after': 'query',
                    'limit': 'query',
                    'offset': 'query',
                    'query_sort': 'query',
                    'include': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_signins
        )

        def __update_signin(
            self,
            signin_id,
            signin_update_params,
            **kwargs
        ):
            """Update a Signin  # noqa: E501

            Update, acknowledge, or `Signout` a `Signin`  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_signin(signin_id, signin_update_params, async_req=True)
            >>> result = thread.get()

            Args:
                signin_id (str):
                signin_update_params (SigninUpdateParams): The only updatable values for a `Signin` are `badge_number`, `badge_returned`, `is_accounted_for`, `is_signed_out`, and `is_acknowledged`.  `is_signed_out` and `is_acknowledged` are pseudo attributes that once set to true, are irreversible.

            Keyword Args:
                idempotency_key (str): An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                SigninDetail
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['signin_id'] = \
                signin_id
            kwargs['signin_update_params'] = \
                signin_update_params
            return self.call_with_http_info(**kwargs)

        self.update_signin = _Endpoint(
            settings={
                'response_type': (SigninDetail,),
                'auth': [],
                'endpoint_path': '/signins/{signin_id}',
                'operation_id': 'update_signin',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'signin_id',
                    'signin_update_params',
                    'idempotency_key',
                ],
                'required': [
                    'signin_id',
                    'signin_update_params',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'signin_id':
                        (str,),
                    'signin_update_params':
                        (SigninUpdateParams,),
                    'idempotency_key':
                        (str,),
                },
                'attribute_map': {
                    'signin_id': 'signin_id',
                    'idempotency_key': 'Idempotency-Key',
                },
                'location_map': {
                    'signin_id': 'path',
                    'signin_update_params': 'body',
                    'idempotency_key': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_signin
        )
