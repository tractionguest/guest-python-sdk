# coding: utf-8

"""
    Traction Guest API

    The Traction Guest API is currently under limited release to select customers as we gather and iterate on feedback.  # Getting Started If you are interested in getting early access to the API, please send us an email to [support@tractionguest.com](mailto:support@tractionguest.com).  We will also add you to our Slack channel where you can ask questions and get further help.  # Terms and Conditions Please visit: [https://tractionguest.com/tos/api/](https://tractionguest.com/tos/api/)  # Versioning This API follows [semantic versioning](https://semver.org/), which follows the `Major`.`Minor`.`Patch` format.  * The `Major` number increments when potentially incompatible changes are made. * The `Minor` number increments when backwards-compatible additions are made. * The `Patch` number increments when backwards-compatible bug-fixes are made.   # noqa: E501

    The version of the OpenAPI document: 0.17.0
    Contact: support@tractionguest.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from TractionGuest.api_client import ApiClient
from TractionGuest.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SigninsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_signin(self, **kwargs):  # noqa: E501
        """Create Signin  # noqa: E501

        Creates a Signin  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_signin(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param SigninCreateParams signin_create_params: Params for creating a Signin can omit certain fields if a `registration_id` is present.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Signin
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_signin_with_http_info(**kwargs)  # noqa: E501

    def create_signin_with_http_info(self, **kwargs):  # noqa: E501
        """Create Signin  # noqa: E501

        Creates a Signin  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_signin_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param SigninCreateParams signin_create_params: Params for creating a Signin can omit certain fields if a `registration_id` is present.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Signin, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'signin_create_params'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_signin" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'signin_create_params' in local_var_params:
            body_params = local_var_params['signin_create_params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TractionGuestAuth']  # noqa: E501

        return self.api_client.call_api(
            '/signins', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Signin',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_signin(self, signin_id, **kwargs):  # noqa: E501
        """Get a Signin  # noqa: E501

        Gets the details of a single instance of a `Signin`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_signin(signin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str signin_id: (required)
        :param str include: A list of comma-separated related models to include
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SigninDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_signin_with_http_info(signin_id, **kwargs)  # noqa: E501

    def get_signin_with_http_info(self, signin_id, **kwargs):  # noqa: E501
        """Get a Signin  # noqa: E501

        Gets the details of a single instance of a `Signin`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_signin_with_http_info(signin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str signin_id: (required)
        :param str include: A list of comma-separated related models to include
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SigninDetail, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'signin_id',
            'include'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_signin" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'signin_id' is set
        if self.api_client.client_side_validation and ('signin_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['signin_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `signin_id` when calling `get_signin`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'signin_id' in local_var_params:
            path_params['signin_id'] = local_var_params['signin_id']  # noqa: E501

        query_params = []
        if 'include' in local_var_params and local_var_params['include'] is not None:  # noqa: E501
            query_params.append(('include', local_var_params['include']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TractionGuestAuth']  # noqa: E501

        return self.api_client.call_api(
            '/signins/{signin_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SigninDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_signins(self, **kwargs):  # noqa: E501
        """List all Signins  # noqa: E501

        Gets a list of all `Signin` entities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_signins(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str location_ids: A comma separated list of Location IDs
        :param str with_colours: A comma separated list of case-insensitive colour values. i.e., `red`, `green`, `yellow`, and `orange`
        :param str query: Allows you to query by `company`, `email`, `first_name`, `last_name`, and `location_name`
        :param bool with_acknowledged: Filters to all those `Signin`s that have, or have not been acknowledged
        :param bool with_signed_in: Filters to all `Signin`s that are, or are not currently signed out.
        :param date signin_before: Filters results to all those *before* the provided datetime
        :param date signin_after: Filters results to all those *after* the provided datetime
        :param int limit: Limits the results to a specified number, defaults to 50
        :param int offset: Offsets the results to a specified number, defaults to 0
        :param str query_sort: Allows you to override ordering by most relevant results when querying
        :param str include: A list of comma-separated related models to include
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PaginatedSigninsList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_signins_with_http_info(**kwargs)  # noqa: E501

    def get_signins_with_http_info(self, **kwargs):  # noqa: E501
        """List all Signins  # noqa: E501

        Gets a list of all `Signin` entities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_signins_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str location_ids: A comma separated list of Location IDs
        :param str with_colours: A comma separated list of case-insensitive colour values. i.e., `red`, `green`, `yellow`, and `orange`
        :param str query: Allows you to query by `company`, `email`, `first_name`, `last_name`, and `location_name`
        :param bool with_acknowledged: Filters to all those `Signin`s that have, or have not been acknowledged
        :param bool with_signed_in: Filters to all `Signin`s that are, or are not currently signed out.
        :param date signin_before: Filters results to all those *before* the provided datetime
        :param date signin_after: Filters results to all those *after* the provided datetime
        :param int limit: Limits the results to a specified number, defaults to 50
        :param int offset: Offsets the results to a specified number, defaults to 0
        :param str query_sort: Allows you to override ordering by most relevant results when querying
        :param str include: A list of comma-separated related models to include
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PaginatedSigninsList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
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
            'include'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_signins" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'location_ids' in local_var_params and local_var_params['location_ids'] is not None:  # noqa: E501
            query_params.append(('location_ids', local_var_params['location_ids']))  # noqa: E501
        if 'with_colours' in local_var_params and local_var_params['with_colours'] is not None:  # noqa: E501
            query_params.append(('with_colours', local_var_params['with_colours']))  # noqa: E501
        if 'query' in local_var_params and local_var_params['query'] is not None:  # noqa: E501
            query_params.append(('query', local_var_params['query']))  # noqa: E501
        if 'with_acknowledged' in local_var_params and local_var_params['with_acknowledged'] is not None:  # noqa: E501
            query_params.append(('with_acknowledged', local_var_params['with_acknowledged']))  # noqa: E501
        if 'with_signed_in' in local_var_params and local_var_params['with_signed_in'] is not None:  # noqa: E501
            query_params.append(('with_signed_in', local_var_params['with_signed_in']))  # noqa: E501
        if 'signin_before' in local_var_params and local_var_params['signin_before'] is not None:  # noqa: E501
            query_params.append(('signin_before', local_var_params['signin_before']))  # noqa: E501
        if 'signin_after' in local_var_params and local_var_params['signin_after'] is not None:  # noqa: E501
            query_params.append(('signin_after', local_var_params['signin_after']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'query_sort' in local_var_params and local_var_params['query_sort'] is not None:  # noqa: E501
            query_params.append(('query_sort', local_var_params['query_sort']))  # noqa: E501
        if 'include' in local_var_params and local_var_params['include'] is not None:  # noqa: E501
            query_params.append(('include', local_var_params['include']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TractionGuestAuth']  # noqa: E501

        return self.api_client.call_api(
            '/signins', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedSigninsList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_signin(self, signin_id, signin_update_params, **kwargs):  # noqa: E501
        """Update a Signin  # noqa: E501

        Update, acknowledge, or `Signout` a `Signin`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_signin(signin_id, signin_update_params, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str signin_id: (required)
        :param SigninUpdateParams signin_update_params: The only updatable values for a `Signin` are `badge_number`, `badge_returned`, `is_accounted_for`, `is_signed_out`, and `is_acknowledged`.  `is_signed_out` and `is_acknowledged` are pseudo attributes that once set to true, are irreversible. (required)
        :param str idempotency_key: An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SigninDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_signin_with_http_info(signin_id, signin_update_params, **kwargs)  # noqa: E501

    def update_signin_with_http_info(self, signin_id, signin_update_params, **kwargs):  # noqa: E501
        """Update a Signin  # noqa: E501

        Update, acknowledge, or `Signout` a `Signin`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_signin_with_http_info(signin_id, signin_update_params, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str signin_id: (required)
        :param SigninUpdateParams signin_update_params: The only updatable values for a `Signin` are `badge_number`, `badge_returned`, `is_accounted_for`, `is_signed_out`, and `is_acknowledged`.  `is_signed_out` and `is_acknowledged` are pseudo attributes that once set to true, are irreversible. (required)
        :param str idempotency_key: An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SigninDetail, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'signin_id',
            'signin_update_params',
            'idempotency_key'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_signin" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'signin_id' is set
        if self.api_client.client_side_validation and ('signin_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['signin_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `signin_id` when calling `update_signin`")  # noqa: E501
        # verify the required parameter 'signin_update_params' is set
        if self.api_client.client_side_validation and ('signin_update_params' not in local_var_params or  # noqa: E501
                                                        local_var_params['signin_update_params'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `signin_update_params` when calling `update_signin`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'signin_id' in local_var_params:
            path_params['signin_id'] = local_var_params['signin_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'idempotency_key' in local_var_params:
            header_params['Idempotency-Key'] = local_var_params['idempotency_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'signin_update_params' in local_var_params:
            body_params = local_var_params['signin_update_params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TractionGuestAuth']  # noqa: E501

        return self.api_client.call_api(
            '/signins/{signin_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SigninDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
