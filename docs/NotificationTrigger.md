# NotificationTrigger

The root of the NotificationTrigger type's schema.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset_direction** | **str** | Whether the offset should be calculated for before, or after the event | 
**offset_amount** | **int** | The amount to offset the notification from the event | 
**offset_origin** | **str** | Whether the offset should be calculated from the start, or finish of the event | 
**email_template_id** | **int** |  | 
**notification_groups** | **list[str]** | An array made of only &#x60;INVITEE&#x60;, &#x60;HOSTS, or &#x60;LEP&#x60; as possible string values | 
**offset_unit** | **str** | Whether the offset should be calculated as &#x60;days&#x60; or &#x60;hours&#x60; | 
**email_template_name** | **str** | The name of the EmailTemplate associated with the NotificationTrigger. This is only given from the server, not used as a create param. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


