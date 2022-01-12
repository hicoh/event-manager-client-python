# event_manager_client.WebhookApi

All URIs are relative to *https://api.highcohesion.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_dynamic_webhook**](WebhookApi.md#post_dynamic_webhook) | **POST** /event_manager/webhook/dynamic/{stream_id} | Dynamic Webhook
[**post_static_webhook**](WebhookApi.md#post_static_webhook) | **POST** /event_manager/webhook/static/{stream_id} | Static Webhook
[**replicate_dynamic_webhook**](WebhookApi.md#replicate_dynamic_webhook) | **POST** /event_manager/job/replicate/webhook/dynamic | Replicate Dynamic Webhook
[**replicate_static_webhook**](WebhookApi.md#replicate_static_webhook) | **POST** /event_manager/job/replicate/webhook/static | Replicate Static Webhook


# **post_dynamic_webhook**
> AsyncResponse post_dynamic_webhook(stream_id, body)

Dynamic Webhook

### Example

* Api Key Authentication (apikey):
```python
import time
import event_manager_client
from event_manager_client.api import webhook_api
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
    api_instance = webhook_api.WebhookApi(api_client)
    stream_id = "123e4567-e89b-12d3-a456-426614174000" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Event Data

    # example passing only required values which don't have defaults set
    try:
        # Dynamic Webhook
        api_response = api_instance.post_dynamic_webhook(stream_id, body)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling WebhookApi->post_dynamic_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Event Data |

### Return type

[**AsyncResponse**](AsyncResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/csv, text/plain
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_static_webhook**
> AsyncResponse post_static_webhook(stream_id, body)

Static Webhook

### Example

* Api Key Authentication (apikey):
```python
import time
import event_manager_client
from event_manager_client.api import webhook_api
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
    api_instance = webhook_api.WebhookApi(api_client)
    stream_id = "123e4567-e89b-12d3-a456-426614174000" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Event Data

    # example passing only required values which don't have defaults set
    try:
        # Static Webhook
        api_response = api_instance.post_static_webhook(stream_id, body)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling WebhookApi->post_static_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Event Data |

### Return type

[**AsyncResponse**](AsyncResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/csv, text/plain
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replicate_dynamic_webhook**
> AsyncResponse replicate_dynamic_webhook(replicate_webhook)

Replicate Dynamic Webhook

### Example

```python
import time
import event_manager_client
from event_manager_client.api import webhook_api
from event_manager_client.model.replicate_webhook import ReplicateWebhook
from event_manager_client.model.async_response import AsyncResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.highcohesion.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = event_manager_client.Configuration(
    host = "https://api.highcohesion.com/v1"
)


# Enter a context with an instance of the API client
with event_manager_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = webhook_api.WebhookApi(api_client)
    replicate_webhook = ReplicateWebhook(
        job_id="60e5b1b405b1e2db6ebd3bee",
    ) # ReplicateWebhook | Job Data

    # example passing only required values which don't have defaults set
    try:
        # Replicate Dynamic Webhook
        api_response = api_instance.replicate_dynamic_webhook(replicate_webhook)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling WebhookApi->replicate_dynamic_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replicate_webhook** | [**ReplicateWebhook**](ReplicateWebhook.md)| Job Data |

### Return type

[**AsyncResponse**](AsyncResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replicate_static_webhook**
> AsyncResponse replicate_static_webhook(replicate_webhook)

Replicate Static Webhook

### Example

```python
import time
import event_manager_client
from event_manager_client.api import webhook_api
from event_manager_client.model.replicate_webhook import ReplicateWebhook
from event_manager_client.model.async_response import AsyncResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.highcohesion.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = event_manager_client.Configuration(
    host = "https://api.highcohesion.com/v1"
)


# Enter a context with an instance of the API client
with event_manager_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = webhook_api.WebhookApi(api_client)
    replicate_webhook = ReplicateWebhook(
        job_id="60e5b1b405b1e2db6ebd3bee",
    ) # ReplicateWebhook | Job Data

    # example passing only required values which don't have defaults set
    try:
        # Replicate Static Webhook
        api_response = api_instance.replicate_static_webhook(replicate_webhook)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling WebhookApi->replicate_static_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replicate_webhook** | [**ReplicateWebhook**](ReplicateWebhook.md)| Job Data |

### Return type

[**AsyncResponse**](AsyncResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

