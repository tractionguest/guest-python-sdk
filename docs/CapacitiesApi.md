# TractionGuest.CapacitiesApi

All URIs are relative to *https://tractionguest.ca/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_capacity**](CapacitiesApi.md#get_capacity) | **GET** /locations/{location_id}/capacities | Get the current capacity details for a location
[**get_capacity_forecast**](CapacitiesApi.md#get_capacity_forecast) | **GET** /locations/{location_id}/capacity_forecasts | Get the capacity details for a location


# **get_capacity**
> Capacity get_capacity(location_id)

Get the current capacity details for a location

Get details of current capacity in a location

### Example

```python
from __future__ import print_function
import time
import TractionGuest
from TractionGuest.rest import ApiException
from pprint import pprint
configuration = TractionGuest.Configuration()

# Defining host is optional and default to https://tractionguest.ca/api/v3
configuration.host = "https://tractionguest.ca/api/v3"

# Enter a context with an instance of the API client
with TractionGuest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TractionGuest.CapacitiesApi(api_client)
    location_id = 'location_id_example' # str | 

    try:
        # Get the current capacity details for a location
        api_response = api_instance.get_capacity(location_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CapacitiesApi->get_capacity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  | 

### Return type

[**Capacity**](Capacity.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response returns the current_signins and expected invites for the next hour. |  -  |
**400** | A generic error |  -  |
**401** | You don&#39;t have permission to view the details of the location&#39;s capacity. |  -  |
**403** | You do not have permission for this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_capacity_forecast**
> CapacityForecast get_capacity_forecast(location_id, hours_to_forecast=hours_to_forecast, timestamp=timestamp)

Get the capacity details for a location

Gets the details of the future capacity in a location.

### Example

```python
from __future__ import print_function
import time
import TractionGuest
from TractionGuest.rest import ApiException
from pprint import pprint
configuration = TractionGuest.Configuration()

# Defining host is optional and default to https://tractionguest.ca/api/v3
configuration.host = "https://tractionguest.ca/api/v3"

# Enter a context with an instance of the API client
with TractionGuest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TractionGuest.CapacitiesApi(api_client)
    location_id = 'location_id_example' # str | 
hours_to_forecast = 8 # int | The next N number of hours, the data needs to be calculated. Range from 1 to 24. If not set, it defaults to 8. (optional) (default to 8)
timestamp = 'timestamp_example' # str | ISO8601 timestamp(includes the offset value) to use as the start point for the capacity estimate report. Defaults to the current local timestamp of the location if not provided. Eg: \"2020-07-16T17:05:08-07:00\" (optional)

    try:
        # Get the capacity details for a location
        api_response = api_instance.get_capacity_forecast(location_id, hours_to_forecast=hours_to_forecast, timestamp=timestamp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CapacitiesApi->get_capacity_forecast: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  | 
 **hours_to_forecast** | **int**| The next N number of hours, the data needs to be calculated. Range from 1 to 24. If not set, it defaults to 8. | [optional] [default to 8]
 **timestamp** | **str**| ISO8601 timestamp(includes the offset value) to use as the start point for the capacity estimate report. Defaults to the current local timestamp of the location if not provided. Eg: \&quot;2020-07-16T17:05:08-07:00\&quot; | [optional] 

### Return type

[**CapacityForecast**](CapacityForecast.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response returns the expected invites for the next N number of hours. |  -  |
**400** | A generic error |  -  |
**401** | You don&#39;t have permission to view the details of the location&#39;s capacity. |  -  |
**403** | You do not have permission for this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

