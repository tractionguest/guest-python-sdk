# AuditLog

The root of the AuditLog type's schema.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**created_at** | **str** |  | [optional] 
**request_uuid** | **str** |  | [optional] 
**remote_address** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**audited_changes** | [**list[AuditLogChange]**](AuditLogChange.md) |  | [optional] 
**action** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**auditable_type** | **str** |  | [optional] 
**auditable_id** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


