# InviteDetail

The root of the InviteDetail type's schema.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**registration** | **object** |  | [optional] 
**mobile_number** | **str** | Phone number | [optional] 
**email_template** | [**EmailTemplate**](EmailTemplate.md) |  | [optional] 
**invite_watchlist** | [**InviteWatchlist**](InviteWatchlist.md) |  | [optional] 
**notification_triggers** | [**list[NotificationTrigger]**](NotificationTrigger.md) | List of scheduled notifications for an invite | [optional] 
**custom_fields** | **list[object]** |  | [optional] 
**watchlist_colour** | **str** |  | [optional] 
**location** | **object** |  | [optional] 
**hosts** | **list[object]** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**last_name** | **str** |  | 
**first_name** | **str** |  | 
**end_date** | **datetime** |  | [optional] 
**email** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**company** | **str** |  | [optional] 
**group_visit** | [**GroupVisit**](GroupVisit.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


