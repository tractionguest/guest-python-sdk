# User

The root of the User type's schema.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**mobile_access_enabled** | **bool** | Identifies if user has access to mobile app features. | 
**permission_groups** | [**list[PermissionGroup]**](PermissionGroup.md) |  | [optional] 
**email** | **str** |  | 
**last_name** | **str** |  | [optional] 
**first_name** | **str** | Determines if the registration portal has been enabled for this account | [optional] 
**registration_portal_enabled** | **bool** | Determines if the registration portal has been enabled for this account | 
**account_uuid** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


