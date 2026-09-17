# Invite

The root of the Invite type's schema.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**checked_in** | **bool** |  | [optional] 
**status** | **str** | &#39;registered&#39; once the guest completed the registration portal form, otherwise &#39;invited&#39;. | [optional] 
**registration** | [**Registration**](Registration.md) |  | [optional] 
**mobile_number** | **str** |  | [optional] 
**email** | **str** |  | 
**end_date** | **datetime** |  | [optional] 
**invite_watchlist** | [**InviteWatchlist**](InviteWatchlist.md) |  | [optional] 
**hosts** | [**list[Host]**](Host.md) |  | [optional] 
**watchlist_colour** | **str** |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**last_name** | **str** |  | 
**first_name** | **str** |  | 
**group_visit** | [**GroupVisit**](GroupVisit.md) |  | [optional] 
**assigned_stall** | [**AssignedStall**](AssignedStall.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


