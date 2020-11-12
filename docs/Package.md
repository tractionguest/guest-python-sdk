# Package

Root for a Package type's schema
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**recipient** | [**Host**](Host.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | 
**package_state** | **str** | this can be one of the following states: &#39;processing&#39;, &#39;recipient_matched&#39;, &#39;needs_attention&#39; or &#39;picked_up&#39; | 
**carrier_name** | **str** | A carrier name that gets detected on the shipping label. i.e. USPS, Purolator, DHL, Canada Post, Royal Mail, etc...  | [optional] 
**picked_up_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**image** | [**Image**](Image.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


