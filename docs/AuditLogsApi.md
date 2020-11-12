# TractionGuest.AuditLogsApi

All URIs are relative to *https://tractionguest.ca/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_log**](AuditLogsApi.md#get_audit_log) | **GET** /audit_logs/{audit_log_id} | Get an AuditLog
[**get_audit_logs**](AuditLogsApi.md#get_audit_logs) | **GET** /audit_logs | List all AuditLogs


# **get_audit_log**
> AuditLog get_audit_log(audit_log_id)

Get an AuditLog

Gets the details of a single instance of an `AuditLog`.

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
    api_instance = TractionGuest.AuditLogsApi(api_client)
    audit_log_id = 'audit_log_id_example' # str | 

    try:
        # Get an AuditLog
        api_response = api_instance.get_audit_log(audit_log_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuditLogsApi->get_audit_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_log_id** | **str**|  | 

### Return type

[**AuditLog**](AuditLog.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns a single &#x60;AuditLog&#x60;. |  -  |
**400** | A generic error |  -  |
**401** | You don&#39;t have permission to view this AuditLog |  -  |
**403** | You do not have permission for this action |  -  |
**404** | The AuditLog does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_logs**
> PaginatedAuditLogsList get_audit_logs(limit=limit, offset=offset, sort_by=sort_by, auditable_id=auditable_id, auditable_type=auditable_type, action_type=action_type, user_id=user_id)

List all AuditLogs

Gets a list of all `AuditLog` entities.

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
    api_instance = TractionGuest.AuditLogsApi(api_client)
    limit = 56 # int | Limits the results to a specified number, defaults to 50 (optional)
offset = 56 # int | Offsets the results to a specified number, defaults to 0 (optional)
sort_by = 'sort_by_example' # str | Sorts by the field name and direction provided where the pattern is `FIELD_NAME_DIRECTION` (optional)
auditable_id = 56 # int | The unique ID of a model that has associated audit logs (optional)
auditable_type = 'auditable_type_example' # str | The name of the model that has associated audit logs. Valid values include: - `user` - `device_configuration` - `signin` - `invite` - `watchlist_record` - `account_preference` - `signout` - `host` - `invite_watchlist` - `location_preference` - `parking_lot` - `parking_stall` - `permission_bundle` - `person` - `physical_access_grant` - `physical_access_provider` - `physical_access_rule` - `security_badge_type` - `signin_watchlist` - `user_group_physical_access_rule` - `visitor` - `bulk_data_batch`  (optional)
action_type = 'action_type_example' # str | The action performed by the user. Valid values include: - `create` - `update` - `destroy`  (optional)
user_id = 56 # int | The ID of the user who performed the database change (optional)

    try:
        # List all AuditLogs
        api_response = api_instance.get_audit_logs(limit=limit, offset=offset, sort_by=sort_by, auditable_id=auditable_id, auditable_type=auditable_type, action_type=action_type, user_id=user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuditLogsApi->get_audit_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the results to a specified number, defaults to 50 | [optional] 
 **offset** | **int**| Offsets the results to a specified number, defaults to 0 | [optional] 
 **sort_by** | **str**| Sorts by the field name and direction provided where the pattern is &#x60;FIELD_NAME_DIRECTION&#x60; | [optional] 
 **auditable_id** | **int**| The unique ID of a model that has associated audit logs | [optional] 
 **auditable_type** | **str**| The name of the model that has associated audit logs. Valid values include: - &#x60;user&#x60; - &#x60;device_configuration&#x60; - &#x60;signin&#x60; - &#x60;invite&#x60; - &#x60;watchlist_record&#x60; - &#x60;account_preference&#x60; - &#x60;signout&#x60; - &#x60;host&#x60; - &#x60;invite_watchlist&#x60; - &#x60;location_preference&#x60; - &#x60;parking_lot&#x60; - &#x60;parking_stall&#x60; - &#x60;permission_bundle&#x60; - &#x60;person&#x60; - &#x60;physical_access_grant&#x60; - &#x60;physical_access_provider&#x60; - &#x60;physical_access_rule&#x60; - &#x60;security_badge_type&#x60; - &#x60;signin_watchlist&#x60; - &#x60;user_group_physical_access_rule&#x60; - &#x60;visitor&#x60; - &#x60;bulk_data_batch&#x60;  | [optional] 
 **action_type** | **str**| The action performed by the user. Valid values include: - &#x60;create&#x60; - &#x60;update&#x60; - &#x60;destroy&#x60;  | [optional] 
 **user_id** | **int**| The ID of the user who performed the database change | [optional] 

### Return type

[**PaginatedAuditLogsList**](PaginatedAuditLogsList.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array of &#x60;AuditLog&#x60; entities. |  -  |
**400** | A generic error |  -  |
**401** | You don&#39;t have permission to view this AuditLog |  -  |
**403** | You do not have permission for this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

