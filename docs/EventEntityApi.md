# event_manager_client.EventEntityApi

All URIs are relative to *https://api.highcohesion.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_event_entity**](EventEntityApi.md#update_event_entity) | **PATCH** /event_manager/event_entity | Update Event Entity


# **update_event_entity**
> AsyncResponse update_event_entity(update_event_entity_request)

Update Event Entity

### Example

* Api Key Authentication (apikey):
```python
import time
import event_manager_client
from event_manager_client.api import event_entity_api
from event_manager_client.model.update_event_entity_request import UpdateEventEntityRequest
from event_manager_client.model.async_response import AsyncResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.highcohesion.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = event_manager_client.Configuration(
    host = "https://api.highcohesion.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with event_manager_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = event_entity_api.EventEntityApi(api_client)
    update_event_entity_request = UpdateEventEntityRequest(
        id="60e5b1b405b1e2db6ebd3bee",
        destination_id="1234567890",
        destination_parent_id="SKU-AAAA",
    ) # UpdateEventEntityRequest | The fields to update

    # example passing only required values which don't have defaults set
    try:
        # Update Event Entity
        api_response = api_instance.update_event_entity(update_event_entity_request)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling EventEntityApi->update_event_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_event_entity_request** | [**UpdateEventEntityRequest**](UpdateEventEntityRequest.md)| The fields to update |

### Return type

[**AsyncResponse**](AsyncResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

