# TractionGuest.GroupVisitsApi

All URIs are relative to *https://us.tractionguest.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group_visit**](GroupVisitsApi.md#create_group_visit) | **POST** /group_visits | Create a new Group Visit (Appointment)
[**delete_group_visit**](GroupVisitsApi.md#delete_group_visit) | **DELETE** /group_visits/{group_visit_id} | Delete a Group Visit (Appointment)
[**get_group_visit**](GroupVisitsApi.md#get_group_visit) | **GET** /group_visits/{group_visit_id} | Get a Group Visit (Appointment)
[**get_group_visits**](GroupVisitsApi.md#get_group_visits) | **GET** /group_visits | List all Group Visits (Appointments)
[**update_group_visit**](GroupVisitsApi.md#update_group_visit) | **PUT** /group_visits/{group_visit_id} | Update a Group Visit (Appointment)


# **create_group_visit**
> GroupVisit create_group_visit()

Create a new Group Visit (Appointment)

Creates a `GroupVisit` (Appointment)

### Example

```python
import time
import TractionGuest
from TractionGuest.api import group_visits_api
from TractionGuest.model.group_visit_create_params import GroupVisitCreateParams
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.group_visit import GroupVisit
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
    api_instance = group_visits_api.GroupVisitsApi(api_client)
    idempotency_key = "Idempotency-Key_example" # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)
    group_visit_create_params = GroupVisitCreateParams(
        name="name_example",
        start_time="start_time_example",
        end_time="end_time_example",
        location_id=1,
        registration_limit=1,
        manual_registration_approval=True,
        public_registration_enabled=True,
        host_ids=[
            1,
        ],
    ) # GroupVisitCreateParams |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new Group Visit (Appointment)
        api_response = api_instance.create_group_visit(idempotency_key=idempotency_key, group_visit_create_params=group_visit_create_params)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling GroupVisitsApi->create_group_visit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it&#39;s submitted. We store idempotency keys for only 24 hours. Any &#x60;Idempotency-Key&#x60; shorter than 10 characters will be ignored | [optional]
 **group_visit_create_params** | [**GroupVisitCreateParams**](GroupVisitCreateParams.md)|  | [optional]

### Return type

[**GroupVisit**](GroupVisit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created the &#x60;GroupVisit&#x60; |  -  |
**400** | A generic error |  -  |
**401** | You do not have permission to create this |  -  |
**403** | You do not have permission for this action |  -  |
**422** | Your request was not formatted correctly |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_visit**
> delete_group_visit(group_visit_id)

Delete a Group Visit (Appointment)

Deletes a single instance of `GroupVisit` (Appointment).

### Example

```python
import time
import TractionGuest
from TractionGuest.api import group_visits_api
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
    api_instance = group_visits_api.GroupVisitsApi(api_client)
    group_visit_id = "group_visit_id_example" # str | 
    idempotency_key = "Idempotency-Key_example" # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a Group Visit (Appointment)
        api_instance.delete_group_visit(group_visit_id)
    except TractionGuest.ApiException as e:
        print("Exception when calling GroupVisitsApi->delete_group_visit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a Group Visit (Appointment)
        api_instance.delete_group_visit(group_visit_id, idempotency_key=idempotency_key)
    except TractionGuest.ApiException as e:
        print("Exception when calling GroupVisitsApi->delete_group_visit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_visit_id** | **str**|  |
 **idempotency_key** | **str**| An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it&#39;s submitted. We store idempotency keys for only 24 hours. Any &#x60;Idempotency-Key&#x60; shorter than 10 characters will be ignored | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The &#x60;GroupVisit&#x60; has been deleted |  -  |
**400** | There was an error in trying to delete the &#x60;GroupVisit&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_visit**
> GroupVisit get_group_visit(group_visit_id)

Get a Group Visit (Appointment)

Gets the details of a single instance of a `GroupVisit`.

### Example

```python
import time
import TractionGuest
from TractionGuest.api import group_visits_api
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.group_visit import GroupVisit
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
    api_instance = group_visits_api.GroupVisitsApi(api_client)
    group_visit_id = "group_visit_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a Group Visit (Appointment)
        api_response = api_instance.get_group_visit(group_visit_id)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling GroupVisitsApi->get_group_visit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_visit_id** | **str**|  |

### Return type

[**GroupVisit**](GroupVisit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns a single &#x60;GroupVisit&#x60;. |  -  |
**400** | A generic error |  -  |
**401** | You do not have permission to view this GroupVisit |  -  |
**403** | You do not have permission for this action |  -  |
**404** | The GroupVisit does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_visits**
> PaginatedGroupVisitsList get_group_visits()

List all Group Visits (Appointments)

Gets a list of all `GroupVisit` entities (Appointments).

### Example

```python
import time
import TractionGuest
from TractionGuest.api import group_visits_api
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.paginated_group_visits_list import PaginatedGroupVisitsList
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
    api_instance = group_visits_api.GroupVisitsApi(api_client)
    limit = "limit_example" # str | Limits the results to a specified number. Defaults to 50. (optional)
    offset = "offset_example" # str | Offsets the results to a specified number. Defaults to 0. (optional)
    location_ids = "location_ids_example" # str | A comma-separated string of locations IDs, to only show group visits (appointments) from those locations. (optional)
    sort_with = "sort_with_example" # str | A combination of attribute and direction, joined with an underscore, for sorting. Valid attributes are: `created_at`, `updated_at`, `name`, and `start_time`. Valid directions are `asc` and `desc`. E.g., `name_desc`, `start_time_asc`. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all Group Visits (Appointments)
        api_response = api_instance.get_group_visits(limit=limit, offset=offset, location_ids=location_ids, sort_with=sort_with)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling GroupVisitsApi->get_group_visits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Limits the results to a specified number. Defaults to 50. | [optional]
 **offset** | **str**| Offsets the results to a specified number. Defaults to 0. | [optional]
 **location_ids** | **str**| A comma-separated string of locations IDs, to only show group visits (appointments) from those locations. | [optional]
 **sort_with** | **str**| A combination of attribute and direction, joined with an underscore, for sorting. Valid attributes are: &#x60;created_at&#x60;, &#x60;updated_at&#x60;, &#x60;name&#x60;, and &#x60;start_time&#x60;. Valid directions are &#x60;asc&#x60; and &#x60;desc&#x60;. E.g., &#x60;name_desc&#x60;, &#x60;start_time_asc&#x60;. | [optional]

### Return type

[**PaginatedGroupVisitsList**](PaginatedGroupVisitsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array of &#x60;GroupVisit&#x60; entities. |  -  |
**400** | A generic error |  -  |
**401** | You do not have permission to view this |  -  |
**403** | You do not have permission for this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_visit**
> GroupVisit update_group_visit(group_visit_id)

Update a Group Visit (Appointment)

Updates an existing `GroupVisit` (Appointment).

### Example

```python
import time
import TractionGuest
from TractionGuest.api import group_visits_api
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.group_visit import GroupVisit
from TractionGuest.model.group_visit_update_params import GroupVisitUpdateParams
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
    api_instance = group_visits_api.GroupVisitsApi(api_client)
    group_visit_id = "group_visit_id_example" # str | 
    idempotency_key = "Idempotency-Key_example" # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)
    group_visit_update_params = GroupVisitUpdateParams(
        name="name_example",
        start_time="start_time_example",
        end_time="end_time_example",
        location_id=1,
        registration_limit=1,
        manual_registration_approval=True,
        public_registration_enabled=True,
        host_ids=[
            1,
        ],
        invite_ids=[
            1,
        ],
        refresh_registration_url=True,
    ) # GroupVisitUpdateParams |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Group Visit (Appointment)
        api_response = api_instance.update_group_visit(group_visit_id)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling GroupVisitsApi->update_group_visit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Group Visit (Appointment)
        api_response = api_instance.update_group_visit(group_visit_id, idempotency_key=idempotency_key, group_visit_update_params=group_visit_update_params)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling GroupVisitsApi->update_group_visit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_visit_id** | **str**|  |
 **idempotency_key** | **str**| An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it&#39;s submitted. We store idempotency keys for only 24 hours. Any &#x60;Idempotency-Key&#x60; shorter than 10 characters will be ignored | [optional]
 **group_visit_update_params** | [**GroupVisitUpdateParams**](GroupVisitUpdateParams.md)|  | [optional]

### Return type

[**GroupVisit**](GroupVisit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful response |  -  |
**400** | A generic error |  -  |
**401** | You do not have permission to view this GroupVisit |  -  |
**403** | You do not have permission for this action |  -  |
**404** | The GroupVisit does not exist |  -  |
**422** | Your request was not formatted correctly |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

