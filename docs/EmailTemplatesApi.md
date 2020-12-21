# TractionGuest.EmailTemplatesApi

All URIs are relative to *https://us.tractionguest.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_email_templates**](EmailTemplatesApi.md#get_email_templates) | **GET** /email_templates | List all EmailTemplates


# **get_email_templates**
> PaginatedEmailTemplatesList get_email_templates(limit=limit, offset=offset, include=include)

List all EmailTemplates

Gets a list of all `EmailTemplate` entities.

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
    api_instance = TractionGuest.EmailTemplatesApi(api_client)
    limit = 56 # int | Limits the results to a specified number, defaults to 50 (optional)
offset = 56 # int | Offsets the results to a specified number, defaults to 0 (optional)
include = 'include_example' # str | A list of comma-separated related models to include (optional)

    try:
        # List all EmailTemplates
        api_response = api_instance.get_email_templates(limit=limit, offset=offset, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailTemplatesApi->get_email_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the results to a specified number, defaults to 50 | [optional] 
 **offset** | **int**| Offsets the results to a specified number, defaults to 0 | [optional] 
 **include** | **str**| A list of comma-separated related models to include | [optional] 

### Return type

[**PaginatedEmailTemplatesList**](PaginatedEmailTemplatesList.md)

### Authorization

[TractionGuestAuth](../README.md#TractionGuestAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array of &#x60;EmailTemplate&#x60; entities. |  -  |
**400** | A generic error |  -  |
**401** | You don&#39;t have permission to view this EmailTemplate |  -  |
**403** | You do not have permission for this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

