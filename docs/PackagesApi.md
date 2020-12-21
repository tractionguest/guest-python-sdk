# TractionGuest.PackagesApi

All URIs are relative to *https://us.tractionguest.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_package**](PackagesApi.md#create_package) | **POST** /packages | Create package
[**delete_package**](PackagesApi.md#delete_package) | **DELETE** /packages/{package_id} | 
[**get_package**](PackagesApi.md#get_package) | **GET** /packages/{package_id} | Get Package
[**get_packages**](PackagesApi.md#get_packages) | **GET** /packages | Get packages
[**update_package**](PackagesApi.md#update_package) | **PUT** /packages/{package_id} | Update Package


# **create_package**
> Package create_package(package_create_params=package_create_params)

Create package

Creates a [Package] entity by extracting information about the recipient and carrier from the given image file.

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
    api_instance = TractionGuest.PackagesApi(api_client)
    package_create_params = TractionGuest.PackageCreateParams() # PackageCreateParams | Parameters for creating a package (optional)

    try:
        # Create package
        api_response = api_instance.create_package(package_create_params=package_create_params)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PackagesApi->create_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_create_params** | [**PackageCreateParams**](PackageCreateParams.md)| Parameters for creating a package | [optional] 

### Return type

[**Package**](Package.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_package**
> delete_package(package_id, idempotency_key=idempotency_key)



Delete a pacakge

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
    api_instance = TractionGuest.PackagesApi(api_client)
    package_id = 'package_id_example' # str | 
idempotency_key = 'idempotency_key_example' # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    try:
        api_instance.delete_package(package_id, idempotency_key=idempotency_key)
    except ApiException as e:
        print("Exception when calling PackagesApi->delete_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **str**|  | 
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
**204** | The package has been deleted |  -  |
**4XX** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_package**
> Package get_package(package_id, include=include)

Get Package

Gets the details of a single instance of a Package

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
    api_instance = TractionGuest.PackagesApi(api_client)
    package_id = 'package_id_example' # str | 
include = 'include_example' # str | A list of comma-separated related models to include  (optional)

    try:
        # Get Package
        api_response = api_instance.get_package(package_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PackagesApi->get_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **str**|  | 
 **include** | **str**| A list of comma-separated related models to include  | [optional] 

### Return type

[**Package**](Package.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**4XX** | User submission error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packages**
> PaginatedPackagesList get_packages(location_ids=location_ids, limit=limit, offset=offset, include=include, picked_up=picked_up, query=query)

Get packages

Gets a list of [Package] entities.

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
    api_instance = TractionGuest.PackagesApi(api_client)
    location_ids = '1,2,3' # str | A comma separated list of Location ids for filtering. i.e. '1,2,3' Will return all packages from all locations if none are specified (optional)
limit = 50 # int | Limits the results to a specified number, defaults to 50 (optional) (default to 50)
offset = 0 # int | Offsets the results to a specified number, defaults to 0 (optional) (default to 0)
include = 'recipient,location,image' # str | A list of comma-separated related models to include. Possible values: 'recipient', 'location', 'image' (optional)
picked_up = True # bool | Filters packages by their \"picked_up\" state.. (optional)
query = 'query_example' # str | Searches for packages by recipient name (optional)

    try:
        # Get packages
        api_response = api_instance.get_packages(location_ids=location_ids, limit=limit, offset=offset, include=include, picked_up=picked_up, query=query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PackagesApi->get_packages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_ids** | **str**| A comma separated list of Location ids for filtering. i.e. &#39;1,2,3&#39; Will return all packages from all locations if none are specified | [optional] 
 **limit** | **int**| Limits the results to a specified number, defaults to 50 | [optional] [default to 50]
 **offset** | **int**| Offsets the results to a specified number, defaults to 0 | [optional] [default to 0]
 **include** | **str**| A list of comma-separated related models to include. Possible values: &#39;recipient&#39;, &#39;location&#39;, &#39;image&#39; | [optional] 
 **picked_up** | **bool**| Filters packages by their \&quot;picked_up\&quot; state.. | [optional] 
 **query** | **str**| Searches for packages by recipient name | [optional] 

### Return type

[**PaginatedPackagesList**](PaginatedPackagesList.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_package**
> Package update_package(package_id, idempotency_key=idempotency_key, package_update_params=package_update_params)

Update Package

Update/Edit information about a Package.  picked_up - changes the package_state to picked up and assigns non null value to picked_up_at  recipient_id - update the package's intended recipient. Changes package_state to 'recipient_matched' if a match hasn't been found and notifies host about their package via email. A previous recipient will stop getting notifications  carrier_name - change/update the package's carrier/courier information    

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
    api_instance = TractionGuest.PackagesApi(api_client)
    package_id = 'package_id_example' # str | 
idempotency_key = 'idempotency_key_example' # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)
package_update_params = TractionGuest.PackageUpdateParams() # PackageUpdateParams |  (optional)

    try:
        # Update Package
        api_response = api_instance.update_package(package_id, idempotency_key=idempotency_key, package_update_params=package_update_params)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PackagesApi->update_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **str**|  | 
 **idempotency_key** | **str**| An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it&#39;s submitted. We store idempotency keys for only 24 hours. Any &#x60;Idempotency-Key&#x60; shorter than 10 characters will be ignored | [optional] 
 **package_update_params** | [**PackageUpdateParams**](PackageUpdateParams.md)|  | [optional] 

### Return type

[**Package**](Package.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | User submission error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

