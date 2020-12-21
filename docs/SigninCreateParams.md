# SigninCreateParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_id** | **str** | UUID of a Registration | [optional] 
**email** | **str** | E-mail, ignored if &#x60;registration_id&#x60; is included | [optional] 
**company** | **str** | Company name, ignored if &#x60;registration_id&#x60; is included | [optional] 
**last_name** | **str** | Last name, ignored if &#x60;registration_id&#x60; is included | [optional] 
**first_name** | **str** | First name, ignored if &#x60;registration_id&#x60; is included | [optional] 
**sms_message** | **str** |  | [optional] 
**send_notifications** | **bool** |  | [optional] 
**location_id** | **int** | ID of the Location where the Signin happened, ignored if &#x60;registration_id&#x60; is included | [optional] 
**host_ids** | **list[int]** | Array of Host ids, ignored if &#x60;registration_id&#x60; is included | [optional] 
**host_email_template_id** | **int** |  | [optional] 
**guest_email_template_id** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


