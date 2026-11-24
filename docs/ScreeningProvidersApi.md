# TractionGuest.ScreeningProvidersApi

All URIs are relative to *https://us.tractionguest.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_screening_provider**](ScreeningProvidersApi.md#create_screening_provider) | **POST** /screening_providers | Connect a ScreeningProvider
[**delete_screening_provider**](ScreeningProvidersApi.md#delete_screening_provider) | **DELETE** /screening_providers/{screening_provider_id} | Disconnect a ScreeningProvider
[**get_screening_provider**](ScreeningProvidersApi.md#get_screening_provider) | **GET** /screening_providers/{screening_provider_id} | Get a ScreeningProvider
[**get_screening_providers**](ScreeningProvidersApi.md#get_screening_providers) | **GET** /screening_providers | List all ScreeningProviders
[**get_screening_providers_usage**](ScreeningProvidersApi.md#get_screening_providers_usage) | **GET** /screening_providers/usage | Read ScreeningProvider credit usage
[**update_screening_provider**](ScreeningProvidersApi.md#update_screening_provider) | **PUT** /screening_providers/{screening_provider_id} | Update a ScreeningProvider


# **create_screening_provider**
> ScreeningProvider create_screening_provider(screening_provider_create_params, idempotency_key=idempotency_key)

Connect a ScreeningProvider

Connects a `ScreeningProvider` by creating the integration with its settings. Only the supported screening provider `type_id` values are accepted.

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
    api_instance = TractionGuest.ScreeningProvidersApi(api_client)
    screening_provider_create_params = {"type_id":3,"integration_settings":[{"field_name":"username","field_value":"vc-user"},{"field_name":"password","field_value":"vc-secret"}]} # ScreeningProviderCreateParams | The `ScreeningProvider` to connect
idempotency_key = 'idempotency_key_example' # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    try:
        # Connect a ScreeningProvider
        api_response = api_instance.create_screening_provider(screening_provider_create_params, idempotency_key=idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScreeningProvidersApi->create_screening_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screening_provider_create_params** | [**ScreeningProviderCreateParams**](ScreeningProviderCreateParams.md)| The &#x60;ScreeningProvider&#x60; to connect | 
 **idempotency_key** | **str**| An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it&#39;s submitted. We store idempotency keys for only 24 hours. Any &#x60;Idempotency-Key&#x60; shorter than 10 characters will be ignored | [optional] 

### Return type

[**ScreeningProvider**](ScreeningProvider.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly connected &#x60;ScreeningProvider&#x60; |  -  |
**4XX** | An error happened. A &#x60;type_id&#x60; outside the supported screening providers is rejected with a not-found error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_screening_provider**
> delete_screening_provider(screening_provider_id, idempotency_key=idempotency_key)

Disconnect a ScreeningProvider

Disconnects a `ScreeningProvider`, removing the integration and its settings.

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
    api_instance = TractionGuest.ScreeningProvidersApi(api_client)
    screening_provider_id = 'screening_provider_id_example' # str | 
idempotency_key = 'idempotency_key_example' # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    try:
        # Disconnect a ScreeningProvider
        api_instance.delete_screening_provider(screening_provider_id, idempotency_key=idempotency_key)
    except ApiException as e:
        print("Exception when calling ScreeningProvidersApi->delete_screening_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screening_provider_id** | **str**|  | 
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
**204** | The ScreeningProvider has been disconnected |  -  |
**4XX** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screening_provider**
> ScreeningProvider get_screening_provider(screening_provider_id)

Get a ScreeningProvider

Gets the details of a single instance of a `ScreeningProvider`.

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
    api_instance = TractionGuest.ScreeningProvidersApi(api_client)
    screening_provider_id = 'screening_provider_id_example' # str | 

    try:
        # Get a ScreeningProvider
        api_response = api_instance.get_screening_provider(screening_provider_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScreeningProvidersApi->get_screening_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screening_provider_id** | **str**|  | 

### Return type

[**ScreeningProvider**](ScreeningProvider.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns a single &#x60;ScreeningProvider&#x60;. |  -  |
**4XX** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screening_providers**
> PaginatedScreeningProvidersList get_screening_providers(limit=limit, offset=offset)

List all ScreeningProviders

Gets a list of the account's connected `ScreeningProvider` entities.

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
    api_instance = TractionGuest.ScreeningProvidersApi(api_client)
    limit = 56 # int | Limits the results to a specified number, defaults to 50 (optional)
offset = 56 # int | Offsets the results to a specified number, defaults to 0 (optional)

    try:
        # List all ScreeningProviders
        api_response = api_instance.get_screening_providers(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScreeningProvidersApi->get_screening_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the results to a specified number, defaults to 50 | [optional] 
 **offset** | **int**| Offsets the results to a specified number, defaults to 0 | [optional] 

### Return type

[**PaginatedScreeningProvidersList**](PaginatedScreeningProvidersList.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array of &#x60;ScreeningProvider&#x60; entities. |  -  |
**4XX** | A generic error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screening_providers_usage**
> ScreeningProvidersUsageList get_screening_providers_usage()

Read ScreeningProvider credit usage

Reads Guard Dog credit usage for each of the account's connected credit-consuming `ScreeningProvider` entities. Credits are billed against a contract-level pool shared by every provider on the same credential, so providers sharing one credential report identical figures. Not paginated.

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
    api_instance = TractionGuest.ScreeningProvidersApi(api_client)
    
    try:
        # Read ScreeningProvider credit usage
        api_response = api_instance.get_screening_providers_usage()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScreeningProvidersApi->get_screening_providers_usage: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ScreeningProvidersUsageList**](ScreeningProvidersUsageList.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns one usage entry per connected credit-consuming &#x60;ScreeningProvider&#x60;, or an empty array when none are connected. |  -  |
**4XX** | A generic error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_screening_provider**
> ScreeningProvider update_screening_provider(screening_provider_id, screening_provider_update_params, idempotency_key=idempotency_key)

Update a ScreeningProvider

Updates the settings of a connected `ScreeningProvider`.

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
    api_instance = TractionGuest.ScreeningProvidersApi(api_client)
    screening_provider_id = 'screening_provider_id_example' # str | 
screening_provider_update_params = {"integration_settings":[{"field_name":"username","field_value":"new-vc-user"}]} # ScreeningProviderUpdateParams | The screening provider settings to update
idempotency_key = 'idempotency_key_example' # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    try:
        # Update a ScreeningProvider
        api_response = api_instance.update_screening_provider(screening_provider_id, screening_provider_update_params, idempotency_key=idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScreeningProvidersApi->update_screening_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screening_provider_id** | **str**|  | 
 **screening_provider_update_params** | [**ScreeningProviderUpdateParams**](ScreeningProviderUpdateParams.md)| The screening provider settings to update | 
 **idempotency_key** | **str**| An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it&#39;s submitted. We store idempotency keys for only 24 hours. Any &#x60;Idempotency-Key&#x60; shorter than 10 characters will be ignored | [optional] 

### Return type

[**ScreeningProvider**](ScreeningProvider.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The complete updated &#x60;ScreeningProvider&#x60; |  -  |
**4XX** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

