# TractionGuest.HostsApi

All URIs are relative to *https://tractionguest.ca/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_host**](HostsApi.md#create_host) | **POST** /hosts | Create a Host
[**create_hosts**](HostsApi.md#create_hosts) | **POST** /hosts/batch | Create multiple Hosts
[**get_hosts**](HostsApi.md#get_hosts) | **GET** /hosts | List all Hosts


# **create_host**
> Host create_host(host_create_params, idempotency_key=idempotency_key)

Create a Host

Creates a Host

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
    api_instance = TractionGuest.HostsApi(api_client)
    host_create_params = TractionGuest.HostCreateParams() # HostCreateParams | 
idempotency_key = 'idempotency_key_example' # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    try:
        # Create a Host
        api_response = api_instance.create_host(host_create_params, idempotency_key=idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HostsApi->create_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_create_params** | [**HostCreateParams**](HostCreateParams.md)|  | 
 **idempotency_key** | **str**| An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it&#39;s submitted. We store idempotency keys for only 24 hours. Any &#x60;Idempotency-Key&#x60; shorter than 10 characters will be ignored | [optional] 

### Return type

[**Host**](Host.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hosts**
> BatchJob create_hosts(idempotency_key=idempotency_key, host_batch_create_params=host_batch_create_params)

Create multiple Hosts

Creates a batch of `Host` records in an async queue. Please note, every action taken against this endpoint is recorded in the audit log.

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
    api_instance = TractionGuest.HostsApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)
host_batch_create_params = TractionGuest.HostBatchCreateParams() # HostBatchCreateParams |  (optional)

    try:
        # Create multiple Hosts
        api_response = api_instance.create_hosts(idempotency_key=idempotency_key, host_batch_create_params=host_batch_create_params)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HostsApi->create_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it&#39;s submitted. We store idempotency keys for only 24 hours. Any &#x60;Idempotency-Key&#x60; shorter than 10 characters will be ignored | [optional] 
 **host_batch_create_params** | [**HostBatchCreateParams**](HostBatchCreateParams.md)|  | [optional] 

### Return type

[**BatchJob**](BatchJob.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hosts**
> PaginatedHostsList get_hosts(query=query, limit=limit, offset=offset, include=include)

List all Hosts

Gets a list of all `Host` entities.

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
    api_instance = TractionGuest.HostsApi(api_client)
    query = 'query_example' # str | Will filter by `first_name`, `last_name`, and `email` (optional)
limit = 56 # int | Limits the results to a specified number, defaults to 50 (optional)
offset = 56 # int | Offsets the results to a specified number, defaults to 0 (optional)
include = 'include_example' # str | A list of comma-separated related models to include (optional)

    try:
        # List all Hosts
        api_response = api_instance.get_hosts(query=query, limit=limit, offset=offset, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HostsApi->get_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Will filter by &#x60;first_name&#x60;, &#x60;last_name&#x60;, and &#x60;email&#x60; | [optional] 
 **limit** | **int**| Limits the results to a specified number, defaults to 50 | [optional] 
 **offset** | **int**| Offsets the results to a specified number, defaults to 0 | [optional] 
 **include** | **str**| A list of comma-separated related models to include | [optional] 

### Return type

[**PaginatedHostsList**](PaginatedHostsList.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array of &#x60;Host&#x60; entities. |  -  |
**400** | A generic error |  -  |
**401** | You don&#39;t have permission to view these Hosts |  -  |
**403** | You do not have permission for this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

