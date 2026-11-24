# ScreeningProviderUsage

Guard Dog credit usage for one connected credit-consuming screening provider. Credit fields are null when `available` is false (Guard Dog could not be reached, or the provider is not activated) and also when the contract has unlimited credits, in which case `available` is true.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**screening_provider_id** | **int** | The screening provider integration the usage belongs to | 
**type_id** | **int** | The provider type identifier | 
**available** | **bool** | Whether usage could be read for this provider | 
**provider** | **str** | Guard Dog&#39;s name for the provider: &#x60;clear&#x60; for Risk Insights, &#x60;checkr&#x60; for Checkr | 
**credits_used** | **int** | Credits consumed in the current contract period | 
**credits_remaining** | **int** | Credits left in the current contract period, null when unlimited | 
**credits_purchased** | **int** | Credits purchased for the current contract period, null when unlimited | 
**credits_start_date** | **str** | First day of the current contract period | 
**credits_end_date** | **str** | Last day of the current contract period | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


