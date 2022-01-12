# openapi_client.OrganisationApi

All URIs are relative to *https://api.highcohesion.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organisation_index**](OrganisationApi.md#create_organisation_index) | **POST** /event_manager/organisation/{organisation_id}/index | Create the organisation tables


# **create_organisation_index**
> SyncResponse create_organisation_index(organisation_id)

Create the organisation tables

### Example

* Api Key Authentication (admin_apikey):
```python
import time
import openapi_client
from Service import organisation_api
from openapi_client.model.sync_response import SyncResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.highcohesion.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    organisation_id = "123e4567-e89b-12d3-a456-426614174000" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Create the organisation tables
        api_response = api_instance.create_organisation_index(organisation_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->create_organisation_index: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**|  |

### Return type

[**SyncResponse**](SyncResponse.md)

### Authorization

[admin_apikey](../README.md#admin_apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

