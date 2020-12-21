# NotificationTrigger1

The root of the NotificationTrigger type's schema.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset_unit** | **str** | Whether the offset should be calculated as &#x60;days&#x60; or &#x60;hours&#x60; | 
**notification_groups** | **list[str]** | An array made of only &#x60;INVITEE&#x60;, &#x60;HOSTS, or &#x60;LEP&#x60; as possible string values | 
**email_template_id** | **int** |  | 
**offset_origin** | **str** | Whether the offset should be calculated from the start, or finish of the event | 
**offset_amount** | **int** | The amount to offset the notification from the event | 
**offset_direction** | **str** | Whether the offset should be calculated for before, or after the event | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


