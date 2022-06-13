# InviteDetail

The root of the InviteDetail type's schema.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**registration** | [**Registration**](Registration.md) |  | [optional] 
**mobile_number** | **str** | Phone number | [optional] 
**email_template** | [**EmailTemplate**](EmailTemplate.md) |  | [optional] 
**invite_watchlist** | [**InviteWatchlist**](InviteWatchlist.md) |  | [optional] 
**notification_triggers** | [**list[NotificationTrigger]**](NotificationTrigger.md) | List of scheduled notifications for an invite | [optional] 
**custom_fields** | [**list[CustomField]**](CustomField.md) |  | [optional] 
**watchlist_colour** | **str** |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**hosts** | [**list[Host]**](Host.md) |  | [optional] 
**start_date** | **datetime** | Deprecated. Use &#x60;start_date_utc&#x60; instead. | [optional] 
**start_date_utc** | **datetime** |  | [optional] 
**last_name** | **str** |  | 
**first_name** | **str** |  | 
**end_date** | **datetime** | Deprecated. Use &#x60;end_date_utc&#x60; instead. | [optional] 
**end_date_utc** | **datetime** |  | [optional] 
**email** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**company** | **str** |  | [optional] 
**checked_in** | **bool** |  | [optional] 
**group_visit** | [**GroupVisit**](GroupVisit.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


