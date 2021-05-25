# TractionGuest.UsersApi

All URIs are relative to *https://us.tractionguest.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_user**](UsersApi.md#get_current_user) | **GET** /users/{user_id} | Get the current User


# **get_current_user**
> User get_current_user(user_id)

Get the current User

Gets the details of a single instance of the current `User`.

### Example

```python
import time
import TractionGuest
from TractionGuest.api import users_api
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.user import User
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "user_id_example" # str | 
    include = "include_example" # str | A list of comma-separated related models to include (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the current User
        api_response = api_instance.get_current_user(user_id)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling UsersApi->get_current_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the current User
        api_response = api_instance.get_current_user(user_id, include=include)
        pprint(api_response)
    except TractionGuest.ApiException as e:
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

No authorization required

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

