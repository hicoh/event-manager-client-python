# event_manager_client.KeyApi

All URIs are relative to *https://api.highcohesion.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_key**](KeyApi.md#get_key) | **GET** /event_manager/key/{id} | Fetch key


# **get_key**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_key(id)

Fetch key

### Example

* Api Key Authentication (apikey):
```python
import time
import event_manager_client
from event_manager_client.api import key_api
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
    api_instance = key_api.KeyApi(api_client)
    id = "123e4567-e89b-12d3-a456-426614174000" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch key
        api_response = api_instance.get_key(id)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling KeyApi->get_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

