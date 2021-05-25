# TractionGuest.LocationsApi

All URIs are relative to *https://us.tractionguest.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_location**](LocationsApi.md#get_location) | **GET** /locations/{location_id} | Get the details of a location
[**get_locations**](LocationsApi.md#get_locations) | **GET** /locations | List all Locations


# **get_location**
> Location get_location(location_id)

Get the details of a location

Gets details of a single instance of `Location`.

### Example

```python
import time
import TractionGuest
from TractionGuest.api import locations_api
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.location import Location
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
    api_instance = locations_api.LocationsApi(api_client)
    location_id = "location_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the details of a location
        api_response = api_instance.get_location(location_id)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling LocationsApi->get_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  |

### Return type

[**Location**](Location.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns a single &#x60;Location&#x60;. |  -  |
**400** | A generic error |  -  |
**401** | You don&#39;t have permission to view this Location |  -  |
**403** | You do not have permission for this action |  -  |
**404** | The Location does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locations**
> PaginatedLocationsList get_locations()

List all Locations

Gets a list of all `Location` entities.

### Example

```python
import time
import TractionGuest
from TractionGuest.api import locations_api
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.paginated_locations_list import PaginatedLocationsList
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
    api_instance = locations_api.LocationsApi(api_client)
    limit = 1 # int | Limits the results to a specified number, defaults to 50 (optional)
    offset = 1 # int | Offsets the results to a specified number, defaults to 0 (optional)
    query = "query_example" # str | Queries by Location `name` (optional)
    include = "include_example" # str | A list of comma-separated related models to include (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all Locations
        api_response = api_instance.get_locations(limit=limit, offset=offset, query=query, include=include)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling LocationsApi->get_locations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the results to a specified number, defaults to 50 | [optional]
 **offset** | **int**| Offsets the results to a specified number, defaults to 0 | [optional]
 **query** | **str**| Queries by Location &#x60;name&#x60; | [optional]
 **include** | **str**| A list of comma-separated related models to include | [optional]

### Return type

[**PaginatedLocationsList**](PaginatedLocationsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array of &#x60;Location&#x60; entities. |  -  |
**400** | A generic error |  -  |
**401** | You don&#39;t have permission to view these Locations |  -  |
**403** | You do not have permission for this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

