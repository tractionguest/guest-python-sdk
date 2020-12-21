# TractionGuest.SigninsApi

All URIs are relative to *https://us.tractionguest.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_signin**](SigninsApi.md#create_signin) | **POST** /signins | Create Signin
[**get_signin**](SigninsApi.md#get_signin) | **GET** /signins/{signin_id} | Get a Signin
[**get_signins**](SigninsApi.md#get_signins) | **GET** /signins | List all Signins
[**update_signin**](SigninsApi.md#update_signin) | **PUT** /signins/{signin_id} | Update a Signin


# **create_signin**
> Signin create_signin(signin_create_params=signin_create_params)

Create Signin

Creates a Signin

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
    api_instance = TractionGuest.SigninsApi(api_client)
    signin_create_params = {"guest_email_template_id":47,"host_email_template_id":65,"host_ids":[77,49],"location_id":79,"send_notifications":true,"photos":[{},{}],"sms_message":"some text","first_name":"some text","last_name":"some text","company":"some text","email":"some text"} # SigninCreateParams | Params for creating a Signin can omit certain fields if a `registration_id` is present. (optional)

    try:
        # Create Signin
        api_response = api_instance.create_signin(signin_create_params=signin_create_params)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SigninsApi->create_signin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signin_create_params** | [**SigninCreateParams**](SigninCreateParams.md)| Params for creating a Signin can omit certain fields if a &#x60;registration_id&#x60; is present. | [optional] 

### Return type

[**Signin**](Signin.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity (WebDAV) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signin**
> SigninDetail get_signin(signin_id, include=include)

Get a Signin

Gets the details of a single instance of a `Signin`.

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
    api_instance = TractionGuest.SigninsApi(api_client)
    signin_id = 'signin_id_example' # str | 
include = 'include_example' # str | A list of comma-separated related models to include (optional)

    try:
        # Get a Signin
        api_response = api_instance.get_signin(signin_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SigninsApi->get_signin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signin_id** | **str**|  | 
 **include** | **str**| A list of comma-separated related models to include | [optional] 

### Return type

[**SigninDetail**](SigninDetail.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns a single &#x60;Signin&#x60;. |  -  |
**400** | A generic error |  -  |
**401** | You don&#39;t have permission to view this Signin |  -  |
**403** | You do not have permission for this action |  -  |
**404** | The Signin does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signins**
> PaginatedSigninsList get_signins(location_ids=location_ids, with_colours=with_colours, query=query, with_acknowledged=with_acknowledged, with_signed_in=with_signed_in, signin_before=signin_before, signin_after=signin_after, limit=limit, offset=offset, query_sort=query_sort, include=include)

List all Signins

Gets a list of all `Signin` entities.

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
    api_instance = TractionGuest.SigninsApi(api_client)
    location_ids = 'location_ids_example' # str | A comma separated list of Location IDs (optional)
with_colours = 'with_colours_example' # str | A comma separated list of case-insensitive colour values. i.e., `red`, `green`, `yellow`, and `orange` (optional)
query = 'query_example' # str | Allows you to query by `company`, `email`, `first_name`, `last_name`, and `location_name` (optional)
with_acknowledged = True # bool | Filters to all those `Signin`s that have, or have not been acknowledged (optional)
with_signed_in = True # bool | Filters to all `Signin`s that are, or are not currently signed out. (optional)
signin_before = '2013-10-20' # date | Filters results to all those *before* the provided datetime (optional)
signin_after = '2013-10-20' # date | Filters results to all those *after* the provided datetime (optional)
limit = 56 # int | Limits the results to a specified number, defaults to 50 (optional)
offset = 56 # int | Offsets the results to a specified number, defaults to 0 (optional)
query_sort = 'query_sort_example' # str | Allows you to override ordering by most relevant results when querying (optional)
include = 'include_example' # str | A list of comma-separated related models to include (optional)

    try:
        # List all Signins
        api_response = api_instance.get_signins(location_ids=location_ids, with_colours=with_colours, query=query, with_acknowledged=with_acknowledged, with_signed_in=with_signed_in, signin_before=signin_before, signin_after=signin_after, limit=limit, offset=offset, query_sort=query_sort, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SigninsApi->get_signins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_ids** | **str**| A comma separated list of Location IDs | [optional] 
 **with_colours** | **str**| A comma separated list of case-insensitive colour values. i.e., &#x60;red&#x60;, &#x60;green&#x60;, &#x60;yellow&#x60;, and &#x60;orange&#x60; | [optional] 
 **query** | **str**| Allows you to query by &#x60;company&#x60;, &#x60;email&#x60;, &#x60;first_name&#x60;, &#x60;last_name&#x60;, and &#x60;location_name&#x60; | [optional] 
 **with_acknowledged** | **bool**| Filters to all those &#x60;Signin&#x60;s that have, or have not been acknowledged | [optional] 
 **with_signed_in** | **bool**| Filters to all &#x60;Signin&#x60;s that are, or are not currently signed out. | [optional] 
 **signin_before** | **date**| Filters results to all those *before* the provided datetime | [optional] 
 **signin_after** | **date**| Filters results to all those *after* the provided datetime | [optional] 
 **limit** | **int**| Limits the results to a specified number, defaults to 50 | [optional] 
 **offset** | **int**| Offsets the results to a specified number, defaults to 0 | [optional] 
 **query_sort** | **str**| Allows you to override ordering by most relevant results when querying | [optional] 
 **include** | **str**| A list of comma-separated related models to include | [optional] 

### Return type

[**PaginatedSigninsList**](PaginatedSigninsList.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array of &#x60;Signin&#x60; entities. |  -  |
**400** | A generic error |  -  |
**401** | You don&#39;t have permission to view these Signins |  -  |
**403** | You do not have permission for this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_signin**
> SigninDetail update_signin(signin_id, signin_update_params, idempotency_key=idempotency_key)

Update a Signin

Update, acknowledge, or `Signout` a `Signin`

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
    api_instance = TractionGuest.SigninsApi(api_client)
    signin_id = 'signin_id_example' # str | 
signin_update_params = {"is_signed_out":true,"is_acknowledged":true,"is_accounted_for":true} # SigninUpdateParams | The only updatable values for a `Signin` are `badge_number`, `badge_returned`, `is_accounted_for`, `is_signed_out`, and `is_acknowledged`.  `is_signed_out` and `is_acknowledged` are pseudo attributes that once set to true, are irreversible.
idempotency_key = 'idempotency_key_example' # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    try:
        # Update a Signin
        api_response = api_instance.update_signin(signin_id, signin_update_params, idempotency_key=idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SigninsApi->update_signin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signin_id** | **str**|  | 
 **signin_update_params** | [**SigninUpdateParams**](SigninUpdateParams.md)| The only updatable values for a &#x60;Signin&#x60; are &#x60;badge_number&#x60;, &#x60;badge_returned&#x60;, &#x60;is_accounted_for&#x60;, &#x60;is_signed_out&#x60;, and &#x60;is_acknowledged&#x60;.  &#x60;is_signed_out&#x60; and &#x60;is_acknowledged&#x60; are pseudo attributes that once set to true, are irreversible. | 
 **idempotency_key** | **str**| An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it&#39;s submitted. We store idempotency keys for only 24 hours. Any &#x60;Idempotency-Key&#x60; shorter than 10 characters will be ignored | [optional] 

### Return type

[**SigninDetail**](SigninDetail.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Signin has been acknowledged, or signed out. |  -  |
**400** | A generic error |  -  |
**401** | You don&#39;t have permission to update this Signin |  -  |
**403** | You do not have permission for this action |  -  |
**404** | The Signin does not exist |  -  |
**422** | Your request was not formatted correctly |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

