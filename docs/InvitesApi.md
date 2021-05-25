# TractionGuest.InvitesApi

All URIs are relative to *https://us.tractionguest.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_delete_invites**](InvitesApi.md#batch_delete_invites) | **POST** /invites/batch_delete | Delete Multiple Invites
[**create_location_invite**](InvitesApi.md#create_location_invite) | **POST** /locations/{location_id}/invites | Create an Invite
[**create_registration_invite**](InvitesApi.md#create_registration_invite) | **POST** /registrations/{registration_id}/invites | Create an Invite from a Registration
[**delete_invite**](InvitesApi.md#delete_invite) | **DELETE** /invites/{invite_id} | Deletes an Invite
[**get_invite**](InvitesApi.md#get_invite) | **GET** /invites/{invite_id} | Get an Invite
[**get_invites**](InvitesApi.md#get_invites) | **GET** /invites | List all Invites
[**update_invite**](InvitesApi.md#update_invite) | **PUT** /invites/{invite_id} | Update an Invite


# **batch_delete_invites**
> BatchJob batch_delete_invites()

Delete Multiple Invites

Queues up a \"delete\" background task for one or more `Invite` entities.

### Example

```python
import time
import TractionGuest
from TractionGuest.api import invites_api
from TractionGuest.model.batch_job import BatchJob
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.identifier_list import IdentifierList
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
    api_instance = invites_api.InvitesApi(api_client)
    identifier_list = IdentifierList(
        ids=[
            "ids_example",
        ],
    ) # IdentifierList |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Multiple Invites
        api_response = api_instance.batch_delete_invites(identifier_list=identifier_list)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling InvitesApi->batch_delete_invites: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_list** | [**IdentifierList**](IdentifierList.md)|  | [optional]

### Return type

[**BatchJob**](BatchJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**4XX** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_location_invite**
> InviteDetail create_location_invite(location_id, invite_create_params)

Create an Invite

Creates a new `Invite` for a specific `Location`.

### Example

```python
import time
import TractionGuest
from TractionGuest.api import invites_api
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.invite_detail import InviteDetail
from TractionGuest.model.invite_create_params import InviteCreateParams
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
    api_instance = invites_api.InvitesApi(api_client)
    location_id = "location_id_example" # str | 
    invite_create_params = InviteCreateParams(
        mobile_number="mobile_number_example",
        notification_triggers=[
            NotificationTriggerCreateParams(
                offset_unit="days",
                notification_groups=[
                    "notification_groups_example",
                ],
                email_template_id=1,
                offset_origin="START",
                offset_amount=1,
                offset_direction="BEFORE",
            ),
        ],
        first_name="first_name_example",
        email_template_id=1,
        custom_fields=[
            CustomField(
                format="string",
                field_name="field_name_example",
                field_value="field_value_example",
                id=1,
            ),
        ],
        host_ids=[
            1,
        ],
        watchlist_colour="RED",
        title="title_example",
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        last_name="last_name_example",
        end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        email="email_example",
        company="company_example",
        group_visit_id=1,
    ) # InviteCreateParams | 
    idempotency_key = "Idempotency-Key_example" # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an Invite
        api_response = api_instance.create_location_invite(location_id, invite_create_params)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling InvitesApi->create_location_invite: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an Invite
        api_response = api_instance.create_location_invite(location_id, invite_create_params, idempotency_key=idempotency_key)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling InvitesApi->create_location_invite: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  |
 **invite_create_params** | [**InviteCreateParams**](InviteCreateParams.md)|  |
 **idempotency_key** | **str**| An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it&#39;s submitted. We store idempotency keys for only 24 hours. Any &#x60;Idempotency-Key&#x60; shorter than 10 characters will be ignored | [optional]

### Return type

[**InviteDetail**](InviteDetail.md)

### Authorization

No authorization required

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
> InviteDetail create_registration_invite(registration_id)

Create an Invite from a Registration

Creates a new `Invite` from `Registration` data.

### Example

```python
import time
import TractionGuest
from TractionGuest.api import invites_api
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.invite_detail import InviteDetail
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
    api_instance = invites_api.InvitesApi(api_client)
    registration_id = "registration_id_example" # str | 
    idempotency_key = "Idempotency-Key_example" # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an Invite from a Registration
        api_response = api_instance.create_registration_invite(registration_id)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling InvitesApi->create_registration_invite: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an Invite from a Registration
        api_response = api_instance.create_registration_invite(registration_id, idempotency_key=idempotency_key)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling InvitesApi->create_registration_invite: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**|  |
 **idempotency_key** | **str**| An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it&#39;s submitted. We store idempotency keys for only 24 hours. Any &#x60;Idempotency-Key&#x60; shorter than 10 characters will be ignored | [optional]

### Return type

[**InviteDetail**](InviteDetail.md)

### Authorization

No authorization required

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
> delete_invite(invite_id)

Deletes an Invite

Deletes a single instance of `Invite`

### Example

```python
import time
import TractionGuest
from TractionGuest.api import invites_api
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
    api_instance = invites_api.InvitesApi(api_client)
    invite_id = "invite_id_example" # str | 
    idempotency_key = "Idempotency-Key_example" # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes an Invite
        api_instance.delete_invite(invite_id)
    except TractionGuest.ApiException as e:
        print("Exception when calling InvitesApi->delete_invite: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes an Invite
        api_instance.delete_invite(invite_id, idempotency_key=idempotency_key)
    except TractionGuest.ApiException as e:
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

No authorization required

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
> InviteDetail get_invite(invite_id)

Get an Invite

Gets the details of a single instance of a `Invite`.

### Example

```python
import time
import TractionGuest
from TractionGuest.api import invites_api
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.invite_detail import InviteDetail
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
    api_instance = invites_api.InvitesApi(api_client)
    invite_id = "invite_id_example" # str | 
    include = "include_example" # str | A list of comma-separated related models to include (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get an Invite
        api_response = api_instance.get_invite(invite_id)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling InvitesApi->get_invite: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an Invite
        api_response = api_instance.get_invite(invite_id, include=include)
        pprint(api_response)
    except TractionGuest.ApiException as e:
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

No authorization required

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
> PaginatedInvitesList get_invites()

List all Invites

Gets a list of all `Invite` entities.

### Example

```python
import time
import TractionGuest
from TractionGuest.api import invites_api
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.paginated_invites_list import PaginatedInvitesList
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
    api_instance = invites_api.InvitesApi(api_client)
    limit = 1 # int | Limits the results to a specified number, defaults to 50 (optional)
    offset = 1 # int | Offsets the results to a specified number, defaults to 0 (optional)
    query = "query_example" # str | Filters by `first_name`, `last_name`, `company`, and `email` (optional)
    with_colours = "with_colours_example" # str | A comma separated list of case-insensitive colour values. i.e., `red`, `green`, `yellow`, and `orange` (optional)
    location_ids = "location_ids_example" # str | A comma separated list of Location IDs (optional)
    sort_by = "start_date_asc" # str | Sorts by the field name and direction provided where the pattern is `FIELD_NAME_DIRECTION` (optional)
    starts_before = dateutil_parser('1970-01-01').date() # date | Filters results to all those *before* the provided datetime (optional)
    starts_after = dateutil_parser('1970-01-01').date() # date | Filters results to all those *after* the provided datetime (optional)
    include = "include_example" # str | A list of comma-separated related models to include (optional)
    is_approved = True # bool | True to return approved and auto approved invites, False to return pending and rejected invites (optional)
    active_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Checks that an invite hasn't yet started, or has started and is still active after a specified time (optional)
    active_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Checks that an invite hasn't ended before a specified time (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all Invites
        api_response = api_instance.get_invites(limit=limit, offset=offset, query=query, with_colours=with_colours, location_ids=location_ids, sort_by=sort_by, starts_before=starts_before, starts_after=starts_after, include=include, is_approved=is_approved, active_after=active_after, active_before=active_before)
        pprint(api_response)
    except TractionGuest.ApiException as e:
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

No authorization required

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
> InviteDetail update_invite(invite_id, invite_update_params)

Update an Invite

Updates an existing `Invite`.

### Example

```python
import time
import TractionGuest
from TractionGuest.api import invites_api
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.invite_detail import InviteDetail
from TractionGuest.model.invite_update_params import InviteUpdateParams
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
    api_instance = invites_api.InvitesApi(api_client)
    invite_id = "invite_id_example" # str | 
    invite_update_params = InviteUpdateParams(
        mobile_number="mobile_number_example",
        user_id=1,
        on_premise=True,
        notification_triggers=[
            NotificationTriggerCreateParams(
                offset_unit="days",
                notification_groups=[
                    "notification_groups_example",
                ],
                email_template_id=1,
                offset_origin="START",
                offset_amount=1,
                offset_direction="BEFORE",
            ),
        ],
        first_name="first_name_example",
        email_template_id=1,
        custom_fields=[
            CustomField(
                format="string",
                field_name="field_name_example",
                field_value="field_value_example",
                id=1,
            ),
        ],
        host_ids=[
            1,
        ],
        title="title_example",
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        last_name="last_name_example",
        end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        email="email_example",
        company="company_example",
        group_visit_id=1,
    ) # InviteUpdateParams | Updated `Invite` information.
    idempotency_key = "Idempotency-Key_example" # str | An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it's submitted. We store idempotency keys for only 24 hours. Any `Idempotency-Key` shorter than 10 characters will be ignored (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an Invite
        api_response = api_instance.update_invite(invite_id, invite_update_params)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling InvitesApi->update_invite: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an Invite
        api_response = api_instance.update_invite(invite_id, invite_update_params, idempotency_key=idempotency_key)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling InvitesApi->update_invite: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**|  |
 **invite_update_params** | [**InviteUpdateParams**](InviteUpdateParams.md)| Updated &#x60;Invite&#x60; information. |
 **idempotency_key** | **str**| An optional idempotency key to allow for repeat API requests. Any API request with this key will only be executed once, no matter how many times it&#39;s submitted. We store idempotency keys for only 24 hours. Any &#x60;Idempotency-Key&#x60; shorter than 10 characters will be ignored | [optional]

### Return type

[**InviteDetail**](InviteDetail.md)

### Authorization

No authorization required

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

