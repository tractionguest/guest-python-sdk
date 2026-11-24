# ScreeningProvider

An external watchlist screening provider connected to the account. Supported providers and their `type_id` values: Visual Compliance (3), Integration Point (5), FinScan (8), Treasury / International Trade Administration (10), Risk Insights (15), Checkr (18).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the screening provider integration | 
**name** | **str** | The provider&#39;s display name | 
**activated** | **bool** | Whether the provider is connected, computed from its required credentials being present | 
**type_id** | **int** | The provider type identifier | 
**account_id** | **int** | The account the provider belongs to | 
**category_id** | **int** | The integration category identifier | 
**integration_settings** | [**list[ScreeningProviderSetting]**](ScreeningProviderSetting.md) | The provider&#39;s settings, keyed by &#x60;field_name&#x60; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


