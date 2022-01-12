# event_manager_client.HealthApi

All URIs are relative to *https://api.highcohesion.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health**](HealthApi.md#get_health) | **GET** /event_manager/health | Get Health


# **get_health**
> Health get_health()

Get Health

### Example

* Api Key Authentication (apikey):
```python
import time
import event_manager_client
from event_manager_client.api import health_api
from event_manager_client.model.health import Health
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
    api_instance = health_api.HealthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Health
        api_response = api_instance.get_health()
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling HealthApi->get_health: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Health**](Health.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

