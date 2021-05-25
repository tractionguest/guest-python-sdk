# TractionGuest.CapacitiesApi

All URIs are relative to *https://us.tractionguest.com/api/v3*

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
import time
import TractionGuest
from TractionGuest.api import capacities_api
from TractionGuest.model.capacity import Capacity
from TractionGuest.model.errors_list import ErrorsList
from pprint import pprint
# Defining the host is optional and defaults to https://us.tractionguest.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = TractionGuest.Configuration(
    host = "https://us.tractionguest.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with TractionGuest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = capacities_api.CapacitiesApi(api_client)
    location_id = "location_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the current capacity details for a location
        api_response = api_instance.get_capacity(location_id)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling CapacitiesApi->get_capacity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  |

### Return type

[**Capacity**](Capacity.md)

### Authorization

No authorization required

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
> CapacityForecast get_capacity_forecast(location_id)

Get the capacity details for a location

Gets the details of the future capacity in a location.

### Example

```python
import time
import TractionGuest
from TractionGuest.api import capacities_api
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.capacity_forecast import CapacityForecast
from pprint import pprint
# Defining the host is optional and defaults to https://us.tractionguest.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = TractionGuest.Configuration(
    host = "https://us.tractionguest.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with TractionGuest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = capacities_api.CapacitiesApi(api_client)
    location_id = "location_id_example" # str | 
    hours_to_forecast = 8 # int | The next N number of hours, the data needs to be calculated. Range from 1 to 24. If not set, it defaults to 8. (optional) if omitted the server will use the default value of 8
    timestamp = "timestamp_example" # str | ISO8601 timestamp(includes the offset value) to use as the start point for the capacity estimate report. Defaults to the current local timestamp of the location if not provided. Eg: \"2020-07-16T17:05:08-07:00\" (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the capacity details for a location
        api_response = api_instance.get_capacity_forecast(location_id)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling CapacitiesApi->get_capacity_forecast: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the capacity details for a location
        api_response = api_instance.get_capacity_forecast(location_id, hours_to_forecast=hours_to_forecast, timestamp=timestamp)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling CapacitiesApi->get_capacity_forecast: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  |
 **hours_to_forecast** | **int**| The next N number of hours, the data needs to be calculated. Range from 1 to 24. If not set, it defaults to 8. | [optional] if omitted the server will use the default value of 8
 **timestamp** | **str**| ISO8601 timestamp(includes the offset value) to use as the start point for the capacity estimate report. Defaults to the current local timestamp of the location if not provided. Eg: \&quot;2020-07-16T17:05:08-07:00\&quot; | [optional]

### Return type

[**CapacityForecast**](CapacityForecast.md)

### Authorization

No authorization required

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

