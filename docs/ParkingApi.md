# TractionGuest.ParkingApi

All URIs are relative to *https://us.tractionguest.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_parking_lot_available_stalls**](ParkingApi.md#get_parking_lot_available_stalls) | **GET** /parking_lots/{parking_lot_id}/available_stalls | Get available stalls for stall type
[**get_parking_lots**](ParkingApi.md#get_parking_lots) | **GET** /parking_lots | Get parking lots
[**get_parking_stalls**](ParkingApi.md#get_parking_stalls) | **GET** /parking_lots/{parking_lot_id}/parking_stalls | Get stalls of parking lot


# **get_parking_lot_available_stalls**
> list[ParkingLotAvailableStalls] get_parking_lot_available_stalls(parking_lot_id, stall_type, start_date, end_date, timezone=timezone)

Get available stalls for stall type

Gets a list of [ParkingLotAvailableStalls] entities.

### Example

```python
from __future__ import print_function
import time
import TractionGuest
from TractionGuest.rest import ApiException
from pprint import pprint
configuration = TractionGuest.Configuration()

# Defining host is optional and default to https://us.tractionguest.com/api/v3
configuration.host = "https://us.tractionguest.com/api/v3"

# Enter a context with an instance of the API client
with TractionGuest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TractionGuest.ParkingApi(api_client)
    parking_lot_id = 'parking_lot_id_example' # str | 
stall_type = 'stall_type_example' # str | The type of stall to filter by. E.g., 'Compact', 'Standard', 'Electric', 'Handicapped'
start_date = '2013-10-20T19:20:30+01:00' # datetime | The start date to filter by. E.g., '2024-06-13T15:30:00'
end_date = '2013-10-20T19:20:30+01:00' # datetime | The end date to filter by. E.g., '2024-06-13T15:30:00'
timezone = 'timezone_example' # str | The IANA timezone to be used if not provided in both start_date and end_date. E.g., 'America/Vancouver' (optional)

    try:
        # Get available stalls for stall type
        api_response = api_instance.get_parking_lot_available_stalls(parking_lot_id, stall_type, start_date, end_date, timezone=timezone)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParkingApi->get_parking_lot_available_stalls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parking_lot_id** | **str**|  | 
 **stall_type** | **str**| The type of stall to filter by. E.g., &#39;Compact&#39;, &#39;Standard&#39;, &#39;Electric&#39;, &#39;Handicapped&#39; | 
 **start_date** | **datetime**| The start date to filter by. E.g., &#39;2024-06-13T15:30:00&#39; | 
 **end_date** | **datetime**| The end date to filter by. E.g., &#39;2024-06-13T15:30:00&#39; | 
 **timezone** | **str**| The IANA timezone to be used if not provided in both start_date and end_date. E.g., &#39;America/Vancouver&#39; | [optional] 

### Return type

[**list[ParkingLotAvailableStalls]**](ParkingLotAvailableStalls.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parking_lots**
> PaginatedParkingLotsList get_parking_lots(limit=limit, offset=offset)

Get parking lots

Gets a list of [ParkingLot] entities.

### Example

```python
from __future__ import print_function
import time
import TractionGuest
from TractionGuest.rest import ApiException
from pprint import pprint
configuration = TractionGuest.Configuration()

# Defining host is optional and default to https://us.tractionguest.com/api/v3
configuration.host = "https://us.tractionguest.com/api/v3"

# Enter a context with an instance of the API client
with TractionGuest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TractionGuest.ParkingApi(api_client)
    limit = 50 # int | Limits the results to a specified number, defaults to 50 (optional) (default to 50)
offset = 0 # int | Offsets the results to a specified number, defaults to 0 (optional) (default to 0)

    try:
        # Get parking lots
        api_response = api_instance.get_parking_lots(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParkingApi->get_parking_lots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the results to a specified number, defaults to 50 | [optional] [default to 50]
 **offset** | **int**| Offsets the results to a specified number, defaults to 0 | [optional] [default to 0]

### Return type

[**PaginatedParkingLotsList**](PaginatedParkingLotsList.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parking_stalls**
> PaginatedParkingStallsList get_parking_stalls(parking_lot_id, limit=limit, offset=offset)

Get stalls of parking lot

Gets a list of [ParkingStall] entities.

### Example

```python
from __future__ import print_function
import time
import TractionGuest
from TractionGuest.rest import ApiException
from pprint import pprint
configuration = TractionGuest.Configuration()

# Defining host is optional and default to https://us.tractionguest.com/api/v3
configuration.host = "https://us.tractionguest.com/api/v3"

# Enter a context with an instance of the API client
with TractionGuest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TractionGuest.ParkingApi(api_client)
    parking_lot_id = 'parking_lot_id_example' # str | 
limit = 50 # int | Limits the results to a specified number, defaults to 50 (optional) (default to 50)
offset = 0 # int | Offsets the results to a specified number, defaults to 0 (optional) (default to 0)

    try:
        # Get stalls of parking lot
        api_response = api_instance.get_parking_stalls(parking_lot_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParkingApi->get_parking_stalls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parking_lot_id** | **str**|  | 
 **limit** | **int**| Limits the results to a specified number, defaults to 50 | [optional] [default to 50]
 **offset** | **int**| Offsets the results to a specified number, defaults to 0 | [optional] [default to 0]

### Return type

[**PaginatedParkingStallsList**](PaginatedParkingStallsList.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

