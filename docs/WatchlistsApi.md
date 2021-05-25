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
> Watchlist create_watchlist(watchlist_create_params)

Create Watchlist

Create a new `Watchlist` record. Please note, every action taken against this endpoint is recorded in the audit log.

### Example

```python
import time
import TractionGuest
from TractionGuest.api import watchlists_api
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.watchlist_create_params import WatchlistCreateParams
from TractionGuest.model.watchlist import Watchlist
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
    api_instance = watchlists_api.WatchlistsApi(api_client)
    watchlist_create_params = WatchlistCreateParams(
        aliases=[
            "aliases_example",
        ],
        notes="notes_example",
        last_name="last_name_example",
        first_name="first_name_example",
        email="email_example",
        colour="RED",
    ) # WatchlistCreateParams | The new `Watchlist` to create
    idempotency_key = "Idempotency-Key_example" # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Watchlist
        api_response = api_instance.create_watchlist(watchlist_create_params)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling WatchlistsApi->create_watchlist: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Watchlist
        api_response = api_instance.create_watchlist(watchlist_create_params, idempotency_key=idempotency_key)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling WatchlistsApi->create_watchlist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_create_params** | [**WatchlistCreateParams**](WatchlistCreateParams.md)| The new &#x60;Watchlist&#x60; to create |
 **idempotency_key** | **str**| An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it&#39;s submitted. We store idempotency keys for only 24 hours. Any &#x60;Idempotency-Key&#x60; shorter than 10 characters will be ignored | [optional]

### Return type

[**Watchlist**](Watchlist.md)

### Authorization

No authorization required

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
> delete_watchlist(watchlist_id)

Deletes a Watchlist

Deletes a single instance of `Watchlist`

### Example

```python
import time
import TractionGuest
from TractionGuest.api import watchlists_api
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
    api_instance = watchlists_api.WatchlistsApi(api_client)
    watchlist_id = "watchlist_id_example" # str | 
    idempotency_key = "Idempotency-Key_example" # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes a Watchlist
        api_instance.delete_watchlist(watchlist_id)
    except TractionGuest.ApiException as e:
        print("Exception when calling WatchlistsApi->delete_watchlist: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes a Watchlist
        api_instance.delete_watchlist(watchlist_id, idempotency_key=idempotency_key)
    except TractionGuest.ApiException as e:
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

No authorization required

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
> Watchlist get_watchlist(watchlist_id)

Get a Watchlist

Gets the details of a single instance of a `Watchlist`.

### Example

```python
import time
import TractionGuest
from TractionGuest.api import watchlists_api
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.watchlist import Watchlist
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
    api_instance = watchlists_api.WatchlistsApi(api_client)
    watchlist_id = "watchlist_id_example" # str | 
    include = "include_example" # str | A list of comma-separated related models to include (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a Watchlist
        api_response = api_instance.get_watchlist(watchlist_id)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling WatchlistsApi->get_watchlist: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a Watchlist
        api_response = api_instance.get_watchlist(watchlist_id, include=include)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling WatchlistsApi->get_watchlist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_id** | **str**|  |
 **include** | **str**| A list of comma-separated related models to include | [optional]

### Return type

[**Watchlist**](Watchlist.md)

### Authorization

No authorization required

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
> PaginatedWatchlistList get_watchlists()

List all Watchlists

Gets a list of all `Watchlist` entities.

### Example

```python
import time
import TractionGuest
from TractionGuest.api import watchlists_api
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.paginated_watchlist_list import PaginatedWatchlistList
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
    api_instance = watchlists_api.WatchlistsApi(api_client)
    limit = 1 # int | Limits the results to a specified number, defaults to 50 (optional)
    offset = 1 # int | Offsets the results to a specified number, defaults to 0 (optional)
    query = "query_example" # str | Query the results by `first_name`, `last_name`, `email`, `colour`, and `notes` all at once. (optional)
    with_colours = "with_colours_example" # str | A comma separated list of case-insensitive colour values. i.e., `red`, `green`, `yellow`, and `orange` (optional)
    include = "include_example" # str | A list of comma-separated related models to include (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all Watchlists
        api_response = api_instance.get_watchlists(limit=limit, offset=offset, query=query, with_colours=with_colours, include=include)
        pprint(api_response)
    except TractionGuest.ApiException as e:
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

No authorization required

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
> Watchlist update_watchlist(watchlist_id, watchlist_create_params)

Update a Watchlist

Update an existing `Watchlist` record. Every operation against this endpoint is recorded in the audit log.

### Example

```python
import time
import TractionGuest
from TractionGuest.api import watchlists_api
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.watchlist_create_params import WatchlistCreateParams
from TractionGuest.model.watchlist import Watchlist
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
    api_instance = watchlists_api.WatchlistsApi(api_client)
    watchlist_id = "watchlist_id_example" # str | 
    watchlist_create_params = WatchlistCreateParams(
        aliases=[
            "aliases_example",
        ],
        notes="notes_example",
        last_name="last_name_example",
        first_name="first_name_example",
        email="email_example",
        colour="RED",
    ) # WatchlistCreateParams | The watchlist record attributes to update
    idempotency_key = "Idempotency-Key_example" # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Watchlist
        api_response = api_instance.update_watchlist(watchlist_id, watchlist_create_params)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling WatchlistsApi->update_watchlist: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Watchlist
        api_response = api_instance.update_watchlist(watchlist_id, watchlist_create_params, idempotency_key=idempotency_key)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling WatchlistsApi->update_watchlist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_id** | **str**|  |
 **watchlist_create_params** | [**WatchlistCreateParams**](WatchlistCreateParams.md)| The watchlist record attributes to update |
 **idempotency_key** | **str**| An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it&#39;s submitted. We store idempotency keys for only 24 hours. Any &#x60;Idempotency-Key&#x60; shorter than 10 characters will be ignored | [optional]

### Return type

[**Watchlist**](Watchlist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The complete updated watchlist record |  -  |
**4XX** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

