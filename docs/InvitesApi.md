# TractionGuest.InvitesApi

All URIs are relative to *https://tractionguest.ca/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_location_invite**](InvitesApi.md#create_location_invite) | **POST** /locations/{location_id}/invites | Create an Invite
[**create_registration_invite**](InvitesApi.md#create_registration_invite) | **POST** /registrations/{registration_id}/invites | Create an Invite from a Registration
[**delete_invite**](InvitesApi.md#delete_invite) | **DELETE** /invites/{invite_id} | Deletes an Invite
[**get_invite**](InvitesApi.md#get_invite) | **GET** /invites/{invite_id} | Get an Invite
[**get_invites**](InvitesApi.md#get_invites) | **GET** /invites | List all Invites
[**update_invite**](InvitesApi.md#update_invite) | **PUT** /invites/{invite_id} | Update an Invite


# **create_location_invite**
> object create_location_invite(location_id, invite_create_params, idempotency_key=idempotency_key)

Create an Invite

Creates a new `Invite` for a specific `Location`.

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
    api_instance = TractionGuest.InvitesApi(api_client)
    location_id = 'location_id_example' # str | 
invite_create_params = TractionGuest.InviteCreateParams() # InviteCreateParams | 
idempotency_key = 'idempotency_key_example' # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    try:
        # Create an Invite
        api_response = api_instance.create_location_invite(location_id, invite_create_params, idempotency_key=idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InvitesApi->create_location_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  | 
 **invite_create_params** | [**InviteCreateParams**](InviteCreateParams.md)|  | 
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
**201** | Created the &#x60;Invite&#x60; for the &#x60;Location&#x60; |  -  |
**400** | A generic error |  -  |
**401** | You don&#39;t have permission to create this Invite |  -  |
**403** | You do not have permission for this action |  -  |
**404** | The Location does not exist |  -  |
**422** | Your request was not formatted correctly |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_registration_invite**
> object create_registration_invite(registration_id, idempotency_key=idempotency_key)

Create an Invite from a Registration

Creates a new `Invite` from `Registration` data.

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
    api_instance = TractionGuest.InvitesApi(api_client)
    registration_id = 'registration_id_example' # str | 
idempotency_key = 'idempotency_key_example' # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    try:
        # Create an Invite from a Registration
        api_response = api_instance.create_registration_invite(registration_id, idempotency_key=idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InvitesApi->create_registration_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**|  | 
 **idempotency_key** | **str**| An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it&#39;s submitted. We store idempotency keys for only 24 hours. Any &#x60;Idempotency-Key&#x60; shorter than 10 characters will be ignored | [optional] 

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
**201** | Created an &#x60;Invite&#x60; from the given &#x60;Registration&#x60; UUID. |  -  |
**400** | A generic error |  -  |
**401** | You don&#39;t have permission to create this Invite |  -  |
**403** | You do not have permission for this action |  -  |
**404** | The Location does not exist |  -  |
**422** | Your request was not formatted correctly |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invite**
> delete_invite(invite_id, idempotency_key=idempotency_key)

Deletes an Invite

Deletes a single instance of `Invite`

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
    api_instance = TractionGuest.InvitesApi(api_client)
    invite_id = 'invite_id_example' # str | 
idempotency_key = 'idempotency_key_example' # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    try:
        # Deletes an Invite
        api_instance.delete_invite(invite_id, idempotency_key=idempotency_key)
    except ApiException as e:
        print("Exception when calling InvitesApi->delete_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**|  | 
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
**204** | The &#x60;Invite&#x60; has been deleted |  -  |
**400** | There was an error in trying to delete the &#x60;Invite&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invite**
> InviteDetail get_invite(invite_id, include=include)

Get an Invite

Gets the details of a single instance of a `Invite`.

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
    api_instance = TractionGuest.InvitesApi(api_client)
    invite_id = 'invite_id_example' # str | 
include = 'include_example' # str | A list of comma-separated related models to include (optional)

    try:
        # Get an Invite
        api_response = api_instance.get_invite(invite_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InvitesApi->get_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**|  | 
 **include** | **str**| A list of comma-separated related models to include | [optional] 

### Return type

[**InviteDetail**](InviteDetail.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns a single &#x60;Invite&#x60;. |  -  |
**400** | A generic error |  -  |
**401** | You don&#39;t have permission to view this Invite |  -  |
**403** | You do not have permission for this action |  -  |
**404** | The Invite you are looking for does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invites**
> PaginatedInvitesList get_invites(limit=limit, offset=offset, query=query, with_colours=with_colours, location_ids=location_ids, sort_by=sort_by, starts_before=starts_before, starts_after=starts_after, include=include, is_approved=is_approved, active_after=active_after, active_before=active_before)

List all Invites

Gets a list of all `Invite` entities.

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
    api_instance = TractionGuest.InvitesApi(api_client)
    limit = 56 # int | Limits the results to a specified number, defaults to 50 (optional)
offset = 56 # int | Offsets the results to a specified number, defaults to 0 (optional)
query = 'query_example' # str | Filters by `first_name`, `last_name`, `company`, and `email` (optional)
with_colours = 'with_colours_example' # str | A comma separated list of case-insensitive colour values. i.e., `red`, `green`, `yellow`, and `orange` (optional)
location_ids = 'location_ids_example' # str | A comma separated list of Location IDs (optional)
sort_by = 'sort_by_example' # str | Sorts by the field name and direction provided where the pattern is `FIELD_NAME_DIRECTION` (optional)
starts_before = '2013-10-20' # date | Filters results to all those *before* the provided datetime (optional)
starts_after = '2013-10-20' # date | Filters results to all those *after* the provided datetime (optional)
include = 'include_example' # str | A list of comma-separated related models to include (optional)
is_approved = True # bool | True to return approved and auto approved invites, False to return pending and rejected invites (optional)
active_after = '2013-10-20T19:20:30+01:00' # datetime | Checks that an invite hasn't yet started, or has started and is still active after a specified time (optional)
active_before = '2013-10-20T19:20:30+01:00' # datetime | Checks that an invite hasn't ended before a specified time (optional)

    try:
        # List all Invites
        api_response = api_instance.get_invites(limit=limit, offset=offset, query=query, with_colours=with_colours, location_ids=location_ids, sort_by=sort_by, starts_before=starts_before, starts_after=starts_after, include=include, is_approved=is_approved, active_after=active_after, active_before=active_before)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InvitesApi->get_invites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the results to a specified number, defaults to 50 | [optional] 
 **offset** | **int**| Offsets the results to a specified number, defaults to 0 | [optional] 
 **query** | **str**| Filters by &#x60;first_name&#x60;, &#x60;last_name&#x60;, &#x60;company&#x60;, and &#x60;email&#x60; | [optional] 
 **with_colours** | **str**| A comma separated list of case-insensitive colour values. i.e., &#x60;red&#x60;, &#x60;green&#x60;, &#x60;yellow&#x60;, and &#x60;orange&#x60; | [optional] 
 **location_ids** | **str**| A comma separated list of Location IDs | [optional] 
 **sort_by** | **str**| Sorts by the field name and direction provided where the pattern is &#x60;FIELD_NAME_DIRECTION&#x60; | [optional] 
 **starts_before** | **date**| Filters results to all those *before* the provided datetime | [optional] 
 **starts_after** | **date**| Filters results to all those *after* the provided datetime | [optional] 
 **include** | **str**| A list of comma-separated related models to include | [optional] 
 **is_approved** | **bool**| True to return approved and auto approved invites, False to return pending and rejected invites | [optional] 
 **active_after** | **datetime**| Checks that an invite hasn&#39;t yet started, or has started and is still active after a specified time | [optional] 
 **active_before** | **datetime**| Checks that an invite hasn&#39;t ended before a specified time | [optional] 

### Return type

[**PaginatedInvitesList**](PaginatedInvitesList.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array of &#x60;Invite&#x60; entities. |  -  |
**400** | A generic error |  -  |
**401** | You don&#39;t have permission to view these Invites |  -  |
**403** | You do not have permission for this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invite**
> object update_invite(invite_id, invite_create_params1, idempotency_key=idempotency_key)

Update an Invite

Updates an existing `Invite`.

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
    api_instance = TractionGuest.InvitesApi(api_client)
    invite_id = 'invite_id_example' # str | 
invite_create_params1 = TractionGuest.InviteCreateParams1() # InviteCreateParams1 | 
idempotency_key = 'idempotency_key_example' # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    try:
        # Update an Invite
        api_response = api_instance.update_invite(invite_id, invite_create_params1, idempotency_key=idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InvitesApi->update_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**|  | 
 **invite_create_params1** | [**InviteCreateParams1**](InviteCreateParams1.md)|  | 
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
**202** | Successful response. |  -  |
**400** | A generic error |  -  |
**401** | You don&#39;t have permission to view this Invite |  -  |
**403** | You do not have permission for this action |  -  |
**404** | The Invite does not exist |  -  |
**422** | Your request was not formatted correctly |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

