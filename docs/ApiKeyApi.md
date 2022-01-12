# event_manager_client.ApiKeyApi

All URIs are relative to *https://api.highcohesion.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](ApiKeyApi.md#create_api_key) | **POST** /event_manager/api_key | Create a new API key
[**delete_api_key**](ApiKeyApi.md#delete_api_key) | **DELETE** /event_manager/api_key/{organisation_id}/{key_id} | Delete an API key
[**get_all_api_keys_by_organisation**](ApiKeyApi.md#get_all_api_keys_by_organisation) | **GET** /event_manager/api_key/all/organisation/{organisation_id} | Fetch all API keys associated with an Organisation


# **create_api_key**
> ApiKeyResponse create_api_key()

Create a new API key

### Example

* Api Key Authentication (admin_apikey):
```python
import time
import event_manager_client
from event_manager_client.api import api_key_api
from event_manager_client.model.api_key_response import ApiKeyResponse
from event_manager_client.model.api_key_request import ApiKeyRequest
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

# Configure API key authorization: admin_apikey
configuration.api_key['admin_apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['admin_apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with event_manager_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_key_api.ApiKeyApi(api_client)
    api_key_request = ApiKeyRequest(
        organisation_id="f0a8ba52-f840-434e-8883-1fbf5ddab7ca",
        name="Test API Key",
        access="DEFAULT",
    ) # ApiKeyRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new API key
        api_response = api_instance.create_api_key(api_key_request=api_key_request)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling ApiKeyApi->create_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_request** | [**ApiKeyRequest**](ApiKeyRequest.md)|  | [optional]

### Return type

[**ApiKeyResponse**](ApiKeyResponse.md)

### Authorization

[admin_apikey](../README.md#admin_apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Api Key Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> delete_api_key(organisation_id, key_id)

Delete an API key

### Example

* Api Key Authentication (admin_apikey):
```python
import time
import event_manager_client
from event_manager_client.api import api_key_api
from event_manager_client.model.error_response import ErrorResponse
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

# Configure API key authorization: admin_apikey
configuration.api_key['admin_apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['admin_apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with event_manager_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_key_api.ApiKeyApi(api_client)
    organisation_id = "123e4567-e89b-12d3-a456-426614174000" # str | 
    key_id = "f0a8ba52-f840-434e-8883-1fbf5ddab7ca" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an API key
        api_instance.delete_api_key(organisation_id, key_id)
    except event_manager_client.ApiException as e:
        print("Exception when calling ApiKeyApi->delete_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**|  |
 **key_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[admin_apikey](../README.md#admin_apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_api_keys_by_organisation**
> ApiKeyList get_all_api_keys_by_organisation(organisation_id)

Fetch all API keys associated with an Organisation

### Example

* Api Key Authentication (admin_apikey):
```python
import time
import event_manager_client
from event_manager_client.api import api_key_api
from event_manager_client.model.api_key_list import ApiKeyList
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

# Configure API key authorization: admin_apikey
configuration.api_key['admin_apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['admin_apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with event_manager_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_key_api.ApiKeyApi(api_client)
    organisation_id = "123e4567-e89b-12d3-a456-426614174000" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch all API keys associated with an Organisation
        api_response = api_instance.get_all_api_keys_by_organisation(organisation_id)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling ApiKeyApi->get_all_api_keys_by_organisation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**|  |

### Return type

[**ApiKeyList**](ApiKeyList.md)

### Authorization

[admin_apikey](../README.md#admin_apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

