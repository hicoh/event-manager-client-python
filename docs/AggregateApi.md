# event_manager_client.AggregateApi

All URIs are relative to *https://api.highcohesion.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aggregate_events**](AggregateApi.md#get_aggregate_events) | **GET** /event_manager/aggregate_events/{organisation_id}/{stream_id}/{job_id} | Aggregate all events from a specific job
[**replicate_child_aggregate_event**](AggregateApi.md#replicate_child_aggregate_event) | **POST** /event_manager/aggregate_events/replicate_child | Replicate Child Aggregate Event
[**replicate_parent_aggregate_event**](AggregateApi.md#replicate_parent_aggregate_event) | **POST** /event_manager/aggregate_events/replicate_parent | Replicate a Parent Aggregate event


# **get_aggregate_events**
> AsyncResponse get_aggregate_events(organisation_id, stream_id, job_id)

Aggregate all events from a specific job

### Example

* Api Key Authentication (admin_apikey):
```python
import time
import event_manager_client
from event_manager_client.api import aggregate_api
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

# Configure API key authorization: admin_apikey
configuration.api_key['admin_apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['admin_apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with event_manager_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aggregate_api.AggregateApi(api_client)
    organisation_id = "123e4567-e89b-12d3-a456-426614174000" # str | 
    stream_id = "123e4567-e89b-12d3-a456-426614174000" # str | 
    job_id = "123e4567-e89b-12d3-a456-426614174000" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Aggregate all events from a specific job
        api_response = api_instance.get_aggregate_events(organisation_id, stream_id, job_id)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling AggregateApi->get_aggregate_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**|  |
 **stream_id** | **str**|  |
 **job_id** | **str**|  |

### Return type

[**AsyncResponse**](AsyncResponse.md)

### Authorization

[admin_apikey](../README.md#admin_apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replicate_child_aggregate_event**
> AsyncResponse replicate_child_aggregate_event()

Replicate Child Aggregate Event

### Example

* Api Key Authentication (apikey):
```python
import time
import event_manager_client
from event_manager_client.api import aggregate_api
from event_manager_client.model.replicate_event_request import ReplicateEventRequest
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
    api_instance = aggregate_api.AggregateApi(api_client)
    organisation_id = "organisation-id_example" # str |  (optional)
    replicate_event_request = ReplicateEventRequest(
        job_id="8c09b496-df2a-11eb-ba80-0242ac130004",
        original_event_id="60e5b1b405b1e2db6ebd3bee",
        payload_in={},
    ) # ReplicateEventRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Replicate Child Aggregate Event
        api_response = api_instance.replicate_child_aggregate_event(organisation_id=organisation_id, replicate_event_request=replicate_event_request)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling AggregateApi->replicate_child_aggregate_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**|  | [optional]
 **replicate_event_request** | [**ReplicateEventRequest**](ReplicateEventRequest.md)|  | [optional]

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

# **replicate_parent_aggregate_event**
> AsyncResponse replicate_parent_aggregate_event(replicate_parent_aggregate_event_request)

Replicate a Parent Aggregate event

### Example

* Api Key Authentication (admin_apikey):
```python
import time
import event_manager_client
from event_manager_client.api import aggregate_api
from event_manager_client.model.replicate_parent_aggregate_event_request import ReplicateParentAggregateEventRequest
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

# Configure API key authorization: admin_apikey
configuration.api_key['admin_apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['admin_apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with event_manager_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aggregate_api.AggregateApi(api_client)
    replicate_parent_aggregate_event_request = ReplicateParentAggregateEventRequest(
        job_id="8c09b496-df2a-11eb-ba80-0242ac130004",
        original_event_id="60e5b1b405b1e2db6ebd3bee",
    ) # ReplicateParentAggregateEventRequest | Event Data
    organisation_id = "organisation-id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Replicate a Parent Aggregate event
        api_response = api_instance.replicate_parent_aggregate_event(replicate_parent_aggregate_event_request)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling AggregateApi->replicate_parent_aggregate_event: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Replicate a Parent Aggregate event
        api_response = api_instance.replicate_parent_aggregate_event(replicate_parent_aggregate_event_request, organisation_id=organisation_id)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling AggregateApi->replicate_parent_aggregate_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replicate_parent_aggregate_event_request** | [**ReplicateParentAggregateEventRequest**](ReplicateParentAggregateEventRequest.md)| Event Data |
 **organisation_id** | **str**|  | [optional]

### Return type

[**AsyncResponse**](AsyncResponse.md)

### Authorization

[admin_apikey](../README.md#admin_apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

