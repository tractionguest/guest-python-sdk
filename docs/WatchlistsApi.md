# TractionGuest.WatchlistsApi

All URIs are relative to *https://us.tractionguest.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_watchlist**](WatchlistsApi.md#create_watchlist) | **POST** /watchlists | Create Watchlist
[**delete_watchlist**](WatchlistsApi.md#delete_watchlist) | **DELETE** /watchlists/{watchlist_id} | Deletes a Watchlist
[**get_watchlist**](WatchlistsApi.md#get_watchlist) | **GET** /watchlists/{watchlist_id} | Get a Watchlist
[**get_watchlists**](WatchlistsApi.md#get_watchlists) | **GET** /watchlists | List all Watchlists
[**update_watchlist**](WatchlistsApi.md#update_watchlist) | **PUT** /watchlists/{watchlist_id} | Update a Watchlist


# **create_watchlist**
> Watchlist create_watchlist(watchlist_create_params, idempotency_key=idempotency_key)

Create Watchlist

Create a new `Watchlist` record. Please note, every action taken against this endpoint is recorded in the audit log.

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
    api_instance = TractionGuest.WatchlistsApi(api_client)
    watchlist_create_params = TractionGuest.WatchlistCreateParams() # WatchlistCreateParams | 
idempotency_key = 'idempotency_key_example' # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    try:
        # Create Watchlist
        api_response = api_instance.create_watchlist(watchlist_create_params, idempotency_key=idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WatchlistsApi->create_watchlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_create_params** | [**WatchlistCreateParams**](WatchlistCreateParams.md)|  | 
 **idempotency_key** | **str**| An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it&#39;s submitted. We store idempotency keys for only 24 hours. Any &#x60;Idempotency-Key&#x60; shorter than 10 characters will be ignored | [optional] 

### Return type

[**Watchlist**](Watchlist.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created &#x60;Watchlist&#x60; |  -  |
**4XX** | An error happened |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_watchlist**
> delete_watchlist(watchlist_id, idempotency_key=idempotency_key)

Deletes a Watchlist

Deletes a single instance of `Watchlist`

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
    api_instance = TractionGuest.WatchlistsApi(api_client)
    watchlist_id = 'watchlist_id_example' # str | 
idempotency_key = 'idempotency_key_example' # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    try:
        # Deletes a Watchlist
        api_instance.delete_watchlist(watchlist_id, idempotency_key=idempotency_key)
    except ApiException as e:
        print("Exception when calling WatchlistsApi->delete_watchlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_id** | **str**|  | 
 **idempotency_key** | **str**| An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it&#39;s submitted. We store idempotency keys for only 24 hours. Any &#x60;Idempotency-Key&#x60; shorter than 10 characters will be ignored | [optional] 

### Return type

void (empty response body)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The Watchlist has been deleted |  -  |
**4XX** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_watchlist**
> object get_watchlist(watchlist_id, include=include)

Get a Watchlist

Gets the details of a single instance of a `Watchlist`.

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
    api_instance = TractionGuest.WatchlistsApi(api_client)
    watchlist_id = 'watchlist_id_example' # str | 
include = 'include_example' # str | A list of comma-separated related models to include (optional)

    try:
        # Get a Watchlist
        api_response = api_instance.get_watchlist(watchlist_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WatchlistsApi->get_watchlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_id** | **str**|  | 
 **include** | **str**| A list of comma-separated related models to include | [optional] 

### Return type

**object**

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns a single &#x60;Watchlist&#x60;. |  -  |
**4XX** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_watchlists**
> PaginatedWatchlistList get_watchlists(limit=limit, offset=offset, query=query, with_colours=with_colours, include=include)

List all Watchlists

Gets a list of all `Watchlist` entities.

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
    api_instance = TractionGuest.WatchlistsApi(api_client)
    limit = 56 # int | Limits the results to a specified number, defaults to 50 (optional)
offset = 56 # int | Offsets the results to a specified number, defaults to 0 (optional)
query = 'query_example' # str | Query the results by `first_name`, `last_name`, `email`, `colour`, and `notes` all at once. (optional)
with_colours = 'with_colours_example' # str | A comma separated list of case-insensitive colour values. i.e., `red`, `green`, `yellow`, and `orange` (optional)
include = 'include_example' # str | A list of comma-separated related models to include (optional)

    try:
        # List all Watchlists
        api_response = api_instance.get_watchlists(limit=limit, offset=offset, query=query, with_colours=with_colours, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WatchlistsApi->get_watchlists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the results to a specified number, defaults to 50 | [optional] 
 **offset** | **int**| Offsets the results to a specified number, defaults to 0 | [optional] 
 **query** | **str**| Query the results by &#x60;first_name&#x60;, &#x60;last_name&#x60;, &#x60;email&#x60;, &#x60;colour&#x60;, and &#x60;notes&#x60; all at once. | [optional] 
 **with_colours** | **str**| A comma separated list of case-insensitive colour values. i.e., &#x60;red&#x60;, &#x60;green&#x60;, &#x60;yellow&#x60;, and &#x60;orange&#x60; | [optional] 
 **include** | **str**| A list of comma-separated related models to include | [optional] 

### Return type

[**PaginatedWatchlistList**](PaginatedWatchlistList.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array of &#x60;Watchlist&#x60; entities. |  -  |
**4XX** | A generic error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_watchlist**
> object update_watchlist(watchlist_id, body, idempotency_key=idempotency_key)

Update a Watchlist

Update an existing `Watchlist` record. Every operation against this endpoint is recorded in the audit log.

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
    api_instance = TractionGuest.WatchlistsApi(api_client)
    watchlist_id = 'watchlist_id_example' # str | 
body = {"colour":"YELLOW","email":"some text","first_name":"some text","last_name":"some text","notes":"some text","aliases":["some text","some text"]} # object | The watchlist record attributes to update
idempotency_key = 'idempotency_key_example' # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    try:
        # Update a Watchlist
        api_response = api_instance.update_watchlist(watchlist_id, body, idempotency_key=idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WatchlistsApi->update_watchlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_id** | **str**|  | 
 **body** | **object**| The watchlist record attributes to update | 
 **idempotency_key** | **str**| An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it&#39;s submitted. We store idempotency keys for only 24 hours. Any &#x60;Idempotency-Key&#x60; shorter than 10 characters will be ignored | [optional] 

### Return type

**object**

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The complete updated watchlist record |  -  |
**4XX** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

