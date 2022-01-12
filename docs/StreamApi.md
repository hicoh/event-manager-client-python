# event_manager_client.StreamApi

All URIs are relative to *https://api.highcohesion.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schedule_configuration**](StreamApi.md#create_schedule_configuration) | **POST** /event_manager/stream/schedule_configuration | Create a new Stream Schedule Configuration
[**delete_schedule_configuration**](StreamApi.md#delete_schedule_configuration) | **DELETE** /event_manager/stream/schedule_configuration/{stream_id} | Delete a Stream Schedule Configuration
[**get_schedule_configuration**](StreamApi.md#get_schedule_configuration) | **GET** /event_manager/stream/schedule_configuration/{stream_id} | Get a Stream Schedule Configuration by Stream Id
[**update_schedule_configuration_attributes**](StreamApi.md#update_schedule_configuration_attributes) | **PATCH** /event_manager/stream/schedule_configuration | Updates Stream Schedule Configuration option and active attributes.


# **create_schedule_configuration**
> ScheduleConfiguration create_schedule_configuration()

Create a new Stream Schedule Configuration

### Example

* Api Key Authentication (apikey):
```python
import time
import event_manager_client
from event_manager_client.api import stream_api
from event_manager_client.model.schedule_configuration_request import ScheduleConfigurationRequest
from event_manager_client.model.schedule_configuration import ScheduleConfiguration
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
    api_instance = stream_api.StreamApi(api_client)
    organisation_id = "organisation-id_example" # str |  (optional)
    schedule_configuration_request = ScheduleConfigurationRequest(
        stream_id="8c09b496-df2a-11eb-ba80-0242ac130004",
        scheduled_option="*/5 * * * *",
        active=True,
    ) # ScheduleConfigurationRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new Stream Schedule Configuration
        api_response = api_instance.create_schedule_configuration(organisation_id=organisation_id, schedule_configuration_request=schedule_configuration_request)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling StreamApi->create_schedule_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**|  | [optional]
 **schedule_configuration_request** | [**ScheduleConfigurationRequest**](ScheduleConfigurationRequest.md)|  | [optional]

### Return type

[**ScheduleConfiguration**](ScheduleConfiguration.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_schedule_configuration**
> SyncResponse delete_schedule_configuration(stream_id)

Delete a Stream Schedule Configuration

### Example

* Api Key Authentication (apikey):
```python
import time
import event_manager_client
from event_manager_client.api import stream_api
from event_manager_client.model.sync_response import SyncResponse
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
    api_instance = stream_api.StreamApi(api_client)
    stream_id = "stream_id_example" # str | Stream Id
    organisation_id = "organisation-id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a Stream Schedule Configuration
        api_response = api_instance.delete_schedule_configuration(stream_id)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling StreamApi->delete_schedule_configuration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a Stream Schedule Configuration
        api_response = api_instance.delete_schedule_configuration(stream_id, organisation_id=organisation_id)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling StreamApi->delete_schedule_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **str**| Stream Id |
 **organisation_id** | **str**|  | [optional]

### Return type

[**SyncResponse**](SyncResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation is accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule_configuration**
> ScheduleConfiguration get_schedule_configuration(stream_id)

Get a Stream Schedule Configuration by Stream Id

### Example

* Api Key Authentication (apikey):
```python
import time
import event_manager_client
from event_manager_client.api import stream_api
from event_manager_client.model.schedule_configuration import ScheduleConfiguration
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

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with event_manager_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stream_api.StreamApi(api_client)
    stream_id = "stream_id_example" # str | Stream Id
    organisation_id = "organisation-id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a Stream Schedule Configuration by Stream Id
        api_response = api_instance.get_schedule_configuration(stream_id)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling StreamApi->get_schedule_configuration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a Stream Schedule Configuration by Stream Id
        api_response = api_instance.get_schedule_configuration(stream_id, organisation_id=organisation_id)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling StreamApi->get_schedule_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **str**| Stream Id |
 **organisation_id** | **str**|  | [optional]

### Return type

[**ScheduleConfiguration**](ScheduleConfiguration.md)

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

# **update_schedule_configuration_attributes**
> PatchSyncResponse update_schedule_configuration_attributes()

Updates Stream Schedule Configuration option and active attributes.

### Example

* Api Key Authentication (apikey):
```python
import time
import event_manager_client
from event_manager_client.api import stream_api
from event_manager_client.model.schedule_configuration_request import ScheduleConfigurationRequest
from event_manager_client.model.patch_sync_response import PatchSyncResponse
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
    api_instance = stream_api.StreamApi(api_client)
    organisation_id = "organisation-id_example" # str |  (optional)
    schedule_configuration_request = ScheduleConfigurationRequest(
        stream_id="8c09b496-df2a-11eb-ba80-0242ac130004",
        scheduled_option="*/5 * * * *",
        active=True,
    ) # ScheduleConfigurationRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates Stream Schedule Configuration option and active attributes.
        api_response = api_instance.update_schedule_configuration_attributes(organisation_id=organisation_id, schedule_configuration_request=schedule_configuration_request)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling StreamApi->update_schedule_configuration_attributes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**|  | [optional]
 **schedule_configuration_request** | [**ScheduleConfigurationRequest**](ScheduleConfigurationRequest.md)|  | [optional]

### Return type

[**PatchSyncResponse**](PatchSyncResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

