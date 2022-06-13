# coding: utf-8

"""
    Traction Guest API

    The Traction Guest API is currently under limited release to select customers as we gather and iterate on feedback.  # Getting Started If you are interested in getting early access to the API, please send us an email to [support@tractionguest.com](mailto:support@tractionguest.com).  We will also add you to our Slack channel where you can ask questions and get further help.  # Terms and Conditions Please visit: [https://tractionguest.com/tos/api/](https://tractionguest.com/tos/api/)  # Versioning This API follows [semantic versioning](https://semver.org/), which follows the `Major`.`Minor`.`Patch` format.  * The `Major` number increments when potentially incompatible changes are made. * The `Minor` number increments when backwards-compatible additions are made. * The `Patch` number increments when backwards-compatible bug-fixes are made.   # noqa: E501

    The version of the OpenAPI document: 0.18.0
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


class WatchlistsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_watchlist(self, watchlist_create_params, **kwargs):  # noqa: E501
        """Create Watchlist  # noqa: E501

        Create a new `Watchlist` record. Please note, every action taken against this endpoint is recorded in the audit log.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_watchlist(watchlist_create_params, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param WatchlistCreateParams watchlist_create_params: The new `Watchlist` to create (required)
        :param str idempotency_key: An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Watchlist
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_watchlist_with_http_info(watchlist_create_params, **kwargs)  # noqa: E501

    def create_watchlist_with_http_info(self, watchlist_create_params, **kwargs):  # noqa: E501
        """Create Watchlist  # noqa: E501

        Create a new `Watchlist` record. Please note, every action taken against this endpoint is recorded in the audit log.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_watchlist_with_http_info(watchlist_create_params, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param WatchlistCreateParams watchlist_create_params: The new `Watchlist` to create (required)
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
        :return: tuple(Watchlist, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'watchlist_create_params',
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
                    " to method create_watchlist" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'watchlist_create_params' is set
        if self.api_client.client_side_validation and ('watchlist_create_params' not in local_var_params or  # noqa: E501
                                                        local_var_params['watchlist_create_params'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `watchlist_create_params` when calling `create_watchlist`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'idempotency_key' in local_var_params:
            header_params['Idempotency-Key'] = local_var_params['idempotency_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'watchlist_create_params' in local_var_params:
            body_params = local_var_params['watchlist_create_params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TractionGuestAuth']  # noqa: E501

        return self.api_client.call_api(
            '/watchlists', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Watchlist',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_watchlist(self, watchlist_id, **kwargs):  # noqa: E501
        """Deletes a Watchlist  # noqa: E501

        Deletes a single instance of `Watchlist`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_watchlist(watchlist_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str watchlist_id: (required)
        :param str idempotency_key: An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_watchlist_with_http_info(watchlist_id, **kwargs)  # noqa: E501

    def delete_watchlist_with_http_info(self, watchlist_id, **kwargs):  # noqa: E501
        """Deletes a Watchlist  # noqa: E501

        Deletes a single instance of `Watchlist`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_watchlist_with_http_info(watchlist_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str watchlist_id: (required)
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
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'watchlist_id',
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
                    " to method delete_watchlist" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'watchlist_id' is set
        if self.api_client.client_side_validation and ('watchlist_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['watchlist_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `watchlist_id` when calling `delete_watchlist`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'watchlist_id' in local_var_params:
            path_params['watchlist_id'] = local_var_params['watchlist_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'idempotency_key' in local_var_params:
            header_params['Idempotency-Key'] = local_var_params['idempotency_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TractionGuestAuth']  # noqa: E501

        return self.api_client.call_api(
            '/watchlists/{watchlist_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_watchlist(self, watchlist_id, **kwargs):  # noqa: E501
        """Get a Watchlist  # noqa: E501

        Gets the details of a single instance of a `Watchlist`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_watchlist(watchlist_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str watchlist_id: (required)
        :param str include: A list of comma-separated related models to include
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Watchlist
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_watchlist_with_http_info(watchlist_id, **kwargs)  # noqa: E501

    def get_watchlist_with_http_info(self, watchlist_id, **kwargs):  # noqa: E501
        """Get a Watchlist  # noqa: E501

        Gets the details of a single instance of a `Watchlist`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_watchlist_with_http_info(watchlist_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str watchlist_id: (required)
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
        :return: tuple(Watchlist, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'watchlist_id',
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
                    " to method get_watchlist" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'watchlist_id' is set
        if self.api_client.client_side_validation and ('watchlist_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['watchlist_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `watchlist_id` when calling `get_watchlist`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'watchlist_id' in local_var_params:
            path_params['watchlist_id'] = local_var_params['watchlist_id']  # noqa: E501

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
            '/watchlists/{watchlist_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Watchlist',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_watchlists(self, **kwargs):  # noqa: E501
        """List all Watchlists  # noqa: E501

        Gets a list of all `Watchlist` entities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_watchlists(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Limits the results to a specified number, defaults to 50
        :param int offset: Offsets the results to a specified number, defaults to 0
        :param str query: Query the results by `first_name`, `last_name`, `email`, `colour`, and `notes` all at once.
        :param str with_colours: A comma separated list of case-insensitive colour values. i.e., `red`, `green`, `yellow`, and `orange`
        :param str include: A list of comma-separated related models to include
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PaginatedWatchlistList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_watchlists_with_http_info(**kwargs)  # noqa: E501

    def get_watchlists_with_http_info(self, **kwargs):  # noqa: E501
        """List all Watchlists  # noqa: E501

        Gets a list of all `Watchlist` entities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_watchlists_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Limits the results to a specified number, defaults to 50
        :param int offset: Offsets the results to a specified number, defaults to 0
        :param str query: Query the results by `first_name`, `last_name`, `email`, `colour`, and `notes` all at once.
        :param str with_colours: A comma separated list of case-insensitive colour values. i.e., `red`, `green`, `yellow`, and `orange`
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
        :return: tuple(PaginatedWatchlistList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'limit',
            'offset',
            'query',
            'with_colours',
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
                    " to method get_watchlists" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'query' in local_var_params and local_var_params['query'] is not None:  # noqa: E501
            query_params.append(('query', local_var_params['query']))  # noqa: E501
        if 'with_colours' in local_var_params and local_var_params['with_colours'] is not None:  # noqa: E501
            query_params.append(('with_colours', local_var_params['with_colours']))  # noqa: E501
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
            '/watchlists', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedWatchlistList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_watchlist(self, watchlist_id, watchlist_create_params, **kwargs):  # noqa: E501
        """Update a Watchlist  # noqa: E501

        Update an existing `Watchlist` record. Every operation against this endpoint is recorded in the audit log.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_watchlist(watchlist_id, watchlist_create_params, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str watchlist_id: (required)
        :param WatchlistCreateParams watchlist_create_params: The watchlist record attributes to update (required)
        :param str idempotency_key: An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Watchlist
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_watchlist_with_http_info(watchlist_id, watchlist_create_params, **kwargs)  # noqa: E501

    def update_watchlist_with_http_info(self, watchlist_id, watchlist_create_params, **kwargs):  # noqa: E501
        """Update a Watchlist  # noqa: E501

        Update an existing `Watchlist` record. Every operation against this endpoint is recorded in the audit log.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_watchlist_with_http_info(watchlist_id, watchlist_create_params, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str watchlist_id: (required)
        :param WatchlistCreateParams watchlist_create_params: The watchlist record attributes to update (required)
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
        :return: tuple(Watchlist, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'watchlist_id',
            'watchlist_create_params',
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
                    " to method update_watchlist" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'watchlist_id' is set
        if self.api_client.client_side_validation and ('watchlist_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['watchlist_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `watchlist_id` when calling `update_watchlist`")  # noqa: E501
        # verify the required parameter 'watchlist_create_params' is set
        if self.api_client.client_side_validation and ('watchlist_create_params' not in local_var_params or  # noqa: E501
                                                        local_var_params['watchlist_create_params'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `watchlist_create_params` when calling `update_watchlist`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'watchlist_id' in local_var_params:
            path_params['watchlist_id'] = local_var_params['watchlist_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'idempotency_key' in local_var_params:
            header_params['Idempotency-Key'] = local_var_params['idempotency_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'watchlist_create_params' in local_var_params:
            body_params = local_var_params['watchlist_create_params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TractionGuestAuth']  # noqa: E501

        return self.api_client.call_api(
            '/watchlists/{watchlist_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Watchlist',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
