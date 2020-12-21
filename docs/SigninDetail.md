# SigninDetail

The root of the Signin type's schema.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**documents** | [**list[SignableDocument]**](SignableDocument.md) |  | [optional] 
**signin_watchlist** | [**SigninWatchlist**](SigninWatchlist.md) |  | [optional] 
**hosts** | [**list[Host]**](Host.md) |  | [optional] 
**signin_data** | [**list[SigninData]**](SigninData.md) |  | [optional] 
**signin_acknowledgement** | [**SigninAcknowledgement**](SigninAcknowledgement.md) |  | [optional] 
**note** | **str** |  | [optional] 
**is_signed_out** | **bool** | A one-way method of Signing out a Signin | [optional] 
**signin_timestamp** | **datetime** |  | [optional] 
**signin_photo_url** | **str** |  | [optional] 
**signed_out_timestamp** | **datetime** |  | [optional] 
**mobile_number** | **str** |  | [optional] 
**location_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**is_acknowledged** | **bool** | Whether this Signin has been acknowledged yet. Can also be used as a one-way method of setting the Signin as acknowledged. | [optional] 
**is_accounted_for** | **bool** |  | [optional] 
**first_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**registration** | [**Registration**](Registration.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


