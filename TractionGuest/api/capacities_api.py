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


class CapacitiesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_capacity(self, location_id, **kwargs):  # noqa: E501
        """Get the current capacity details for a location  # noqa: E501

        Get details of current capacity in a location  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_capacity(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str location_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Capacity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_capacity_with_http_info(location_id, **kwargs)  # noqa: E501

    def get_capacity_with_http_info(self, location_id, **kwargs):  # noqa: E501
        """Get the current capacity details for a location  # noqa: E501

        Get details of current capacity in a location  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_capacity_with_http_info(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str location_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Capacity, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'location_id'
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
                    " to method get_capacity" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'location_id' is set
        if self.api_client.client_side_validation and ('location_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['location_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `location_id` when calling `get_capacity`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'location_id' in local_var_params:
            path_params['location_id'] = local_var_params['location_id']  # noqa: E501

        query_params = []

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
            '/locations/{location_id}/capacities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Capacity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_capacity_forecast(self, location_id, **kwargs):  # noqa: E501
        """Get the capacity details for a location  # noqa: E501

        Gets the details of the future capacity in a location.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_capacity_forecast(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str location_id: (required)
        :param int hours_to_forecast: The next N number of hours, the data needs to be calculated. Range from 1 to 24. If not set, it defaults to 8.
        :param str timestamp: ISO8601 timestamp(includes the offset value) to use as the start point for the capacity estimate report. Defaults to the current local timestamp of the location if not provided. Eg: \"2020-07-16T17:05:08-07:00\"
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CapacityForecast
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_capacity_forecast_with_http_info(location_id, **kwargs)  # noqa: E501

    def get_capacity_forecast_with_http_info(self, location_id, **kwargs):  # noqa: E501
        """Get the capacity details for a location  # noqa: E501

        Gets the details of the future capacity in a location.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_capacity_forecast_with_http_info(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str location_id: (required)
        :param int hours_to_forecast: The next N number of hours, the data needs to be calculated. Range from 1 to 24. If not set, it defaults to 8.
        :param str timestamp: ISO8601 timestamp(includes the offset value) to use as the start point for the capacity estimate report. Defaults to the current local timestamp of the location if not provided. Eg: \"2020-07-16T17:05:08-07:00\"
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CapacityForecast, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'location_id',
            'hours_to_forecast',
            'timestamp'
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
                    " to method get_capacity_forecast" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'location_id' is set
        if self.api_client.client_side_validation and ('location_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['location_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `location_id` when calling `get_capacity_forecast`")  # noqa: E501

        if self.api_client.client_side_validation and 'hours_to_forecast' in local_var_params and local_var_params['hours_to_forecast'] > 24:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `hours_to_forecast` when calling `get_capacity_forecast`, must be a value less than or equal to `24`")  # noqa: E501
        if self.api_client.client_side_validation and 'hours_to_forecast' in local_var_params and local_var_params['hours_to_forecast'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `hours_to_forecast` when calling `get_capacity_forecast`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'location_id' in local_var_params:
            path_params['location_id'] = local_var_params['location_id']  # noqa: E501

        query_params = []
        if 'hours_to_forecast' in local_var_params and local_var_params['hours_to_forecast'] is not None:  # noqa: E501
            query_params.append(('hours_to_forecast', local_var_params['hours_to_forecast']))  # noqa: E501
        if 'timestamp' in local_var_params and local_var_params['timestamp'] is not None:  # noqa: E501
            query_params.append(('timestamp', local_var_params['timestamp']))  # noqa: E501

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
            '/locations/{location_id}/capacity_forecasts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CapacityForecast',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
