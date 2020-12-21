# TractionGuest.RegistrationsApi

All URIs are relative to *https://us.tractionguest.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_registration**](RegistrationsApi.md#get_registration) | **GET** /registrations/{registration_id} | Get a Registration
[**get_registrations**](RegistrationsApi.md#get_registrations) | **GET** /registrations | List all Registrations


# **get_registration**
> RegistrationDetail get_registration(registration_id, include=include)

Get a Registration

Gets the details of a single instance of a `Registration`

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
    api_instance = TractionGuest.RegistrationsApi(api_client)
    registration_id = 'registration_id_example' # str | 
include = 'include_example' # str | A list of comma-separated related models to include (optional)

    try:
        # Get a Registration
        api_response = api_instance.get_registration(registration_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RegistrationsApi->get_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**|  | 
 **include** | **str**| A list of comma-separated related models to include | [optional] 

### Return type

[**RegistrationDetail**](RegistrationDetail.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns a single &#x60;RegistrationDetail&#x60;. |  -  |
**400** | A generic error |  -  |
**403** | You do not have permission for this action |  -  |
**404** | The specified Registration was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registrations**
> PaginatedRegistrationsList get_registrations(limit=limit, offset=offset, location_ids=location_ids, created_before=created_before, created_after=created_after)

List all Registrations

Gets a list of all `Registration` entities.

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
    api_instance = TractionGuest.RegistrationsApi(api_client)
    limit = 56 # int | Limits the results to a specified number, defaults to 50 (optional)
offset = 56 # int | Offsets the results to a specified number, defaults to 0 (optional)
location_ids = 'location_ids_example' # str | A comma separated list of Location IDs (optional)
created_before = 'created_before_example' # str | Restricts results to only those that were created before the provided date (optional)
created_after = 'created_after_example' # str | Restricts results to only those that were created after the provided date (optional)

    try:
        # List all Registrations
        api_response = api_instance.get_registrations(limit=limit, offset=offset, location_ids=location_ids, created_before=created_before, created_after=created_after)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RegistrationsApi->get_registrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the results to a specified number, defaults to 50 | [optional] 
 **offset** | **int**| Offsets the results to a specified number, defaults to 0 | [optional] 
 **location_ids** | **str**| A comma separated list of Location IDs | [optional] 
 **created_before** | **str**| Restricts results to only those that were created before the provided date | [optional] 
 **created_after** | **str**| Restricts results to only those that were created after the provided date | [optional] 

### Return type

[**PaginatedRegistrationsList**](PaginatedRegistrationsList.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

