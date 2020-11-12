# PackageUpdateParams

Update/Edit information about a Package.  [picked_up] - changes the package_state to picked up and assigns non null value to picked_up_at  [recipient_id] - update the package's intended recipient. Changes package_state to 'recipient_matched' and notifies host about their package via email. A previous recipient will stop getting notifications  [carrier_name] - change/update the package's carrier/courier information 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**picked_up** | **bool** | changes the package_state to picked up and assigns non null value to picked_up_at | [optional] 
**carrier_name** | **str** | change/update the package&#39;s carrier/courier information | [optional] 
**recipient_id** | **int** | id of the Host for which you want to send notifications to regarding their package | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


