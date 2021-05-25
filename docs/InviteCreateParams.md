# InviteCreateParams

The root of the InviteCreateParams type's schema.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**mobile_number** | **str** |  | [optional] 
**notification_triggers** | [**[NotificationTriggerCreateParams]**](NotificationTriggerCreateParams.md) |  | [optional] 
**email_template_id** | **int** |  | [optional] 
**custom_fields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**host_ids** | **[int]** |  | [optional] 
**watchlist_colour** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**start_date** | **datetime** | The &#x60;start_date&#x60; is required for invitations to lobbies | [optional] 
**end_date** | **datetime** |  | [optional] 
**company** | **str** |  | [optional] 
**group_visit_id** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


