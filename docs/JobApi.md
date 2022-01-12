# event_manager_client.JobApi

All URIs are relative to *https://api.highcohesion.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job**](JobApi.md#create_job) | **POST** /event_manager/job | Create a new job
[**create_job_schedule**](JobApi.md#create_job_schedule) | **POST** /event_manager/job/schedule | Create a job schedule
[**delete_job**](JobApi.md#delete_job) | **DELETE** /event_manager/job | Delete jobs
[**get_job_by_id**](JobApi.md#get_job_by_id) | **GET** /event_manager/job/{job_id} | Get a job by job id
[**get_jobs_by**](JobApi.md#get_jobs_by) | **GET** /event_manager/job | Get a list of jobs by
[**replicate_job**](JobApi.md#replicate_job) | **POST** /event_manager/job/replicate | Replicate job
[**update_job**](JobApi.md#update_job) | **PATCH** /event_manager/job | Update job


# **create_job**
> AsyncResponse create_job()

Create a new job

### Example

* Api Key Authentication (apikey):
```python
import time
import event_manager_client
from event_manager_client.api import job_api
from event_manager_client.model.job_request import JobRequest
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
    api_instance = job_api.JobApi(api_client)
    job_request = JobRequest(
        stream_id="8c09b496-df2a-11eb-ba80-0242ac130004",
        payload_in_list=PayloadInList([
            {},
        ]),
    ) # JobRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new job
        api_response = api_instance.create_job(job_request=job_request)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling JobApi->create_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_request** | [**JobRequest**](JobRequest.md)|  | [optional]

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
**202** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job_schedule**
> AsyncResponse create_job_schedule()

Create a job schedule

### Example

* Api Key Authentication (apikey):
```python
import time
import event_manager_client
from event_manager_client.api import job_api
from event_manager_client.model.job_schedule_request import JobScheduleRequest
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
    api_instance = job_api.JobApi(api_client)
    organisation_id = "organisation-id_example" # str |  (optional)
    job_schedule_request = JobScheduleRequest(
        stream_id="60e5b1b405b1e2db6ebd3bee",
        original_job_id="60e5b1b405b1e2db6ebd3bee",
        due_at="2021/03/21 12:23:22",
    ) # JobScheduleRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a job schedule
        api_response = api_instance.create_job_schedule(organisation_id=organisation_id, job_schedule_request=job_schedule_request)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling JobApi->create_job_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**|  | [optional]
 **job_schedule_request** | [**JobScheduleRequest**](JobScheduleRequest.md)|  | [optional]

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

# **delete_job**
> SyncResponse delete_job()

Delete jobs

### Example

* Api Key Authentication (apikey):
```python
import time
import event_manager_client
from event_manager_client.api import job_api
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
    api_instance = job_api.JobApi(api_client)
    organisation_id = "organisation-id_example" # str |  (optional)
    id = "id_example" # str | The job id (optional)
    stream_id = "stream_id_example" # str | The stream id of the job (optional)
    status = "status_example" # str | The job status (optional)
    due_at = "2021/03/21 12:23:22" # str | Delete jobs filtered by due_at date (due_at=2021/03/21 12:23:22,gte) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete jobs
        api_response = api_instance.delete_job(organisation_id=organisation_id, id=id, stream_id=stream_id, status=status, due_at=due_at)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling JobApi->delete_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**|  | [optional]
 **id** | **str**| The job id | [optional]
 **stream_id** | **str**| The stream id of the job | [optional]
 **status** | **str**| The job status | [optional]
 **due_at** | **str**| Delete jobs filtered by due_at date (due_at&#x3D;2021/03/21 12:23:22,gte) | [optional]

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
**200** | Request accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_by_id**
> Job get_job_by_id(job_id)

Get a job by job id

### Example

* Api Key Authentication (apikey):
```python
import time
import event_manager_client
from event_manager_client.api import job_api
from event_manager_client.model.job import Job
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
    api_instance = job_api.JobApi(api_client)
    job_id = "job_id_example" # str | The job id

    # example passing only required values which don't have defaults set
    try:
        # Get a job by job id
        api_response = api_instance.get_job_by_id(job_id)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling JobApi->get_job_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job id |

### Return type

[**Job**](Job.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucessful operation |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs_by**
> JobList get_jobs_by()

Get a list of jobs by

### Example

* Api Key Authentication (apikey):
```python
import time
import event_manager_client
from event_manager_client.api import job_api
from event_manager_client.model.job_list import JobList
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
    api_instance = job_api.JobApi(api_client)
    id = "id_example" # str | The job id (optional)
    stream_id = "stream_id_example" # str | The stream id of the job (optional)
    status = "status_example" # str | The job status (optional)
    limit = "limit_example" # str | The limit (limit=20 to get the first 20 jobs) (optional)
    order_by = "order_by_example" # str | order by one specific field (orderBy=createdAt,desc, orderBy=status,asc) (optional)
    offset = "offset_example" # str | the position of the first result to retrieve (offset=100) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of jobs by
        api_response = api_instance.get_jobs_by(id=id, stream_id=stream_id, status=status, limit=limit, order_by=order_by, offset=offset)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling JobApi->get_jobs_by: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The job id | [optional]
 **stream_id** | **str**| The stream id of the job | [optional]
 **status** | **str**| The job status | [optional]
 **limit** | **str**| The limit (limit&#x3D;20 to get the first 20 jobs) | [optional]
 **order_by** | **str**| order by one specific field (orderBy&#x3D;createdAt,desc, orderBy&#x3D;status,asc) | [optional]
 **offset** | **str**| the position of the first result to retrieve (offset&#x3D;100) | [optional]

### Return type

[**JobList**](JobList.md)

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

# **replicate_job**
> AsyncResponse replicate_job()

Replicate job

### Example

* Api Key Authentication (apikey):
```python
import time
import event_manager_client
from event_manager_client.api import job_api
from event_manager_client.model.replicate_job_request import ReplicateJobRequest
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
    api_instance = job_api.JobApi(api_client)
    replicate_job_request = ReplicateJobRequest(
        job_id="60e5b1b405b1e2db6ebd3bee",
        payload_in_list=PayloadInList([
            {},
        ]),
    ) # ReplicateJobRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Replicate job
        api_response = api_instance.replicate_job(replicate_job_request=replicate_job_request)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling JobApi->replicate_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replicate_job_request** | [**ReplicateJobRequest**](ReplicateJobRequest.md)|  | [optional]

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

# **update_job**
> AsyncResponse update_job(update_job_request)

Update job

### Example

* Api Key Authentication (apikey):
```python
import time
import event_manager_client
from event_manager_client.api import job_api
from event_manager_client.model.update_job_request import UpdateJobRequest
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
    api_instance = job_api.JobApi(api_client)
    update_job_request = UpdateJobRequest(
        id="60e5b1b405b1e2db6ebd3bee",
        status="FINISHED",
        message="The job finished",
    ) # UpdateJobRequest | The fields to update

    # example passing only required values which don't have defaults set
    try:
        # Update job
        api_response = api_instance.update_job(update_job_request)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling JobApi->update_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_job_request** | [**UpdateJobRequest**](UpdateJobRequest.md)| The fields to update |

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

