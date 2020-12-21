# TractionGuest.UsersApi

All URIs are relative to *https://us.tractionguest.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_user**](UsersApi.md#get_current_user) | **GET** /users/{user_id} | Get the current User


# **get_current_user**
> User get_current_user(user_id, include=include)

Get the current User

Gets the details of a single instance of the current `User`.

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
    api_instance = TractionGuest.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
include = 'include_example' # str | A list of comma-separated related models to include (optional)

    try:
        # Get the current User
        api_response = api_instance.get_current_user(user_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->get_current_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **include** | **str**| A list of comma-separated related models to include | [optional] 

### Return type

[**User**](User.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns a single &#x60;User&#x60;. |  -  |
**400** | A generic error |  -  |
**401** | You don&#39;t have permission to view this User |  -  |
**403** | You do not have permission for this action |  -  |
**404** | The User does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

