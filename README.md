# TractionGuest
The Traction Guest API is currently under limited release to select customers as we gather and iterate on feedback.

# Getting Started
If you are interested in getting early access to the API, please send us an email to [support@tractionguest.com](mailto:support@tractionguest.com).

We will also add you to our Slack channel where you can ask questions and get further help.

# Terms and Conditions
Please visit: [https://tractionguest.com/tos/api/](https://tractionguest.com/tos/api/)

# Versioning
This API follows [semantic versioning](https://semver.org/), which follows the `Major`.`Minor`.`Patch` format.

* The `Major` number increments when potentially incompatible changes are made.
* The `Minor` number increments when backwards-compatible additions are made.
* The `Patch` number increments when backwards-compatible bug-fixes are made.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.15.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://tractionguest.com](https://tractionguest.com)

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import TractionGuest
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import TractionGuest
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import TractionGuest
from pprint import pprint
from TractionGuest.api import audit_logs_api
from TractionGuest.model.audit_log import AuditLog
from TractionGuest.model.errors_list import ErrorsList
from TractionGuest.model.paginated_audit_logs_list import PaginatedAuditLogsList
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
    api_instance = audit_logs_api.AuditLogsApi(api_client)
    audit_log_id = "audit_log_id_example" # str | 

    try:
        # Get an AuditLog
        api_response = api_instance.get_audit_log(audit_log_id)
        pprint(api_response)
    except TractionGuest.ApiException as e:
        print("Exception when calling AuditLogsApi->get_audit_log: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://us.tractionguest.com/api/v3*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuditLogsApi* | [**get_audit_log**](docs/AuditLogsApi.md#get_audit_log) | **GET** /audit_logs/{audit_log_id} | Get an AuditLog
*AuditLogsApi* | [**get_audit_logs**](docs/AuditLogsApi.md#get_audit_logs) | **GET** /audit_logs | List all AuditLogs
*BatchesApi* | [**batch_delete_invites**](docs/BatchesApi.md#batch_delete_invites) | **POST** /invites/batch_delete | Delete Multiple Invites
*BatchesApi* | [**get_batch**](docs/BatchesApi.md#get_batch) | **GET** /batches/{batch_id} | Get a BatchJob
*CapacitiesApi* | [**get_capacity**](docs/CapacitiesApi.md#get_capacity) | **GET** /locations/{location_id}/capacities | Get the current capacity details for a location
*CapacitiesApi* | [**get_capacity_forecast**](docs/CapacitiesApi.md#get_capacity_forecast) | **GET** /locations/{location_id}/capacity_forecasts | Get the capacity details for a location
*EmailTemplatesApi* | [**get_email_templates**](docs/EmailTemplatesApi.md#get_email_templates) | **GET** /email_templates | List all EmailTemplates
*GroupVisitsApi* | [**create_group_visit**](docs/GroupVisitsApi.md#create_group_visit) | **POST** /group_visits | Create a new Group Visit (Appointment)
*GroupVisitsApi* | [**delete_group_visit**](docs/GroupVisitsApi.md#delete_group_visit) | **DELETE** /group_visits/{group_visit_id} | Delete a Group Visit (Appointment)
*GroupVisitsApi* | [**get_group_visit**](docs/GroupVisitsApi.md#get_group_visit) | **GET** /group_visits/{group_visit_id} | Get a Group Visit (Appointment)
*GroupVisitsApi* | [**get_group_visits**](docs/GroupVisitsApi.md#get_group_visits) | **GET** /group_visits | List all Group Visits (Appointments)
*GroupVisitsApi* | [**update_group_visit**](docs/GroupVisitsApi.md#update_group_visit) | **PUT** /group_visits/{group_visit_id} | Update a Group Visit (Appointment)
*HostsApi* | [**create_host**](docs/HostsApi.md#create_host) | **POST** /hosts | Create a Host
*HostsApi* | [**create_hosts**](docs/HostsApi.md#create_hosts) | **POST** /hosts/batch | Create multiple Hosts
*HostsApi* | [**get_hosts**](docs/HostsApi.md#get_hosts) | **GET** /hosts | List all Hosts
*InvitesApi* | [**batch_delete_invites**](docs/InvitesApi.md#batch_delete_invites) | **POST** /invites/batch_delete | Delete Multiple Invites
*InvitesApi* | [**create_location_invite**](docs/InvitesApi.md#create_location_invite) | **POST** /locations/{location_id}/invites | Create an Invite
*InvitesApi* | [**create_registration_invite**](docs/InvitesApi.md#create_registration_invite) | **POST** /registrations/{registration_id}/invites | Create an Invite from a Registration
*InvitesApi* | [**delete_invite**](docs/InvitesApi.md#delete_invite) | **DELETE** /invites/{invite_id} | Deletes an Invite
*InvitesApi* | [**get_invite**](docs/InvitesApi.md#get_invite) | **GET** /invites/{invite_id} | Get an Invite
*InvitesApi* | [**get_invites**](docs/InvitesApi.md#get_invites) | **GET** /invites | List all Invites
*InvitesApi* | [**update_invite**](docs/InvitesApi.md#update_invite) | **PUT** /invites/{invite_id} | Update an Invite
*LocationsApi* | [**get_location**](docs/LocationsApi.md#get_location) | **GET** /locations/{location_id} | Get the details of a location
*LocationsApi* | [**get_locations**](docs/LocationsApi.md#get_locations) | **GET** /locations | List all Locations
*PackagesApi* | [**create_package**](docs/PackagesApi.md#create_package) | **POST** /packages | Create package
*PackagesApi* | [**delete_package**](docs/PackagesApi.md#delete_package) | **DELETE** /packages/{package_id} | 
*PackagesApi* | [**get_package**](docs/PackagesApi.md#get_package) | **GET** /packages/{package_id} | Get Package
*PackagesApi* | [**get_packages**](docs/PackagesApi.md#get_packages) | **GET** /packages | Get packages
*PackagesApi* | [**update_package**](docs/PackagesApi.md#update_package) | **PUT** /packages/{package_id} | Update Package
*RegistrationsApi* | [**get_registration**](docs/RegistrationsApi.md#get_registration) | **GET** /registrations/{registration_id} | Get a Registration
*RegistrationsApi* | [**get_registrations**](docs/RegistrationsApi.md#get_registrations) | **GET** /registrations | List all Registrations
*SigninsApi* | [**create_signin**](docs/SigninsApi.md#create_signin) | **POST** /signins | Create Signin
*SigninsApi* | [**get_signin**](docs/SigninsApi.md#get_signin) | **GET** /signins/{signin_id} | Get a Signin
*SigninsApi* | [**get_signins**](docs/SigninsApi.md#get_signins) | **GET** /signins | List all Signins
*SigninsApi* | [**update_signin**](docs/SigninsApi.md#update_signin) | **PUT** /signins/{signin_id} | Update a Signin
*UsersApi* | [**get_current_user**](docs/UsersApi.md#get_current_user) | **GET** /users/{user_id} | Get the current User
*WatchlistsApi* | [**create_watchlist**](docs/WatchlistsApi.md#create_watchlist) | **POST** /watchlists | Create Watchlist
*WatchlistsApi* | [**delete_watchlist**](docs/WatchlistsApi.md#delete_watchlist) | **DELETE** /watchlists/{watchlist_id} | Deletes a Watchlist
*WatchlistsApi* | [**get_watchlist**](docs/WatchlistsApi.md#get_watchlist) | **GET** /watchlists/{watchlist_id} | Get a Watchlist
*WatchlistsApi* | [**get_watchlists**](docs/WatchlistsApi.md#get_watchlists) | **GET** /watchlists | List all Watchlists
*WatchlistsApi* | [**update_watchlist**](docs/WatchlistsApi.md#update_watchlist) | **PUT** /watchlists/{watchlist_id} | Update a Watchlist


## Documentation For Models

 - [AuditLog](docs/AuditLog.md)
 - [AuditLogChange](docs/AuditLogChange.md)
 - [BatchJob](docs/BatchJob.md)
 - [Capacity](docs/Capacity.md)
 - [CapacityByHourResponse](docs/CapacityByHourResponse.md)
 - [CapacityForecast](docs/CapacityForecast.md)
 - [CustomField](docs/CustomField.md)
 - [Docusign](docs/Docusign.md)
 - [EmailTemplate](docs/EmailTemplate.md)
 - [Error](docs/Error.md)
 - [ErrorsList](docs/ErrorsList.md)
 - [ExternalWatchlistResult](docs/ExternalWatchlistResult.md)
 - [GroupVisit](docs/GroupVisit.md)
 - [GroupVisitCreateParams](docs/GroupVisitCreateParams.md)
 - [GroupVisitUpdateParams](docs/GroupVisitUpdateParams.md)
 - [GuestResponse](docs/GuestResponse.md)
 - [Host](docs/Host.md)
 - [HostBatchCreateParams](docs/HostBatchCreateParams.md)
 - [HostCreateParams](docs/HostCreateParams.md)
 - [IdentifierList](docs/IdentifierList.md)
 - [Image](docs/Image.md)
 - [InternalWatchlistResult](docs/InternalWatchlistResult.md)
 - [Invite](docs/Invite.md)
 - [InviteCreateParams](docs/InviteCreateParams.md)
 - [InviteDetail](docs/InviteDetail.md)
 - [InviteUpdateParams](docs/InviteUpdateParams.md)
 - [InviteWatchlist](docs/InviteWatchlist.md)
 - [Location](docs/Location.md)
 - [NotificationTrigger](docs/NotificationTrigger.md)
 - [NotificationTriggerCreateParams](docs/NotificationTriggerCreateParams.md)
 - [Package](docs/Package.md)
 - [PackageCreateParams](docs/PackageCreateParams.md)
 - [PackageUpdateParams](docs/PackageUpdateParams.md)
 - [PaginatedAuditLogsList](docs/PaginatedAuditLogsList.md)
 - [PaginatedEmailTemplatesList](docs/PaginatedEmailTemplatesList.md)
 - [PaginatedGroupVisitsList](docs/PaginatedGroupVisitsList.md)
 - [PaginatedHostsList](docs/PaginatedHostsList.md)
 - [PaginatedInvitesList](docs/PaginatedInvitesList.md)
 - [PaginatedLocationsList](docs/PaginatedLocationsList.md)
 - [PaginatedPackagesList](docs/PaginatedPackagesList.md)
 - [PaginatedRegistrationsList](docs/PaginatedRegistrationsList.md)
 - [PaginatedSigninsList](docs/PaginatedSigninsList.md)
 - [PaginatedWatchlistList](docs/PaginatedWatchlistList.md)
 - [Pagination](docs/Pagination.md)
 - [PermissionGroup](docs/PermissionGroup.md)
 - [Registration](docs/Registration.md)
 - [RegistrationDetail](docs/RegistrationDetail.md)
 - [SignableDocument](docs/SignableDocument.md)
 - [Signin](docs/Signin.md)
 - [SigninAcknowledgement](docs/SigninAcknowledgement.md)
 - [SigninCreateParams](docs/SigninCreateParams.md)
 - [SigninData](docs/SigninData.md)
 - [SigninDetail](docs/SigninDetail.md)
 - [SigninUpdateParams](docs/SigninUpdateParams.md)
 - [SigninWatchlist](docs/SigninWatchlist.md)
 - [SimpleSignature](docs/SimpleSignature.md)
 - [User](docs/User.md)
 - [Visitor](docs/Visitor.md)
 - [Watchlist](docs/Watchlist.md)
 - [WatchlistCreateParams](docs/WatchlistCreateParams.md)
 - [WatchlistMatch](docs/WatchlistMatch.md)
 - [WatchlistSearch](docs/WatchlistSearch.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

support@tractionguest.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in TractionGuest.apis and TractionGuest.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from TractionGuest.api.default_api import DefaultApi`
- `from TractionGuest.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import TractionGuest
from TractionGuest.apis import *
from TractionGuest.models import *
```

