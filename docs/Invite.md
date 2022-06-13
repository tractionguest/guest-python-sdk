# Invite

The root of the Invite type's schema.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**registration** | [**Registration**](Registration.md) |  | [optional] 
**mobile_number** | **str** |  | [optional] 
**email** | **str** |  | 
**end_date** | **datetime** | Deprecated. Use &#x60;end_date_utc&#x60; instead. | [optional] 
**end_date_utc** | **datetime** |  | [optional] 
**invite_watchlist** | [**InviteWatchlist**](InviteWatchlist.md) |  | [optional] 
**hosts** | [**list[Host]**](Host.md) |  | [optional] 
**watchlist_colour** | **str** |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**start_date** | **datetime** | Deprecated. Use &#x60;start_date_utc&#x60; instead. | [optional] 
**start_date_utc** | **datetime** |  | [optional] 
**last_name** | **str** |  | 
**first_name** | **str** |  | 
**group_visit** | [**GroupVisit**](GroupVisit.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


