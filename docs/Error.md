# Error

The root of the Error type's schema.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The name of the model with the error, or global if it is something outside a model | 
**code** | **str** | An error code reference for the specific error that occured | 
**attribute** | **str, none_type** | The model attribute where the error occured | [optional] 
**message** | **str, none_type** | A human readable error message that can be discarded for internationalization purposes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


