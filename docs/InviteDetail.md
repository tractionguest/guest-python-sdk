# InviteDetail

The root of the InviteDetail type's schema.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**last_name** | **str** |  | 
**first_name** | **str** |  | 
**email** | **str** |  | 
**registration** | [**Registration**](Registration.md) |  | [optional] 
**mobile_number** | **str** | Phone number | [optional] 
**email_template** | [**EmailTemplate**](EmailTemplate.md) |  | [optional] 
**invite_watchlist** | [**InviteWatchlist**](InviteWatchlist.md) |  | [optional] 
**notification_triggers** | [**[NotificationTrigger]**](NotificationTrigger.md) | List of scheduled notifications for an invite | [optional] 
**custom_fields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**watchlist_colour** | **str** |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**hosts** | [**[Host]**](Host.md) |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**company** | **str** |  | [optional] 
**checked_in** | **bool** |  | [optional] 
**group_visit** | [**GroupVisit**](GroupVisit.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


