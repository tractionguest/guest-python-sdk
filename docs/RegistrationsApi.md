# TractionGuest.RegistrationsApi

All URIs are relative to *https://us.tractionguest.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_registration**](RegistrationsApi.md#get_registration) | **GET** /registrations/{registration_id} | Get a Registration
[**get_registrations**](RegistrationsApi.md#get_registrations) | **GET** /registrations | List all Registrations


# **get_registration**
> RegistrationDetail get_registration(registration_id)

Get a Registration

Gets the details of a single instance of a `Registration`

### Example

```python
import time
import TractionGuest
from TractionGuest.api import registrations_api
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.registration_detail import RegistrationDetail
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
    api_instance = registrations_api.RegistrationsApi(api_client)
    registration_id = "registration_id_example" # str | 
    include = "include_example" # str | A list of comma-separated related models to include (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a Registration
        api_response = api_instance.get_registration(registration_id)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling RegistrationsApi->get_registration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a Registration
        api_response = api_instance.get_registration(registration_id, include=include)
        pprint(api_response)
    except TractionGuest.ApiException as e:
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

No authorization required

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
> PaginatedRegistrationsList get_registrations()

List all Registrations

Gets a list of all `Registration` entities.

### Example

```python
import time
import TractionGuest
from TractionGuest.api import registrations_api
from TractionGuest.model.paginated_registrations_list import PaginatedRegistrationsList
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
    api_instance = registrations_api.RegistrationsApi(api_client)
    limit = 1 # int | Limits the results to a specified number, defaults to 50 (optional)
    offset = 1 # int | Offsets the results to a specified number, defaults to 0 (optional)
    location_ids = "location_ids_example" # str | A comma separated list of Location IDs (optional)
    created_before = "created_before_example" # str | Restricts results to only those that were created before the provided date (optional)
    created_after = "created_after_example" # str | Restricts results to only those that were created after the provided date (optional)
    needs_confirmation = True # bool | A confirmed `Registration` is one with an associated `Invite`. This filter returns those without an `Invite` when true, and those with an `Invite` when false. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all Registrations
        api_response = api_instance.get_registrations(limit=limit, offset=offset, location_ids=location_ids, created_before=created_before, created_after=created_after, needs_confirmation=needs_confirmation)
        pprint(api_response)
    except TractionGuest.ApiException as e:
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
 **needs_confirmation** | **bool**| A confirmed &#x60;Registration&#x60; is one with an associated &#x60;Invite&#x60;. This filter returns those without an &#x60;Invite&#x60; when true, and those with an &#x60;Invite&#x60; when false. | [optional]

### Return type

[**PaginatedRegistrationsList**](PaginatedRegistrationsList.md)

### Authorization

No authorization required

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

