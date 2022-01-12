# openapi_client.EventApi

All URIs are relative to *https://api.highcohesion.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_by_id**](EventApi.md#get_event_by_id) | **GET** /event_manager/event/{event_id} | Get an event by event id
[**get_events_by**](EventApi.md#get_events_by) | **GET** /event_manager/event | Get a list of events by
[**redrive_event**](EventApi.md#redrive_event) | **POST** /event_manager/event/redrive | Redrive Event
[**replicate_event**](EventApi.md#replicate_event) | **POST** /event_manager/event/replicate | Replicate Event
[**update_child_event**](EventApi.md#update_child_event) | **PATCH** /event_manager/child_event | Update Child Event via the Parent Event ID and the entity name
[**update_event**](EventApi.md#update_event) | **PATCH** /event_manager/event | Update Event


# **get_event_by_id**
> Event get_event_by_id(event_id)

Get an event by event id

### Example

* Api Key Authentication (apikey):
```python
import time
import openapi_client
from Service import event_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.event import Event
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

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = event_api.EventApi(api_client)
    event_id = "event_id_example" # str | The event id

    # example passing only required values which don't have defaults set
    try:
        # Get an event by event id
        api_response = api_instance.get_event_by_id(event_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EventApi->get_event_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| The event id |

### Return type

[**Event**](Event.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_by**
> EventList get_events_by()

Get a list of events by

### Example

* Api Key Authentication (apikey):
```python
import time
import openapi_client
from Service import event_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.event_list import EventList
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

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = event_api.EventApi(api_client)
    id = "id_example" # str | The event id (optional)
    job_id = "job_id_example" # str | The job id (optional)
    stream_id = "stream_id_example" # str | The stream id (optional)
    status = "status_example" # str | The status (optional)
    limit = "limit_example" # str | The limit (limit=20 to get the first 20 events) (optional)
    order_by = "order_by_example" # str | order by one specific field (orderBy=createdAt,desc, orderBy=status,asc) (optional)
    offset = "offset_example" # str | the position of the first result to retrieve (offset=100) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of events by
        api_response = api_instance.get_events_by(id=id, job_id=job_id, stream_id=stream_id, status=status, limit=limit, order_by=order_by, offset=offset)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EventApi->get_events_by: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The event id | [optional]
 **job_id** | **str**| The job id | [optional]
 **stream_id** | **str**| The stream id | [optional]
 **status** | **str**| The status | [optional]
 **limit** | **str**| The limit (limit&#x3D;20 to get the first 20 events) | [optional]
 **order_by** | **str**| order by one specific field (orderBy&#x3D;createdAt,desc, orderBy&#x3D;status,asc) | [optional]
 **offset** | **str**| the position of the first result to retrieve (offset&#x3D;100) | [optional]

### Return type

[**EventList**](EventList.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redrive_event**
> AsyncResponse redrive_event(redrive_event_request)

Redrive Event

### Example

* Api Key Authentication (apikey):
```python
import time
import openapi_client
from Service import event_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.redrive_event_request import RedriveEventRequest
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

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = event_api.EventApi(api_client)
    redrive_event_request = RedriveEventRequest(
        event_id="60e5b1b405b1e2db6ebd3bee",
    ) # RedriveEventRequest | The event to redrive

    # example passing only required values which don't have defaults set
    try:
        # Redrive Event
        api_response = api_instance.redrive_event(redrive_event_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EventApi->redrive_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redrive_event_request** | [**RedriveEventRequest**](RedriveEventRequest.md)| The event to redrive |

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

# **replicate_event**
> AsyncResponse replicate_event()

Replicate Event

### Example

* Api Key Authentication (apikey):
```python
import time
import openapi_client
from Service import event_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.replicate_event_request import ReplicateEventRequest
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

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = event_api.EventApi(api_client)
    organisation_id = "organisation-id_example" # str |  (optional)
    replicate_event_request = ReplicateEventRequest(
        job_id="8c09b496-df2a-11eb-ba80-0242ac130004",
        original_event_id="60e5b1b405b1e2db6ebd3bee",
        payload_in={},
    ) # ReplicateEventRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Replicate Event
        api_response = api_instance.replicate_event(organisation_id=organisation_id, replicate_event_request=replicate_event_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EventApi->replicate_event: %s\n" % e)
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

# **update_child_event**
> AsyncResponse update_child_event(update_child_event_request)

Update Child Event via the Parent Event ID and the entity name

### Example

* Api Key Authentication (apikey):
```python
import time
import openapi_client
from Service import event_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.update_child_event_request import UpdateChildEventRequest
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

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = event_api.EventApi(api_client)
    update_child_event_request = UpdateChildEventRequest(
        parent_id="60e5b1b405b1e2db6ebd3bee",
        entity_name="#1001",
        status="OK",
        message="The event has been sent OK to destination system",
        destination_id="1234567890",
    ) # UpdateChildEventRequest | The parent ID and entity name identify the child event, the other fields will be updated on that event
    organisation_id = "organisation-id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Child Event via the Parent Event ID and the entity name
        api_response = api_instance.update_child_event(update_child_event_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EventApi->update_child_event: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Child Event via the Parent Event ID and the entity name
        api_response = api_instance.update_child_event(update_child_event_request, organisation_id=organisation_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EventApi->update_child_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_child_event_request** | [**UpdateChildEventRequest**](UpdateChildEventRequest.md)| The parent ID and entity name identify the child event, the other fields will be updated on that event |
 **organisation_id** | **str**|  | [optional]

### Return type

[**AsyncResponse**](AsyncResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: array
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event**
> AsyncResponse update_event(update_event_request)

Update Event

### Example

* Api Key Authentication (apikey):
```python
import time
import openapi_client
from Service import event_api
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.update_event_request import UpdateEventRequest
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

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = event_api.EventApi(api_client)
    update_event_request = UpdateEventRequest(
        id="60e5b1b405b1e2db6ebd3bee",
        status="OK",
        message="The event has been sent OK to destination system",
        destination_id="1234567890",
        destination_parent_id="1234567890",
    ) # UpdateEventRequest | The fields to update

    # example passing only required values which don't have defaults set
    try:
        # Update Event
        api_response = api_instance.update_event(update_event_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EventApi->update_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_event_request** | [**UpdateEventRequest**](UpdateEventRequest.md)| The fields to update |

### Return type

[**AsyncResponse**](AsyncResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: array
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

