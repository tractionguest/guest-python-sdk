# TractionGuest.BatchesApi

All URIs are relative to *https://us.tractionguest.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_delete_invites**](BatchesApi.md#batch_delete_invites) | **POST** /invites/batch_delete | Delete Multiple Invites
[**get_batch**](BatchesApi.md#get_batch) | **GET** /batches/{batch_id} | Get a BatchJob


# **batch_delete_invites**
> BatchJob batch_delete_invites(identifier_list=identifier_list)

Delete Multiple Invites

Queues up a \"delete\" background task for one or more `Invite` entities.

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
    api_instance = TractionGuest.BatchesApi(api_client)
    identifier_list = TractionGuest.IdentifierList() # IdentifierList |  (optional)

    try:
        # Delete Multiple Invites
        api_response = api_instance.batch_delete_invites(identifier_list=identifier_list)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchesApi->batch_delete_invites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_list** | [**IdentifierList**](IdentifierList.md)|  | [optional] 

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
**4XX** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch**
> BatchJob get_batch(batch_id)

Get a BatchJob

Retrieve a given `BatchJob` entity.

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
    api_instance = TractionGuest.BatchesApi(api_client)
    batch_id = 'batch_id_example' # str | 

    try:
        # Get a BatchJob
        api_response = api_instance.get_batch(batch_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchesApi->get_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**|  | 

### Return type

[**BatchJob**](BatchJob.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

