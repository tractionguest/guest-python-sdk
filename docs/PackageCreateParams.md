# PackageCreateParams

A [base64_image] string is provided as an encoded image of a shipping label. The image will be processed to determine the package's intended recipient. If a match is found between the recipient and an existing host, they'll be notified about the arrival of their package at the [location_id] specified.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base64_image** | **str** | Base64 encoded image on which to perform processing | 
**location_id** | **int** | Location id for where the package was delivered | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


