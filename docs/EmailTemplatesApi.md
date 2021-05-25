# TractionGuest.EmailTemplatesApi

All URIs are relative to *https://us.tractionguest.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_email_templates**](EmailTemplatesApi.md#get_email_templates) | **GET** /email_templates | List all EmailTemplates


# **get_email_templates**
> PaginatedEmailTemplatesList get_email_templates()

List all EmailTemplates

Gets a list of all `EmailTemplate` entities.

### Example

```python
import time
import TractionGuest
from TractionGuest.api import email_templates_api
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.paginated_email_templates_list import PaginatedEmailTemplatesList
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
    api_instance = email_templates_api.EmailTemplatesApi(api_client)
    limit = 1 # int | Limits the results to a specified number, defaults to 50 (optional)
    offset = 1 # int | Offsets the results to a specified number, defaults to 0 (optional)
    include = "include_example" # str | A list of comma-separated related models to include (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all EmailTemplates
        api_response = api_instance.get_email_templates(limit=limit, offset=offset, include=include)
        pprint(api_response)
    except TractionGuest.ApiException as e:
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

No authorization required

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

